/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.10-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: chamados
-- ------------------------------------------------------
-- Server version	10.11.10-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `artigos`
--

DROP TABLE IF EXISTS `artigos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `artigos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `descricao` text NOT NULL,
  `data_publicacao` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artigos`
--

LOCK TABLES `artigos` WRITE;
/*!40000 ALTER TABLE `artigos` DISABLE KEYS */;
INSERT INTO `artigos` VALUES
(1,'Artigo de teste','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras commodo eget lacus nec eleifend. Proin eu luctus nisl. Maecenas ac turpis accumsan, venenatis magna vestibulum, vestibulum nibh. Praesent eu commodo sem, et accumsan eros. Integer euismod felis vitae tempor ultrices. Ut convallis ut mi at varius. Vivamus purus mi, pulvinar eu diam sed, lobortis scelerisque tellus. Mauris dolor tellus, facilisis sed interdum id, laoreet vel nisi. Duis a eleifend turpis. Sed eget pulvinar ligula. Donec felis massa, volutpat at efficitur in, posuere sed erat. Duis sit amet sollicitudin urna. Aliquam erat volutpat. Sed et nibh vitae justo malesuada malesuada. Suspendisse potenti. Vestibulum accumsan nec sem non placerat.','2024-12-02'),
(2,'Titulo','descrição de um artigo, deixa minha fonte de máquina de escrever em paz!','2024-12-02'),
(3,'Teste','Phasellus ullamcorper massa eget est mattis, ac sodales est auctor. Donec lobortis ex in tincidunt molestie. Mauris egestas ex ut orci feugiat, quis ornare nibh tincidunt. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse iaculis nulla massa, rutrum porta quam tempor et. Vestibulum hendrerit diam vitae diam tempus facilisis. Phasellus varius, nunc non lobortis consequat, ipsum dolor maximus velit, vel efficitur augue felis ac arcu. Vivamus at tortor eget neque eleifend suscipit in ut enim. Maecenas non tortor ut risus aliquam bibendum sed eget libero. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum aliquam tristique pulvinar. Etiam sed neque et neque lacinia consequat. Etiam placerat nec augue sit amet interdum. Sed vitae euismod risus. ','2024-12-08');
/*!40000 ALTER TABLE `artigos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chamado`
--

DROP TABLE IF EXISTS `chamado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chamado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` varchar(255) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `setor` varchar(100) NOT NULL,
  `tipo_de_problema` varchar(100) NOT NULL,
  `especificacao_problema` varchar(255) DEFAULT NULL,
  `titulo` varchar(255) NOT NULL,
  `descricao` text NOT NULL,
  `data` varchar(25) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `prioridade` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chamado_ibfk_1` (`usuario_id`),
  CONSTRAINT `chamado_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chamado`
--

