# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel)
from PyQt5.QtWidgets import QMessageBox,QLineEdit
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import cv2,os,time
import mysql.connector
import math
from sklearn import neighbors
import os.path
import pickle
import dlib
from PIL import Image, ImageDraw
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
db_connection = mysql.connector.connect(host="localhost",user="root",password="*Anum#123",database="StudentMonitor")
mycursor = db_connection.cursor()
from datetime import datetime
from datetime import date
import PIL.Image as Image
import io
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import numpy as np
import urllib.request as ur
import json

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterationUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
class_labels = ['Angry','Happy','Neutral','Sad','Surprise']
classifier =load_model(r'FaceExpressionTrainedModelonSixCasses (1).h5')
hogFaceDetector = dlib.get_frontal_face_detector()
 
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 598)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        
        self.MainScreen=Ui_MainScreen()
        self.MainWindow=Ui_MainWindow()
        
        MainWindow.setStyleSheet("background-color: rgb(144, 255, 246);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_captureImage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_captureImage.setGeometry(QtCore.QRect(210, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_captureImage.setFont(font)
        self.btn_captureImage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_captureImage.setIconSize(QtCore.QSize(20, 20))
        self.btn_captureImage.setAutoDefault(False)
        self.btn_captureImage.setDefault(False)
        self.btn_captureImage.setFlat(False)
        self.btn_captureImage.setObjectName("btn_captureImage")
        self.btn_captureImage.clicked.connect(self.CaptureImages)
        self.Regno
        self.btn_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setGeometry(QtCore.QRect(340, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_register.setFont(font)
        self.btn_register.setStyleSheet("background-color: rgb(28, 206, 255);")
        self.btn_register.setObjectName("btn_register")
        self.btn_register.clicked.connect(self.stopClicked)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color: rgb(28, 206, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 125, 711, 451))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.btn_mainWindow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mainWindow.setGeometry(QtCore.QRect(490, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mainWindow.setFont(font)
        self.btn_mainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_mainWindow.setIconSize(QtCore.QSize(20, 20))
        self.btn_mainWindow.setAutoDefault(False)
        self.btn_mainWindow.setDefault(False)
        self.btn_mainWindow.setFlat(False)
        self.btn_mainWindow.setObjectName("btn_mainWindow")
        self.btn_mainWindow.clicked.connect(self.GotoMainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_captureImage.setText(_translate("MainWindow", "Start Camera"))
        self.btn_register.setText(_translate("MainWindow", "Stop Camera"))
        self.label_4.setText(_translate("MainWindow", "Capture Images"))
        self.label_7.setText(_translate("MainWindow", "Click to Capture Images"))
        self.btn_mainWindow.setText(_translate("MainWindow", "Go to MainWindow"))
        
    def GotoMainWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.MainScreen.setupUi(self.window)
        self.window.show()
        #MainWindow.hide()
        return
    def stopClicked(self):
        self.logic=0
    def displayImage(self,img):
        
        qformat=QImage.Format_Indexed8
        if len(img.shape)==3:
            if (img.shape[2]) == 4:
                qformat=QImage.Format_RGBA888
            else:
                qformat=QImage.Format_RGB888 
        img=QImage(img,img.shape[1],img.shape[0],qformat)
        img=img.rgbSwapped()
        self.label_3.setPixmap(QPixmap.fromImage(img))    
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
    def CaptureImages(self):
        regNo=self.Regno
        self.logic=1
        cap = cv2.VideoCapture(0)
        while True:
            ret,frame=cap.read()
            if ret==True:
                self.displayImage(frame)
                cv2.waitKey()
                if(self.logic==0): 
                    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    pil_im = Image.fromarray(rgb)
                    b = io.BytesIO()
                    pil_im.save(b, 'jpeg')
                    im_bytes = b.getvalue()
                    #print(im_bytes)
                    SQLStatement="INSERT INTO Trainingdata (regNo,photo) VALUES (%s,%s)"
                    mycursor .execute(SQLStatement,(regNo,im_bytes))
                    db_connection.commit()
                    print("Training KNN classifier...")
                    self.train(frame,regNo, model_save_path="trained_knn_model.clf", n_neighbors=1)
                    print("Training complete!")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Training Done Successfully.You can go to Main Screen by Clicking the Button")
                    msg.exec_()
                    break 
            else:
                print('return not found')
        cap.release()
    def train(self,frame,ID,model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
        X = []
        y = []
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_bounding_boxes = face_recognition.face_locations(rgb,model='Hog')

        if len(face_bounding_boxes) != 1:
            # If there are no people (or too many people) in a training image, skip the image.
            if verbose:
                print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(face_bounding_boxes) < 1 else "Found more than one face"))
        else:
            # Add face encoding for current image to the training set
            X.append(face_recognition.face_encodings(frame, known_face_locations=face_bounding_boxes)[0])
            y.append(ID)
        # Create and train the KNN classifier
        knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
        knn_clf.fit(X, y)

        # Save the trained KNN classifier
        if model_save_path is not None:
            with open(model_save_path, 'wb') as f:
                pickle.dump(knn_clf, f)

        return    
class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(695, 523)
        LoginForm.setStyleSheet("background-color: rgb(144, 255, 246);")
        self.centralwidget = QtWidgets.QWidget(LoginForm)
        self.centralwidget.setObjectName("centralwidget")
        
        self.mainWindow=Ui_MainWindow()
        self.LoginForm=Ui_LoginForm()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(28, 206, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.le_regno = QtWidgets.QLineEdit(self.centralwidget)
        self.le_regno.setGeometry(QtCore.QRect(340, 150, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_regno.setFont(font)
        self.le_regno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_regno.setObjectName("le_regno")
        input_validator = QRegExpValidator(QRegExp("[0-9]{4}([a-zA-Z]{2})[0-9]{3}"))
        self.le_regno.setValidator(input_validator)
        #self.regNo=self.le_regno.text()
        self.lbl_regno = QtWidgets.QLabel(self.centralwidget)
        self.lbl_regno.setGeometry(QtCore.QRect(150, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_regno.setFont(font)
        self.lbl_regno.setObjectName("lbl_regno")
        self.le_password = QtWidgets.QLineEdit(self.centralwidget)
        self.le_password.setGeometry(QtCore.QRect(340, 220, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_password.setFont(font)
        self.le_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_password.setObjectName("le_password")
        self.le_password.setEchoMode(QLineEdit.Password)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(270, 320, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("background-color: rgb(28, 206, 255);")
        self.btn_login.setObjectName("btn_login")
        self.btn_login.clicked.connect(self.func_login)
        LoginForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 21))
        self.menubar.setObjectName("menubar")
        LoginForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginForm)
        self.statusbar.setObjectName("statusbar")
        LoginForm.setStatusBar(self.statusbar)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
    def func_login(self,):
        regno=self.le_regno.text()
        password=self.le_password.text()
        response=ur.urlopen ("https://smarteducationsystem.000webhostapp.com/api.php").read().decode('UTF-8')
        #print(response)
        # with response as json_file:
        data = json.loads(response)
        n= len(data)
        flag=False
        for i in range(n): 
            if data[i]['regNo']==regno and data[i]['password']==password:
                print("Successful")
                flag=True
                fileName='login.txt'
                with open(fileName,'w') as f:
                    f.write(regno)
                self.passingInfo()
                self.window=QtWidgets.QMainWindow()
                self.mainWindow.setupUi(self.window)
                self.window.show()
                #self.LoginForm.hide()
                break
        if flag==False:
            print("Invalid")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Invalid Username or Password")
            msg.exec_()
        return
    def passingInfo(self):
        self.mainWindow.Regno=self.le_regno.text()
        print(self.mainWindow.Regno)
  
    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "MainWindow"))
        self.label.setText(_translate("LoginForm", "Configuration"))
        self.lbl_regno.setText(_translate("LoginForm", "Registration No"))
        self.label_5.setText(_translate("LoginForm", "Password"))
        self.btn_login.setText(_translate("LoginForm", "Login"))

class Ui_MainScreen(object):
    def __init__( self ):
        '''Initialize the super class
        '''
        super().__init__()
    def setupUi(self, MainScreen):
        
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(653, 470)
        MainScreen.setStyleSheet("background-color: rgb(150, 170, 170);")
        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 110, 541, 261))
        self.frame.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #call function for monitoring 
        self.CallFunction()
        
        self.LoginForm=Ui_LoginForm()
        
        self.login_lbl = QtWidgets.QLabel(self.frame)
        self.login_lbl.setGeometry(QtCore.QRect(60, 100, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.login_lbl.setFont(font)
        self.login_lbl.setObjectName("login_lbl")
        self.Login_btn = QtWidgets.QCommandLinkButton(self.frame)
        self.Login_btn.setGeometry(QtCore.QRect(300, 90, 185, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.Login_btn.setFont(font)
        self.Login_btn.setObjectName("Login_btn")
        self.Login_btn.clicked.connect(self.loginFunction)
        self.main_lbl = QtWidgets.QLabel(self.centralwidget)
        self.main_lbl.setGeometry(QtCore.QRect(90, 10, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.main_lbl.setFont(font)
        self.main_lbl.setObjectName("main_lbl")
        MainScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        MainScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainScreen)
        self.statusbar.setObjectName("statusbar")
        MainScreen.setStatusBar(self.statusbar)

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)
        
    def loginFunction(self):
        #path=r"C:/Users/Haier/login.txt"
        #isFile = os.path.isfile(path)
        #print(isFile)
        #if(isFile):
        #    msg = QMessageBox()
         #   msg.setWindowTitle("Information Box")
          #  msg.setText("Could'nt Login Because you have already Login to this application")
           # x = msg.exec_()            
        #else:
        self.window=QtWidgets.QMainWindow()
        self.LoginForm.setupUi(self.window)
        self.window.show()
        MainScreen.hide()
        return
    def CallFunction(self):
        path=r"C:/Users/Haier/login.txt"
        isFile = os.path.isfile(path)
        print(isFile)
        if(isFile):
            f=open("login.txt", "r")
            if f.mode == 'r':
                regNo=f.read()
                response=ur.urlopen ("http://localhost:10080/part1/tableApi.php").read().decode('UTF-8')
                data = json.loads(response)
                n= len(data)
                flag=False
                list=[]
                for i in range(n):
                    list.append((data[i]['day'],data[i]['start_at'],data[i]['end_at']))
                print(list) 
                days=[]
                strtTime=[]
                for i in list:
                    for y in i:
                        days.append(i[0])
                        now = datetime.now()
                        currentDay=now.strftime("%A") 
                        print(currentDay,i[1],i[0],i[2])
                        b = str(now.hour) + ":" + str(now.strftime("%M:%S"))  
                #         current_time = now.strftime("%h:%M:%S")
                #         print(current_time,i[1],i[0],i[2])
                        #print(b,i[1],i[0],i[2],currentDay)
                        if i[0]==currentDay and  b >= i[1] and  b <= i[2] :
                            #print("Friday",str(i[2]))
                            FMT = '%H:%M:%S'
                            tdelta = datetime.strptime(str(i[2]), FMT) - datetime.strptime(str(b), FMT)
                            totalSeconds=tdelta.total_seconds()
                            self.Monitoring(totalSeconds,regNo)
                            break
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Information error")
            msg.setText("You Have to login First")
            x = msg.exec_()            
        return 
    def predict(self,X_frame,knn_clf=None, model_path=None, distance_threshold=0.5):

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
        closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
        are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]

        # Predict classes and remove classifications that aren't within the threshold 
        for pred,loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches):
            if rec:
                return pred
            else:
                return "unknown"
    def Monitoring(self,totalSeconds,regNo):
        angry=0 
        happy=0 
        sad=0
        surprise=0
        neutral=0
        summ=0
        presentCount=0
        absentCount=0
        dateToday  = date.today()
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        video_capture = cv2.VideoCapture(0)
        end = time.time() + totalSeconds
        i=0
        while time.time() < end:
            print("monitering.....")
            ret, img = video_capture.read()
            if ret:
                img1 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
                predictions = self.predict(img1, model_path="trained_knn_model.clf")
                print(predictions)
                #Emotions prediction
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                roi_gray = cv2.resize(gray,(48,48) )
                if np.sum([roi_gray])!=0:
                    roi = roi_gray.astype('float')/255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi,axis=0)

                # make a prediction on the ROI, then lookup the class
                    preds = classifier.predict(roi)[0]
                    value=preds.argmax() 
                    if value==0:
                        angry=angry+1
                    elif value==1:
                        happy=happy+1
                    elif value==2:
                        neutral=neutral+1
                    elif value==3:
                        sad=sad+1
                    else:
                        surprise=surprise+1
                    emotion=class_labels[preds.argmax()]
                    print(emotion)
                rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                pil_im = Image.fromarray(rgb)
                b = io.BytesIO()
                pil_im.save(b, 'jpeg')
                im_bytes = b.getvalue()
                if predictions!=[]:
                    if regNo==predictions:
                        presentCount=presentCount+1
                    else:
                        absentCount=absentCount+1                    
                    SQLStatement="INSERT INTO Monitoring (regNo,Images,ImageStatus,Emotion,Date,Time) VALUES (%s,%s,%s,%s,%s,%s)"
                    mycursor .execute(SQLStatement,(regNo,im_bytes,predictions,emotion,dateToday,currentTime))
                    db_connection.commit()
            time.sleep(10 )
            i=i+1
        print("endddddd")

        summ =angry+happy+sad+surprise+neutral 
        res=[(angry/summ)*100,(happy/summ)*100,(neutral/summ)*100,(sad/summ)*100,(surprise/summ)*100]
        print(res)
        dominentEmotionPercentage=max(res)
        index=res.index(dominentEmotionPercentage)
        dominentEmotion=class_labels[index]
        print("Dominent Emotion is ", dominentEmotion)
        inactive=['Sad','Angry']
        active=['Happy','Neutral','Surprise']
        if presentCount>absentCount:
            attendence="Present"
        else:
            attendence="Absent"
        self.MarkFinalResult(inactive,regNo,dominentEmotion,dateToday,currentTime,attendence)
        # releasing web-cam
        video_capture.release()
        # Destroying output window
        cv2.destroyAllWindows()  
    def MarkFinalResult(self,list,regNo,dominentExp,dateToday,currentTime,attendence):
        for i in range(len(list)):
            if list[i] == dominentExp:
                print("Student is Non Active")
                participation='Non Attentive'
                break
            else:
                print("Attentive")
                participation='Attentive'
                break

        SQLStatement="INSERT INTO FinalReport (regNo,Attendence,DominentEmotion,Participation,Date,Time) VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor .execute(SQLStatement,(regNo,attendence,dominentExp,participation,dateToday,currentTime))
        db_connection.commit()
        return
    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "MainWindow"))
        self.login_lbl.setText(_translate("MainScreen", "Click Here to Login"))
        self.Login_btn.setText(_translate("MainScreen", "Login"))
        self.main_lbl.setText(_translate("MainScreen", "Welome To Smart Monitoring System "))
        
if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainScreen = QtWidgets.QMainWindow()
    ui = Ui_MainScreen()
    ui.setupUi(MainScreen)
    MainScreen.show()
    #MainScreen.CallFunction()
    sys.exit(app.exec_())


