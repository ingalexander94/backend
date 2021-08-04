from flask import Blueprint
from middleware.validate_token import token_required
from middleware.validate_request import required_params
from database.models import Meet
from validator.meet import MeetSchema

meet_rest = Blueprint("meet_rest", __name__)
instance = Meet.Meet()

@meet_rest.route("/", methods=["POST"])
@token_required
@required_params(MeetSchema())
def createMeet(_):
    return instance.createMeet()

@meet_rest.route("/")
@meet_rest.route("/<code>") 
@token_required
def getMeetOfStudent(_, code=None):
    return instance.getMeetOfStudent(code)

@meet_rest.route("/", methods=["PUT"])
@meet_rest.route("/<id>", methods=["PUT"]) 
@token_required
def acceptMeet(_, id=None):
    return instance.acceptMeet(id)



@meet_rest.route("/meet")
@meet_rest.route("/meets/<code>")
@token_required
def getMeeetsStudent(_, code=None):
    return instance.getMeeetsStudent(code)

@meet_rest.route("/paginate")
@token_required
def paginateMeets(userAuth):
    return instance.paginateMeets(userAuth["rol"])
