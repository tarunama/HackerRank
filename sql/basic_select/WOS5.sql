/* Problem Description: 
   https://www.hackerrank.com/challenges/weather-observation-station-5
*/

SELECT city
      ,LENGTH(city) as city_length
FROM station
ORDER BY city_length, city
LIMIT 1
;

SELECT city
      ,LENGTH(city) as city_length
FROM station
ORDER BY city_length DESC, city
LIMIT 1
;
