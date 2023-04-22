#!/usr/bin/python3

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXIXTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hnbn'@'localhost';
