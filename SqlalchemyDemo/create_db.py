from main import engine
from modeles.base import Model
from modeles.user import *

Model.metadata.create_all(engine)