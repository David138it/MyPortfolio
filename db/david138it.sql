-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: david138it
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

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
-- Table structure for table `experience`
--

DROP TABLE IF EXISTS `experience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experience` (
  `experience_id` int NOT NULL AUTO_INCREMENT,
  `place` varchar(255) DEFAULT NULL,
  `specialization` varchar(255) DEFAULT NULL,
  `content` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `scan` varchar(255) DEFAULT NULL,
  `begin` date DEFAULT NULL,
  `finish` date DEFAULT NULL,
  PRIMARY KEY (`experience_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experience`
--

LOCK TABLES `experience` WRITE;
/*!40000 ALTER TABLE `experience` DISABLE KEYS */;
INSERT INTO `experience` VALUES (1,'Иркутский государственный университет, Иркутск','Информационные технологии и телекоммуникационные системы (Квалификация бакалавр)','Skills: html, css, timeweb, linux, qemu-kvm, lamp, phpmyadmin, mysql, php',NULL,'2011-09-01','2015-06-30'),(2,'Иркутский государственный университет, Иркутск','Электроника и наноэлектроника (Квалификация магистр)','Skills: Ионосфера, Спутниковые радионавигационные системы (СРНС), C++, Rinex, Одночастотные приемники СРНС',NULL,'2011-09-01','2017-06-30'),(3,'Иркутский государственный университет, Иркутск','Информационная безопасность (Дополнительное образование)','Skills: Qemu-Kvm, Virtualbox, Linux, Ssh, Iptables, Nmap, Bash, Vsftpd, Telnet, Nginx, Squid, Tcpdump, Icmp, Tripwire, Rkhunter, Crontab9',NULL,'2017-09-01','2018-05-01'),(4,'Easy School, Иркутск','English Level Elementary A (Дополнительное образование)',NULL,NULL,NULL,NULL),(5,'Иркутский государственный университет, Иркутск','Информационные технологии и телекоммуникационные системы (Квалификация бакалавр)','Skills: Qemu-Kvm, Linux, Cisco Packet Tracer, Virtualbox, Windows, DHCP-протокол, DNS;',NULL,'2011-09-01','2015-06-30'),(7,'Всероссийский государственный университет юстиции (РПА Минюста России), Иркутск;','Technical Specialist;','Обязанности: работа с сайтами, поддержка функционирования серверов, в том числе с использованием сред виртуализации, восстановление работоспособности ПК, периферийных устройств, оборудования видеоконференцсвязи, аудио-видеофиксации, локальной сети при сбоях или выходе из строя сетевого оборудования, техническая поддержка пользователей, разрабатывать решения, которые упростят эксплуатацию и автоматизируют рутину, поддержка функционирования сервисов СУБД; Skills: Python, Html, Wordpress, Bash;',NULL,'2018-03-01','2022-11-01'),(8,'Всероссийский государственный университет юстиции (РПА Минюста России), Иркутск','Technical Specialist','Обязанности: работа с сайтами, поддержка функционирования серверов, в том числе с использованием сред виртуализации, восстановление работоспособности ПК, периферийных устройств, оборудования видеоконференцсвязи, аудио-видеофиксации, локальной сети при сбоях или выходе из строя сетевого оборудования, техническая поддержка пользователей, разрабатывать решения, которые упростят эксплуатацию и автоматизируют рутину, поддержка функционирования сервисов СУБД; Skills: Windows, Powershell, Hyper-v, Redos, Pxe, Dhcp, Http, Tftp, Kickstart',NULL,'2018-03-01','2022-11-01'),(9,'Всероссийский государственный университет юстиции (РПА Минюста России), Иркутск','Technical Specialist','Обязанности: работа с сайтами, поддержка функционирования серверов, в том числе с использованием сред виртуализации, восстановление работоспособности ПК, периферийных устройств, оборудования видеоконференцсвязи, аудио-видеофиксации, локальной сети при сбоях или выходе из строя сетевого оборудования, техническая поддержка пользователей, разрабатывать решения, которые упростят эксплуатацию и автоматизируют рутину, поддержка функционирования сервисов СУБД; Skills: Hyper-V, Powershell, Altlinux, Redos, Postgresql, Pgadmin4',NULL,'2018-03-01','2022-11-01'),(10,'Всероссийский государственный университет юстиции (РПА Минюста России), Иркутск','Technical Specialist','Обязанности: работа с сайтами, поддержка функционирования серверов, в том числе с использованием сред виртуализации, восстановление работоспособности ПК, периферийных устройств, оборудования видеоконференцсвязи, аудио-видеофиксации, локальной сети при сбоях или выходе из строя сетевого оборудования, техническая поддержка пользователей, разрабатывать решения, которые упростят эксплуатацию и автоматизируют рутину, поддержка функционирования сервисов СУБД; Skills: Bash, Python','Разработал скрипты на языках Bash и Python для автоматизации работы в компьютерных классах и аудиториях','2018-03-01','2022-11-01'),(11,'Информационно-аналитический центр поддержки ГАС правосудие, Иркутск','Engineer / System administrator','Обязанности: установка, обновление и контроль состояния программного обеспечения на объектах автоматизации, введение эксплуатационной документации, поддержка функционирования серверов, в том числе с использованием сред виртуализации, восстановление работоспособности ПК, периферийных устройств, оборудования видеоконференцсвязи, аудио-видеофиксации, локальной сети при сбоях или выходе из строя сетевого оборудования, техническая поддержка пользователей, разрабатывать решения, которые упростят эксплуатацию и автоматизируют рутину, поддержка функционирования сервисов СУБД; Skills: Windows, Powershell, Bash',NULL,'2022-11-01',NULL);
/*!40000 ALTER TABLE `experience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `results_id` int NOT NULL AUTO_INCREMENT,
  `experienceId` int DEFAULT NULL,
  `progress` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`results_id`),
  KEY `experienceId` (`experienceId`),
  CONSTRAINT `results_ibfk_1` FOREIGN KEY (`experienceId`) REFERENCES `experience` (`experience_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (1,1,'Для разработки своего сайта, куда публиковал все решенные мной интересные задачи, отчеты лабораторных работ и презентации, сверстал простой сайт, развернул в Qemu-kvm виртуальную машину с операционной системой Ubuntu, в котором установил и настроил веб-сервер Lamp с своей базой данных на Mysql, опубликовал сайт в сервис Timeweb и в нем разрегистрировал домен'),(8,2,'Для защиты диссертации по теме \"Использование данных с одночастотных приемников спутниковых радионавигационных систем для коррекции модели ионосферы\" освоил технологию приёма получения данных с одночастотных приемников спутниковых радионавигационных систем, получил данные, разработал программу на C++, которая обрабатывает и сортирует данные двух координат из файла по столбцам, рисует график, чтобы увидеть желаемый результат в точности определения координат спутников, рассмотрел способы уменьшения ошибок измерения псевдодальности и показал, что из-за нестабильности аппаратуры потребителя информация о состоянии ионосферы может быть получена в каждый момент времени по разностям ПД двух навигационных спутников'),(9,5,'Для защиты лабораторных работ по дисциплине Локально-вычислительные сети в виртуальной машине Ubuntu настроил программу для проектирования сетей Packet Tracer, спроектрировал лабораторные работы по темам \"Использование DHCP-протокола через маршрутизатор и через сервер\", \"Wi-Fi - беспроводная передача данных\", а также по теме \"Локальная сеть\" развернул виртуальные машины в Virtualbox две операционные системы Windows 10 и Windows Server 2012 для настройки локальной сети. В Windows Server установил DHCP и DNS сервера и добавил в домен клиентского компьютера Windows 10.'),(10,3,'Для защиты выпускной квалификационной работы по теме \"Утилита для сканирования безопасности сети Nmap\" проанализировал состояние виртуальных машин в Qemu-Kvm инструментом Nmap. Дополнительно для перехвата трафиков использовал Tcpdump. Для того чтобы обезопасить свои системы, настроил правила в Iptables и развернул антируткит, который по определенному раписанию выгружал отчет о состоянии системы. В курсовой работе своил навыки по следующим инструментам: Qemu-Kvm, Virtualbox, Linux, Ssh, Iptables, Nmap, Bash, Vsftpd, Telnet, Nginx, Squid, Tcpdump, Icmp, Tripwire, Rkhunter, Crontab'),(11,7,'Разработал программы, которые анализируют, обрабатывают и сортируют код на сайте организации. Это позволило мне ускорить процесс корректировки тегов на сайте по запросу Россобрнадзор'),(12,8,'Для импортозамещения с Windows на Redos, развернул виртуальную тестовую машину Redos в Hyber-v, в котором развернул Pxe сервер для развертывания Redos с загрузкой в Uefi по сети. Это сэкономило время на внедрение системы Redos в компьютерных классах'),(13,9,'Развернул виртуальный сервер в Altlinux и разработал в нем базу \"Инвентаризация компьютерной техники в здании\". Это позволило мне быстро предоставлять отчеты об оборудовании в здании'),(14,10,'Разработал скрипты на языках Bash и Python для автоматизации работы в компьютерных классах и аудиториях'),(15,11,'Разработал скрипты для автоматизации работы с системой Гас правосудия');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-11 21:27:53
