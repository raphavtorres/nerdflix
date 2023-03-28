CREATE DATABASE nerdflix;

USE nerdflix;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nameUser VARCHAR(50),
    emailUser VARCHAR(50),
    ageUser INT,
    typeUser VARCHAR(20),
    planUser VARCHAR(20)
);

CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nameMovie VARCHAR(50),
    ageGroup INT,
    category VARCHAR(20),
    planMovie VARCHAR(20)
);

INSERT INTO user (nameUser, emailUser, ageUser, typeUser, planUser) VALUES ('{name}','{email}','{age}','{usertype}','{plan}')

INSERT INTO user (nameMovie, ageGroup, category, planMovie) VALUES ('{name}','{age}','{category}','{plan}')


UPDATE user
SET nameUser = '{name}'
WHERE id = '{id}'

















-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28-Mar-2023 às 02:05
-- Versão do servidor: 10.4.21-MariaDB
-- versão do PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `nerdflix`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `movie`
--

CREATE TABLE `movie` (
  `id` int(11) NOT NULL,
  `nameMovie` varchar(50) DEFAULT NULL,
  `ageGroup` int(11) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `planMovie` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `movie`
--

INSERT INTO `movie` (`id`, `nameMovie`, `ageGroup`, `category`, `planMovie`) VALUES
(1, 'Die Hard', 16, 'suspense', 'medium'),
(2, 'Shrek', 0, 'animation', 'basic');

-- --------------------------------------------------------

--
-- Estrutura da tabela `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `nameUser` varchar(50) DEFAULT NULL,
  `emailUser` varchar(50) DEFAULT NULL,
  `ageUser` int(11) DEFAULT NULL,
  `typeUser` varchar(20) DEFAULT NULL,
  `planUser` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `user`
--

INSERT INTO `user` (`id`, `nameUser`, `emailUser`, `ageUser`, `typeUser`, `planUser`) VALUES
(1, 'Ester', 'ester@', 18, 'regular', 'basic'),
(2, 'Estevan', 'raphael@', 19, 'adm', 'basic'),
(3, 'Raphael', 'raphael', 19, 'regular', 'medium');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `movie`
--
ALTER TABLE `movie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