LOCK TABLES `chamado` WRITE;
/*!40000 ALTER TABLE `chamado` DISABLE KEYS */;
INSERT INTO `chamado` VALUES
(36,'#DES0001',1,'Desenvolvimento','Software','Erro de software','DES20241204 - SOLICITAÇÃO DE SENHA','Não consigo logar no Nexus, minha senha está expirada.','2024-12-05 12:54:45','Aberto','A definir'),
(37,'#PRO0001',2,'Projetos','Hardware','Problema físico','PRO20241205 - MOUSE PAROU DE FUNCIONAR','Meu mouse não está funcionando, solicito a troca do mesmo.','2024-12-05 12:56:04','Fechado','Baixa'),
(39,'#DES0002',1,'Desenvolvimento','Software','Erro de software','TESTE','test\n','2024-12-05 13:08:36','Aberto','A definir'),
(40,'#DES0003',1,'Desenvolvimento','Software','Erro de software','TSETE','TSETE2','2024-12-05 13:09:10','Aberto','A definir'),
(41,'#DES0004',1,'Desenvolvimento','Hardware','Problema físico','TSETE','TESTE3','2024-12-05 13:09:24','Aberto','A definir'),
(42,'#DES0005',1,'Desenvolvimento','Hardware','Configuração de dispositivos','TSET$','TESTE4','2024-12-05 13:09:43','Aberto','A definir'),
(43,'#DES0006',1,'Desenvolvimento','Hardware','Configuração de dispositivos','Resumo do Problema','Descrição do problema.','2024-12-06 10:25:34','Aberto','A definir'),
(44,'#DES0007',1,'Desenvolvimento','Software','Erro de software','Resumo de Probmea 2 ','Descrição do Problema 2 ','2024-12-06 10:28:15','Aberto','A definir'),
(45,'#DES0008',1,'Desenvolvimento','Hardware','Problema físico','aaaaaaaaa','aaaaaaaaaaaaaaaaaaaaaaaaa','2024-12-06 10:34:21','Aberto','A definir'),
(46,'#DES0009',1,'Desenvolvimento','Hardware','Problema físico','llllllllllllllll','llllllllllllllllllllllllllllllll','2024-12-06 11:17:30','Aberto','A definir'),
(47,'#DES0010',1,'Desenvolvimento','Hardware','Problema físico','llllllllllllllll','llllllllllllllllllllllllllllllll','2024-12-06 11:18:18','Espera','A definir'),
(48,'#DES0011',1,'Desenvolvimento','Hardware','Problema físico','aaaaaaa','aaaaaaaaaaaaaaaaa','2024-12-06 11:26:34','Em Andamento','A definir'),
(49,'#DES0012',1,'Desenvolvimento','Hardware','Problema físico','aaaaaaa','aaaaaaaaaaaaaaaaa','2024-12-06 11:29:28','Fechado','A definir'),
(52,'#CGR0001',5,'CGR','Hardware','Configuração de dispositivos','Problema de mouse','Mouse parou de funcionar, solicito a troca.','2024-12-08 14:28:20','Fechado','Alta');
/*!40000 ALTER TABLE `chamado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colaboradores`
--

DROP TABLE IF EXISTS `colaboradores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `colaboradores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(255) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `cargo` varchar(255) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colaboradores`
--

LOCK TABLES `colaboradores` WRITE;
/*!40000 ALTER TABLE `colaboradores` DISABLE KEYS */;
INSERT INTO `colaboradores` VALUES
(1,'maria_zefiro','Maria Carolina Zefiro Couto','Auxiliar de TIC','senhaMaria'),
(2,'taina_rocha','Tainá Silva Rocha','HelpDesk','senhaTaina');
/*!40000 ALTER TABLE `colaboradores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colaboradores_chamados`
--

DROP TABLE IF EXISTS `colaboradores_chamados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `colaboradores_chamados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `colaborador_id` int(11) NOT NULL,
  `chamado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `colaborador_id` (`colaborador_id`),
  KEY `chamado_id` (`chamado_id`),
  CONSTRAINT `colaboradores_chamados_ibfk_1` FOREIGN KEY (`colaborador_id`) REFERENCES `colaboradores` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `colaboradores_chamados_ibfk_2` FOREIGN KEY (`chamado_id`) REFERENCES `chamado` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colaboradores_chamados`
--

LOCK TABLES `colaboradores_chamados` WRITE;
/*!40000 ALTER TABLE `colaboradores_chamados` DISABLE KEYS */;
INSERT INTO `colaboradores_chamados` VALUES
(24,1,37),
(25,1,52),
(26,2,47);
/*!40000 ALTER TABLE `colaboradores_chamados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setores`
--

DROP TABLE IF EXISTS `setores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `setores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setores`
--

LOCK TABLES `setores` WRITE;
/*!40000 ALTER TABLE `setores` DISABLE KEYS */;
INSERT INTO `setores` VALUES
(1,'Administração'),
(2,'CGR'),
(3,'Call Center'),
(4,'Comunicação'),
(5,'Desenvolvimento'),
(6,'Diretoria'),
(7,'Engenharia'),
(8,'Expansão'),
(9,'Estoque'),
(10,'Frota'),
(11,'Jurídico'),
(12,'Logística'),
(13,'Loja'),
(14,'Operacional'),
(15,'Patrimônio'),
(16,'Projetos'),
(17,'Recursos Humanos'),
(18,'TIC');
/*!40000 ALTER TABLE `setores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(255) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `cargo` varchar(255) DEFAULT NULL,
  `setor` int(11) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `setor` (`setor`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`setor`) REFERENCES `setores` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES
(1,'jdoe','John Doe','Analista de Sistemas',5,'senha123'),
(2,'asmith','Alice Smith','Gerente de Projetos',16,'senha456'),
(5,'fulana_tal','Fula de Tal','Analista de Projetos',2,'senha789');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-08 15:38:27
