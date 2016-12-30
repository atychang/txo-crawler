-- MySQL dump 10.13  Distrib 5.7.16, for osx10.11 (x86_64)
--
-- Host: 140.116.39.176    Database: txo
-- ------------------------------------------------------
-- Server version	5.7.13-log

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
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `table` varchar(30) CHARACTER SET utf8 NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`table`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `options`
--

DROP TABLE IF EXISTS `options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `options` (
  `balance_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `expire_month` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `contract_type` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `contract_name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `settlement_price` float(20,2) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rawdata`
--

DROP TABLE IF EXISTS `rawdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rawdata` (
  `trade_date` timestamp NULL DEFAULT NULL COMMENT '交易日期',
  `contract_type` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT '契約種類',
  `expire_month` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT '到期月份(週別)',
  `contract_price` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT '履約價',
  `buy_sell` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT '買賣權',
  `price_open` float(20,2) DEFAULT NULL COMMENT '開盤價',
  `price_high` float(20,2) DEFAULT NULL COMMENT '最高價',
  `price_low` float(20,2) DEFAULT NULL COMMENT '最低價',
  `price_close` float(20,2) DEFAULT NULL COMMENT '收盤價',
  `transaction` float(20,2) DEFAULT NULL COMMENT '成交量',
  `price_end_call` float(20,2) DEFAULT NULL COMMENT '結算價',
  `contract_not_trade` int(20) unsigned DEFAULT NULL COMMENT '未沖銷契約數',
  `good_to_buy` float(20,2) DEFAULT NULL COMMENT '最後最佳買價',
  `good_to_sell` float(20,2) DEFAULT NULL COMMENT '最後最佳賣價',
  `history_high` float(20,2) DEFAULT NULL COMMENT '歷史最高價',
  `history_end` float(20,2) DEFAULT NULL COMMENT '歷史最低價',
  `suspend_trading` varchar(20) CHARACTER SET utf8 DEFAULT NULL COMMENT '是否因訊息面暫停交易',
  `tid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '歷史資料交易流水號',
  PRIMARY KEY (`tid`)
) ENGINE=MyISAM AUTO_INCREMENT=873382 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `taiex`
--

DROP TABLE IF EXISTS `taiex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `taiex` (
  `trade_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '日期',
  `price_open` float(20,2) DEFAULT NULL COMMENT '開盤價',
  `price_high` float(20,2) DEFAULT NULL COMMENT '最高價',
  `price_low` float(20,2) DEFAULT NULL COMMENT '最低價',
  `price_close` float(20,2) DEFAULT NULL COMMENT '收盤價'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `trading_days`
--

DROP TABLE IF EXISTS `trading_days`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trading_days` (
  `tid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `trading_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`tid`)
) ENGINE=MyISAM AUTO_INCREMENT=4495 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-30  0:45:29
