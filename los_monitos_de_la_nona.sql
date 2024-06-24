-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3308
-- Tiempo de generación: 24-06-2024 a las 19:59:04
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `los_monitos_de_la_nona`
--
CREATE DATABASE IF NOT EXISTS `los_monitos_de_la_nona` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `los_monitos_de_la_nona`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador`
--

DROP TABLE IF EXISTS `administrador`;
CREATE TABLE `administrador` (
  `id_admin` int(11) NOT NULL,
  `usuario` varchar(45) NOT NULL,
  `password` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`id_admin`, `usuario`, `password`) VALUES
(1, 'admin', '202cb962ac59075b964b07152d234b70');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega`
--

DROP TABLE IF EXISTS `bodega`;
CREATE TABLE `bodega` (
  `id_bodega` int(11) NOT NULL,
  `nombre` varchar(55) NOT NULL,
  `direccion` varchar(55) NOT NULL,
  `fk_id_producto` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bodega`
--

INSERT INTO `bodega` (`id_bodega`, `nombre`, `direccion`, `fk_id_producto`, `CREATEDAT`, `UPDATEDAT`) VALUES
(9, 'bodega 1', 'calle 1', NULL, '2024-06-23 21:01:33', '2024-06-23 21:01:33');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega_producto`
--

DROP TABLE IF EXISTS `bodega_producto`;
CREATE TABLE `bodega_producto` (
  `id` int(11) NOT NULL,
  `fk_id_bodega` int(11) NOT NULL,
  `fk_id_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `bodega_producto`
--

INSERT INTO `bodega_producto` (`id`, `fk_id_bodega`, `fk_id_producto`, `cantidad`) VALUES
(6, 9, 19, 100),
(7, 9, 20, 100);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boleta`
--

DROP TABLE IF EXISTS `boleta`;
CREATE TABLE `boleta` (
  `id_venta_boleta` int(11) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `fk_id_cliente` int(11) DEFAULT NULL,
  `subtotal` int(11) NOT NULL,
  `iva` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `boleta`
--

INSERT INTO `boleta` (`id_venta_boleta`, `fk_id_vendedor`, `fk_id_cliente`, `subtotal`, `iva`, `total`, `fecha`, `CREATEDAT`, `UPDATEDAT`) VALUES
(27, 3, 0, 1000, 190, 1190, '2024-06-24', '2024-06-24 16:09:20', '2024-06-24 16:09:20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE `cliente` (
  `rut_cliente` int(11) NOT NULL,
  `direccion_cliente` varchar(50) NOT NULL,
  `nombre_cliente` varchar(50) NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`rut_cliente`, `direccion_cliente`, `nombre_cliente`, `CREATEDAT`, `UPDATEDAT`) VALUES
(0, 'calle 1', 'cholita', '2024-06-23 22:52:23', NULL),
(2, '', 'holas', '2024-06-24 03:45:46', NULL),
(14578, 'sda', 'cholita insana', '2024-06-23 23:57:18', NULL),
(11111111, 'bejamin@gmail.com', 'bnejamin', '2024-06-23 23:11:52', NULL),
(11123321, 'calle 6', 'violeta', '2024-06-23 23:12:58', NULL),
(111111111, 'calle 4', 'benjamin', '2024-06-23 23:11:26', NULL),
(1234567890, 'calle 3', 'crisstian', '2024-06-23 23:09:26', NULL),
(2147483647, 'calle 1', 'cholita', '2024-06-23 22:51:28', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_venta`
--

DROP TABLE IF EXISTS `detalle_venta`;
CREATE TABLE `detalle_venta` (
  `id_detalle_venta` int(11) NOT NULL,
  `id_venta_boleta` int(11) DEFAULT NULL,
  `id_venta_factura` int(11) DEFAULT NULL,
  `id_nota_credito` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalle_venta`
--

INSERT INTO `detalle_venta` (`id_detalle_venta`, `id_venta_boleta`, `id_venta_factura`, `id_nota_credito`, `id_producto`, `cantidad`, `CREATEDAT`, `UPDATEDAT`) VALUES
(11, 27, NULL, NULL, 20, 1, '2024-06-24 16:09:20', '2024-06-24 16:09:20'),
(12, 27, NULL, 8, 20, 1, '2024-06-24 16:09:56', '2024-06-24 16:09:56');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_cliente`
--

DROP TABLE IF EXISTS `email_cliente`;
CREATE TABLE `email_cliente` (
  `id_email_cliente` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fk_rut_cliente` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `email_cliente`
--

INSERT INTO `email_cliente` (`id_email_cliente`, `email`, `fk_rut_cliente`, `CREATEDAT`, `UPDATEDAT`) VALUES
(1, 'emailq@gmail.com', 2147483647, '2024-06-23 22:51:28', NULL),
(2, '454dsa', 0, '2024-06-23 22:52:23', NULL),
(3, 'cristian@mail.com', 1234567890, '2024-06-23 23:09:26', NULL),
(4, 'benja@gmial.com', 111111111, '2024-06-23 23:11:26', NULL),
(5, 'benjamin@gmail', 11111111, '2024-06-23 23:11:52', NULL),
(6, 'violeta@gmail.com', 11123321, '2024-06-23 23:12:58', NULL),
(7, 'hola', 14578, '2024-06-23 23:57:18', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_jefe_ventas`
--

DROP TABLE IF EXISTS `email_jefe_ventas`;
CREATE TABLE `email_jefe_ventas` (
  `id_email` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fk_id_jefe_ventas` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `email_jefe_ventas`
--

INSERT INTO `email_jefe_ventas` (`id_email`, `email`, `fk_id_jefe_ventas`, `CREATEDAT`, `UPDATEDAT`) VALUES
(3, '', 3, '2024-06-22 02:43:31', '2024-06-22 02:43:31');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_proveedor`
--

DROP TABLE IF EXISTS `email_proveedor`;
CREATE TABLE `email_proveedor` (
  `id_email` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fk_rut_prov` varchar(10) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `email_proveedor`
--

INSERT INTO `email_proveedor` (`id_email`, `email`, `fk_rut_prov`, `CREATEDAT`, `UPDATEDAT`) VALUES
(4, 'cristian@gmail.com', '19346666-4', '2024-06-23 19:13:53', '2024-06-23 19:13:53'),
(5, 'alejo@gmail.com', '11745778-8', '2024-06-23 19:19:44', '2024-06-23 19:19:44');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_vendedor`
--

DROP TABLE IF EXISTS `email_vendedor`;
CREATE TABLE `email_vendedor` (
  `id_email` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `email_vendedor`
--

INSERT INTO `email_vendedor` (`id_email`, `email`, `fk_id_vendedor`, `CREATEDAT`, `UPDATEDAT`) VALUES
(2, '', 2, '2024-06-22 02:42:20', '2024-06-22 02:42:20'),
(3, 'emilio@gmail.com', 3, '2024-06-23 21:04:34', '2024-06-23 21:04:34');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

DROP TABLE IF EXISTS `factura`;
CREATE TABLE `factura` (
  `id_venta_factura` int(11) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `fk_id_cliente` int(11) DEFAULT NULL,
  `subtotal` int(11) NOT NULL,
  `iva` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jefe_ventas`
--

DROP TABLE IF EXISTS `jefe_ventas`;
CREATE TABLE `jefe_ventas` (
  `id_jefe_ventas` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `fk_id_admin` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  `state_at` char(1) NOT NULL CHECK (`state_at` in ('Y','N'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `jefe_ventas`
--

INSERT INTO `jefe_ventas` (`id_jefe_ventas`, `nombre`, `password`, `fk_id_admin`, `CREATEDAT`, `UPDATEDAT`, `state_at`) VALUES
(3, 'cristian', '202cb962ac59075b964b07152d234b70', 1, '2024-06-22 02:43:31', '2024-06-22 02:43:31', 'y');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nota_credito`
--

DROP TABLE IF EXISTS `nota_credito`;
CREATE TABLE `nota_credito` (
  `id_nota_credito` int(11) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `fk_id_cliente` int(11) DEFAULT NULL,
  `fk_id_boleta` int(11) DEFAULT NULL,
  `fk_id_factura` int(11) DEFAULT NULL,
  `subtotal` int(11) DEFAULT NULL,
  `iva` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `motivo` varchar(255) NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `nota_credito`
--

INSERT INTO `nota_credito` (`id_nota_credito`, `fk_id_vendedor`, `fk_id_cliente`, `fk_id_boleta`, `fk_id_factura`, `subtotal`, `iva`, `total`, `fecha`, `motivo`, `CREATEDAT`, `UPDATEDAT`) VALUES
(8, 3, 0, 27, NULL, 1000, 190, 1190, '2024-06-24', 'vencido', '2024-06-24 16:09:56', '2024-06-24 16:09:56');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

DROP TABLE IF EXISTS `producto`;
CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `valor_unitario` int(11) NOT NULL,
  `fk_rut_prov` varchar(10) DEFAULT NULL,
  `fecha_elaboracion` date NOT NULL,
  `fecha_caducidad` date NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id_producto`, `nombre`, `cantidad`, `valor_unitario`, `fk_rut_prov`, `fecha_elaboracion`, `fecha_caducidad`, `CREATEDAT`, `UPDATEDAT`) VALUES
(19, 'chocolate insano', 0, 1500, '11745778-8', '2023-02-02', '2023-03-02', '2024-06-24 00:21:46', '2024-06-24 00:21:46'),
(20, 'coca cola 1l ', 7, 1000, '19346666-4', '2023-01-01', '2023-02-02', '2024-06-24 00:22:42', '2024-06-24 00:22:42');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
CREATE TABLE `proveedor` (
  `rut_prov` varchar(10) NOT NULL,
  `nombre` varchar(55) NOT NULL,
  `direccion_prov` varchar(55) NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`rut_prov`, `nombre`, `direccion_prov`, `CREATEDAT`, `UPDATEDAT`) VALUES
('11745778-8', 'alejo', '123', '2024-06-23 19:19:36', '2024-06-23 19:19:36'),
('19346666-4', 'cristian', 'calle 3', '2024-06-23 19:13:47', '2024-06-23 19:13:47');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_cliente`
--

DROP TABLE IF EXISTS `telefono_cliente`;
CREATE TABLE `telefono_cliente` (
  `id_telefono_cliente` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `fk_rut_cliente` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `telefono_cliente`
--

INSERT INTO `telefono_cliente` (`id_telefono_cliente`, `telefono`, `fk_rut_cliente`, `CREATEDAT`, `UPDATEDAT`) VALUES
(1, '11554', 2147483647, '2024-06-23 22:51:28', NULL),
(2, '465445', 0, '2024-06-23 22:52:23', NULL),
(3, '+56988888', 1234567890, '2024-06-23 23:09:26', NULL),
(4, '554446545', 111111111, '2024-06-23 23:11:26', NULL),
(5, '4645546', 11111111, '2024-06-23 23:11:52', NULL),
(6, '45645456', 11123321, '2024-06-23 23:12:58', NULL),
(7, '5546', 14578, '2024-06-23 23:57:18', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_jefe_ventas`
--

DROP TABLE IF EXISTS `telefono_jefe_ventas`;
CREATE TABLE `telefono_jefe_ventas` (
  `id_telefono` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `fk_id_jefe_ventas` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `telefono_jefe_ventas`
--

INSERT INTO `telefono_jefe_ventas` (`id_telefono`, `telefono`, `fk_id_jefe_ventas`, `CREATEDAT`, `UPDATEDAT`) VALUES
(3, '', 3, '2024-06-22 02:43:31', '2024-06-22 02:43:31');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_proveedor`
--

DROP TABLE IF EXISTS `telefono_proveedor`;
CREATE TABLE `telefono_proveedor` (
  `id_telefono` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `fk_rut_prov` varchar(10) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `telefono_proveedor`
--

INSERT INTO `telefono_proveedor` (`id_telefono`, `telefono`, `fk_rut_prov`, `CREATEDAT`, `UPDATEDAT`) VALUES
(4, '+569888', '19346666-4', '2024-06-23 19:13:56', '2024-06-23 19:13:56'),
(5, '122222', '11745778-8', '2024-06-23 19:19:48', '2024-06-23 19:19:48');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_vendedor`
--

DROP TABLE IF EXISTS `telefono_vendedor`;
CREATE TABLE `telefono_vendedor` (
  `id_telefono` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `telefono_vendedor`
--

INSERT INTO `telefono_vendedor` (`id_telefono`, `telefono`, `fk_id_vendedor`, `CREATEDAT`, `UPDATEDAT`) VALUES
(2, '', 2, '2024-06-22 02:42:20', '2024-06-22 02:42:20'),
(3, '+5698787878', 3, '2024-06-23 21:04:34', '2024-06-23 21:04:34');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

DROP TABLE IF EXISTS `vendedor`;
CREATE TABLE `vendedor` (
  `id_vendedor` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `fk_id_admin` int(11) DEFAULT NULL,
  `password` varchar(50) NOT NULL,
  `state_at` char(1) NOT NULL CHECK (`state_at` in ('Y','N')),
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vendedor`
--

INSERT INTO `vendedor` (`id_vendedor`, `nombre`, `fk_id_admin`, `password`, `state_at`, `CREATEDAT`, `UPDATEDAT`) VALUES
(2, 'mia', 1, '202cb962ac59075b964b07152d234b70', 'y', '2024-06-22 02:42:20', '2024-06-22 02:42:20'),
(3, 'emilio', 1, '202cb962ac59075b964b07152d234b70', 'y', '2024-06-23 21:04:34', '2024-06-23 21:04:34');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indices de la tabla `bodega`
--
ALTER TABLE `bodega`
  ADD PRIMARY KEY (`id_bodega`),
  ADD KEY `bodega_ibfk_1` (`fk_id_producto`);

--
-- Indices de la tabla `bodega_producto`
--
ALTER TABLE `bodega_producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_bodega` (`fk_id_bodega`),
  ADD KEY `fk_id_producto` (`fk_id_producto`);

--
-- Indices de la tabla `boleta`
--
ALTER TABLE `boleta`
  ADD PRIMARY KEY (`id_venta_boleta`),
  ADD KEY `fk_id_vendedor` (`fk_id_vendedor`),
  ADD KEY `fk_id_cliente` (`fk_id_cliente`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`rut_cliente`);

--
-- Indices de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD PRIMARY KEY (`id_detalle_venta`),
  ADD KEY `id_venta_boleta` (`id_venta_boleta`),
  ADD KEY `id_venta_factura` (`id_venta_factura`),
  ADD KEY `id_nota_credito` (`id_nota_credito`),
  ADD KEY `id_producto` (`id_producto`);

--
-- Indices de la tabla `email_cliente`
--
ALTER TABLE `email_cliente`
  ADD PRIMARY KEY (`id_email_cliente`),
  ADD KEY `fk_rut_cliente` (`fk_rut_cliente`);

--
-- Indices de la tabla `email_jefe_ventas`
--
ALTER TABLE `email_jefe_ventas`
  ADD PRIMARY KEY (`id_email`),
  ADD KEY `fk_id_jefe_ventas` (`fk_id_jefe_ventas`);

--
-- Indices de la tabla `email_proveedor`
--
ALTER TABLE `email_proveedor`
  ADD PRIMARY KEY (`id_email`),
  ADD KEY `fk_rut_prov` (`fk_rut_prov`);

--
-- Indices de la tabla `email_vendedor`
--
ALTER TABLE `email_vendedor`
  ADD PRIMARY KEY (`id_email`),
  ADD KEY `fk_id_vendedor` (`fk_id_vendedor`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`id_venta_factura`),
  ADD KEY `fk_id_vendedor` (`fk_id_vendedor`),
  ADD KEY `fk_id_cliente` (`fk_id_cliente`);

--
-- Indices de la tabla `jefe_ventas`
--
ALTER TABLE `jefe_ventas`
  ADD PRIMARY KEY (`id_jefe_ventas`),
  ADD KEY `fk_admin_id` (`fk_id_admin`);

--
-- Indices de la tabla `nota_credito`
--
ALTER TABLE `nota_credito`
  ADD PRIMARY KEY (`id_nota_credito`),
  ADD KEY `fk_id_vendedor` (`fk_id_vendedor`),
  ADD KEY `fk_id_cliente` (`fk_id_cliente`),
  ADD KEY `fk_id_boleta` (`fk_id_boleta`),
  ADD KEY `fk_id_factura` (`fk_id_factura`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `fk_rut_prov` (`fk_rut_prov`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`rut_prov`);

--
-- Indices de la tabla `telefono_cliente`
--
ALTER TABLE `telefono_cliente`
  ADD PRIMARY KEY (`id_telefono_cliente`),
  ADD KEY `fk_rut_cliente` (`fk_rut_cliente`);

--
-- Indices de la tabla `telefono_jefe_ventas`
--
ALTER TABLE `telefono_jefe_ventas`
  ADD PRIMARY KEY (`id_telefono`),
  ADD KEY `fk_id_jefe_ventas` (`fk_id_jefe_ventas`);

--
-- Indices de la tabla `telefono_proveedor`
--
ALTER TABLE `telefono_proveedor`
  ADD PRIMARY KEY (`id_telefono`),
  ADD KEY `fk_rut_prov` (`fk_rut_prov`);

--
-- Indices de la tabla `telefono_vendedor`
--
ALTER TABLE `telefono_vendedor`
  ADD PRIMARY KEY (`id_telefono`),
  ADD KEY `fk_id_vendedor` (`fk_id_vendedor`);

--
-- Indices de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`id_vendedor`),
  ADD KEY `fk_id_admin` (`fk_id_admin`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `bodega`
--
ALTER TABLE `bodega`
  MODIFY `id_bodega` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `bodega_producto`
--
ALTER TABLE `bodega_producto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `boleta`
--
ALTER TABLE `boleta`
  MODIFY `id_venta_boleta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  MODIFY `id_detalle_venta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `email_cliente`
--
ALTER TABLE `email_cliente`
  MODIFY `id_email_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `email_jefe_ventas`
--
ALTER TABLE `email_jefe_ventas`
  MODIFY `id_email` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `email_proveedor`
--
ALTER TABLE `email_proveedor`
  MODIFY `id_email` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `email_vendedor`
--
ALTER TABLE `email_vendedor`
  MODIFY `id_email` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `id_venta_factura` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `jefe_ventas`
--
ALTER TABLE `jefe_ventas`
  MODIFY `id_jefe_ventas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `nota_credito`
--
ALTER TABLE `nota_credito`
  MODIFY `id_nota_credito` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `telefono_cliente`
--
ALTER TABLE `telefono_cliente`
  MODIFY `id_telefono_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `telefono_jefe_ventas`
--
ALTER TABLE `telefono_jefe_ventas`
  MODIFY `id_telefono` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `telefono_proveedor`
--
ALTER TABLE `telefono_proveedor`
  MODIFY `id_telefono` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `telefono_vendedor`
--
ALTER TABLE `telefono_vendedor`
  MODIFY `id_telefono` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  MODIFY `id_vendedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `bodega`
--
ALTER TABLE `bodega`
  ADD CONSTRAINT `bodega_ibfk_1` FOREIGN KEY (`fk_id_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `bodega_producto`
--
ALTER TABLE `bodega_producto`
  ADD CONSTRAINT `bodega_producto_ibfk_1` FOREIGN KEY (`fk_id_bodega`) REFERENCES `bodega` (`id_bodega`),
  ADD CONSTRAINT `bodega_producto_ibfk_2` FOREIGN KEY (`fk_id_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `boleta`
--
ALTER TABLE `boleta`
  ADD CONSTRAINT `boleta_ibfk_1` FOREIGN KEY (`fk_id_vendedor`) REFERENCES `vendedor` (`id_vendedor`),
  ADD CONSTRAINT `boleta_ibfk_2` FOREIGN KEY (`fk_id_cliente`) REFERENCES `cliente` (`rut_cliente`);

--
-- Filtros para la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD CONSTRAINT `detalle_venta_ibfk_1` FOREIGN KEY (`id_venta_boleta`) REFERENCES `boleta` (`id_venta_boleta`),
  ADD CONSTRAINT `detalle_venta_ibfk_2` FOREIGN KEY (`id_venta_factura`) REFERENCES `factura` (`id_venta_factura`),
  ADD CONSTRAINT `detalle_venta_ibfk_3` FOREIGN KEY (`id_nota_credito`) REFERENCES `nota_credito` (`id_nota_credito`),
  ADD CONSTRAINT `detalle_venta_ibfk_4` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`);

--
-- Filtros para la tabla `email_cliente`
--
ALTER TABLE `email_cliente`
  ADD CONSTRAINT `email_cliente_ibfk_1` FOREIGN KEY (`fk_rut_cliente`) REFERENCES `cliente` (`rut_cliente`);

--
-- Filtros para la tabla `email_jefe_ventas`
--
ALTER TABLE `email_jefe_ventas`
  ADD CONSTRAINT `email_jefe_ventas_ibfk_1` FOREIGN KEY (`fk_id_jefe_ventas`) REFERENCES `jefe_ventas` (`id_jefe_ventas`);

--
-- Filtros para la tabla `email_proveedor`
--
ALTER TABLE `email_proveedor`
  ADD CONSTRAINT `email_proveedor_ibfk_1` FOREIGN KEY (`fk_rut_prov`) REFERENCES `proveedor` (`rut_prov`);

--
-- Filtros para la tabla `email_vendedor`
--
ALTER TABLE `email_vendedor`
  ADD CONSTRAINT `email_vendedor_ibfk_1` FOREIGN KEY (`fk_id_vendedor`) REFERENCES `vendedor` (`id_vendedor`);

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`fk_id_vendedor`) REFERENCES `vendedor` (`id_vendedor`),
  ADD CONSTRAINT `factura_ibfk_2` FOREIGN KEY (`fk_id_cliente`) REFERENCES `cliente` (`rut_cliente`);

--
-- Filtros para la tabla `jefe_ventas`
--
ALTER TABLE `jefe_ventas`
  ADD CONSTRAINT `fk_admin_id` FOREIGN KEY (`fk_id_admin`) REFERENCES `administrador` (`id_admin`);

--
-- Filtros para la tabla `nota_credito`
--
ALTER TABLE `nota_credito`
  ADD CONSTRAINT `nota_credito_ibfk_1` FOREIGN KEY (`fk_id_vendedor`) REFERENCES `vendedor` (`id_vendedor`),
  ADD CONSTRAINT `nota_credito_ibfk_2` FOREIGN KEY (`fk_id_cliente`) REFERENCES `cliente` (`rut_cliente`),
  ADD CONSTRAINT `nota_credito_ibfk_3` FOREIGN KEY (`fk_id_boleta`) REFERENCES `boleta` (`id_venta_boleta`),
  ADD CONSTRAINT `nota_credito_ibfk_4` FOREIGN KEY (`fk_id_factura`) REFERENCES `factura` (`id_venta_factura`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`fk_rut_prov`) REFERENCES `proveedor` (`rut_prov`);

--
-- Filtros para la tabla `telefono_cliente`
--
ALTER TABLE `telefono_cliente`
  ADD CONSTRAINT `telefono_cliente_ibfk_1` FOREIGN KEY (`fk_rut_cliente`) REFERENCES `cliente` (`rut_cliente`);

--
-- Filtros para la tabla `telefono_jefe_ventas`
--
ALTER TABLE `telefono_jefe_ventas`
  ADD CONSTRAINT `telefono_jefe_ventas_ibfk_1` FOREIGN KEY (`fk_id_jefe_ventas`) REFERENCES `jefe_ventas` (`id_jefe_ventas`);

--
-- Filtros para la tabla `telefono_proveedor`
--
ALTER TABLE `telefono_proveedor`
  ADD CONSTRAINT `telefono_proveedor_ibfk_1` FOREIGN KEY (`fk_rut_prov`) REFERENCES `proveedor` (`rut_prov`);

--
-- Filtros para la tabla `telefono_vendedor`
--
ALTER TABLE `telefono_vendedor`
  ADD CONSTRAINT `telefono_vendedor_ibfk_1` FOREIGN KEY (`fk_id_vendedor`) REFERENCES `vendedor` (`id_vendedor`);

--
-- Filtros para la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD CONSTRAINT `vendedor_ibfk_1` FOREIGN KEY (`fk_id_admin`) REFERENCES `administrador` (`id_admin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
