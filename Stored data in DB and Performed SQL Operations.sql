create schema electricity;
use electricity;
select * from consumption;

USE electricity;
SHOW TABLES;
RENAME TABLE `consumption (1)` TO consumption;
SELECT * FROM consumption;
SELECT States, Regions
FROM consumption;
SELECT *
FROM consumption
ORDER BY Dates;



