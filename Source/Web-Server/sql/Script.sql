CREATE SCHEMA IF NOT EXISTS `Raspagem` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `Raspagem`.`Tipo_Vaga` (
            ID Int not null Auto_increment,
            Descricao Varchar(50),
            Primary Key (ID)
             ) Engine = InnoDB;

CREATE TABLE IF NOT EXISTS `Raspagem`.`Vagas` (
            ID INT NOT NULL AUTO_INCREMENT,
            Vaga VARCHAR(200) NOT NULL,
            Empresa VARCHAR(200) NOT NULL,
            Local VARCHAR(200) NOT NULL,
            Data DATE NOT NULL,
            Descricao MEDIUMTEXT NOT NULL,
            Tipo_Vaga INT NOT NULL, 
            Primary Key (ID),
            FOREIGN KEY (Tipo_Vaga) REFERENCES Tipo_Vaga(ID)
            ) ENGINE = InnoDB;

