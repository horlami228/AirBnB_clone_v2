-- This script prepares a MySQL server for our project

-- create a database if not exists

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a new user if not exists

CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";

-- grant the user hbnb_test all privileges to the db hbnb_test_db

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO "hbnb_test"@"localhost";
FLUSH PRIVILEGES;

-- grant the user hbnb_test SELECT privilege on db performance_schema

GRANT SELECT ON performance_schema.* TO "hbnb_test"@"localhost";
FLUSH PRIVILEGES;
