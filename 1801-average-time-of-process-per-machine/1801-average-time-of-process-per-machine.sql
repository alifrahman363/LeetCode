# Write your MySQL query statement below
SELECT start.machine_id, round( avg(end.timestamp - start.timestamp) ,3) as processing_time
FROM Activity start, Activity end
WHERE start.machine_id = end.machine_id 
AND start.process_id = end.process_id
AND start.activity_type = 'start'
AND end.activity_type = 'end'
GROUP BY start.machine_id
