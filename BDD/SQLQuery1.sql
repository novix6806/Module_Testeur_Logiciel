CREATE DATABASE GesCom;
GO
USE GesCom;

CREATE TABLE Clients(
id_client INT          CONSTRAINT PK_Clients PRIMARY KEY,
nom VARCHAR(50)        NOT NULL,
prenom VARCHAR(40)     NULL,
date_naissance DATE    NULL,
ville VARCHAR(50)      NOT NULL,
portable NUMERIC(10)   NULL,
fixe NUMERIC(10)       NULL
);

CREATE TABLE Categories(
id_categorie INT       CONSTRAINT PK_Categories PRIMARY KEY,
libelle VARCHAR(50)    NOT NULL  CONSTRAINT UN_Categories_libelle UNIQUE,
id_cat_parent INT      NULL
);

CREATE TABLE Artcles(
id_article INT          CONSTRAINT PK_Articles PRIMARY KEY,
designation VARCHAR(50) NOT NULL   CONSTRAINT UN_Articles_designation UNIQUE,
prix_ht DECIMAL(8,2)    NOT NULL
);

CREATE TABLE Commandes(
id_commande INT        CONSTRAINT PK_Commandes PRIMARY KEY,
date_cmd DATETIME2     NOT NULL  CONSTRAINT CHK_Commandes_date_cmd CHECK (date_cmd <= GETDATE()),
statut CHAR(2)         NOT NULL  CONSTRAINT CHK_Commandes_statut CHECK (statut IN('AP','EP','PR','AC','LI','EL')),
id_client INT          NOT NULL
);

CREATE TABLE Details_Commande(
id_commande INT       NOT NULL,
numero_ligne INT      NOT NULL,
id_article INT        NOT NULL,
CONSTRAINT PK_Details_Commande PRIMARY KEY (id_commande, numero_ligne)
);