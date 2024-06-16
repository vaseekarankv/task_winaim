
/*Query to find all employees who have been hired in the last year:*/

SELECT *
FROM employees
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);


