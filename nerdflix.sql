CREATE DATABASE nerdflix;

USE nerdflix;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nameUser VARCHAR(50),
    emailUser VARCHAR(50),
    ageUser INT,
    typeUser VARCHAR(20),
    planUser VARCHAR(20)
);

CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nameMovie VARCHAR(50),
    ageGroup INT,
    category VARCHAR(20),
    planMovie VARCHAR(20)
);

INSERT INTO user (nameUser, emailUser, ageUser, typeUser, planUser) VALUES ('{name}','{email}','{age}','{usertype}','{plan}')

INSERT INTO user (nameMovie, ageGroup, category, planMovie) VALUES ('{name}','{age}','{category}','{plan}')


UPDATE user
SET nameUser = '{name}'
WHERE id = '{id}'
