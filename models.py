from enum import unique
from operator import index
from sqlalchemy import  Column, Integer, String, ForeignKey,true
from database import Base
from sqlalchemy.orm import relationship


class xpay_user(Base):
   
    __tablename__ = "user_register"
    id           = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    username     = Column(String(255), index=True, nullable=False)
    email        = Column(String(100), index=True, nullable=False,unique=True)
    mobile_no    = Column(String(100), index=True, nullable=False,unique=True)
    password     =Column(String(255),index=True, nullable=False, unique=True)

class xpay_profile(Base):    

    __tablename__ = "user_profile"
    id           = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    first_name     = Column(String(255),index=True, nullable=False)
    last_name     = Column(String(255),index=True, nullable=False)
    city           = Column(String(255),index=True,nullable=False)
    place_of_birth = Column(String(255), index=True,nullable=False)
    image     = Column(String(255),index=True, nullable=False)
    user_id        = Column(Integer,ForeignKey('user_register.id'))    


   


