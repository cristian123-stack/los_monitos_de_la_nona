-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3308
-- Tiempo de generación: 08-07-2024 a las 17:12:50
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
CREATE TABLE IF NOT EXISTS `administrador` (
  `id_admin` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `password` varchar(55) NOT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
CREATE TABLE IF NOT EXISTS `bodega` (
  `id_bodega` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(55) NOT NULL,
  `direccion` varchar(55) NOT NULL,
  `fk_id_producto` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_bodega`),
  KEY `bodega_ibfk_1` (`fk_id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bodega_producto`
--

DROP TABLE IF EXISTS `bodega_producto`;
CREATE TABLE IF NOT EXISTS `bodega_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fk_id_bodega` int(11) NOT NULL,
  `fk_id_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_id_bodega` (`fk_id_bodega`),
  KEY `fk_id_producto` (`fk_id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `boleta`
--

DROP TABLE IF EXISTS `boleta`;
CREATE TABLE IF NOT EXISTS `boleta` (
  `id_venta_boleta` int(11) NOT NULL AUTO_INCREMENT,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `fk_id_cliente` int(11) DEFAULT NULL,
  `subtotal` int(11) NOT NULL,
  `iva` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_venta_boleta`),
  KEY `fk_id_vendedor` (`fk_id_vendedor`),
  KEY `fk_id_cliente` (`fk_id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE IF NOT EXISTS `cliente` (
  `rut_cliente` int(11) NOT NULL,
  `direccion_cliente` varchar(50) NOT NULL,
  `nombre_cliente` varchar(50) NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`rut_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_venta`
--

DROP TABLE IF EXISTS `detalle_venta`;
CREATE TABLE IF NOT EXISTS `detalle_venta` (
  `id_detalle_venta` int(11) NOT NULL AUTO_INCREMENT,
  `id_venta_boleta` int(11) DEFAULT NULL,
  `id_venta_factura` int(11) DEFAULT NULL,
  `id_nota_credito` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id_detalle_venta`),
  KEY `id_venta_boleta` (`id_venta_boleta`),
  KEY `id_venta_factura` (`id_venta_factura`),
  KEY `id_nota_credito` (`id_nota_credito`),
  KEY `id_producto` (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_cliente`
--

DROP TABLE IF EXISTS `email_cliente`;
CREATE TABLE IF NOT EXISTS `email_cliente` (
  `id_email_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `fk_rut_cliente` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_email_cliente`),
  KEY `fk_rut_cliente` (`fk_rut_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_jefe_ventas`
--

DROP TABLE IF EXISTS `email_jefe_ventas`;
CREATE TABLE IF NOT EXISTS `email_jefe_ventas` (
  `id_email` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `fk_id_jefe_ventas` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_email`),
  KEY `fk_id_jefe_ventas` (`fk_id_jefe_ventas`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_proveedor`
--

DROP TABLE IF EXISTS `email_proveedor`;
CREATE TABLE IF NOT EXISTS `email_proveedor` (
  `id_email` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `fk_rut_prov` varchar(10) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_email`),
  KEY `fk_rut_prov` (`fk_rut_prov`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `email_vendedor`
--

DROP TABLE IF EXISTS `email_vendedor`;
CREATE TABLE IF NOT EXISTS `email_vendedor` (
  `id_email` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_email`),
  KEY `fk_id_vendedor` (`fk_id_vendedor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

DROP TABLE IF EXISTS `factura`;
CREATE TABLE IF NOT EXISTS `factura` (
  `id_venta_factura` int(11) NOT NULL AUTO_INCREMENT,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `fk_id_cliente` int(11) DEFAULT NULL,
  `subtotal` int(11) NOT NULL,
  `iva` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_venta_factura`),
  KEY `fk_id_vendedor` (`fk_id_vendedor`),
  KEY `fk_id_cliente` (`fk_id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jefe_ventas`
--

DROP TABLE IF EXISTS `jefe_ventas`;
CREATE TABLE IF NOT EXISTS `jefe_ventas` (
  `id_jefe_ventas` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `fk_id_admin` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  `state_at` char(1) NOT NULL CHECK (`state_at` in ('Y','N')),
  PRIMARY KEY (`id_jefe_ventas`),
  KEY `fk_admin_id` (`fk_id_admin`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nota_credito`
--

DROP TABLE IF EXISTS `nota_credito`;
CREATE TABLE IF NOT EXISTS `nota_credito` (
  `id_nota_credito` int(11) NOT NULL AUTO_INCREMENT,
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
  `UPDATEDAT` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id_nota_credito`),
  KEY `fk_id_vendedor` (`fk_id_vendedor`),
  KEY `fk_id_cliente` (`fk_id_cliente`),
  KEY `fk_id_boleta` (`fk_id_boleta`),
  KEY `fk_id_factura` (`fk_id_factura`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

DROP TABLE IF EXISTS `producto`;
CREATE TABLE IF NOT EXISTS `producto` (
  `id_producto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `valor_unitario` int(11) NOT NULL,
  `fk_rut_prov` varchar(10) DEFAULT NULL,
  `fecha_elaboracion` date NOT NULL,
  `fecha_caducidad` date NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `fk_rut_prov` (`fk_rut_prov`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
CREATE TABLE IF NOT EXISTS `proveedor` (
  `rut_prov` varchar(10) NOT NULL,
  `nombre` varchar(55) NOT NULL,
  `direccion_prov` varchar(55) NOT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`rut_prov`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_cliente`
--

DROP TABLE IF EXISTS `telefono_cliente`;
CREATE TABLE IF NOT EXISTS `telefono_cliente` (
  `id_telefono_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `telefono` varchar(20) NOT NULL,
  `fk_rut_cliente` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_telefono_cliente`),
  KEY `fk_rut_cliente` (`fk_rut_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_jefe_ventas`
--

DROP TABLE IF EXISTS `telefono_jefe_ventas`;
CREATE TABLE IF NOT EXISTS `telefono_jefe_ventas` (
  `id_telefono` int(11) NOT NULL AUTO_INCREMENT,
  `telefono` varchar(20) NOT NULL,
  `fk_id_jefe_ventas` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_telefono`),
  KEY `fk_id_jefe_ventas` (`fk_id_jefe_ventas`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_proveedor`
--

DROP TABLE IF EXISTS `telefono_proveedor`;
CREATE TABLE IF NOT EXISTS `telefono_proveedor` (
  `id_telefono` int(11) NOT NULL AUTO_INCREMENT,
  `telefono` varchar(20) NOT NULL,
  `fk_rut_prov` varchar(10) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_telefono`),
  KEY `fk_rut_prov` (`fk_rut_prov`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `telefono_vendedor`
--

DROP TABLE IF EXISTS `telefono_vendedor`;
CREATE TABLE IF NOT EXISTS `telefono_vendedor` (
  `id_telefono` int(11) NOT NULL AUTO_INCREMENT,
  `telefono` varchar(20) NOT NULL,
  `fk_id_vendedor` int(11) DEFAULT NULL,
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_telefono`),
  KEY `fk_id_vendedor` (`fk_id_vendedor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

DROP TABLE IF EXISTS `vendedor`;
CREATE TABLE IF NOT EXISTS `vendedor` (
  `id_vendedor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `fk_id_admin` int(11) DEFAULT NULL,
  `password` varchar(50) NOT NULL,
  `state_at` char(1) NOT NULL CHECK (`state_at` in ('Y','N')),
  `CREATEDAT` timestamp NOT NULL DEFAULT current_timestamp(),
  `UPDATEDAT` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_vendedor`),
  KEY `fk_id_admin` (`fk_id_admin`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
