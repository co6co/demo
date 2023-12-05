#--*-- encoding=utf-8 --*--
# ./main.py
import os
from sqlalchemy import create_engine,event ,Engine
from sqlalchemy.orm import scoped_session,sessionmaker
from co6co.utils import log



from sqlalchemy.ext.asyncio import AsyncSession 

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

engine=create_engine(f"sqlite:///{BASE_DIR}/db",echo=True)
engine=create_engine(f"mysql+aiomysql://root:mysql12345@127.0.0.1/wx_db", echo=True)

async_session_factory  = sessionmaker(engine, expire_on_commit=False,class_=AsyncSession)# AsyncSession,
session= async_session_factory()
session.query()
log.succ(type(session))
 
'''
session=scoped_session(
    sessionmaker(autoflush=False, autocommit=False,bind=engine)
)
'''
@event.listens_for(Engine,"connect")
def set_sqlite_parama(dbapi_connection,connection_recore):
    cursor=dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON") #默认情况下，是允许将外键字段设为 NULL 的 #不会触发外键约束引发错误。 
    cursor.close()