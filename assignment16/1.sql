CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade_level INT
);

INSERT INTO students (first_name, last_name, age, grade_level)
VALUES
('John', 'Doe', 15, 10),
('Jane', 'Smith', 16, 11),
('Alice', 'Johnson', 14, 9),
('Bob', 'Brown', 17, 12),
('Charlie', 'Davis', 15, 10);

EXPLAIN ANALYZE SELECT * FROM students WHERE age = 15;

CREATE INDEX idx_age ON students(age);

EXPLAIN ANALYZE SELECT * FROM students WHERE age = 15;