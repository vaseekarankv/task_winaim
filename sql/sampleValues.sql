INSERT INTO departments (department_name) VALUES
    ('Engineering'),
    ('Marketing'),
    ('Finance');



INSERT INTO employees (first_name, last_name, department_id, hire_date) VALUES
    ('John', 'Doe', 1, '2023-06-15'),
    ('Vikram', 'V', 2, '2022-12-01'),
    ('markiv', 'vikram', 1, '2024-03-20'),
    ('micheal', 'jackson', 3, '2023-09-10'),
    ('eren', 'Jaegar', 1, '2024-01-05');



INSERT INTO salaries (employee_id, salary, from_date, to_date) VALUES
    (1, 60000, '2023-06-15', NULL),
    (2, 55000, '2022-12-01', NULL),
    (3, 70000, '2024-03-20', NULL),
    (4, 60000, '2023-09-10', NULL),
    (5, 75000, '2024-01-05', NULL);
