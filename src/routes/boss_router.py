from flask import Blueprint
from database.models import Institutional
from middleware.validate_token import token_required

boss_rest = Blueprint("boss_rest", __name__)
instance = Institutional.Institutional()

@boss_rest.route("/semesters")
@token_required
def numberOfSemesters(userAuth):
    return instance.getNumberSemesters(userAuth)

@boss_rest.route("/semesters/students/")
@boss_rest.route("/semesters/students/<semester>")
@token_required
def studentsOfSemesters(userAuth, semester=None):    
    return instance.studentsOfSemesters(userAuth, semester)