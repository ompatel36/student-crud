from models.student_model import Student
from fastapi import Response

students = []
id = 0


async def create_student_controller(student: Student, response: Response):
    global id
    id += 1
    student.id = id
    students.append(student)
    response.status_code = 201
    return {"message": "Student created successfully", "student": student}


async def get_student_controller(response: Response):
    response.status_code = 200
    return {"students": students}


async def get_student_by_id_controller(studentid: int, response: Response):
    try:
        for student in students:
            if student.id == studentid:
                response.status_code = 200
                return {"student": student}

        response.status_code = 404
        return {"message": "Student not found"}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": str(e)}


async def update_student_controller(studentid: int, student: Student, response: Response):
    try:
        for index in range(0, len(students)):
            if students[index].id == studentid:
                student.id = studentid
                students[index] = student
                response.status_code = 200
                return {"message": "Student updated successfully", "student": student}

        response.status_code = 404
        return {"message": "Student not found"}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": str(e)}


async def delete_student_controller(studentid: int, response: Response):
    try:
        for index in range(0, len(students)):
            if students[index].id == studentid:
                students.pop(index)
                return Response(status_code=204)

        response.status_code = 404
        return {"message": "Student not found"}

    except Exception as e:
        print(e)
        response.status_code = 500
        return {"message": str(e)}