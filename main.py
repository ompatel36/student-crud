from fastapi import FastAPI
from routes.student_router import studentRouter

app = FastAPI()

app.include_router(studentRouter)