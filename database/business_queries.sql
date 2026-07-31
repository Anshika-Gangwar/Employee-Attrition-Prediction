-- Attrition Count
SELECT Attrition,
       COUNT(*) AS total
FROM employee_attrition
GROUP BY Attrition;

-- Employees by Department
SELECT Department,
       COUNT(*) AS employees
FROM employee_attrition
GROUP BY Department;

-- Employees by Job Role
SELECT JobRole,
       COUNT(*) AS employees
FROM employee_attrition
GROUP BY JobRole;

-- Employees by Overtime
SELECT OverTime,
       COUNT(*) AS employees
FROM employee_attrition
GROUP BY OverTime;