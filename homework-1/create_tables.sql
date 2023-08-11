-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(101) NOT NULL,
	last_name varchar(101) NOT NULL,
	title varchar(256) NOT NULL,
	birth_date varchar(10)NOT NULL,
	notes text NOT NULL
);

SELECT * FROM employees;
SELECT * FROM customers;
SELECT * FROM orders;

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(101) NOT NULL,
	contact_name varchar(201) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date varchar(10) NOT NULL,
	ship_city varchar(101) NOT NULL
)

