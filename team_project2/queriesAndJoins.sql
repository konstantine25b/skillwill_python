SELECT s.student_id, s.first_name, s.last_name, c.class_name
FROM Students s
JOIN Classes c ON s.class_id = c.class_id;

SELECT t.teacher_id, t.first_name, t.last_name, c.class_name
FROM Teachers t
JOIN Classes c ON t.teacher_id = c.teacher_id;

SELECT s.student_id, s.first_name, s.last_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.class_id = 1; 

SELECT s.student_id, s.first_name, s.last_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.class_id = 1; -- Example class_id

SELECT sub.subject_name
FROM Subjects sub
JOIN Class_Subjects cs ON sub.subject_id = cs.subject_id
WHERE cs.class_id = 1; -- Example class_id

SELECT c.class_id, c.class_name
FROM Classes c
WHERE c.teacher_id = 1; -- Example teacher_id

SELECT s.first_name, s.last_name, e.enrollment_date
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id;

SELECT c.class_name, COUNT(s.student_id) AS student_count
FROM Classes c
JOIN Students s ON c.class_id = s.class_id
GROUP BY c.class_name;


SELECT first_name, last_name
FROM Teachers
WHERE hire_date > '2020-01-01';

SELECT c.class_name
FROM Classes c
JOIN Class_Subjects cs ON c.class_id = cs.class_id
WHERE cs.subject_id = 1; -- Example subject_id

SELECT first_name, last_name
FROM Students
WHERE YEAR(enrollment_date) = YEAR(CURDATE());

SELECT c.class_name, COUNT(s.student_id) AS student_count
FROM Classes c
JOIN Students s ON c.class_id = s.class_id
GROUP BY c.class_name;

SELECT first_name, last_name
FROM Students
WHERE YEAR(enrollment_date) = YEAR(CURDATE());

