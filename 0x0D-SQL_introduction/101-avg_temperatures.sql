-- A script that displays the average tempratue in Fahrenheit
-- by city ordered by ascending temprature
SELECT city, AVG(value) AS avg_temp
FROM temprature
GROUP BY city 
ORDER BY avg_temp DESC;
