-- CREATE TABLE customers (
--     customer_id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(100),
--     email VARCHAR(150),
--     age INT,
--     phone VARCHAR(15),
--     is_active BOOLEAN,
--     signup_date DATE,
--     created_at DATETIME,
--     total_spent DECIMAL(10,2)
-- );

-- DROP TABLE customers;

ALTER TABLE customers RENAME TO clients;

 