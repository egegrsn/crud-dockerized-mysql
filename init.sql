CREATE DATABASE school;
use school;

CREATE TABLE students (
	id INT(5) NOT NULL,
  	name VARCHAR(20) NOT NULL,
  	department VARCHAR(20) NOT NULL
);

INSERT INTO students
  (id,name, department)
VALUES
  ('1','Ege Girsen', 'CTIS'),
  ('2','Umay Durur', 'EE'),
  ('3','Jankat Kozok', 'MECH'),
  ('4','Ali Turan', 'MATH'),
  ('5','Eda Zorlu', 'ARCH');

ALTER TABLE students
ADD PRIMARY KEY (id),
MODIFY id int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;