-- This script prepares a MySQL server for our project

-- create a database if not exists

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a new user if not exists

CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";

-- grant the user hbnb_dev all privileges to the db hbnb_dev_db

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;

-- grant the user hbnb_dev SELECT privilege on db performance_schema

GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";
FLUSH PRIVILEGES;
