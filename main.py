from fastapi import FastAPI
from fastApi_start import app as fastapi_router

app = FastAPI()


app.include_router(fastapi_router)