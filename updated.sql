CREATE DATABASE  IF NOT EXISTS `dcs_archiving_system` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `dcs_archiving_system`;
-- MySQL dump 10.13  Distrib 5.5.16, for Win32 (x86)
--
-- Host: localhost    Database: dcs_archiving_system
-- ------------------------------------------------------
-- Server version	5.5.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add log entry',6,'add_logentry'),(17,'Can change log entry',6,'change_logentry'),(18,'Can delete log entry',6,'delete_logentry'),(19,'Can add college',7,'add_college'),(20,'Can change college',7,'change_college'),(21,'Can delete college',7,'delete_college'),(22,'Can add department',8,'add_department'),(23,'Can change department',8,'change_department'),(24,'Can delete department',8,'delete_department'),(25,'Can add course',9,'add_course'),(26,'Can change course',9,'change_course'),(27,'Can delete course',9,'delete_course'),(28,'Can add faculty',10,'add_faculty'),(29,'Can change faculty',10,'change_faculty'),(30,'Can delete faculty',10,'delete_faculty'),(31,'Can add alternate_email',11,'add_alternate_email'),(32,'Can change alternate_email',11,'change_alternate_email'),(33,'Can delete alternate_email',11,'delete_alternate_email'),(34,'Can add contact',12,'add_contact'),(35,'Can change contact',12,'change_contact'),(36,'Can delete contact',12,'delete_contact'),(37,'Can add address',13,'add_address'),(38,'Can change address',13,'change_address'),(39,'Can delete address',13,'delete_address'),(40,'Can add transaction',14,'add_transaction'),(41,'Can change transaction',14,'change_transaction'),(42,'Can delete transaction',14,'delete_transaction'),(43,'Can add file',15,'add_file'),(44,'Can change file',15,'change_file'),(45,'Can delete file',15,'delete_file'),(46,'Can add action',16,'add_action'),(47,'Can change action',16,'change_action'),(48,'Can delete action',16,'delete_action'),(49,'Can add log',17,'add_log'),(50,'Can change log',17,'change_log'),(51,'Can delete log',17,'delete_log');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','Admin First','Admin Last','admin@yahoo.com','pbkdf2_sha256$10000$IItMsSxO2XHJ$UCiKmeuTuSp3RGoRd7pVAeJoaP7OmVt73ddDGCGpdAE=',1,1,1,'2013-02-07 14:09:47','2013-01-28 07:20:57');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`),
  CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2013-01-28 07:23:06',1,7,'1','Engineering',1,''),(2,'2013-01-28 07:23:07',1,8,'1','Computer Science, Engineering',1,''),(3,'2013-01-28 07:23:08',1,9,'1','BS Computer Science, Computer Science',1,''),(4,'2013-01-28 07:24:10',1,3,'2','user1',1,''),(5,'2013-01-28 07:25:02',1,3,'2','user1',2,'Changed password, first_name, last_name and email.'),(6,'2013-02-01 07:47:48',1,3,'3','user2',1,''),(7,'2013-02-01 07:54:53',1,3,'4','user3',1,''),(8,'2013-02-01 08:03:10',1,3,'3','user2',3,''),(9,'2013-02-01 08:03:10',1,3,'4','user3',3,''),(10,'2013-02-01 08:04:13',1,3,'5','user2',1,''),(11,'2013-02-01 08:04:33',1,3,'5','user2',2,'Changed password.'),(12,'2013-02-01 08:05:58',1,3,'5','user2',2,'Changed password, first_name, last_name and email.'),(13,'2013-02-01 08:13:38',1,3,'1','cha',2,'Changed password, first_name and last_name.'),(14,'2013-02-01 08:13:54',1,3,'1','cha',2,'Changed password. Added contact \"09064565456\".'),(15,'2013-02-01 08:22:52',1,14,'1','Resource 1',1,''),(16,'2013-02-01 08:24:51',1,14,'1','Resource 1',3,''),(17,'2013-02-01 08:25:16',1,14,'2','Leave of Absence',1,''),(18,'2013-02-01 08:25:57',1,14,'3','1',1,''),(19,'2013-02-01 08:27:39',1,14,'4','Leave of Absence',1,''),(20,'2013-02-01 08:29:46',1,14,'4','Leave of Absence',3,''),(21,'2013-02-01 08:29:46',1,14,'3','1',3,''),(22,'2013-02-05 17:20:49',1,3,'1','cha',2,'Changed password.'),(23,'2013-02-05 17:22:06',1,3,'1','cha',2,'Changed password. Changed first_name, middle_name, last_name, photo, birthday, course, highest_degree_attained and length_of_service for faculty \"Faculty object\".'),(24,'2013-02-05 17:24:47',1,3,'6','User4',1,''),(25,'2013-02-05 17:26:11',1,3,'6','User4',2,'Changed password, first_name, last_name and email. Changed first_name, middle_name, last_name, photo, birthday, course, highest_degree_attained and length_of_service for faculty \"Faculty object\".'),(26,'2013-02-05 19:03:27',1,3,'1','admin',2,'Changed username, password, first_name, last_name and email. Changed first_name, middle_name, last_name and photo for faculty \"Faculty object\".'),(27,'2013-02-05 19:03:42',1,3,'2','user1',2,'Changed password. Changed photo for faculty \"Faculty object\".'),(28,'2013-02-05 19:03:57',1,3,'5','user2',2,'Changed password. Changed photo for faculty \"Faculty object\".'),(29,'2013-02-05 19:04:08',1,3,'6','User4',2,'Changed password. Changed photo for faculty \"Faculty object\".'),(30,'2013-02-05 19:04:49',1,3,'7','user5',1,''),(31,'2013-02-05 19:05:20',1,3,'7','user5',2,'Changed password, first_name, last_name and email.'),(32,'2013-02-05 19:05:38',1,3,'6','user4',2,'Changed username and password.'),(33,'2013-02-07 04:39:22',1,3,'2','user1',3,''),(34,'2013-02-07 04:39:22',1,3,'5','user2',3,''),(35,'2013-02-07 04:39:22',1,3,'6','user4',3,''),(36,'2013-02-07 04:39:22',1,3,'7','user5',3,''),(37,'2013-02-07 04:43:26',1,3,'1','admin',2,'Changed password. Added faculty \"Faculty object\". Added faculty \"Faculty object\". Added faculty \"Faculty object\". Added faculty \"Faculty object\". Changed first_name, middle_name, last_name and highest_degree_attained for faculty \"Faculty object\".'),(38,'2013-02-07 04:43:40',1,3,'1','admin',2,'Changed password.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'log entry','admin','logentry'),(7,'college','testapp','college'),(8,'department','testapp','department'),(9,'course','testapp','course'),(10,'faculty','testapp','faculty'),(11,'alternate_email','testapp','alternate_email'),(12,'contact','testapp','contact'),(13,'address','testapp','address'),(14,'transaction','testapp','transaction'),(15,'file','testapp','file'),(16,'action','testapp','action'),(17,'log','testapp','log');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1ab67a8ea19971720fa9255ad6db0b7e','ZmYxYjcwNjI2OTI1NzJjODg4NWE3NmZiYjJhNTA0OTM3Y2M5MzMxMzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQV1Lg==\n','2013-02-20 12:59:48'),('66f05780465e977ad1ce5acbfc3ae1cf','MDk4ZTI1ZjFlNjJhMjI4NGYxMDgwZTFlMjM0OTQ0YmQyNzRhMTM2MjqAAn1xAS4=\n','2013-02-21 14:09:53');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_action`
