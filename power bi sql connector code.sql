CREATE USER 'powerbi_user'@'localhost' IDENTIFIED BY 'PowerBI@123';
GRANT ALL PRIVILEGES ON student_health.* TO 'powerbi_user'@'localhost';
FLUSH PRIVILEGES;
student_mental_health