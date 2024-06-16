/*Query to calculate the total salary expenditure for each department:*/

SELECT d.department_name, SUM(s.salary) AS total_salary_expenditure
FROM employees e
JOIN salaries s ON e.employee_id = s.employee_id
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
