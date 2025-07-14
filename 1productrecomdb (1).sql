-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 08, 2022 at 11:17 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1productrecomdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admintb`
--

CREATE TABLE `admintb` (
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admintb`
--

INSERT INTO `admintb` (`UserName`, `Password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` bigint(250) NOT NULL auto_increment,
  `Bookingid` varchar(250) NOT NULL,
  `ProductId` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Qty` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Mac` varchar(250) NOT NULL,
  `CardType` varchar(250) NOT NULL,
  `CardNo` varchar(250) NOT NULL,
  `CvNo` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `Bookingid`, `ProductId`, `ProductName`, `UserName`, `Mobile`, `Email`, `Qty`, `Amount`, `Mac`, `CardType`, `CardNo`, `CvNo`, `Date`) VALUES
(4, 'BOOKID004', '4', 'SamsungTv', 'san', '9486365535', 'sangeeth5535@gmail.com', '2', '1600.0', '163580561205031', 'MasterCard', '1242363475698', '123', '28-Dec-2021'),
(6, 'BOOKID002', '6', 'Applewatch', 'rajiya', '948636553', 'rajiya@gmail.com', '2', '16000.0', '163580561205031', 'MasterCard', '1242363475698', '123', '08-Jan-2022');

-- --------------------------------------------------------

--
-- Table structure for table `companytb`
--

CREATE TABLE `companytb` (
  `Name` varchar(250) NOT NULL,
  `Regno` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `LandLine` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Website` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `companytb`
--

INSERT INTO `companytb` (`Name`, `Regno`, `Mobile`, `LandLine`, `Email`, `Website`, `Address`, `UserName`, `Password`) VALUES
('fantasy', '844101', '9600357839', '09600357839', 'fantasy@gmail.com', 'www.fantasy.com', 'no 6 trichy', 'fantasy', 'fantasy');

-- --------------------------------------------------------

--
-- Table structure for table `protb`
--

CREATE TABLE `protb` (
  `id` bigint(250) NOT NULL auto_increment,
  `CompanyName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `Color` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `VideoUrl` varchar(250) NOT NULL,
  `Specifications` varchar(500) NOT NULL,
  `Image` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `protb`
--

INSERT INTO `protb` (`id`, `CompanyName`, `ProductType`, `ProductName`, `Color`, `Price`, `VideoUrl`, `Specifications`, `Image`) VALUES
(4, 'Samsung', 'TV', 'SamsungTv', 'white', '800', 'https://www.youtube.com/embed/18zfbyijdy4', ' no 6 6', 'images_1.jpg'),
(5, 'Apple', 'TV', 'Apple Tv', 'white', '9000', 'https://www.youtube.com/embed/6d71oGtvnxM', ' gdf', 'Penguins.jpg'),
(6, 'Apple', 'Watch', 'Applewatch', 'white', '8000', 'https://www.youtube.com/embed/MMdQ-gWBNZE', ' Stay connected to family and friends with calls, texts and email, even when you don’t have your phone', 'download.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Name`, `Gender`, `Age`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
('san', 'male', '20', 'sangeeth5535@gmail.com', '9486365535', 'no 6 trichy', 'san', 'san'),
('sanNew', 'male', '20', 'sangeeth5535@gmail.com', '9486365535', 'no ', 'sanNew', 'sanNew'),
('mani', 'male', '33', 'ishu@gmail.com', '9486365535', 'dgh', 'mani', 'mani'),
('Rajiya', 'female', '20', 'rajiya@gmail.com', '948636553', 'no 6 trichy', 'rajiya', 'rajiya');

-- --------------------------------------------------------

--
-- Table structure for table `reviewtb`
--

CREATE TABLE `reviewtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `ProductId` varchar(250) NOT NULL,
  `CompanyName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Bookid` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `MacAddress` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Rate` int(250) NOT NULL,
  `Review` varchar(500) NOT NULL,
  `Smile1` int(250) NOT NULL,
  `Smile2` int(250) NOT NULL,
  `Smile3` int(250) NOT NULL,
  `Smile4` int(250) NOT NULL,
  `Smile5` int(250) NOT NULL,
  `Smile6` int(250) NOT NULL,
  `Result` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `reviewtb`
--

INSERT INTO `reviewtb` (`id`, `ProductId`, `CompanyName`, `ProductType`, `ProductName`, `Price`, `Image`, `Bookid`, `Email`, `MacAddress`, `UserName`, `Rate`, `Review`, `Smile1`, `Smile2`, `Smile3`, `Smile4`, `Smile5`, `Smile6`, `Result`) VALUES
(3, '4', 'Samsung', 'TV', 'SamsungTv', '800', 'images_1.jpg', 'BOOKID004', 'sangeeth5535@gmail.com', '163580561205031', 'san', 5, 'good', 1, 0, 0, 0, 0, 0, 'Postive'),
(4, '6', 'Apple', 'Watch', 'Applewatch', '8000', 'download.jpg', 'BOOKID002', 'rajiya@gmail.com', '163580561205031', 'rajiya', 5, 'good product', 1, 0, 0, 0, 0, 0, 'Postive');

-- --------------------------------------------------------

--
-- Table structure for table `temptb`
--

CREATE TABLE `temptb` (
  `ProductId` varchar(250) NOT NULL,
  `CompanyName` varchar(250) NOT NULL,
  `ProductType` varchar(250) NOT NULL,
  `ProductName` varchar(250) NOT NULL,
  `Price` varchar(250) NOT NULL,
  `Image` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `temptb`
--

INSERT INTO `temptb` (`ProductId`, `CompanyName`, `ProductType`, `ProductName`, `Price`, `Image`) VALUES
('4', 'Samsung', 'TV', 'SamsungTv', '800', 'images_1.jpg'),
('6', 'Apple', 'Watch', 'Applewatch', '8000', 'download.jpg');
