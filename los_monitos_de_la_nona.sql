-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3308
-- Tiempo de generación: 10-06-2024 a las 17:36:23
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

CREATE TABLE `administrador` (
  `id_admin` int(11) NOT NULL,
  `usuario` varchar(45) NOT NULL,
  `password` varchar(55) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`id_admin`, `usuario`, `password`) VALUES
(1, 'cholita', '202cb962ac59075b964b07152d234b70');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega`
--

CREATE TABLE `bodega` (
  `id_bodega` int(11) NOT NULL,
  `nombre` varchar(55) NOT NULL,
  `direccion` varchar(55) NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boleta`
--

CREATE TABLE `boleta` (
  `id_venta_boleta` int(11) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `fk_id_cliente` int(11) DEFAULT NULL,
  `productos` text NOT NULL,
  `cantidad` text NOT NULL,
  `subtotal` int(11) NOT NULL,
  `iva` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `rut_cliente` int(11) NOT NULL,
  `direccion_cliente` varchar(50) NOT NULL,
  `nombre_cliente` varchar(50) NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_cliente`
--

CREATE TABLE `email_cliente` (
  `id_email_cliente` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fk_rut_cliente` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_jefe_ventas`
--

CREATE TABLE `email_jefe_ventas` (
  `id_email` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fk_id_jefe_ventas` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_proveedor`
--

CREATE TABLE `email_proveedor` (
  `id_email` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fk_rut_prov` varchar(10) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_vendedor`
--

CREATE TABLE `email_vendedor` (
  `id_email` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `id_venta_factura` int(11) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `fk_id_cliente` int(11) DEFAULT NULL,
  `productos` text NOT NULL,
  `cantidad` text NOT NULL,
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

CREATE TABLE `jefe_ventas` (
  `id_jefe_ventas` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `fk_id_admin` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  `state_at` char(1) NOT NULL CHECK (`state_at` in ('Y','N'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `rut_prov` varchar(10) NOT NULL,
  `nombre` varchar(55) NOT NULL,
  `direccion_prov` varchar(55) NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_cliente`
--

CREATE TABLE `telefono_cliente` (
  `id_telefono_cliente` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `fk_rut_cliente` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_jefe_ventas`
--

CREATE TABLE `telefono_jefe_ventas` (
  `id_telefono` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `fk_id_jefe_ventas` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_proveedor`
--

CREATE TABLE `telefono_proveedor` (
  `id_telefono` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `fk_rut_prov` varchar(10) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_vendedor`
--

CREATE TABLE `telefono_vendedor` (
  `id_telefono` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

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
  ADD PRIMARY KEY (`id_bodega`);

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
-- AUTO_INCREMENT de la tabla `boleta`
--
ALTER TABLE `boleta`
  MODIFY `id_venta_boleta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `email_cliente`
--
ALTER TABLE `email_cliente`
  MODIFY `id_email_cliente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `email_jefe_ventas`
--
ALTER TABLE `email_jefe_ventas`
  MODIFY `id_email` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `email_proveedor`
--
ALTER TABLE `email_proveedor`
  MODIFY `id_email` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `email_vendedor`
--
ALTER TABLE `email_vendedor`
  MODIFY `id_email` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `id_venta_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `jefe_ventas`
--
ALTER TABLE `jefe_ventas`
  MODIFY `id_jefe_ventas` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `telefono_cliente`
--
ALTER TABLE `telefono_cliente`
  MODIFY `id_telefono_cliente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `telefono_jefe_ventas`
--
ALTER TABLE `telefono_jefe_ventas`
  MODIFY `id_telefono` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `telefono_proveedor`
--
ALTER TABLE `telefono_proveedor`
  MODIFY `id_telefono` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `telefono_vendedor`
--
ALTER TABLE `telefono_vendedor`
  MODIFY `id_telefono` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  MODIFY `id_vendedor` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `boleta`
--
ALTER TABLE `boleta`
  ADD CONSTRAINT `boleta_ibfk_1` FOREIGN KEY (`fk_id_vendedor`) REFERENCES `vendedor` (`id_vendedor`),
  ADD CONSTRAINT `boleta_ibfk_2` FOREIGN KEY (`fk_id_cliente`) REFERENCES `cliente` (`rut_cliente`);

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
