from flask import Blueprint
from middleware.validate_token import token_required
from middleware.validate_request import required_params
from validator.postulation import PostulationSchema, PostulateSchema
from database.models import Institutional
from database.models import Postulation

instance_institutional = Institutional.Institutional()
instance_postulation = Postulation.Postulation()

student_rest = Blueprint("student_rest", __name__)

@student_rest.route("/")
@student_rest.route("/<code>")
@token_required
def getStudent(_, code = None):
    return instance_institutional.getByCode(code, "estudiante")

@student_rest.route("/course/")
@student_rest.route("/course/<code>")
@token_required
def getCourses(_,code = None):
    return instance_institutional.getMyCoursesStudent(code)

@student_rest.route("/postulate", methods=["POST"])
@token_required
@required_params(PostulationSchema())
def postulateStudent(_):
    return instance_postulation.generatePostulation()

@student_rest.route("/postulate/validate", methods=["POST"])
@token_required
@required_params(PostulateSchema())
def validatePostulation(_):
    return instance_postulation.validatePostulation()

