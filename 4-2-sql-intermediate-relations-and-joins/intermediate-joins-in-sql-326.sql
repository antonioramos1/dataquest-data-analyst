## 2. Joining Three Tables ##

SELECT t.track_id, t.name track_name, mt.name track_type, il.unit_price, il.quantity
FROM track t
JOIN invoice_line il ON il.track_id = t.track_id
JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE il.invoice_id = 4

## 3. Joining More Than Three Tables ##

SELECT
    il.track_id,
    t.name track_name,
    ar.name artist_name,
    mt.name track_type,
    il.unit_price,
    il.quantity
FROM invoice_line il
JOIN track t ON t.track_id = il.track_id
JOIN media_type mt ON mt.media_type_id = t.media_type_id
JOIN album al ON al.album_id = t.album_id
JOIN artist ar ON ar.artist_id = al.artist_id
WHERE il.invoice_id = 4;

## 4. Combining Multiple Joins with Subqueries ##

SELECT
    album,
    artist,
    COUNT(*) tracks_purchased
FROM invoice_line il
INNER JOIN (
            SELECT
                al.album_id album_id,
                al.title album,
                t.name track_name,
                ar.name artist,
                t.track_id
            FROM track t
            INNER JOIN album al ON al.album_id = t.album_id
            INNER JOIN artist ar ON ar.artist_id = al.artist_id
           ) ta
           ON ta.track_id = il.track_id
GROUP BY 1
ORDER BY tracks_purchased DESC
LIMIT 5;

## 5. Recursive Joins ##

SELECT
e.first_name ||' ' || e.last_name AS employee_name,
e.title employee_title,
e2.first_name ||' ' || e2.last_name AS supervisor_name,
e2.title supervisor_title
FROM employee e
LEFT JOIN employee e2 ON e.reports_to = e2.employee_id
ORDER BY employee_name


## 6. Pattern Matching Using Like ##

SELECT first_name, last_name, phone
FROM customer
WHERE first_name LIKE '%Belle%';

## 7. Generating Columns With The Case Statement ##

SELECT
    c.first_name || ' ' || c.last_name AS customer_name,
    COUNT(*) number_of_purchases,
    SUM(i.total) total_spent,
    CASE
        WHEN SUM(i.total) < 40 THEN 'small spender'
        WHEN SUM(i.total) > 100 THEN 'big spender'
        WHEN SUM(i.total) >= 40 AND SUM(i.total) <= 100 THEN 'regular'
        END
        AS customer_category
FROM invoice i
JOIN customer c ON i.customer_id = c.customer_id
GROUP BY customer_name
ORDER BY customer_name