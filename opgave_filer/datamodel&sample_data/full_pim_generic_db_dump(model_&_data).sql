CREATE DATABASE  IF NOT EXISTS `pim_generic` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `pim_generic`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: pim_generic
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `construction`
--

DROP TABLE IF EXISTS `construction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `construction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `specifications` text,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `manager_id` int NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `construction_manager_idx` (`manager_id`),
  CONSTRAINT `construction_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  CONSTRAINT `construction_manager` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `construction`
--

LOCK TABLES `construction` WRITE;
/*!40000 ALTER TABLE `construction` DISABLE KEYS */;
INSERT INTO `construction` VALUES (1,'Sommerskjorte','Stil: Sommerskjorte med korte ??rmer - Materiale: 100% bomuldsstof - Farve: Lysebl?? med hvide prikker - St??rrelse: S, M, L, XL - Pasform: L??s og afslappet - Knapper: 5 knapper i matchende farve - Lommer: En lille lomme p?? venstre bryst - Halsudsk??ring: Rundet hals med krave - ??rmer: Korte ??rmer med manchetter - M??rkning: Brandlogo p?? venstre bryst - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','2022-09-22','2022-10-17',5,1),(2,'Kjole med blomsterprint','Stil: Sommerkjole med blomsterprint - Materiale: 100% bomuldsstof med blomsterprint - Farve: Lysegr??n med hvide blomster - St??rrelse: XS, S, M, L, XL - Pasform: L??s og afslappet - Lynl??s: En lynl??s i ryggen - Skulderstropper: Skulderstropper i matchende farve - L??ngde: Kjolen skal have en l??ngde p?? midten af l??ret - M??rkning: Brandlogo i nederste h??jre hj??rne - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','2022-09-23','2022-10-18',5,2),(3,'Solbriller med pilotstel','Stil: Solbriller med pilotstel - Materiale: 100% UV-beskyttende plastik - Farve: Sort med sorte st??nger - St??rrelse: En st??rrelse, der passer de fleste ansigter - St??nger: Justerbare st??nger i matchende farve - Glas: Runde glas med m??rk toning - M??rkning: Brandlogo p?? hver stang - ??vrigt: Skal leveres i en lille sort pose med brandlogo','2022-09-24','2022-10-19',5,3),(4,'Hat med kant','Stil: Hat med kant - Materiale: 100% bomuldsstof med kant - Farve: Hvid med sort kant - St??rrelse: En st??rrelse, der passer de fleste hoveder - Form: Rund med kant hele vejen rundt - M??rkning: Brandlogo i nederste h??jre hj??rne - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','2022-09-25','2022-10-20',5,4),(5,'Sandaler med ankelrem',NULL,NULL,NULL,5,5),(6,'Strandtaske',NULL,NULL,NULL,5,6),(7,'Tanktop med racerryg',NULL,NULL,NULL,5,7),(8,'T-shirt med print',NULL,NULL,NULL,5,8),(9,'Bikini med bandeau-top',NULL,NULL,NULL,5,9),(10,'Let regnfrakke',NULL,NULL,NULL,5,10),(11,'Shorts med r?? kanter',NULL,NULL,NULL,5,11),(12,'Sportstaske med lynl??s',NULL,NULL,NULL,5,12);
/*!40000 ALTER TABLE `construction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `design`
--

