/*
Question 1: Total Orders Per Customer

Write a query to display the total number of orders placed by each customer, 
along with their name and the date they joined. Sort the results by the total number of orders in descending order.
*/
SELECT 
    c.customer_name, c.join_date, COUNT(o.order_date) as "Total Orders"
FROM
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id, c.join_date, c.customer_name
ORDER BY
    "Total Orders" DESC



/*
Question 2: Rank Customers by Spending

For each customer, calculate their total spending (sum of the total amounts from the `Orders` table) 
and rank them by total spending within their respective country. 
Use a **window function** to rank the customers.
*/

SELECT 
    c.customer_name, SUM(oi.price * oi.quantity) as Spending
FROM
    customers c
JOIN
    Orders o ON c.customer_id = o.customer_id
JOIN 
    OrderItems oi ON o.order_id = oi.order_id
GROUP BY
    customer_name
ORDER BY
    Spending DESC