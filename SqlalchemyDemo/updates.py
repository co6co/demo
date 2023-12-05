from modeles.user import Preference, User
from main import session

user_preference:Preference=(
    Preference.query.join(Preference.user)
    .filter(User.email .like("%user3%"))
    .first()
)
user_preference.currency="GBP"
session.commit()

print(user_preference.currency)
# 下面这样会触发一次 user 表的查询 可在查询中找到相关的解决方法
print(user_preference.user.user_name) 

update_number:User=User.query \
    .filter(User.user_name=="user3") \
    .filter(User.email.like ("%user3%")) \
    .update({"email":"admin_user3@hotmail.com"})  #update 将返回更新条数 
session.commit() 
print(update_number)
