from flask import Blueprint
from database.models import Institutional
from middleware.validate_token import token_required

boss_rest = Blueprint("boss_rest", __name__)
instance = Institutional.Institutional()

@boss_rest.route("/semesters/students/")
@boss_rest.route("/semesters/students/<period>")
@token_required
def studentsOfPeriod(userAuth, period=None):    
    return instance.studentsOfPeriod(userAuth, period)