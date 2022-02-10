from fastapi import FastAPI
from routes import router
from database import setup_db

app = FastAPI()
setup_db()
app.include_router(router)
