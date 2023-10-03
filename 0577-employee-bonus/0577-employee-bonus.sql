# Write your MySQL query statement below
SELECT e.name as name, b.bonus as bonus
FROM Employee e 
LEFT JOIN Bonus b on e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL