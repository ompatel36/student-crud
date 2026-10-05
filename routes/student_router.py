from fastapi import APIRouter, Response
from controllers.student_controller import create_student_controller, get_student_controller, get_student_by_id_controller, update_student_controller, delete_student_controller
from models.student_model import Student

studentRouter = APIRouter(
    prefix="/students",
    tags=["students"]
)


@studentRouter.post("/")
async def create_student(student: Student, response: Response):
    return await create_student_controller(student, response)


@studentRouter.get("/")
async def get_students(response: Response):
    return await get_student_controller(response)


@studentRouter.get("/{studentid}")
async def get_student(studentid: int, response: Response):
    return await get_student_by_id_controller(studentid, response)


@studentRouter.put("/{studentid}")
async def update_student(studentid: int, student: Student, response: Response):
    return await update_student_controller(studentid, student, response)


@studentRouter.delete("/{studentid}")
async def delete_student(studentid: int, response: Response):
    return await delete_student_controller(studentid, response)