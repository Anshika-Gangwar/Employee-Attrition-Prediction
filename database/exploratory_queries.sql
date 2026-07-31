-- Count the total number of employees by attrition status
SELECT Attrition,
       COUNT(*) AS total_employees
FROM employee_attrition
GROUP BY Attrition;


-- Calculate the overall employee attrition rate (%)
SELECT
ROUND(
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) * 100.0 /
COUNT(*), 2) AS attrition_rate
FROM employee_attrition;


-- Find the average age of employees
SELECT
ROUND(AVG(Age),2) AS average_age
FROM employee_attrition;


-- Find the youngest and oldest employees
SELECT
MIN(Age) AS youngest,
MAX(Age) AS oldest
FROM employee_attrition;


-- Count the number of employees in each department
SELECT
Department,
COUNT(*) AS total
FROM employee_attrition
GROUP BY Department
ORDER BY total DESC;


-- Calculate the average monthly income by department
SELECT
Department,
ROUND(AVG(MonthlyIncome),2) AS average_salary
FROM employee_attrition
GROUP BY Department
ORDER BY average_salary DESC;


-- Display the top 10 highest-paid employees
SELECT
EmployeeNumber,
JobRole,
MonthlyIncome
FROM employee_attrition
ORDER BY MonthlyIncome DESC
LIMIT 10;


-- Count employees based on overtime status
SELECT
OverTime,
COUNT(*) AS total
FROM employee_attrition
GROUP BY OverTime;


-- Analyze attrition based on overtime status
SELECT
OverTime,
Attrition,
COUNT(*) AS total
FROM employee_attrition
GROUP BY OverTime, Attrition;


-- Analyze attrition across different departments
SELECT
Department,
Attrition,
COUNT(*) AS total
FROM employee_attrition
GROUP BY Department, Attrition
ORDER BY Department;


-- Find the average monthly income of employees who left the company
SELECT
ROUND(AVG(MonthlyIncome),2) AS avg_salary
FROM employee_attrition
WHERE Attrition='Yes';


-- Calculate the average years employees have worked at the company
SELECT
ROUND(AVG(YearsAtCompany),2) AS average_years
FROM employee_attrition;


-- Compare average years at the company by attrition status
SELECT
Attrition,
ROUND(AVG(YearsAtCompany),2) AS avg_years
FROM employee_attrition
GROUP BY Attrition;


-- Identify job roles with the highest number of employees who left
SELECT
JobRole,
COUNT(*) AS total_left
FROM employee_attrition
WHERE Attrition='Yes'
GROUP BY JobRole
ORDER BY total_left DESC;


-- Calculate the average job satisfaction score
SELECT
ROUND(AVG(JobSatisfaction),2) AS avg_job_satisfaction
FROM employee_attrition;


-- Analyze employee attrition by gender
SELECT
Gender,
Attrition,
COUNT(*) AS total
FROM employee_attrition
GROUP BY Gender, Attrition;


-- Count employees by marital status
SELECT
MaritalStatus,
COUNT(*) AS total
FROM employee_attrition
GROUP BY MaritalStatus;


-- Calculate the average distance employees travel from home to work
SELECT
ROUND(AVG(DistanceFromHome),2) AS avg_distance
FROM employee_attrition;


-- Display the top 5 highest-paid employees
SELECT
EmployeeNumber,
JobRole,
MonthlyIncome
FROM employee_attrition
ORDER BY MonthlyIncome DESC
LIMIT 5;


-- Count employees based on work-life balance rating
SELECT
WorkLifeBalance,
COUNT(*) AS employees
FROM employee_attrition
GROUP BY WorkLifeBalance;