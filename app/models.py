from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Person(Base):
    __tablename__ = 'person'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    subdivision_id: Mapped[int] = mapped_column(ForeignKey("subdivision.id", ondelete="SET NUll"))
    job_title_id: Mapped[int] = mapped_column(ForeignKey("job_title.id", ondelete="SET NUll"))
    rank_id: Mapped[int] = mapped_column(ForeignKey("rank.id", ondelete="SET NUll"))
    name: Mapped[str]
    cabinet: Mapped[int | None]
    phone: Mapped[int | None] = mapped_column(unique=True)
    nfc_id: Mapped[int] = mapped_column(unique=True)

    subdivision: Mapped["Subdivision"] = relationship(back_populates="person")
    job_title: Mapped["JobTitle"] = relationship(back_populates="person")
    rank: Mapped["Rank"] = relationship(back_populates="person")

    def __str__(self):
        return self.name


class Subdivision(Base):
    __tablename__ = 'subdivision'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    person: Mapped["Person"] = relationship(back_populates='subdivision')

    def __str__(self):
        return self.name


class JobTitle(Base):
    __tablename__ = 'job_title'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    person: Mapped["Person"] = relationship(back_populates='job_title')

    def __str__(self):
        return self.name
    
class Rank(Base):
    __tablename__ = 'rank'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    person: Mapped["Person"] = relationship(back_populates='rank')

    def __str__(self):
        return self.name



    