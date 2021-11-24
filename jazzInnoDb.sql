-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-07-2021 a las 01:14:44
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `jazz`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `id` int(10) NOT NULL,
  `spa` varchar(10) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `proceso` varchar(20) NOT NULL,
  `duracion` varchar(20) NOT NULL,
  `precio` decimal(6,2) NOT NULL,
  `foto` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `servicios`
--

INSERT INTO `servicios` (`id`, `spa`, `nombre`, `proceso`, `duracion`, `precio`, `foto`) VALUES
(1, 'uñas', 'Manicuría básica con opción de esmaltado común', '1 hora', '7 a 15 días', '700.00', '2021144846mani.png'),
(2, 'uñas', 'Manicuría con esmaltado semipermanente (Incluye 2 decoraciones)', '2 horas', '20 a 40 días', '1000.00', '2021144944semi.jpg'),
(3, 'uñas', 'Capping con gel o acrigel. Incluye 2 decoraciones a elección en total.', '3 horas', '20 a 40 días', '1200.00', '2021145028capping.jpg'),
(4, 'uñas', 'Esculpidas con gel o acrigel. Incluye 2 decoraciones a elección en total.', '4 horas', '20 a 40 días', '1650.00', '2021145129esculpidas.jpg'),
(5, 'uñas', 'Reparación/reconstrucción de uña rota natural o esculpida.', '30 minutos', '20 a 40 días', '200.00', '2021145202reparacion.png'),
(6, 'uñas', 'Decoración de uña extra. Glitter, piedras, dibujo, etc.', '30 minutos', '20 a 40 días', '100.00', '2021145237deco.jpg'),
(7, 'uñas', 'Remoción sin renovación del servicio.\\r\\nIncluye manicuría básica.\\r\\nSemipermanente', '60 minutos', '', '400.00', '2021145351remocion.jpg'),
(8, 'uñas', 'Remoción sin renovación del servicio. Incluye manicuría básica. Capping.', '60 minutos', '', '500.00', '2021145556remocion.jpg'),
(9, 'uñas', 'Remoción sin renovación del servicio. Incluye manicuría básica. Esculpidas.', '60 minutos', '', '600.00', '2021145629remocion.jpg'),
(10, 'uñas', 'Pedicuría básica con opción de esmaltado común.', '60 minutos', '15 a 30 días', '1000.00', '2021145704pedi.jpg'),
(11, 'uñas', 'Pedicuría con esmaltado semipermanente.', '2 horas', '1 a 2 meses', '1200.00', '2021145741pedi-semi.png'),
(12, 'pestañas', 'Lifting de pestañas', '30 minutos', '1 a 2 meses', '900.00', '2021145827lifting.png'),
(13, 'pestañas', 'Lifting de pestañas + tinte', '60 minutos', '1 a 2 meses', '1000.00', '2021145859lifting+tinte.png'),
(14, 'cejas', 'Perfilado y diseño de cejas', '30 minutos', '1 a 2 meses', '750.00', '2021145931cejas.png'),
(15, 'cejas', 'Perfilado + tinte de cejas', '60 minutos', '1 a 2 meses', '850.00', '2021150007cejas-tinte.png'),
(16, 'were', 'Trinidad Boragini', '60 minutos', '7 a 15 días', '1200.00', '2021200119logo.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(255) NOT NULL,
  `username` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(10) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
