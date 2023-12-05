from main import session
from sqlalchemy import desc

from modeles.user import User,Role


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
    User.query.limit(3)
    .order_by(desc( User.user_name))
    .order_by( User.email)
    .all()
)