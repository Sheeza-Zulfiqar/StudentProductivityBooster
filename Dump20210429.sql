-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: smartclassroom
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `finalreport`
--

DROP TABLE IF EXISTS `finalreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `finalreport` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `regNo` varchar(255) DEFAULT NULL,
  `Attendence` varchar(255) DEFAULT NULL,
  `DominentEmotion` varchar(255) DEFAULT NULL,
  `Participation` varchar(255) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` time DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `regNo` (`regNo`),
  CONSTRAINT `finalreport_ibfk_1` FOREIGN KEY (`regNo`) REFERENCES `monitoring` (`regNo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finalreport`
--

LOCK TABLES `finalreport` WRITE;
/*!40000 ALTER TABLE `finalreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `finalreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitoring`
--

DROP TABLE IF EXISTS `monitoring`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monitoring` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `regNo` varchar(255) DEFAULT NULL,
  `Images` longblob NOT NULL,
  `ImageStatus` varchar(255) DEFAULT NULL,
  `Emotion` varchar(255) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` time DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `regNo` (`regNo`),
  CONSTRAINT `monitoring_ibfk_1` FOREIGN KEY (`regNo`) REFERENCES `trainingdata` (`regNo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitoring`
--

LOCK TABLES `monitoring` WRITE;
/*!40000 ALTER TABLE `monitoring` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitoring` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject_timetable`
--

DROP TABLE IF EXISTS `subject_timetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject_timetable` (
  `std_id` int NOT NULL AUTO_INCREMENT,
  `day_name` varchar(255) DEFAULT NULL,
  `startTime` time DEFAULT NULL,
  `endTime` time DEFAULT NULL,
  PRIMARY KEY (`std_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject_timetable`
--

LOCK TABLES `subject_timetable` WRITE;
/*!40000 ALTER TABLE `subject_timetable` DISABLE KEYS */;
INSERT INTO `subject_timetable` VALUES (1,'Monday','08:00:00','08:00:00'),(2,'Tuesday','08:00:00','08:00:00'),(3,'Wednesday','08:00:00','08:00:00'),(4,'Thursday','16:00:00','16:15:00'),(5,'Friday','08:00:00','08:00:00');
/*!40000 ALTER TABLE `subject_timetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainingdata`
--

DROP TABLE IF EXISTS `trainingdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainingdata` (
  `regNo` varchar(255) NOT NULL,
  `photo` longblob NOT NULL,
  PRIMARY KEY (`regNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainingdata`
--

LOCK TABLES `trainingdata` WRITE;
/*!40000 ALTER TABLE `trainingdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `trainingdata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-29 19:54:19
