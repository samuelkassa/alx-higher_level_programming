-- A script that converts hbtn_0c_0 database into UTF8 in your mysql server
USE hbtn_0c_0
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
