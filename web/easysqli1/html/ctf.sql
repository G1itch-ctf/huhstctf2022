ALTER USER 'root'@'localhost' IDENTIFIED BY 'pcs1.1.2.3' PASSWORD EXPIRE NEVER;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'pcs1.1.2.3';

drop database if exists `orderbysql`;
create database orderbysql;
use orderbysql;
create table users
                (
                id int(3) NOT NULL AUTO_INCREMENT,
                username varchar(20) NOT NULL,
                password varchar(20) NOT NULL,
                PRIMARY KEY (id)
                );

CREATE TABLE emails
                (
                id int(3) NOT NULL AUTO_INCREMENT,
                email_id varchar(30) NOT NULL,
                PRIMARY KEY (id)
                );
CREATE TABLE uagents
                (
                id int(3) NOT NULL AUTO_INCREMENT,
                uagent varchar(256) NOT NULL,
                ip_address varchar(35) NOT NULL,
                username varchar(20) NOT NULL,
                PRIMARY KEY (id)
                );
CREATE TABLE referers
                (
                id int(3) NOT NULL AUTO_INCREMENT,
                referer varchar(256) NOT NULL,
                ip_address varchar(35) NOT NULL,
                PRIMARY KEY (id)
                );
CREATE TABLE flag
               (
                flag varchar(255)
               );

INSERT INTO orderbysql.users (id, username, password) VALUES ('1', 'Dumb', 'Dumb'), ('2', 'Angelina', 'I-kill-you'), ('3', 'Dummy', 'p@ssword'), ('4', 'secure', 'crappy'), ('5', 'stupid', 'stupidity'), ('6', 'superman', 'genious'), ('7', 'batman', 'mob!le'), ('8', 'admin', 'admin');

INSERT INTO `orderbysql`.`emails` (id, email_id) VALUES ('1', 'Dumb@dhakkan.com'), ('2', 'Angel@iloveu.com'), ('3', 'Dummy@dhakkan.local'), ('4', 'secure@dhakkan.local'), ('5', 'stupid@dhakkan.local'), ('6', 'superman@dhakkan.local'), ('7', 'batman@dhakkan.local'), ('8', 'admin@dhakkan.com');

insert into `orderbysql`.`flag` (flag) value ("flagtest");

