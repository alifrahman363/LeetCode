# Write your MySQL query statement below
SELECT C.name as Customers from Customers C 
LEFT JOIN Orders O on C.id = O.customerId
where O.customerId IS NULL 