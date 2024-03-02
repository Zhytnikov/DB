from sqlalchemy import func
from models import Student, Grade, Subject, Teacher, Group

def select_1(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()

def select_2(session, subject_name):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()

def select_3(session, subject_name):
    return session.query(Group.group_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Subject).join(Group).filter(Subject.name == subject_name) \
        .group_by(Group.group_name).all()

def select_4(session):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()

def select_5(session, teacher_name):
    return session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()

def select_6(session, group_name):
    return session.query(Student.fullname).join(Group).filter(Group.group_name == group_name).all()

def select_7(session, group_name, subject_name):
    return session.query(Student.fullname, Grade.grade).join(Group).join(Grade).join(Subject) \
        .filter(Group.group_name == group_name, Subject.name == subject_name).all()

def select_8(session, teacher_name):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Subject).join(Teacher).filter(Teacher.name == teacher_name) \
        .scalar()

def select_9(session, student_name):
    return session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name).all()

def select_10(session, student_name, teacher_name):
    return session.query(Subject.name).join(Grade).join(Student).join(Subject.teacher).filter(Student.fullname == student_name, Teacher.name == teacher_name).all()
