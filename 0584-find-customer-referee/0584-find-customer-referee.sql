# Write your MySQL query statement below
# SELECT c1.name
# FROM Customer c1
# LEFT JOIN Customer c2 ON c1.id = c2.id
# WHERE c1.referee_id != 2 or c1.referee_id IS NULL

SELECT name 
FROM Customer
WHERE referee_id != 2 or referee_id IS NULL