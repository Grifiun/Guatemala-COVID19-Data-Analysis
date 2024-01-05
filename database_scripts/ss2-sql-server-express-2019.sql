USE master;
GO

-- Drop the database if it exists
IF EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N'ss2')
    DROP DATABASE ss2;
GO

-- Create the database
CREATE DATABASE ss2;
GO

-- Use the newly created database
USE ss2;
GO

-- Create the Country table
CREATE TABLE Country (
    code_country VARCHAR(10) NOT NULL PRIMARY KEY,
    name_country VARCHAR(45) NOT NULL
);
GO

-- Create the Department table
CREATE TABLE Department (
    code_department VARCHAR(10) NOT NULL PRIMARY KEY,
    name_department VARCHAR(45) NOT NULL,
    code_country VARCHAR(10) NOT NULL,
    FOREIGN KEY (code_country) REFERENCES Country (code_country) ON DELETE CASCADE
);
GO

-- Create the Municipality table
CREATE TABLE Municipality (
    code_municipality VARCHAR(10) NOT NULL PRIMARY KEY,
    population INT NOT NULL DEFAULT 0,
    municipality VARCHAR(45) NOT NULL,
    code_department VARCHAR(10) NOT NULL,
    FOREIGN KEY (code_department) REFERENCES Department (code_department) ON DELETE CASCADE
);
GO

-- Create the MunicipalityDeathsReported table
CREATE TABLE MunicipalityDeathsReported (
    code_municipality VARCHAR(10) NOT NULL,
    date_reported DATE NOT NULL,
    new_deaths INT NOT NULL DEFAULT 0,
    PRIMARY KEY (code_municipality, date_reported),
    FOREIGN KEY (code_municipality) REFERENCES Municipality (code_municipality) ON DELETE CASCADE
);
GO

-- Create the Cases table (renamed from Case to Cases)
CREATE TABLE Cases (
    code_country VARCHAR(10) NOT NULL,
    date_reported DATE NOT NULL,
    new_cases INT NOT NULL DEFAULT 0,
    cumulative_cases INT NOT NULL DEFAULT 0,
    new_deaths INT NOT NULL DEFAULT 0,
    cumulative_deaths INT NOT NULL DEFAULT 0,
    PRIMARY KEY (code_country, date_reported),
    FOREIGN KEY (code_country) REFERENCES Country (code_country) ON DELETE CASCADE
);
GO

-- Create the Log table
CREATE TABLE Log (
    id_log INT NOT NULL PRIMARY KEY IDENTITY,
    message VARCHAR(300) NOT NULL
);
GO
