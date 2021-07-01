from flask import Blueprint
from middleware.validate_token import token_required
from database.models import Institutional

instance = Institutional.Institutional()

student_rest = Blueprint("student_rest", __name__)

@student_rest.route("/")
@student_rest.route("/<code>")
@token_required
def getStudent(_, code = None):
    return instance.getByCode(code)

@student_rest.route("/course/")
@student_rest.route("/course/<code>")
@token_required
def getCourses(_,code = None):
    return instance.getMyCoursesStudent(code)

