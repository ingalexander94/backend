from flask import Blueprint
from middleware.validate_token import token_required
from database.models import Administrative

wellness_rest = Blueprint("wellness_rest", __name__)

instance = Administrative.Administrative()

@wellness_rest.route("/faculties")
@token_required
def getFaculties(_):
    return instance.getFaculties()
    
