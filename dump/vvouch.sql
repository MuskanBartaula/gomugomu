-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 05, 2021 at 02:39 PM
-- Server version: 5.7.33-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vvouch`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add activation', 7, 'add_activation'),
(26, 'Can change activation', 7, 'change_activation'),
(27, 'Can delete activation', 7, 'delete_activation'),
(28, 'Can view activation', 7, 'view_activation'),
(29, 'Can add products', 8, 'add_products'),
(30, 'Can change products', 8, 'change_products'),
(31, 'Can delete products', 8, 'delete_products'),
(32, 'Can view products', 8, 'view_products'),
(33, 'Can add product images', 9, 'add_productimages'),
(34, 'Can change product images', 9, 'change_productimages'),
(35, 'Can delete product images', 9, 'delete_productimages'),
(36, 'Can view product images', 9, 'view_productimages');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(7, 'vvouch', 'activation'),
(9, 'vvouch', 'productimages'),
(8, 'vvouch', 'products'),
(6, 'vvouch', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-04-28 17:07:53.235431'),
(2, 'contenttypes', '0002_remove_content_type_name', '2021-04-28 17:07:53.255239'),
(3, 'auth', '0001_initial', '2021-04-28 17:07:53.289971'),
(4, 'auth', '0002_alter_permission_name_max_length', '2021-04-28 17:07:53.331979'),
(5, 'auth', '0003_alter_user_email_max_length', '2021-04-28 17:07:53.352304'),
(6, 'auth', '0004_alter_user_username_opts', '2021-04-28 17:07:53.357321'),
(7, 'auth', '0005_alter_user_last_login_null', '2021-04-28 17:07:53.363099'),
(8, 'auth', '0006_require_contenttypes_0002', '2021-04-28 17:07:53.364672'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2021-04-28 17:07:53.368970'),
(10, 'auth', '0008_alter_user_username_max_length', '2021-04-28 17:07:53.373606'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2021-04-28 17:07:53.378027'),
(12, 'auth', '0010_alter_group_name_max_length', '2021-04-28 17:07:53.384309'),
(13, 'auth', '0011_update_proxy_permissions', '2021-04-28 17:07:53.389336'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2021-04-28 17:07:53.395388'),
(15, 'vvouch', '0001_initial', '2021-04-28 17:07:53.421149'),
(16, 'admin', '0001_initial', '2021-04-28 17:07:53.475276'),
(17, 'admin', '0002_logentry_remove_auto_add', '2021-04-28 17:07:53.500353'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2021-04-28 17:07:53.509974'),
(19, 'sessions', '0001_initial', '2021-04-28 17:07:53.517472'),
(20, 'vvouch', '0002_activation', '2021-04-28 17:07:53.528686'),
(21, 'vvouch', '0003_auto_20210220_1613', '2021-04-28 17:07:53.728504'),
(22, 'vvouch', '0004_products', '2021-04-28 17:07:53.745714'),
(23, 'vvouch', '0005_auto_20210315_1740', '2021-04-28 17:07:53.772975'),
(24, 'vvouch', '0006_auto_20210315_1740', '2021-04-28 17:07:53.791951'),
(25, 'vvouch', '0007_productimages', '2021-04-28 17:07:53.807474'),
(26, 'vvouch', '0008_auto_20210315_1831', '2021-04-28 17:07:53.830766'),
(27, 'vvouch', '0009_auto_20210420_1704', '2021-04-28 17:07:53.838758');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('o5c4bkzjnewtvcdo59ioch08d9uewyfx', '.eJxVjM0KwjAQhN8lZwn5XVOP3n2GsNkspioJNO1JfHdT6EEPA8N8M_MWEbe1xK3zEucsLgLE6TdLSE-uO8gPrPcmqdV1mZPcK_KgXd5a5tf16P4dFOxlrK2ZIDivkVFrsmcNkEiRCSpkZDM55djbYZA1JvB2iECx9yF4ME58vsO4Nt0:1leDx2:EABO6jhOBbuD9acE_Drg-G7NEADT1syPBqeoz-X5-7Y', '2021-05-19 09:36:16.781594');

-- --------------------------------------------------------

--
-- Table structure for table `vvouch_activation`
--

CREATE TABLE `vvouch_activation` (
  `id` int(11) NOT NULL,
  `user` varchar(40) NOT NULL,
  `activation_key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vvouch_productimages`
--

CREATE TABLE `vvouch_productimages` (
  `id` int(11) NOT NULL,
  `file` varchar(255) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `date_added` datetime(6) DEFAULT NULL,
  `created_by_id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vvouch_productimages`
--

INSERT INTO `vvouch_productimages` (`id`, `file`, `is_deleted`, `date_added`, `created_by_id`, `product_id`) VALUES
(1, 'Screenshot_from_2021-05-02_22-25-31.png', 0, '2021-04-20 16:37:03.962963', 6, 13);

-- --------------------------------------------------------

--
-- Table structure for table `vvouch_products`
--

CREATE TABLE `vvouch_products` (
  `id` int(11) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `product_type` varchar(100) NOT NULL,
  `product_quantity` varchar(100) NOT NULL,
  `product_reviews` varchar(100) NOT NULL,
  `product_website` varchar(100) NOT NULL,
  `product_relevant_page` varchar(100) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `seller_email` varchar(255) DEFAULT NULL,
  `product_status` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vvouch_products`
