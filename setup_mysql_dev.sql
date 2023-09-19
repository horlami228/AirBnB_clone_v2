-- This script prepares a MySQL server for our project

-- create a database if not exists

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a new user if not exists

CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "Hbnb_dev_pwd#mega228";

-- grant the user hbnb_dev all privileges to the db hbnb_dev_db

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";

-- grant the user hbnb_dev SELECT privilege on db performance_schema

GRANT SELECT ON performance_schema.* TO "hbnb_dev"@"localhost";
