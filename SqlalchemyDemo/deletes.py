from modeles.user import User
from main import session


user= User.query.first()
print(user)

session.delete(user)
session.commit()

user= User.query.first()
print(user)
