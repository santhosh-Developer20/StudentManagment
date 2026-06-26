-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: studentrecords
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `Course_ID` int NOT NULL AUTO_INCREMENT,
  `Course_code` char(6) DEFAULT NULL,
  `Course_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Course_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'CO2724','COMPUTER SCIENCE ENGINEERING(CSE)'),(2,'EL2220','ELECTRONICS COMMUNUCATION ENGINEERING(ECE)'),(3,'IN2141','INFORMATION TECHNOLOGY(IT)'),(4,'EL5178','ELECTRICAL ELECTRONICS ENGINEERING(EEE)'),(5,'ME1699','MECHANICAL ENGINEERING'),(6,'CI2495','CIVIL ENGINEERING'),(7,'CH2326','CHEMICAL ENGINEERING'),(8,'RO7519','ROBOTICS AND AUTOMATION'),(9,'AR4893','ARTIFICIAL INTELLIGENCE AND DATA SCIENCE'),(10,'CY3605','CYBERSECURITY ENGINEERING'),(11,'CI5555','CIVIL ENGINEERING');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrollments`
--

DROP TABLE IF EXISTS `enrollments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollments` (
  `Enrollment_ID` int NOT NULL AUTO_INCREMENT,
  `Student_ID` int DEFAULT NULL,
  `Course_ID` int DEFAULT NULL,
  `Enrollment_Date` date DEFAULT NULL,
  PRIMARY KEY (`Enrollment_ID`),
  KEY `Student_ID` (`Student_ID`),
  KEY `Course_ID` (`Course_ID`),
  CONSTRAINT `enrollments_ibfk_1` FOREIGN KEY (`Student_ID`) REFERENCES `students` (`Student_ID`),
  CONSTRAINT `enrollments_ibfk_2` FOREIGN KEY (`Course_ID`) REFERENCES `course` (`Course_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollments`
--

LOCK TABLES `enrollments` WRITE;
/*!40000 ALTER TABLE `enrollments` DISABLE KEYS */;
INSERT INTO `enrollments` VALUES (1,1,1,'2026-06-25'),(2,2,5,'2026-06-25'),(3,3,9,'2026-06-25'),(4,4,1,'2026-06-25'),(5,5,8,'2026-06-25'),(6,6,10,'2026-06-25'),(7,7,6,'2026-06-25'),(8,8,7,'2026-06-25'),(9,9,4,'2026-06-25'),(10,10,3,'2026-06-25'),(11,11,1,'2026-06-26'),(12,12,5,'2026-06-26');
/*!40000 ALTER TABLE `enrollments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `Student_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Phone` varchar(15) NOT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `Admission_year` year DEFAULT NULL,
  PRIMARY KEY (`Student_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'SANTHOSH KUMAR','2009-05-20','MALE','santhoshkumar@gmail.com','6381923936','COMPUUTER SCIENCE',2026),(2,'BALAJI','2008-07-10','MALE','balaji32@gmail.com','5646373838','MECHANICAL ',2026),(3,'KARTHIK','2008-03-12','MALE','karthiakandan@gmail.com','6457894738','ARTIFICIAL INTELLIGENCE',2026),(4,'HEMAMALINI','2002-05-18','FEMALE','hemamalini876@gmail.com','6380532101','COMPUTER SCIENCE',2026),(5,'NITHIN KUMAR','2008-07-12','MALE','nithinkumar@gmail.com','6728282828','ROBOTICS ',2026),(6,'ARISWAR','2008-12-11','MALE','ariswar@gmail.com','7329292929','CYBERSECURITY',2026),(7,'MONIKA','2008-06-09','FEMALE','monika@gmail.com','6402028492','CIVIL ENGINEERING',2026),(8,'MADUMITHA','2008-06-09','FEMALE','madumitha@gmail.com','6748204829','CHEMICAL ENGINEERING',2026),(9,'NARANE','2008-08-27','MALE','narane453@gmail.com','9836736336','ELECTRICAL AND ELECTRONICS',2026),(10,'THARANIDHARAN','2009-07-08','MALE','tharanidharan@gmail.com','8936363636','INFORMATION TECHNOLOGY',2026),(11,'SANTHOSH','2009-09-09','MALE','santhosh@gmail.com','6309303930','COMPUTER SCIENCE',2006),(12,'BALAJI','2008-09-09','MALE','balaji@gmail.comn','2828282828','MACHANICAL',2026);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-26 13:13:37
