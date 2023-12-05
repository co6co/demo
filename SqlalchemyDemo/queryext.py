 
from modeles.user import Address, Preference, Role, User
from sqlalchemy.orm.query import Query
from main import session

 
if  hasattr(Role,"query") and isinstance(Role.query,Query): print(type(Role.query))
else :
    query=session.query_property()  
    Role.query=query 
    print(type(Role.query))
admin_role=Role.query.filter(Role.slug=="admin").first()
if  admin_role ==None:
    role=Role()
    role.name="admim"
    role.slug="admin"
    session.add(role)
    session.commit()
    admin_role=Role.query.filter(Role.slug=="admin").first()
print(admin_role)
    