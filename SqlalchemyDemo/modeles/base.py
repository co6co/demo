
# -*- coding: utf-8 -*-
# modueles/base.py
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm  import declarative_base

from main import session
Model=declarative_base()

#Model.query=session.query_property()

class TimeStampedModel(Model):
    __abstract__=True
    
    create_time=Column(DateTime,default=datetime.utcnow())
    update_time=Column(DateTime,default=datetime.utcnow())

