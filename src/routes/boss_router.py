from flask import Blueprint
from database.models import Institutional
from validator.program import ProgramSchema
from middleware.validate_token import token_required
from middleware.validate_request import required_params

boss_rest = Blueprint("boss_rest", __name__)
instance = Institutional.Institutional()

@boss_rest.route("/semesters/students", methods=["POST"])
@token_required
@required_params(ProgramSchema())
def studentsOfPeriod(_):    
    return instance.studentsOfPeriod()