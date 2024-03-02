from faker import Faker
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade, Base

fake = Faker()

engine = create_engine('postgresql://sasha:1234@localhost:5432/db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create groups
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

# Create teachers
teachers = [Teacher(fullname=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

# Create subjects with assigned teachers
subjects = [Subject(name=fake.word(), teacher=teachers[i % len(teachers)]) for i in range(5)]
session.add_all(subjects)
session.commit()

# Create students
students = [Student(fullname=fake.name()) for _ in range(30)]
session.add_all(students)
session.commit()

# Assign students to groups
for student in students:
    student.group = fake.random_element(groups)
session.commit()

# Generate grades for each student for each subject
for student in students:
    for subject in subjects:
        grade = fake.random_int(min=1, max=10)
        date = fake.date_time_between(start_date='-1y', end_date='now')
        session.add(Grade(student=student, subject=subject, grade=grade, date=date))
session.commit()
