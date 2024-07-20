CREATE DATABASE UniversityDB;
USE UniversityDB;
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
    DepartmentName VARCHAR(100) NOT NULL
);
CREATE TABLE Professors (
    ProfessorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    EnrollmentYear INT NOT NULL
);
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    CourseName VARCHAR(100) NOT NULL,
    DepartmentID INT,
    ProfessorID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
    FOREIGN KEY (ProfessorID) REFERENCES Professors(ProfessorID)
);
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
INSERT INTO Departments (DepartmentName) VALUES ('Computer Science'), ('Mathematics'), ('Physics');
INSERT INTO Professors (FirstName, LastName, DepartmentID) VALUES ('Alice', 'Smith', 1), ('Bob', 'Johnson', 2), ('Carol', 'Davis', 3);
INSERT INTO Students (FirstName, LastName, EnrollmentYear) VALUES ('John', 'Doe', 2022), ('Jane', 'Roe', 2023), ('Jim', 'Beam', 2024);
INSERT INTO Courses (CourseName, DepartmentID, ProfessorID) VALUES ('Introduction to Programming', 1, 1), ('Calculus I', 2, 2), ('Physics I', 3, 3);
INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate) VALUES (1, 1, '2023-09-01'), (2, 2, '2023-09-01'), (3, 3, '2023-09-01');
SELECT 
    Students.FirstName AS StudentFirstName, 
    Students.LastName AS StudentLastName, 
    Courses.CourseName 
FROM 
    Enrollments
INNER JOIN 
    Students ON Enrollments.StudentID = Students.StudentID
INNER JOIN 
    Courses ON Enrollments.CourseID = Courses.CourseID;
SELECT 
    Students.FirstName AS StudentFirstName, 
    Students.LastName AS StudentLastName, 
    Courses.CourseName 
FROM 
    Students
LEFT JOIN 
    Enrollments ON Students.StudentID = Enrollments.StudentID
LEFT JOIN 
    Courses ON Enrollments.CourseID = Courses.CourseID;
SELECT 
    Students.FirstName AS StudentFirstName, 
    Students.LastName AS StudentLastName, 
    Courses.CourseName 
FROM 
    Courses
RIGHT JOIN 
    Enrollments ON Courses.CourseID = Enrollments.CourseID
RIGHT JOIN 
    Students ON Enrollments.StudentID = Students.StudentID;