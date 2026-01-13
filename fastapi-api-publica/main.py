from fastapi import FastAPI
from model.user_connection import UserConnection
from starlette.status import HTTP_200_OK
from services.agify_service import AgifyService

conn = UserConnection()
agify = AgifyService()


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "running"}

@app.get("/api/age/{name}", status_code= HTTP_200_OK)
async def get_age (name: str):
    data = await agify.get_ages(name)
    conn.inser_db(data)
    return data
@app.get("/api/get_record_users/")
async def get_users():
    return conn.read_db()