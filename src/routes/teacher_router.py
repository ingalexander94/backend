from flask import Blueprint
from database.models import Institutional

instance = Institutional.Institutional()
teacher_rest = Blueprint("teacher_rest", __name__)

@teacher_rest.route("/<code>")
def getTeacher(code):
    return instance.getByCode(code)

@teacher_rest.route("/course/<code>")
def getCourses(code):
    return instance.getMyCoursesTeacher(code)

