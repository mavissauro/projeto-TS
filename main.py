from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from business.database.database import Base
from business.database.database import engine

from api.endpoints.user import router as user_router
from api.endpoints.item import router as item_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(item_router, prefix="/item", tags=["item"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
