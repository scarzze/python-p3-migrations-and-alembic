from sqlalchemy import create_engine, desc
from sqlalchemy.orm import declarative_base
from sqlalchemy import (CheckConstraint, UniqueConstraint, Column, DateTime, Integer, String)
from datetime import datetime

engine = create_engine('sqlite:///migrations_test.db')
Base = declarative_base()

class Student(Base):
    __tablename__= 'students'
    __table_args__= (
        UniqueConstraint('email', 
            name= 'unique_email'),
        CheckConstraint('grade BETWEEN 1 AND 12', 
            name='grade_between_1_and_12')

    )
    id = Column (Integer(), primary_key= True)
    name = Column (String (), index= True)
    email= Column (String(55))
    grade = Column(Integer())
    birthday= Column(DateTime())
    enrolled_date = Column(DateTime(), default= datetime.now)

    def __repr__(self):
        return f"student {self.id}: " \
            +f"{self.name}, " \
            +f"Grade {self.grade}"
