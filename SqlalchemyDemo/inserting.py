 
from modeles.user import Address, Preference, Role, User
from main import session

admin_role=Role.query.filter(Role.slug=="admin").first()
if  admin_role ==None:
    role=Role()
    role.name="admim"
    role.slug="admin"
    session.add(role)
    session.commit()
    admin_role=Role.query.filter(Role.slug=="admin").first()
print(admin_role)
    

user= User(
    user_name="admin",
    email="admin@gmail.com"
) 
print("这里不执行吗")
session.add(user)

user2=User()
user2.email="user2@gmail.com"
user2.user_name="user2"
session.add(user2)


user3=User()
user3.email="user3@gmail.com"
user3.user_name="user3"

user3.roles.append(admin_role)
address=Address()
address.road_name="kkk"
address.city="km"
address.pastcode="655200"
user3.addresses.append(
    address
)
user3.preference=Preference(
    language="english",
    currency="GBP"
)

session.add(user3)
session.commit()
