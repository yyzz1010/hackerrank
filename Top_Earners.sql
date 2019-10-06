SELECT earnings, COUNT(*)
FROM (
SELECT (months * salary) AS earnings
FROM Employee) AS TABLE1
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1
