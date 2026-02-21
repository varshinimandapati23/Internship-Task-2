-- 1. Total number of smartphones
SELECT COUNT(*) AS total_models
FROM smartphones;

-- 2. Average smartphone price
SELECT AVG(price) AS average_price
FROM smartphones;

-- 3. Minimum and Maximum price
SELECT MIN(price) AS min_price,
       MAX(price) AS max_price
FROM smartphones;

-- 4. Average price per brand
SELECT brand_name,
       AVG(price) AS avg_price
FROM smartphones
GROUP BY brand_name
ORDER BY avg_price DESC;

-- 5. Top 5 most expensive smartphones
SELECT model,
       price
FROM smartphones
ORDER BY price DESC
LIMIT 5;

-- 6. Average RAM per brand
SELECT brand_name,
       AVG(ram) AS avg_ram
FROM smartphones
GROUP BY brand_name
ORDER BY avg_ram DESC;