INSERT INTO Teachers (first_name, last_name, email, hire_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2015-08-15'),
('Jane', 'Smith', 'jane.smith@example.com', '2017-09-01'),
('Alice', 'Johnson', 'alice.johnson@example.com', '2020-01-10');

INSERT INTO Classes (class_name, teacher_id) VALUES
('Math 101', 1),
('History 201', 2),
('Science 301', 3);

INSERT INTO Students (first_name, last_name, date_of_birth, email, enrollment_date, class_id) VALUES
('Emily', 'Brown', '2005-04-23', 'emily.brown@example.com', '2021-09-01', 1),
('Michael', 'Davis', '2004-06-12', 'michael.davis@example.com', '2021-09-01', 2),
('Jessica', 'Miller', '2005-11-30', 'jessica.miller@example.com', '2021-09-01', 3),
('David', 'Wilson', '2004-01-20', 'david.wilson@example.com', '2021-09-01', 1);

INSERT INTO Subjects (subject_name) VALUES
('Algebra'),
('Geometry'),
('World History'),
('Biology'),
('Chemistry');

INSERT INTO Enrollments (student_id, class_id, enrollment_date) VALUES
(1, 1, '2021-09-01'),
(2, 2, '2021-09-01'),
(3, 3, '2021-09-01'),
(4, 1, '2021-09-01');

INSERT INTO Class_Subjects (class_id, subject_id) VALUES
(1, 1), -- Math 101 offers Algebra
(1, 2), -- Math 101 offers Geometry
(2, 3), -- History 201 offers World History
(3, 4), -- Science 301 offers Biology
(3, 5); -- Science 301 offers Chemistry

