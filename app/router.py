from fastapi import APIRouter

from app.dao import PersonDAO
from app.database import async_session_maker
from sqlalchemy import delete, insert, select, update
from app.schemas import PersonBase
from app.models import Person


router = APIRouter(
    prefix="/main",
    tags=["Main"],
)


# @router.post('/create_person')
# async def create_person(person: PersonBase):
#     await PersonDAO.add(**person.model_dump())
#     return {'status': 200, 'detail': 'Человек успешно добавлен.'}


# @router.post('/get_all_person', response_model=list[PersonBase])
# async def create_person():
#     persons = await PersonDAO.find_all()
#     return persons