--

INSERT INTO `vvouch_products` (`id`, `product_name`, `product_type`, `product_quantity`, `product_reviews`, `product_website`, `product_relevant_page`, `seller_id`, `seller_email`, `product_status`) VALUES
(6, 'abs', 'clothing', 'jkhjk', 'hkjk', 'jhkkj', 'kjh', 15, NULL, 0),
(7, 'abs', 'clothing', 'jkhjk', 'hkjk', 'jhkkj', 'kjh', 15, NULL, 0),
(8, 'abs', 'clothing', 'jkhjk', 'hkjk', 'jhkkj', 'kjh', 15, NULL, 0),
(9, 'abs', 'clothing', 'jkhjk', 'hkjk', 'jhkkj', 'kjh', 15, NULL, 0),
(10, 'test.com', 'bags', 'https://www.instagram.com/', 'https://www.instagram.com/', 'https://www.instagram.com/', 'https://www.instagram.com/', 6, NULL, 1),
(11, 'test.com', 'bags', 'https://www.instagram.com/', 'https://www.instagram.com/', 'https://www.instagram.com/', 'https://www.instagram.com/', 6, NULL, 0),
(12, 'test.com', 'clothing', 'https://www.instagram.com/', 'https://www.instagram.com/', 'https://www.instagram.com/', 'https://www.instagram.com/', 6, NULL, 0),
(13, 'Product', 'bags', '100', 'Test', 'https://google.com', 'https://ABC.com', 6, 'seller@seller.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `vvouch_user`
--

CREATE TABLE `vvouch_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `type` varchar(30) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` longtext NOT NULL,
  `business_category` varchar(100) NOT NULL,
  `business_name` varchar(100) NOT NULL,
  `cnic` varchar(100) NOT NULL,
  `courier` varchar(100) NOT NULL,
  `fb_page` varchar(100) NOT NULL,
  `insta_page` varchar(100) NOT NULL,
  `is_cod` varchar(100) NOT NULL,
  `is_secp_registered` tinyint(1) NOT NULL,
  `message` longtext NOT NULL,
  `mobile_number` varchar(100) NOT NULL,
  `payment_mode` varchar(100) NOT NULL,
  `website` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vvouch_user`
--

INSERT INTO `vvouch_user` (`id`, `password`, `last_login`, `is_superuser`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `type`, `username`, `email`, `address`, `business_category`, `business_name`, `cnic`, `courier`, `fb_page`, `insta_page`, `is_cod`, `is_secp_registered`, `message`, `mobile_number`, `payment_mode`, `website`) VALUES
(1, 'pbkdf2_sha256$216000$a7RQCEkKJOZk$/6WJMQBPEhjzo7I6dPqS0Ql6oMvbk/g2HEXAdOOHWB4=', '2021-02-21 16:24:21.356826', 0, 'Hassan', 'Shahbaz', 0, 1, '2020-11-03 19:19:44.397226', 'user', '', 'hassan@gmail.com', '', '', '', '', '', '', '', '', 0, '', '', '', ''),
(2, 'pbkdf2_sha256$216000$ttpw4FkJvIeN$4AitJnG7cbmNZIHQBW765HMq0DC1FpoKKLuhBG86AJU=', '2020-11-03 19:21:00.583476', 0, 'Hassan', 'Shahbaz', 0, 1, '2020-11-03 19:21:00.290507', 'user', '', 'hassan+1@gmail.com', '', '', '', '', '', '', '', '', 0, '', '', '', ''),
(3, 'pbkdf2_sha256$216000$ElfMIUDL691O$7Hu3Exsbu1uI5cOcaEh9pMKzBXhpcRWvmCCRjqpCQF8=', '2021-01-18 17:48:38.539647', 0, 'Hassan', 'Shahbaz', 0, 1, '2021-01-18 11:43:28.501262', 'user', '', 'hassanuppal@gmail.com', '', '', '', '', '', '', '', '', 0, '', '', '', ''),
(4, 'pbkdf2_sha256$216000$AoQj8R2x80S3$33q482iP7F2oE8Lmy6XiJdxgFKi4jqbkAskDICOp62Q=', '2021-02-18 17:29:15.423345', 0, 'Hasssan', 'Shahbaz', 0, 1, '2021-02-18 17:29:15.113526', 'user', '', 'hassan+100@gmail.com', '', '', '', '', '', '', '', '', 0, '', '', '', ''),
(5, 'asdasdasd', NULL, 0, 'Hassa', 'Shahbaz', 0, 1, '2021-02-20 16:35:44.291232', 'user', '', '', 'jhjk', 'https://www.instagram.com/', '', '3410284656943', '', 'https://www.instagram.com/', 'https://www.instagram.com/', 'Cash On Delivery', 0, 'jhjk', '03217769665', 'Card', ''),
(6, 'pbkdf2_sha256$216000$0vxiTxHRqJd5$Dh0+lrfC7M2dJY2/pYsOcIokOVmw6xnHZXC6TlCIw0o=', '2021-05-05 09:36:16.777282', 0, 'Hassan', 'Shahbaz', 0, 1, '2021-02-20 16:44:01.382859', 'seller', '', 'hassanhhhh@gmail.com', 'kjkjk', 'https://www.instagram.com/', 'test.com', '34102-8465694-3', 'https://www.instagram.com/', 'https://www.instagram.com/', 'https://www.instagram.com/', 'Advance', 1, 'kjkjk', '0321-7769665', 'Card', 'test.com'),
(7, 'asdasdasd', NULL, 0, 'Hassan', 'Shahbaz', 0, 0, '2021-02-21 14:06:51.945029', 'seller', '', 'hassan+888@gmail.com', 'khjk', 'TCS', 'test', '3410284656943', 'TCS', 'https://www.instagram.com/', 'https://www.instagram.com/', 'Advance', 0, 'khjk', '03217769665', 'Card', 'test.com'),
(9, 'asdasdasd', NULL, 0, 'Hassa', 'Shahbaz', 0, 0, '2021-02-21 14:19:08.027161', 'seller', '', 'hassan+000@gmail.com', 'jkhjkh', 'TCS', 'test', '3410284656943', 'TCS', 'https://www.instagram.com/', 'https://www.instagram.com/', 'Advance', 0, 'jkhjkh', '03217769665', 'Cash', 'test.com'),
(10, 'asdasd', NULL, 0, 'jkj', 'jkkl', 0, 1, '2021-02-21 14:42:29.637181', 'seller', '', 'jkhk@gmail.com', 'jhkk', 'j', 'ljklj', 'hjkh', 'jl', 'lj', 'jkl', 'Advance', 0, 'jhkk', 'kjhjk', 'Card', 'lkjlk'),
(11, 'pbkdf2_sha256$216000$Z0uNpjPJCJuK$+UnivJtTe+4ntjYiF1ODy0JaNnOoQiHzw2LXCeSiIpU=', '2021-02-21 14:49:15.331262', 0, 'hk', 'hkh', 0, 1, '2021-02-21 14:47:29.102106', 'seller', '', 'kjkhkjh@gmail.com', 'hkj', 'i', 'yuiyiyi', 'hjk', 'uiy', 'yiy', 'yiy', 'Advance', 0, 'hkj', 'hjk', 'Cash', 'uyui'),
(12, 'pbkdf2_sha256$216000$UfKu6rip7Jqv$wD2jdUmUsWuSY1a5FGgP32OGYowGLjwFIz130JsW1mg=', NULL, 0, 'lj', 'klj', 0, 1, '2021-02-21 15:16:24.668358', 'seller', '', 'kljkjhkl@gmail.com', 'l', 'kj', 'hk', 'klj', 'kjh', 'hkh', 'h', 'Advance', 0, 'l', 'kj', 'Card', 'khkj'),
(13, 'pbkdf2_sha256$216000$dpzecQ303xBY$j+ivBNY/qX433hmYkT1DLKyqv6wb5Kae0dQagYB043Y=', NULL, 0, 'Hassan', 'Shahbaz', 0, 1, '2021-02-21 16:04:18.202582', 'user', '', 'hassan+0909@gmail.com', '', '', '', '', '', '', '', '', 0, '', '', '', ''),
(14, 'pbkdf2_sha256$216000$AHMYV5ukGzD6$waJdOj+0WElz5kFeX/+431sjT0XB245yBpB6wu5HbVc=', NULL, 0, 'Hassan', 'Shahbaz', 0, 1, '2021-02-21 16:06:37.900716', 'user', '', 'hassan+98766@gmail.com', '', '', '', '', '', '', '', '', 0, '', '', '', ''),
(15, 'pbkdf2_sha256$216000$HU9rhL8XWNMY$OOW+2uWs6KoaEhF0sDHFlwK04M6dB+5vACDyestEQ1M=', '2021-04-20 16:17:57.112123', 0, 'Hassan', 'Shahbaz', 0, 1, '2021-02-24 18:07:41.964656', 'seller', '', 'hassanshahbaz97@gmail.com', 'jkhk', 'jhkkj', 'abs', '34102-8465694-3', 'hkjk', 'kjh', 'jkhjk', 'Advance', 0, 'jkhk', '0321-7769665', 'Cash', 'abddd'),
(16, 'pbkdf2_sha256$216000$yNqIYPiyumGw$DN4O6uFx3+oyFsMKmRQ3c7zT45NQsVw3jWxKkLsWIto=', NULL, 0, 'Hassan', 'Shahbaz', 0, 0, '2021-02-24 19:16:18.013001', 'user', '', 'hassanshahbaz97+000@gmail.com', '', '', '', '', '', '', '', '', 0, '', '', '', ''),
(17, 'pbkdf2_sha256$216000$FYVPiIH2NwgH$1fY+zZdRyoC5hBv6rin/Q6hmEoTb/UqIBDHrqABt/jc=', '2021-03-15 18:17:48.612205', 0, 'Hassan', 'Shahbaz', 0, 1, '2021-02-24 19:16:43.843234', 'user', '', 'hassanshahbaz97+0900@gmail.com', '', '', '', '', '', '', '', '', 0, '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `vvouch_user_groups`
--

CREATE TABLE `vvouch_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vvouch_user_user_permissions`
--

CREATE TABLE `vvouch_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_vvouch_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `vvouch_activation`
--
ALTER TABLE `vvouch_activation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vvouch_productimages`
--
ALTER TABLE `vvouch_productimages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vvouch_productimages_created_by_id_d2990104_fk_vvouch_user_id` (`created_by_id`),
  ADD KEY `vvouch_productimages_product_id_a4b5ab0d_fk_vvouch_products_id` (`product_id`);

--
-- Indexes for table `vvouch_products`
--
ALTER TABLE `vvouch_products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vvouch_products_seller_id_ed60453a_fk_vvouch_user_id` (`seller_id`);

--
-- Indexes for table `vvouch_user`
--
ALTER TABLE `vvouch_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `vvouch_user_groups`
--
ALTER TABLE `vvouch_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `vvouch_user_groups_user_id_group_id_b8df31e0_uniq` (`user_id`,`group_id`),
  ADD KEY `vvouch_user_groups_group_id_e227d0f3_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `vvouch_user_user_permissions`
--
ALTER TABLE `vvouch_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `vvouch_user_user_permissions_user_id_permission_id_00fdfa18_uniq` (`user_id`,`permission_id`),
  ADD KEY `vvouch_user_user_per_permission_id_53154cfb_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- AUTO_INCREMENT for table `vvouch_activation`
--
ALTER TABLE `vvouch_activation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `vvouch_productimages`
--
ALTER TABLE `vvouch_productimages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `vvouch_products`
--
ALTER TABLE `vvouch_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `vvouch_user`
--
ALTER TABLE `vvouch_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT for table `vvouch_user_groups`
--
ALTER TABLE `vvouch_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `vvouch_user_user_permissions`
--
ALTER TABLE `vvouch_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_vvouch_user_id` FOREIGN KEY (`user_id`) REFERENCES `vvouch_user` (`id`);

--
-- Constraints for table `vvouch_productimages`
--
ALTER TABLE `vvouch_productimages`
  ADD CONSTRAINT `vvouch_productimages_created_by_id_d2990104_fk_vvouch_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `vvouch_user` (`id`),
  ADD CONSTRAINT `vvouch_productimages_product_id_a4b5ab0d_fk_vvouch_products_id` FOREIGN KEY (`product_id`) REFERENCES `vvouch_products` (`id`);

--
-- Constraints for table `vvouch_products`
--
ALTER TABLE `vvouch_products`
  ADD CONSTRAINT `vvouch_products_seller_id_ed60453a_fk_vvouch_user_id` FOREIGN KEY (`seller_id`) REFERENCES `vvouch_user` (`id`);

--
-- Constraints for table `vvouch_user_groups`
--
ALTER TABLE `vvouch_user_groups`
  ADD CONSTRAINT `vvouch_user_groups_group_id_e227d0f3_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `vvouch_user_groups_user_id_0245a1ef_fk_vvouch_user_id` FOREIGN KEY (`user_id`) REFERENCES `vvouch_user` (`id`);

--
-- Constraints for table `vvouch_user_user_permissions`
--
ALTER TABLE `vvouch_user_user_permissions`
  ADD CONSTRAINT `vvouch_user_user_per_permission_id_53154cfb_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `vvouch_user_user_permissions_user_id_99bf28a7_fk_vvouch_user_id` FOREIGN KEY (`user_id`) REFERENCES `vvouch_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
