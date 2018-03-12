-- phpMyAdmin SQL Dump
-- version 3.5.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 12, 2015 at 07:54 PM
-- Server version: 5.5.29-log
-- PHP Version: 5.3.21

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `calendar`
--

-- --------------------------------------------------------

--
-- Table structure for table `calendar`
--

CREATE TABLE IF NOT EXISTS `pome_calendar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(160) NOT NULL,
  `description` text NOT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  `allDay` varchar(5) NOT NULL,
  `color` varchar(7) NOT NULL,
  `url` varchar(255) NOT NULL,
  `category` varchar(200) NOT NULL,
  `repeat_type` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `repeat_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `calendar`
--

INSERT INTO `pome_calendar` (`id`, `title`, `description`, `start`, `end`, `allDay`, `color`, `url`, `category`, `repeat_type`, `user_id`, `repeat_id`) VALUES
(1, 'fds', 'dff', '2015-04-14 10:06:00', '2015-04-15 05:15:00', 'false', '#a80b0b', 'sdfsd', '', 'no', 0, 1),
(2, 'hgdh', 'gdhdgh', '2015-04-01 00:00:00', '2015-04-22 11:19:00', 'false', '#080122', 'false', '', 'no', 0, 2);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
