# -*- coding: utf-8 -*-
# modueles/po.py

from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import Relationship
from modeles.base import Model, TimeStampedModel


class User(TimeStampedModel):
    """
    角色对象
    属性的注解也是在下面，很是不习惯
    """
    __tablename__="users"
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(String(64),nullable=False)
    email = Column(String(320),nullable=False,unique=True)
    
    
    preference=Relationship("Preference",back_populates="user",uselist=False,passive_deletes=True)
    '''偏好 1对1''' 
    
    addresses=Relationship("Address",back_populates="user",uselist=True,passive_deletes=True)
    '''地址 1对多'''
    
    roles=Relationship("Role",secondary="user_roles",back_populates="users",passive_deletes=True)
    '''角色 多对多'''
    
    def __repr__(self):
        return f"{self.__class__.__name__},name:{self.user_name}"
    
class Preference(TimeStampedModel):
    """
        一对一
    """
    __tablename__="preference"
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    language = Column(String(64),nullable=False)
    currency = Column(String(3),nullable=False )
    
    user_id=Column(Integer,ForeignKey(f"{User.__tablename__}.{User.id.key}",ondelete="CASCADE"),nullable=False,index=True,unique=True)
    user=Relationship("User",back_populates="preference") # 是否还少个 uselist=False
    
class Address(TimeStampedModel):
    """
        一对多
    """
    __tablename__="addresses"
    id = Column(Integer,primary_key=True,autoincrement=True)
    road_name =Column(String(128),nullable=False )
    pastcode =Column(String(128),nullable=False )
    city =Column(String(128),nullable=False )
    
    user_id=Column(Integer,ForeignKey(f"{User.__tablename__}.{User.id.key}",ondelete="CASCADE"),nullable=False,index=True) 
    user=Relationship("User",back_populates="addresses")
    
    def __repr__(self):
        return f"{self.__class__.__name__}->city:{self.city}"

class Role(Model):
    """
        角色
    """
    __tablename__="roles"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name =Column(String(128),nullable=False )
    slug=Column(String(128),nullable=False ,unique=True)
    
    users=Relationship("User",back_populates="roles",secondary="user_roles", passive_deletes=True)
    '''多对多'''
    
    def __repr__(self):
        return f"{self.__class__.__name__},name:{self.name}"
    
class UserRole(TimeStampedModel):
    __tablename__="user_roles"
    
    user_id=Column(Integer,ForeignKey(f"{User.__tablename__}.{User.id.key}",ondelete="CASCADE"),primary_key=True)
    role_id=Column(Integer,ForeignKey(f"{Role.__tablename__}.{Role.id.key}",ondelete="CASCADE"),primary_key=True)