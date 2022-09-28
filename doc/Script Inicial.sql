-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_revision
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_revision
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_revision` DEFAULT CHARACTER SET utf8 ;
USE `db_revision` ;

-- -----------------------------------------------------
-- Table `db_revision`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_revision`.`usuarios` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(250) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_revision`.`pensamientos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_revision`.`pensamientos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `texto` VARCHAR(200) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `usuario_creador` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pensamientos_usuarios_idx` (`usuario_creador` ASC),
  CONSTRAINT `fk_pensamientos_usuarios`
    FOREIGN KEY (`usuario_creador`)
    REFERENCES `db_revision`.`usuarios` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_revision`.`megusta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_revision`.`megusta` (
  `usuario_id` INT UNSIGNED NOT NULL,
  `pensamiento_id` INT UNSIGNED NOT NULL,
  INDEX `fk_usuarios_has_pensamientos_pensamientos1_idx` (`pensamiento_id` ASC),
  INDEX `fk_usuarios_has_pensamientos_usuarios1_idx` (`usuario_id` ASC),
  CONSTRAINT `fk_usuarios_has_pensamientos_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_revision`.`usuarios` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_usuarios_has_pensamientos_pensamientos1`
    FOREIGN KEY (`pensamiento_id`)
    REFERENCES `db_revision`.`pensamientos` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
