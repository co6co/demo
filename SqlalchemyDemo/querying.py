# -*- coding: utf-8 -*-
# ./demo.py
from main import session
from sqlalchemy import desc
from sqlalchemy.orm import joinedload,subqueryload,contains_eager
from modeles.user import User,Role,Address
from co6co.utils import log


log.start_mark("基础查询")
all_user = session.query(User).all()
print(all_user) 
all_user = User.query.all()
print(all_user)

first_user = User.query.first()
first_user = User.query.filter(User.user_name=="aa").all()
gmail_users = User.query.filter(User.email.like("%@gmail.com")).all()

super_admins= (
    User.query
    .join(User.roles)
    .filter(Role.slug == "auper-admin")
    .all()
)
users_by_name =(
    User.query
    .order_by(desc( User.user_name))
    .order_by( User.email)
    .all()
)

first_three_user=User.query.limit(3).all()
skip_three_user=User.query.offset(3).all()
num_of_users=User.query.count()
log.end_mark("基础查询")
log.start_mark("高级查询")
## 高级查询
users = (
    User.query
        .all()
)
print(type(users))
for item in users:
    user:User=item
    print(f"{user.user_name}地址：",user.addresses) # 触发一次地址查询

log.succ("解决方法:1. joinedload ====> LEFT OUTER JOIN ")
users = (
    User.query
        .options(joinedload(User.addresses))
        .filter(User.user_name .like("%user%"))
        .all()
)
print(type(users))
for item in users:
    user:User=item
    print(f"{user.user_name}地址：",user.addresses) 


log.succ("解决方法:2. subqueryload ====> 先查询 users, 在 select * from (user) u join address on u.u_id == address.user_id  ")
users = (
    User.query
        .options(subqueryload(User.addresses))
        .filter(User.user_name .like("%user%"))
        .all()
)
print(type(users))
for item in users:
    user:User=item
    print(f"{user.user_name}地址：",user.addresses) 

log.succ("解决方法:3. contains_eager ====> select * from user,address ==> 数据做笛卡儿积 ，程序为每个元素间应用连接条件进行解析 ")
users = (
    User.query
        .options(contains_eager(User.addresses))
        .filter(Address.city .like("%km%"))
        .all()
)
print(len(users))
for item in users:
    user:User=item
    print(f"{user.user_name}地址：",user.addresses) 

log.succ("解决方法:3.1. join(Address),  contains_eager ====>  join ==> 内连接 ，删除所有空 ")
users = (
    User.query
        .join(User.addresses)
        .options(contains_eager(User.addresses))
        .filter(Address.city .like("%km%"))
        .all()
)
print(len(users))
for item in users:
    user:User=item
    print(f"{user.user_name}地址：",user.addresses) 
    
log.end_mark("高级查询")
