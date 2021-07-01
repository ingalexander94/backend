from flask import Blueprint
from middleware.validate_token import token_required
from database.models import Institutional

instance = Institutional.Institutional()
teacher_rest = Blueprint("teacher_rest", __name__)

@teacher_rest.route("/")
@teacher_rest.route("/<code>")
@token_required
def getTeacher(_,code = None):
    return instance.getByCode(code)

@teacher_rest.route("/course/")
@teacher_rest.route("/course/<code>")
@token_required
def getCourses(_,code = None):
    return instance.getMyCoursesTeacher(code)

