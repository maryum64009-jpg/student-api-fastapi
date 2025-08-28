from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    email: str

students = [
    Student(id=1,  name="Shehzil", age=20, gender="Female", email="shehzil@example.com"),
    Student(id=2,  name="Fizza",   age=21, gender="Female", email="fizza@example.com"),
    Student(id=3,  name="Sakina",  age=19, gender="Female", email="sakina@example.com"),
    Student(id=4,  name="Hiba",    age=22, gender="Female", email="hiba@example.com"),
    Student(id=5,  name="Areesha", age=23, gender="Female", email="areesha@example.com"),
    Student(id=6,  name="Zain",    age=20, gender="Male",   email="zain@example.com"),
    Student(id=7,  name="Jhon",    age=24, gender="Male",   email="jhon@example.com"),
    Student(id=8,  name="Farhan",  age=21, gender="Male",   email="farhan@example.com"),
    Student(id=9,  name="Ali",     age=22, gender="Male",   email="ali@example.com"),
    Student(id=10, name="Rana",    age=23, gender="Female", email="rana@example.com")
]

@app.get("/student")
def get_students():
    return students

@app.get("/students/{student_id}")
def fetch_student(student_id:int):
    for student in students:
        if student.id == student_id:
            return student
    return {"message": "Student not found"}

@app.post("/students")
def add_student(student: Student):
    students.append(student)  
    return student   

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in students:             
        if student.id == student_id:     
            student.name = updated_student.name
            student.age = updated_student.age
            student.gender = updated_student.gender
            student.email = updated_student.email
            return student              
    return {"message": "Student not found"}  

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:             
        if student.id == student_id:     
            students.remove(student)     
            return {"message": f"{student.name} has been deleted"}  
    return {"message": "Student not found"} 
        



