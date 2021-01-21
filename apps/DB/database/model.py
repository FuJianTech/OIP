# !/bin/env python
# -*- coding=utf-8 -*-

# init database
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(String(32))
    num = Column(Integer)

class Todolist(Base):
    __tablename__ = 'todolist'
    id = Column(Integer, primary_key=True)
    date = Column(String(64))
    mission = Column(String(64))
    level = Column(String(64))
    pic_path = Column(String(1024))

init_data_url = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'init_data.db')
engine = create_engine(init_data_url)
Base.metadata.create_all(engine)
