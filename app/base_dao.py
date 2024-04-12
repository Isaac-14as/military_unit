from sqlalchemy import delete, insert, select, update
from app.database import async_session_maker

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
            return data
    
    @classmethod
    async def delete_by_id(cls, model_id):
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == model_id)
            result = await session.execute(query)
            await session.commit()
            return result
        
    @classmethod
    async def change_by_id(cls, model_id, **data):
        async with async_session_maker() as session:
            stmt = (
                update(cls.model).
                where(cls.model.id == model_id).
                values(**data)
                )
            result = await session.execute(stmt)
            await session.commit()
            return result