DROP TABLE IF EXISTS `design`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `design` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `specifications` text,
  `beskrivelse` text,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `manager_id` int NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `design_manager_idx` (`manager_id`),
  CONSTRAINT `design_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  CONSTRAINT `design_manager` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `design`
--

LOCK TABLES `design` WRITE;
/*!40000 ALTER TABLE `design` DISABLE KEYS */;
INSERT INTO `design` VALUES (1,'Sommerskjorte','Stil: Sommerskjorte med korte ??rmer - Materiale: 100% bomuldsstof - Farve: Lysebl?? med hvide prikker - St??rrelse: S, M, L, XL - Pasform: L??s og afslappet - Knapper: 5 knapper i matchende farve - Lommer: En lille lomme p?? venstre bryst - Halsudsk??ring: Rundet hals med krave - ??rmer: Korte ??rmer med manchetter - M??rkning: Brandlogo p?? venstre bryst - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','Sommerskjorte: \"Vores f??rste udkast til design af sommerskjorten er en let og luftig skjorte i et friskt og sommerligt m??nster. Skjorten vil have en klassisk pasform med en knapkant ned langs fronten og korte ??rmer. Vi vil bruge en bl??d og behagelig bomuldsstof, der vil v??re let at vedligeholde og bevare sin form. Vores m??l med designet er at skabe en skjorte, der vil v??re en fast bestanddel af din sommergarderobe.\"','2022-09-08','2022-09-21',4,1),(2,'Kjole med blomsterprint','Stil: Sommerkjole med blomsterprint - Materiale: 100% bomuldsstof med blomsterprint - Farve: Lysegr??n med hvide blomster - St??rrelse: XS, S, M, L, XL - Pasform: L??s og afslappet - Lynl??s: En lynl??s i ryggen - Skulderstropper: Skulderstropper i matchende farve - L??ngde: Kjolen skal have en l??ngde p?? midten af l??ret - M??rkning: Brandlogo i nederste h??jre hj??rne - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','Kjole med blomsterprint: \"Vores f??rste udkast til design af kjolen med blomsterprint er en smuk og feminin kjole med et farverigt og sprudlende blomsterprint. Kjolen vil have en A-formet silhuet med en halterneck-top og en udsk??ring ved taljen. Vi vil bruge et let og str??kbart stof, der vil f??lge kroppens bev??gelser og f??les behageligt at have p??. Vores m??l med designet er at skabe en kjole, der vil f?? dig til at f??le sig godt tilpas og femine p?? samme tid.','2022-09-09','2022-09-22',4,2),(3,'Solbriller med pilotstel','Stil: Solbriller med pilotstel - Materiale: 100% UV-beskyttende plastik - Farve: Sort med sorte st??nger - St??rrelse: En st??rrelse, der passer de fleste ansigter - St??nger: Justerbare st??nger i matchende farve - Glas: Runde glas med m??rk toning - M??rkning: Brandlogo p?? hver stang - ??vrigt: Skal leveres i en lille sort pose med brandlogo','Solbriller med pilotstel: \"Vores f??rste udkast til design af solbrillerne med pilotstel er et par solbriller i et klassisk og stilfuldt pilotstel. Solbrillerne vil have en roundet ramme i sort plastik med en m??rk og reflekterende lins, der vil beskytte dine ??jne mod solen. Vi vil bruge et st??rkt og b??jeligt stof til stellet, der vil holde sig p?? plads og v??re behageligt at have p??. Vores m??l med designet er at skabe et par solbriller, der vil give dig et cool og afslappet look, uanset om du er p?? stranden eller i byen.\"','2022-09-10','2022-09-23',4,3),(4,'Hat med kant','Stil: Hat med kant - Materiale: 100% bomuldsstof med kant - Farve: Hvid med sort kant - St??rrelse: En st??rrelse, der passer de fleste hoveder - Form: Rund med kant hele vejen rundt - M??rkning: Brandlogo i nederste h??jre hj??rne - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','Hat med kant: \"Vores f??rste udkast til design af hatte med kant er en solhat med en stilfuld kant, der vil beskytte dit ansigt mod solen og holde dig k??lig. Hatte med kant vil have en bred skygge i et lyst og sommerligt farve.','2022-09-11','2022-09-24',4,4),(5,'Sandaler med ankelrem','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','Sandaler med ankelrem: \"Vores f??rste udkast til design af sandalerne med ankelrem er et par komfortable og tidsl??se sandaler med en justerbar ankelrem, der vil give dig god st??tte og holde f??dderne t??rre. Sandalerne vil have en bred sko med en h??l, der ikke er for h??j, og en st??rk ankelrem, der vil holde skoen p?? plads. Vi vil bruge et bl??dt og ??ndbart stof til inders??len, der vil give dine f??dder god komfort og ??ndbarhed. Vores m??l med designet er at skabe et par sandaler, der vil v??re behagelige at have p?? og give dig en god st??tte, uanset om du er p?? stranden eller i byen.\"','2022-10-20',NULL,4,5),(6,'Strandtaske','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','Strandtaske: \"Vores f??rste udkast til design af strandtasken er en rummelig og stilfuld strandtaske, der vil holde dine ting sikre og organiseret, mens du nyder solen og stranden. Strandtasken vil have en stor lomme med lynl??s p?? fronten og to mindre lommer p?? siden, der vil give dig plads til alt, hvad du beh??ver. Vi vil bruge et st??rkt og vandafvisende stof, der vil holde dine ting t??rre, selv n??r der er lidt regn. Vores m??l med designet er at skabe en strandtaske, der vil v??re praktisk og stilfuld p?? samme tid.\"','2022-10-21',NULL,4,6),(7,'Tanktop med racerryg','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','Tanktop med racerryg: \"Vores f??rste udkast til design af tanktopet med racerryg er et l??kkert og bl??dt tanktop med racerryg, der vil fremh??ve din figur og f?? dig til at f??le dig sekset. Tanktopet vil have en racerback-design med brede stropper og en l??s pasform, der vil give dig god bev??gelsesfrihed. Vi vil bruge et ??ndbart og svedtransporterende stof, der vil holde dig t??r og komfortable, selv n??r temperaturen stiger. Vores m??l med designet er at skabe et tanktop, der vil v??re behageligt at have p?? og g??re dig klar til at nyde sommeren i fuld styrke.\"','2022-10-22',NULL,4,7),(8,'T-shirt med print','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','T-shirt med print: \"Vores f??rste udkast til design af T-shirten med print er en cool og komfortabel t-shirt med et trendy print, der vil give dig et unikt og personligt look. T-shirten vil have en rund hals og en normal pasform, der vil give dig god bev??gelsesfrihed og en afslappet stil. Vi vil bruge et bl??dt og ??ndbart stof, der vil v??re behageligt at have p?? og give dig en god f??lelse hele dagen. Vores m??l med designet er at skabe en t-shirt, der vil v??re en fast bestanddel af din sommergarderobe og give dig et cool og casual look.\"','2022-10-23',NULL,4,8),(9,'Bikini med bandeau-top','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','Bikini med bandeau-top: \"Vores f??rste udkast til design af bikini med bandeau-top er et moderne og st??ttende bikini-s??t med en bandeau-top, der vil fremh??ve dine skuldre og g??re dig klar til at nyde livet p?? stranden. Bikini med bandeau-top vil have en h??j talje og en st??ttende b??jle i topen, der vil give dig god st??tte og komfort. Vi vil bruge et bl??dt og st??rkt stof, der vil holde sig p?? plads og bevare sin form, selv n??r du sv??mmer. Vores m??l med designet er at skabe et bikini-s??t, der vil give dig en smuk og sexet silhouette og f?? dig til at f??le dig fantastisk p?? stranden.\"','2022-10-24',NULL,4,9),(10,'Let regnfrakke','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','Let regnfrakke: \"Vores f??rste udkast til design af regnfrakken er en let og praktisk regnfrakke, der vil holde dig t??r, uanset vejret, og samtidig give dig et stilfuldt og trendy look. Regnfrakken vil have en l??s pasform med lange ??rmer og en h??j krave, der vil give dig god d??kning og komfort. Vi vil bruge et st??rkt og vandafvisende stof, der vil holde dine ting t??rre, selv n??r det regner meget. Vores m??l med designet er at skabe en regnfrakke, der vil v??re let at have med sig og give dig et stilfuldt og trendy look, uanset vejret.\"','2022-10-25',NULL,4,10),(11,'Shorts med r?? kanter','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','Shorts med r?? kanter: \"Vores f??rste udkast til design af shorts med r?? kanter er et par komfortable og tidsl??se shorts med r?? kanter, der vil give dig et afslappet og cool look. Shorts med r?? kanter vil have en l??s pasform med en elastisk linning og r?? kanter ved benene, der vil give dig god bev??gelsesfrihed og en unik stil. Vi vil bruge et bl??dt og ??ndbart stof, der vil v??re behageligt at have p?? og holde sig p?? plads, selv n??r du bev??ger dig meget. Vores m??l med designet er at skabe et par shorts, der vil v??re en fast bestanddel af din sommergarderobe og give dig et afslappet og trendy look.\"','2022-10-26',NULL,4,11),(12,'Sportstaske med lynl??s','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','Sportstaske med lynl??s: \"Vores f??rste udkast til design af sportstasken med lynl??s er en rummelig og st??rk sportstaske med en l??kker lynl??s, der vil holde dine ting sikre og organiseret, mens du er p?? farten. Sportstasken vil have to store rum med lynl??s p?? fronten og to mindre lommer p?? siden, der vil give dig plads til alt, hvad du beh??ver. Vi vil bruge et st??rkt og vandafvisende stof, der vil holde dine ting t??rre, selv n??r det regner. Vores m??l med designet er at skabe en sportstaske, der vil v??re praktisk og st??rk p?? samme tid og give dig en god m??de at b??re dine ting p??, n??r du er p?? farten.\"','2022-10-27',NULL,4,12);
/*!40000 ALTER TABLE `design` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `role` varchar(150) DEFAULT NULL,
  `supervisor` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `employee_supervisor_idx` (`supervisor`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Kim','CEO',NULL),(2,'Jesper','Portef??lgechef',1),(3,'Karl','Projektleder',2),(4,'Hans','designleder',3),(5,'Brian','konstrukt??rleder',3),(6,'Svend','prototypeleder',3),(7,'Thomas','Designer',4),(8,'Lars','Designer',4),(9,'William','Designer',4),(10,'Victor','Designer',4),(11,'Karsten','Konstrukt??r',5),(12,'S??ren','Konstrukt??r',5),(13,'Kurt','Konstrukt??r',5),(14,'Steffan','Prototyper',6),(15,'Steen','Prototyper',6),(16,'Per','Prototyper',6),(17,'Ole','Prototyper',6),(18,'Markus','Prototyper',6);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio`
