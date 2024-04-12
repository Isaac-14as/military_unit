from sqladmin import Admin, ModelView

from app.models import *


class PersonAdmin(ModelView, model=Person):
    # column_list = [c.name for c in Person.__table__.c] + [Person.subdivision, Person.job_title, Person.rank]
    column_list = [Person.id, Person.subdivision, Person.job_title, Person.rank, Person.name, Person.cabinet, Person.phone, Person.nfc_id]
    column_labels = {
        Person.id: "id",
        Person.subdivision: "Подразделение", 
        Person.job_title: "Штатная должность",
        Person.rank: "Штатное звание",
        Person.name: "ФИО",
        Person.cabinet: "№ кабинет",
        Person.phone: "Телефон",
        Person.nfc_id: "NFC id", 
        }
    name = 'Должностное лицо'
    name_plural = "Должностные лица"
    icon = "fa-solid fa-user"
    page_size = 10



class SubdivisionAdmin(ModelView, model=Subdivision):
    column_list = [Subdivision.id, Subdivision.name]
    name = 'Подразделение'
    name_plural = "Подразделения"
    # icon = "fa-object-group"
    page_size = 10

class JobTitleAdmin(ModelView, model=JobTitle):
    column_list = [JobTitle.id, JobTitle.name]
    column_labels = {
        JobTitle.id: "id",
        JobTitle.name: "Название",
    }
    name = 'Штатная должность'
    name_plural = "Штатные должности"
    # icon = "fa-shopping-bag"
    page_size = 10

class RankAdmin(ModelView, model=Rank):
    column_list = [Rank.id, Rank.name]
    column_labels = {
        JobTitle.id: "id",
        JobTitle.name: "Название",
    }
    name = 'Штатное звание'
    name_plural = "Штатные звания"
    # icon = "fa-star-half-o"
    page_size = 10