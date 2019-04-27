# greenhouse
Automatic greenhouse with a Raspberry Pi and Makeblock Orion

# mysql database
mysqladmin -u root -p
CREATE DATABASE greenhouse;
USE greenhouse;
CREATE TABLE enviroment (ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE enviroment ADD temperate VARCHAR(2);
ALTER TABLE enviroment ADD humidity VARCHAR(2);
# controle
select * from enviroment;
-----------------------------------------------
| ts                  |temperature | humidity | 
-----------------------------------------------
| YYYY-MM-DD HH-MM-SS |xx          |xx        |
-----------------------------------------------

# waarden.php
bestand toont de waarden van database via internet
