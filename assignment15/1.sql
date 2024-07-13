CREATE TABLE products (
    product VARCHAR(50),
    price DECIMAL(10, 2),
    quantity INT,
    color VARCHAR(50),
    area DECIMAL(10, 2)
);
INSERT INTO products (product, price, quantity, color, area) VALUES
('Phone', 700, 5, 'Blue', 12),
('Laptop', 1200, 3, 'Red', 15),
('Tablet', 300, 10, 'Blue', 9),
('Headphones', 100, 7, 'Black', 6),
('Charger', 20, 15, 'Blue', 2),
('Mouse', 25, 20, 'Blue', 2),
('Keyboard', 75, 8, 'Black', 3),
('Monitor', 200, 2, 'Black', 20);

SELECT * FROM products
WHERE price > 600;

SELECT * FROM products
WHERE quantity > 2 AND color = 'Blue';

SELECT *, (quantity * price) AS total_value FROM products;

SELECT * FROM products
WHERE area > 10;