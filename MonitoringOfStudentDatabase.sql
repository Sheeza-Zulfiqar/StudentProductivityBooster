Create Database MonitorigOfStudent;
use MonitorigOfStudent;
show tables;
CREATE TABLE IF NOT EXISTS Trainingdata
 (regNo varchar(255) NOT NULL AUTO_INCREMENT PRIMARY KEY,
 photo LONGBLOB not null);
  select * from Trainingdata;
 CREATE TABLE IF NOT EXISTS Monitoring (
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    regNo varchar(255),
    Images LONGBLOB NOT NULL,
    ImageStatus varchar(255),
    Emotion varchar(255),
	Date date, 
    Time time,
    FOREIGN KEY (regNo) REFERENCES Trainingdata(regNo)
);
select * from Monitoring;
 CREATE TABLE IF NOT EXISTS FinalReport (
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    regNo varchar(255),
    Attendence varchar(255),
    DominentEmotion varchar(255),
	Participation varchar(255),
    Date date, 
    Time time,
    FOREIGN KEY (regNo) REFERENCES Monitoring(regNo)
);
select * from FinalReport;