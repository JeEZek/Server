import uvicorn
from fastapi import FastAPI

from database.database import engine
from models import models
from routers.clients import router as clients_router
from routers.users import router as users_router

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(
    router=users_router,
    prefix="/users"
)

app.include_router(
    router=clients_router,
    prefix="/clients"
)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
