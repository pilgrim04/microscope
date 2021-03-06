-- phpMyAdmin SQL Dump
-- version 3.5.8.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 15, 2014 at 06:41 PM
-- Server version: 5.5.31
-- PHP Version: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ivlev`
--
-- CREATE DATABASE `ivlev` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
create database ivlev character set utf8 collate utf8_general_ci;
USE `ivlev`;

-- --------------------------------------------------------

--
-- Table structure for table `apps_orderitems`
--

CREATE TABLE IF NOT EXISTS `apps_orderitems` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `parent` int(11) unsigned NOT NULL DEFAULT '0',
  `product` int(11) unsigned NOT NULL DEFAULT '0',
  `title` varchar(255) NOT NULL DEFAULT '',
  `url` varchar(64) NOT NULL DEFAULT '',
  `price` float(10,2) unsigned NOT NULL DEFAULT '0.00',
  `count` tinyint(3) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=59 ;

--
-- Dumping data for table `apps_orderitems`
--

INSERT INTO `apps_orderitems` (`id`, `parent`, `product`, `title`, `url`, `price`, `count`) VALUES
(1, 1, 432, 'МЕДИЦИНСКИЙ МИКРОСКОП МИКМЕД-5 УНИВЕР', 'meditcinskii-mikroskop-mikmed-5-univer', 13000.00, 1),
(2, 1, 2, 'Микроскоп  Микромед С-12', 'mikroskop-mikromed-s-12', 2750.00, 1),
(3, 2, 432, 'МЕДИЦИНСКИЙ МИКРОСКОП МИКМЕД-5 УНИВЕР', 'meditcinskii-mikroskop-mikmed-5-univer', 13000.00, 1),
(4, 2, 2, 'Микроскоп  Микромед С-12', 'mikroskop-mikromed-s-12', 2750.00, 1),
(5, 3, 432, 'МЕДИЦИНСКИЙ МИКРОСКОП МИКМЕД-5 УНИВЕР', 'meditcinskii-mikroskop-mikmed-5-univer', 13000.00, 1),
(6, 3, 2, 'Микроскоп  Микромед С-12', 'mikroskop-mikromed-s-12', 2750.00, 1),
(7, 4, 432, 'МЕДИЦИНСКИЙ МИКРОСКОП МИКМЕД-5 УНИВЕР', 'meditcinskii-mikroskop-mikmed-5-univer', 13000.00, 1),
(8, 4, 2, 'Микроскоп  Микромед С-12', 'mikroskop-mikromed-s-12', 2750.00, 1),
(9, 5, 432, 'МЕДИЦИНСКИЙ МИКРОСКОП МИКМЕД-5 УНИВЕР', 'meditcinskii-mikroskop-mikmed-5-univer', 13000.00, 1),
(10, 5, 2, 'Микроскоп  Микромед С-12', 'mikroskop-mikromed-s-12', 2750.00, 1),
(11, 6, 432, 'МЕДИЦИНСКИЙ МИКРОСКОП МИКМЕД-5 УНИВЕР', 'meditcinskii-mikroskop-mikmed-5-univer', 13000.00, 1),
(12, 6, 2, 'Микроскоп  Микромед С-12', 'mikroskop-mikromed-s-12', 2750.00, 1),
(13, 7, 432, 'МЕДИЦИНСКИЙ МИКРОСКОП МИКМЕД-5 УНИВЕР', 'meditcinskii-mikroskop-mikmed-5-univer', 13000.00, 1),
(14, 7, 2, 'Микроскоп  Микромед С-12', 'mikroskop-mikromed-s-12', 2750.00, 1),
(15, 8, 515, 'EULER Hobby 5M Plus с набором Инфузория Туфелька', 'mikroskop-euler-hobby-5m-plus', 4190.00, 1),
(16, 8, 432, 'МЕДИЦИНСКИЙ МИКРОСКОП МИКМЕД-5 УНИВЕР', 'meditcinskii-mikroskop-mikmed-5-univer', 13000.00, 1),
(17, 8, 2, 'Микроскоп  Микромед С-12', 'mikroskop-mikromed-s-12', 2750.00, 1),
(18, 9, 197, 'Микроскоп Bresser Analyth ICD 20x-40x', 'mikroskop-bresser-analyth-icd-20x-40x', 18500.00, 1),
(19, 9, 429, 'Микроскоп Levenhuk 2ST', 'mikroskop-levenhuk-2st', 4430.00, 1),
(20, 9, 674, 'Микроскоп Levenhuk 3ST', 'mikroskop-levenhuk-3st', 8700.00, 1),
(21, 9, 675, 'Микроскоп Levenhuk 5ST', 'mikroskop-levenhuk-5st', 12900.00, 1),
(22, 10, 429, 'Микроскоп Levenhuk 2ST', 'mikroskop-levenhuk-2st', 4430.00, 1),
(23, 10, 674, 'Микроскоп Levenhuk 3ST', 'mikroskop-levenhuk-3st', 8700.00, 1),
(24, 10, 675, 'Микроскоп Levenhuk 5ST', 'mikroskop-levenhuk-5st', 12900.00, 1),
(25, 10, 197, 'Микроскоп Bresser Analyth ICD 20x-40x', 'mikroskop-bresser-analyth-icd-20x-40x', 18500.00, 1),
(26, 11, 197, 'Микроскоп Bresser Analyth ICD 20x-40x', 'mikroskop-bresser-analyth-icd-20x-40x', 18500.00, 1),
(27, 11, 429, 'Микроскоп Levenhuk 2ST', 'mikroskop-levenhuk-2st', 4430.00, 1),
(28, 12, 1407, 'Столик Морозова', 'stolik-morozova', 2600.00, 1),
(29, 13, 1379, 'Микроскоп &quot;Первоклашка 3D&quot;', 'mikroskop-pervoklashka-3d', 2650.00, 1),
(30, 14, 1407, 'Столик Морозова', 'stolik-morozova', 2600.00, 1),
(31, 14, 1379, 'Микроскоп &quot;Первоклашка 3D&quot;', 'mikroskop-pervoklashka-3d', 2650.00, 1),
(32, 14, 1387, 'Батарейка JazzWay AA, 1 уп. (2шт.)', 'batareika-jazzway-aa-1-up-2sht', 75.00, 3),
(33, 15, 1406, 'Лампа для микрсокопов МБС', 'lampa-dlya-mikrsokopov-mbs', 190.00, 1),
(34, 16, 1379, 'Микроскоп &quot;Первоклашка 3D&quot;', 'mikroskop-pervoklashka-3d', 2650.00, 1),
(35, 17, 1407, 'Столик Морозова', 'stolik-morozova', 2600.00, 1),
(36, 18, 1406, 'Лампа для микрсокопов МБС', 'lampa-dlya-mikrsokopov-mbs', 190.00, 1),
(37, 19, 113, 'Микроскоп MP- 450 (2135)', 'mikroskop-mp-450-2135', 590.00, 1),
(38, 20, 520, 'LabZZ! Химия вокруг нас', 'labzz-himiya-vokrug-nas', 3390.00, 3),
(39, 21, 114, 'Микроскоп MP- 600 (2133)', 'mikroskop-mp-600-2133', 820.00, 2),
(40, 22, 1375, 'Стереоскопический микроскоп МСП-1 вар. 3Ц', 'stereoskopicheskii-mikroskop-msp-1-var-3tc', 34500.00, 1),
(41, 22, 1356, 'Система визуализации ToupCam 3.1mp (USB3.0)', 'sistema-vizualizatcii-toupcam-3-1mp-usb3-0', 32000.00, 1),
(42, 23, 513, 'Микроскоп EULER Hobby 5S', 'mikroskop-euler-hobby-5s', 3190.00, 1),
(43, 24, 196, 'Микроскоп Bresser Advance ICD 10x-160x', 'mikroskop-bresser-advance-icd-10x-160x', 39600.00, 1),
(44, 25, 144, 'Цифровой микроскоп (микровизор) Celestron 44340 LCD', 'tcifrovoi-mikroskop-mikrovizor-celestron-44340-lcd', 9500.00, 1),
(45, 25, 594, 'Система визуализации SCMOS02000KPA', 'scmostp502000a', 3350.00, 1),
(46, 26, 659, 'Цифровой одноканальный электрокардиограф SENSITEC ECG-1001B', 'tcifrovoi-odnokanalinii-elektrokardiograf-sensitec-ecg-1001b', 32700.00, 1),
(47, 27, 234, 'Стереоскопический микроскоп МСП-1 вариант 2', 'stereoskopicheskii-mikroskop-msp-1-variant-2', 18500.00, 1),
(48, 28, 234, 'Стереоскопический микроскоп МСП-1 вариант 2', 'stereoskopicheskii-mikroskop-msp-1-variant-2', 18500.00, 1),
(49, 29, 1369, 'Микроскоп Микромед MC-2-Z00M Digital', 'mikroskop-mikromed-mc-2-z00m-digital', 22200.00, 1),
(50, 29, 1395, 'Видеоокуляр ToupCam UCMOS 10 MP', 'videookulyar-toupcam-ucmos-10-mp', 16000.00, 3),
(51, 30, 658, 'Цифровой одноканальный электрокардиограф SENSITEC ECG-1001A', 'tcifrovoi-odnokanalinii-elektrokardiograf-sensitec-ecg-1001a', 24600.00, 1),
(52, 31, 205, 'Микроскоп Биомед-2Led', 'biomed-2', 7000.00, 1),
(53, 31, 21, 'Видеоокуляр DCM-130 SCOPE', 'videookulyar-dcm-130-scope', 7500.00, 1),
(54, 32, 625, 'Электрокардиограф многоканальный с автоматическим режимом переносной  ЭК12Т модель &quot;АЛЬТОН-106&quot;', 'alton-106', 69900.00, 1),
(55, 33, 662, 'Цифровой 12-канальный электрокардиограф SENSITEC ECG-1012', 'tcifrovoi-shestikanalinii-elektrokardiograf-sensitec-ecg-1012', 88100.00, 1),
(56, 34, 307, 'Детский микроскоп GL-MM', 'detskii-mikroskop-gl-mm', 1620.00, 1),
(57, 35, 124, 'Безокулярный стерео микроскоп', 'bezokulyarnii-stereo-mikroskop', 92000.00, 1),
(58, 35, 133, 'Видеоокуляр DCM-900 SCOPE', 'videookulyar-dcm-900-scope', 30000.00, 1);

-- --------------------------------------------------------

--
-- Table structure for table `apps_orders`
--

CREATE TABLE IF NOT EXISTS `apps_orders` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) NOT NULL DEFAULT '',
  `name` varchar(32) NOT NULL DEFAULT '',
  `email` varchar(32) NOT NULL DEFAULT '',
  `phone` varchar(32) NOT NULL DEFAULT '',
  `city` varchar(32) NOT NULL DEFAULT '',
  `index` varchar(32) NOT NULL DEFAULT '',
  `street` varchar(128) NOT NULL DEFAULT '',
  `house` varchar(32) NOT NULL DEFAULT '',
  `housing` varchar(32) NOT NULL DEFAULT '',
  `office` varchar(32) NOT NULL DEFAULT '',
  `comments` text NOT NULL,
  `delivery` int(11) NOT NULL DEFAULT '0',
  `cdate` int(11) NOT NULL DEFAULT '0',
  `uid` int(11) NOT NULL DEFAULT '0',
  `pay` int(11) NOT NULL DEFAULT '0',
  `company` varchar(32) NOT NULL DEFAULT '',
  `inn` varchar(32) NOT NULL DEFAULT '',
  `kpp` varchar(32) NOT NULL DEFAULT '',
  `juraddress` varchar(32) NOT NULL DEFAULT '',
  `bank_r_acc` varchar(32) NOT NULL DEFAULT '',
  `bank_k_acc` varchar(32) NOT NULL DEFAULT '',
  `bank_bik` varchar(32) NOT NULL DEFAULT '',
  `baddress` text NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=36 ;

--
-- Dumping data for table `apps_orders`
--

INSERT INTO `apps_orders` (`id`, `ip`, `name`, `email`, `phone`, `city`, `index`, `street`, `house`, `housing`, `office`, `comments`, `delivery`, `cdate`, `uid`, `pay`, `company`, `inn`, `kpp`, `juraddress`, `bank_r_acc`, `bank_k_acc`, `bank_bik`, `baddress`, `status`) VALUES
(1, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', '', '', '', '', '', '', '', 0, 1395649985, 293, 1, '', '', '', '', '', '', '', '', 188),
(2, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', 'Кишинев', '9999', 'Димо', '21', '1', '151', '', 187, 1395650161, 293, 2, 'devleader', '11111', '22222', 'Кишинев Димо', '123', '123', '444', 'wwwwwwwwwwwwwwwwwwww', 189),
(3, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', 'q', 'q', 'q', 'q', 'q', 'q', '', 187, 1395650436, 293, 2, 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 190),
(4, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', 'Кишинев', '9999', 'Димо', '21', '1', '151', 'кул', 187, 1395650643, 293, 2, 'devleader', '11111', '22222', 'Кишинев Димо', '123', '123', '444', 'wwwwwwwwwwwwwwwwwwww', 188),
(5, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', 'Кишинев', '9999', 'Димо', '21', '1', '151', 'кул', 186, 1395651105, 293, 2, 'devleader', '11111', '22222', 'Кишинев Димо', '123', '123', '444', 'wwwwwwwwwwwwwwwwwwww', 189),
(6, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', 'Кишинев', '9999', 'Димо', '21', '1', '151', 'кул', 186, 1395651790, 293, 2, 'devleader', '11111', '22222', 'Кишинев Димо', '123', '123', '444', 'wwwwwwwwwwwwwwwwwwww', 190),
(7, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', 'Кишинев', '9999', 'Димо', '21', '1', '151', 'кул', 187, 1395653812, 293, 2, 'devleader', '11111', '22222', 'Кишинев Димо', '123', '123', '444', 'wwwwwwwwwwwwwwwwwwww', 188),
(8, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', 'Кишинев', '1234', 'Димо', '10', '1', '151', 'ццццц', 187, 1395733541, 293, 2, 'devleader', '123', '123', 'alba', '123', '123', '123', 'qqqqqqqqq', 189),
(9, '192.168.194.201', 'yyy', 'eduard@devleader.net', '12345', 'yyy', 'yyy', 'yyy', 'yyy', 'yyy', 'yy', 'yyy', 187, 1395821420, 0, 0, '', '', '', '', '', '', '', '', 190),
(10, '192.168.194.201', 'zz', 'eduard@devleader.net', '342', '23', '23', '23', '23', '23', '23', '23', 186, 1395821631, 0, 0, '', '', '', '', '', '', '', '', 188),
(11, '192.168.194.201', 'q', 'eduard@devleader.net', 'q', 'q', 'q', 'qwe', 'q', 'q', 'q', 'q', 0, 1395822321, 0, 0, 'q', 'q', 'q', '', 'q', 'q', 'q', 'q', 189),
(12, '192.168.194.201', 'вася', 'vasika@devleader.net', '2143324234234', 'Омск', '24234', 'Вишневая', '1', '1', '11', 'ыва', 186, 1396342693, 276, 2, 'ООО Губки', '123123123', '1321', 'аыаываыва', '123213', '123123', '123123', 'вввв', 188),
(13, '192.168.194.201', 'вася', 'vasika@devleader.net', '2324234', 'Омск', '24234', 'Вишневая', '1', '1', '11', 'ыва', 0, 1396359856, 276, 1, '', '', '', '', '', '', '', '', 188),
(14, '192.168.194.201', 'вася', 'vasika@devleader.net', '1111', '', '', '', '', '', '', '', 0, 1396428144, 276, 1, '', '', '', '', '', '', '', '', 188),
(15, '192.168.194.201', 'вася', 'vasika@devleader.net', '5555', '', '', '', '', '', '', '', 0, 1396428554, 276, 1, '', '', '', '', '', '', '', '', 188),
(16, '192.168.194.201', 'вася', 'vasika@devleader.net', '234234234', '', '', '', '', '', '', '', 0, 1396428656, 276, 2, 'ООО Губки', '123123123', '1321', 'аыаываыва', '123213', '123123', '123123', 'вввв', 188),
(17, '192.168.194.201', 'вася', 'vasika@devleader.net', '3333', '3', '3', '234', '234', '34', '324', '234234', 187, 1396428677, 276, 1, '', '', '', '', '', '', '', '', 188),
(18, '192.168.194.201', 'edik', 'edik@devleader.net', '321878', 'Кишинев', '1234', 'Димо', '10', '1', '151', 'ццццц', 187, 1396429231, 293, 1, '', '', '', '', '', '', '', '', 188),
(19, '109.172.15.17', 'KV', 'kv@micromed.pro', '8128420984', '', '', '', '', '', '', '', 0, 1396514938, 0, 0, '', '', '', '', '', '', '', '', 188),
(20, '109.172.15.17', 'Генадий', 'genadiy@gmail.com', '89523847975', '', '', '', '', '', '', '', 0, 1396516082, 0, 0, '', '', '', '', '', '', '', '', 188),
(21, '109.172.15.17', 'ляля', 'dbr@dbr.com', '89006007070', '', '', '', '', '', '', '', 0, 1396516310, 0, 0, '', '', '', '', '', '', '', '', 188),
(22, '109.172.15.17', 'вася', 'vasika@devleader.net', '5643654642', 'Майами', '197198', 'Жаркая', '712', '', '23', '', 186, 1396516339, 276, 1, '', '', '', '', '', '', '', '', 188),
(23, '109.172.15.17', '111', '111@1111111.ru', '11111111111', 'Москва', '123132', 'Короблёф', '34', '', '2', 'Хочу бла-бла', 186, 1396516370, 0, 0, '', '', '', '', '', '', '', '', 188),
(24, '109.172.15.17', 'Генадий', 'genadiy@gmail.com', '89523847975', '', '', '', '', '', '', '', 0, 1396516553, 0, 0, '', '', '', '', '', '', '', '', 188),
(25, '109.172.15.17', 'Maxmed', 'glebkryachok@mail.ru', '1234567890', 'Мимими', '143256', 'Няняня', '3', '', '32', '', 186, 1396516783, 312, 1, '', '', '', '', '', '', '', '', 188),
(26, '109.172.15.17', 'Maxmed', 'glebkryachok@mail.ru', '1234567890', 'Мимими', '143256', 'Няняня', '1', '', '2', '', 186, 1396516985, 312, 2, 'НАНАНАНА', '123454325', '234к4343', 'МИМИМИ', '3433', '433434', '345354535', 'АААААА', 188),
(27, '109.172.15.17', 'вася', 'vasika@devleader.net', '1111111111', '', '', '', '', '', '', '', 0, 1396517065, 276, 1, '', '', '', '', '', '', '', '', 188),
(28, '109.172.15.17', 'вася', 'vasika@devleader.net', '1234567890', '', '', '', '', '', '', '', 0, 1396517159, 276, 1, '', '', '', '', '', '', '', '', 188),
(29, '109.172.15.17', 'gena', 'yakov@glavindex.ru', '89523847975', '', '', '', '', '', '', '', 0, 1396517249, 315, 1, '', '', '', '', '', '', '', '', 188),
(30, '109.172.15.17', 'вася', 'vasika@devleader.net', '1234567890', '', '', '', '', '', '', '', 0, 1396517282, 276, 2, 'ООО Губки', '123123123', '1321', 'аыаываыва', '123213', '123123', '123123', 'вввв', 188),
(31, '109.172.15.17', 'kv@micromed.pro', 'kv@micromed.pro', '1111111111', 'Санкт Петербург', '197198', 'Ропшинская', '1', '1', '1', 'нужен пропуск', 187, 1396517865, 316, 1, '', '', '', '', '', '', '', '', 188),
(32, '109.172.15.17', 'kv@micromed.pro', 'kv@micromed.pro', '1111111111', '', '', '', '', '', '', '', 0, 1396518178, 316, 2, 'Ромашка', '781025548', '1457852', 'г. Чайка', '408751225487745', '454461254747', '564821', 'г. Чайка, ул. Портовая', 188),
(33, '109.172.15.17', 'gena', 'yakov@glavindex.ru', '89523847975', '', '', '', '', '', '', '', 0, 1396527439, 315, 2, 'Yakov Corp', '777655433', '45645', 'Ростов ул.Шелгунова д.4', '68678678', '67868768', '6795494799', 'Санкт-Петербург ул.Черкизова д.8', 188),
(34, '109.172.15.17', 'аяптияпа', 'fgxgf@xghn.ru', '9219922335', '', '', '', '', '', '', '', 0, 1396528716, 0, 0, '', '', '', '', '', '', '', '', 188),
(35, '109.172.15.17', 'вася', 'vasika@devleader.net', '9210912335', '', '', '', '', '', '', '', 0, 1396529174, 276, 1, '', '', '', '', '', '', '', '', 188);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
