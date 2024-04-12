import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

sys.path.insert(1, os.path.join(sys.path[0], '..')) # решение проблемы import


from app.admin.views import *
from app.router import router as router_main
from app.database import engine


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_main)



admin = Admin(app, engine)


admin.add_view(PersonAdmin)
admin.add_view(SubdivisionAdmin)
admin.add_view(JobTitleAdmin)
admin.add_view(RankAdmin)