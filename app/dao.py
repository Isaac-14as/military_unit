from app.base_dao import BaseDAO
from app.models import Person



class PersonDAO(BaseDAO):
    model = Person