--

DROP TABLE IF EXISTS `testapp_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_action`
--

LOCK TABLES `testapp_action` WRITE;
/*!40000 ALTER TABLE `testapp_action` DISABLE KEYS */;
/*!40000 ALTER TABLE `testapp_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_address`
--

DROP TABLE IF EXISTS `testapp_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testapp_address_403f60f` (`user_id`),
  CONSTRAINT `user_id_refs_id_d540a6f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_address`
--

LOCK TABLES `testapp_address` WRITE;
/*!40000 ALTER TABLE `testapp_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `testapp_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_alternate_email`
--

DROP TABLE IF EXISTS `testapp_alternate_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_alternate_email` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `email_address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testapp_alternate_email_403f60f` (`user_id`),
  CONSTRAINT `user_id_refs_id_5d6248bc` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_alternate_email`
--

LOCK TABLES `testapp_alternate_email` WRITE;
/*!40000 ALTER TABLE `testapp_alternate_email` DISABLE KEYS */;
/*!40000 ALTER TABLE `testapp_alternate_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_college`
--

DROP TABLE IF EXISTS `testapp_college`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_college`
--

LOCK TABLES `testapp_college` WRITE;
/*!40000 ALTER TABLE `testapp_college` DISABLE KEYS */;
INSERT INTO `testapp_college` VALUES (1,'Engineering');
/*!40000 ALTER TABLE `testapp_college` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_contact`
--

DROP TABLE IF EXISTS `testapp_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testapp_contact_403f60f` (`user_id`),
  CONSTRAINT `user_id_refs_id_307af2e3` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_contact`
--

LOCK TABLES `testapp_contact` WRITE;
/*!40000 ALTER TABLE `testapp_contact` DISABLE KEYS */;
INSERT INTO `testapp_contact` VALUES (4,1,'09064565456');
/*!40000 ALTER TABLE `testapp_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_course`
--

DROP TABLE IF EXISTS `testapp_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testapp_course_2ae7390` (`department_id`),
  CONSTRAINT `department_id_refs_id_25a042f2` FOREIGN KEY (`department_id`) REFERENCES `testapp_department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_course`
--

LOCK TABLES `testapp_course` WRITE;
/*!40000 ALTER TABLE `testapp_course` DISABLE KEYS */;
INSERT INTO `testapp_course` VALUES (1,'BS Computer Science',1);
/*!40000 ALTER TABLE `testapp_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_department`
--

DROP TABLE IF EXISTS `testapp_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `college_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testapp_department_6d2e0b0` (`college_id`),
  CONSTRAINT `college_id_refs_id_430833cf` FOREIGN KEY (`college_id`) REFERENCES `testapp_college` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_department`
--

LOCK TABLES `testapp_department` WRITE;
/*!40000 ALTER TABLE `testapp_department` DISABLE KEYS */;
INSERT INTO `testapp_department` VALUES (1,'Computer Science',1);
/*!40000 ALTER TABLE `testapp_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_faculty`
--

DROP TABLE IF EXISTS `testapp_faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_faculty` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(64) DEFAULT NULL,
  `middle_name` varchar(32) DEFAULT NULL,
  `last_name` varchar(32) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `highest_degree_attained` varchar(100) DEFAULT NULL,
  `length_of_service` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `testapp_faculty_403f60f` (`user_id`),
  KEY `testapp_faculty_b7271b` (`course_id`),
  CONSTRAINT `course_id_refs_id_5895d879` FOREIGN KEY (`course_id`) REFERENCES `testapp_course` (`id`),
  CONSTRAINT `user_id_refs_id_1274dc6f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_faculty`
--

LOCK TABLES `testapp_faculty` WRITE;
/*!40000 ALTER TABLE `testapp_faculty` DISABLE KEYS */;
INSERT INTO `testapp_faculty` VALUES (1,1,'Edgar','Middle','Felizmenio','photos/sir_edgar.jpg','2013-02-06',1,'Masterals','1 year'),(13,1,'Paul','Middle','Regonia','photos/sir_paul_1.jpg','2013-02-11',1,'Masterals','2 years'),(14,1,'Lester','Middle','Nacu','photos/sir_lester_1.jpg','2013-02-26',1,'Graduate','2 years'),(15,1,'Wilson','Middle','Tan','photos/sir_tan_1.jpg','2013-02-03',1,'Masterals','5 years'),(16,1,'Zuniga','Middle','Philip','photos/sir_philip_1.jpg','2013-02-07',1,'Masterals','5 years');
/*!40000 ALTER TABLE `testapp_faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_file`
--

DROP TABLE IF EXISTS `testapp_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `transaction_id` int(11) NOT NULL,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testapp_file_403f60f` (`user_id`),
  KEY `testapp_file_45d19ab3` (`transaction_id`),
  CONSTRAINT `transaction_id_refs_id_7cc4d790` FOREIGN KEY (`transaction_id`) REFERENCES `testapp_transaction` (`id`),
  CONSTRAINT `user_id_refs_id_413e793e` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_file`
--

LOCK TABLES `testapp_file` WRITE;
/*!40000 ALTER TABLE `testapp_file` DISABLE KEYS */;
/*!40000 ALTER TABLE `testapp_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_log`
--

DROP TABLE IF EXISTS `testapp_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `action_id` int(11) NOT NULL,
  `file_id` int(11) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `testapp_log_403f60f` (`user_id`),
  KEY `testapp_log_206b3f10` (`action_id`),
  KEY `testapp_log_2243e3be` (`file_id`),
  CONSTRAINT `action_id_refs_id_3b2dc6de` FOREIGN KEY (`action_id`) REFERENCES `testapp_action` (`id`),
  CONSTRAINT `file_id_refs_id_6b0688f8` FOREIGN KEY (`file_id`) REFERENCES `testapp_file` (`id`),
  CONSTRAINT `user_id_refs_id_29582d5f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_log`
--

LOCK TABLES `testapp_log` WRITE;
/*!40000 ALTER TABLE `testapp_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `testapp_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testapp_transaction`
--

DROP TABLE IF EXISTS `testapp_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testapp_transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testapp_transaction`
--

LOCK TABLES `testapp_transaction` WRITE;
/*!40000 ALTER TABLE `testapp_transaction` DISABLE KEYS */;
INSERT INTO `testapp_transaction` VALUES (2,'Leave of Absence');
/*!40000 ALTER TABLE `testapp_transaction` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-02-07 22:51:50
