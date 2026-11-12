-- Apagar o Database, caso exista
DROP DATABASE IF EXISTS estodolist;

-- Criar novo database
CREATE DATABASE estodolist;

-- Colocar o database em uso
USE estodolist;

-- Criar tabela
CREATE TABLE tarefa(
    idTarefa INT PRIMARY KEY AUTO_INCREMENT,
    nomeTarefa VARCHAR(30) NOT NULL,
    descricao VARCHAR(100),
    categoria VARCHAR(30) NOT NULL,
    dataPrazo DATE NOT NULL,
    prioridade ENUM('ALTA', 'MEDIA', 'BAIXA') NOT NULL,
    status ENUM('Pendente', 'Concluída', 'Não realizada') DEFAULT 'Pendente'
);

CREATE TABLE 