--

DROP TABLE IF EXISTS `portfolio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `portfolio` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio`
--

LOCK TABLES `portfolio` WRITE;
/*!40000 ALTER TABLE `portfolio` DISABLE KEYS */;
INSERT INTO `portfolio` VALUES (1,'FODT??J','Portef??lge til projekter inden for fodt??jsprodukter'),(2,'BUKSER','Portef??lge til projekter inden for bukser'),(3,'T-SHIRTS','Portef??lge til projekter inden for T-shirts'),(4,'JAKKER','Portef??lge til projekter inden for jakker'),(5,'KOMBI KOLLEKTION','Portef??lge til specielle kombi kollektioner');
/*!40000 ALTER TABLE `portfolio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  `manager_id` int NOT NULL,
  `project_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  KEY `product_employee_idx` (`manager_id`),
  CONSTRAINT `product_employee` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Sommerskjorte','En let og luftig skjorte i et friskt m??nster, perfekt til varme sommerdage.',3,11),(2,'Kjole med blomsterprint','En smuk og feminin kjole med et farverigt blomsterprint, der vil f?? dig til at skille dig ud.',3,11),(3,'Solbriller med pilotstel','Et par solbriller i et klassisk pilotstel, der vil give dig et cool og afslappet look.',3,11),(4,'Hat med kant','En solhat med en stilfuld kant, der vil beskytte dit ansigt mod solen og holde dig k??lig.',3,11),(5,'Sandaler med ankelrem','Et par komfortable sandaler med en justerbar ankelrem, der vil give dig god st??tte og holde f??dderne t??rre.',3,11),(6,'Strandtaske','En rummelig og stilfuld strandtaske, der vil holde dine ting sikre og organiseret, mens du nyder solen og stranden.',3,11),(7,'Tanktop med racerryg','Et l??kkert og bl??dt tanktop med racerryg, der vil fremh??ve din figur og f?? dig til at f??le dig sekset.',3,11),(8,'T-shirt med print','En cool og komfortabel t-shirt med et trendy print, der vil give dig et unikt og personligt look.',3,11),(9,'Bikini med bandeau-top','Et moderne og st??ttende bikini-s??t med en bandeau-top, der vil fremh??ve dine skuldre og g??re dig klar til at nyde livet p?? stranden.',3,11),(10,'Let regnfrakke','En let og praktisk regnfrakke, der vil holde dig t??r, uanset vejret, og samtidig give dig et stilfuldt og trendy look.',3,11),(11,'Shorts med r?? kanter','Et par komfortable og tidsl??se shorts med r?? kanter, der vil give dig et afslappet og cool look.',3,11),(12,'Sportstaske med lynl??s','En rummelig og st??rk sportstaske med en l??kker lynl',3,11);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  `start_date` date NOT NULL,
  `est_end_date` date NOT NULL,
  `ended_date` date DEFAULT NULL,
  `manager_id` int NOT NULL,
  `portfolio_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `portfolio_id` (`portfolio_id`),
  KEY `project_employee_idx` (`manager_id`),
  CONSTRAINT `project_employee` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `project_ibfk_1` FOREIGN KEY (`portfolio_id`) REFERENCES `portfolio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'Sommersandaler 2019','Projekt til at lave kollektionen indenfor: Sommersandaler 2019','2018-09-05','2019-03-24','2019-06-12',2,1),(2,'Vinterst??vler 2020','Projekt til at lave kollektionen indenfor:  Vinterst??vler 2020','2019-02-01','2019-08-20','2019-10-30',2,1),(3,'Crocs Look-a-like','Projekt til at lave kollektionen indenfor:  Crocs Look-a-like','2018-09-20','2019-04-08','2019-08-03',2,1),(4,'Hel??rssko Trendy 2021','Projekt til at lave kollektionen indenfor:  Hel??rssko Trendy 2021','2020-04-08','2020-10-25','2020-11-12',2,1),(5,'Vinterst??vler 2022','Projekt til at lave kollektionen indenfor:  Vinterst??vler 2022','2021-02-02','2021-08-21','2022-03-09',2,1),(6,'Klassisk Jeanwear','Projekt til at lave kollektionen indenfor:  Klassisk Jeanwear','2021-09-20','2022-04-08','2022-06-23',2,2),(7,'H??rbukser Sommmer 2022','Projekt til at lave kollektionen indenfor:  H??rbukser Sommmer 2022','2021-09-25','2022-04-13','2022-10-30',2,2),(8,'Slim-Fit Jeans 2022','Projekt til at lave kollektionen indenfor:  Slim-Fit Jeans 2022','2021-09-26','2022-04-14','2022-10-30',2,2),(9,'Arbejdsbukser - Generisk','Projekt til at lave kollektionen indenfor:  Arbejdsbukser - Generisk','2022-03-01','2022-09-17',NULL,2,2),(10,'Outdoor - Vinterbukser','Projekt til at lave kollektionen indenfor:  Outdoor - Vinterbukser','2022-07-07','2023-01-23',NULL,2,2),(11,'Sommerkollektion 2023','Vores Sommerkollektion 2022 byder p?? et bredt udvalg af l??kre og stilfulde produkter, der vil f?? dig til at skille dig ud og nyde livet i solen. Fra lette og luftige skjorter til farverige kjoler og solbriller med pilotstel, vil du finde alt, hvad du beh??ver for at opdatere din garderobe og f??le dig sommerklar. Med vores unikke designs og kvalitetsmaterialer vil du se og f??le dig fantastisk i vores Sommerkollektion 2022.','2022-09-08','2023-03-27',NULL,2,5);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prototype`
--

DROP TABLE IF EXISTS `prototype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prototype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `specifications` text,
  `start_date` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  `manager_id` int NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `prototype_manager_idx` (`manager_id`),
  CONSTRAINT `prototype_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  CONSTRAINT `prototype_manager` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prototype`
--

LOCK TABLES `prototype` WRITE;
/*!40000 ALTER TABLE `prototype` DISABLE KEYS */;
INSERT INTO `prototype` VALUES (1,'Sommerskjorte','Stil: Sommerskjorte med korte ??rmer - Materiale: 100% bomuldsstof - Farve: Lysebl?? med hvide prikker - St??rrelse: S, M, L, XL - Pasform: L??s og afslappet - Knapper: 5 knapper i matchende farve - Lommer: En lille lomme p?? venstre bryst - Halsudsk??ring: Rundet hals med krave - ??rmer: Korte ??rmer med manchetter - M??rkning: Brandlogo p?? venstre bryst - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','2022-10-17','2022-11-28',6,1),(2,'Kjole med blomsterprint','Stil: Sommerkjole med blomsterprint - Materiale: 100% bomuldsstof med blomsterprint - Farve: Lysegr??n med hvide blomster - St??rrelse: XS, S, M, L, XL - Pasform: L??s og afslappet - Lynl??s: En lynl??s i ryggen - Skulderstropper: Skulderstropper i matchende farve - L??ngde: Kjolen skal have en l??ngde p?? midten af l??ret - M??rkning: Brandlogo i nederste h??jre hj??rne - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','2022-10-18','2022-12-03',6,2),(3,'Solbriller med pilotstel','Stil: Solbriller med pilotstel - Materiale: 100% UV-beskyttende plastik - Farve: Sort med sorte st??nger - St??rrelse: En st??rrelse, der passer de fleste ansigter - St??nger: Justerbare st??nger i matchende farve - Glas: Runde glas med m??rk toning - M??rkning: Brandlogo p?? hver stang - ??vrigt: Skal leveres i en lille sort pose med brandlogo','2022-10-19',NULL,6,3),(4,'Hat med kant','Stil: Hat med kant - Materiale: 100% bomuldsstof med kant - Farve: Hvid med sort kant - St??rrelse: En st??rrelse, der passer de fleste hoveder - Form: Rund med kant hele vejen rundt - M??rkning: Brandlogo i nederste h??jre hj??rne - ??vrigt: Skal vaskes ved 30 grader og stryges med lav varme','2022-10-20',NULL,6,4),(5,'Sandaler med ankelrem',NULL,NULL,NULL,6,5),(6,'Strandtaske',NULL,NULL,NULL,6,6),(7,'Tanktop med racerryg',NULL,NULL,NULL,6,7),(8,'T-shirt med print',NULL,NULL,NULL,6,8),(9,'Bikini med bandeau-top',NULL,NULL,NULL,6,9),(10,'Let regnfrakke',NULL,NULL,NULL,6,10),(11,'Shorts med r?? kanter',NULL,NULL,NULL,6,11),(12,'Sportstaske med lynl??s',NULL,NULL,NULL,6,12);
/*!40000 ALTER TABLE `prototype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-08 12:18:49
