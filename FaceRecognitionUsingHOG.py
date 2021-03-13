#!/usr/bin/env python
# coding: utf-8

# # Import Following Liabraries For Face Recognition

# In[1]:


import cv2
import math
from sklearn import neighbors
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import face_recognition # must install this liabray using pip install face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import numpy as np


# # Here is the Train function to train Model 

# In[2]:


# This function uses KNN_Classifier to train model for face recognition
def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
    #initialize two lists for storing encoding images and their respective label
    X = []
    y = []

    # Loop through each person in the training directory to get respected label of image  
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        # Loop through each training image for the current person in the path
        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition.load_image_file(img_path)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)# convert image to gray scale.
            #Use HOG face detection Classifier to find faces in Given Image
            face_bounding_boxes = face_recognition.face_locations(rgb,model='Hog')

            if len(face_bounding_boxes) != 1:
                # If there are no people (or too many people) in a training image, skip that image.
                if verbose:
                    print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(face_bounding_boxes) < 1 else "Found more than one face"))
            else:
                # Add face encoding of current image to the training list X and its respective label in list Y
                X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                y.append(class_dir)

    # Determine how many neighbors to use for weighting in the KNN classifier
    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))
        if verbose:
            print("Chose n_neighbors automatically:", n_neighbors)

    # Create and train the KNN_Classifier with given n_neighbours
    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)

    # Save the trained KNN classifier for furthur Use
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf


# In[4]:


def trainFunction():
    print("Training KNN classifier...")
    classifier = train("TrainingImage", model_save_path="trained_knn_model.clf", n_neighbors=2)
    print("Training complete!")


# # Call this trainFunction for training of model on given images

# In[5]:


trainFunction()


# # Predict function that Recognizes faces in given image using a trained KNN classifier

# In[6]:


def predict(X_frame,knn_clf=None, model_path=None, distance_threshold=0.5):
    
    # Load a trained KNN model (if one was passed in)
    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)
    #For face detection Again convert frame into gray scale
    rgb = cv2.cvtColor(X_frame, cv2.COLOR_BGR2RGB)
    #Use HOG classifier for finding face in given frame. 
    X_face_locations = face_recognition.face_locations(rgb,model='Hog')
    
    # If no faces are found in the image, return an empty result.
    if len(X_face_locations) == 0:
        return []

    # Find encodings for faces in the X_frame
    faces_encodings = face_recognition.face_encodings(X_frame, known_face_locations=X_face_locations)

    # Use the KNN model to find the best matches for the test face
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=2)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]

    # Predict classes and remove classifications that aren't within the threshold
    return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]


# # show_perdiction_on_label function is used to shows the face recognition results visually by drawing rectangle with recognized label

# In[7]:


def show_prediction_labels_on_image(frame, predictions):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)

    for name, (top, right, bottom, left) in predictions:
        # enlarge the predictions for the full sized image.
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # There's a bug in Pillow where it blows up with non-UTF-8 text
        # when using the default bitmap font
        name = name.encode("UTF-8")

        # Draw a label with a name below the face on rectangle shape
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
       

    # Remove the drawing library from memory as per the Pillow docs.
    del draw
    # Save image in open-cv format to be able to show it.

    opencvimage = np.array(pil_image)
    return opencvimage


# 
# # Now finally Setting up Camera for Testing 

# In[9]:


process_this_frame = 4
print('Setting cameras up...')
# multiple cameras can be used with the format url = 'http://username:password@camera_ip:port'
#url = 'http://admin:admin12345@192.168.1.1:8800'
#Use this format to use Mobile Camera
#url='http://192.168.0.100:4747/video'
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    #print('welcome')
    if ret:
        # Different resizing options can be chosen based on desired program runtime.
        # Image resizing for more stable streaming
        img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        process_this_frame = process_this_frame + 1
        if process_this_frame % 5 == 0:
            predictions = predict(img, model_path="trained_knn_model.clf")
        frame = show_prediction_labels_on_image(frame, predictions)
        cv2.imshow('camera', frame)
        if ord('q') == cv2.waitKey(10):
            break
            
cap.release()
cv2.destroyAllWindows()


# In[ ]:




