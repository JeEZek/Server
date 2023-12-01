import uvicorn
from fastapi import FastAPI
from sqlalchemy.future import engine

import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
