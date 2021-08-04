from flask import Flask
from flask_cors import CORS
from middleware.validate_token import token_required
from routes.institutonal_router import institutional_rest
from routes.administrative_router import administrative_rest
from routes.notification_router import notification_rest
from routes.boss_router import boss_rest
from routes.student_router import student_rest
from routes.teacher_router import teacher_rest
from routes.chat_router import chat_rest
from routes.wellness_router  import wellness_rest
from routes.meet_router  import meet_rest
from util import environment, jwt
from database import config

app = Flask(__name__)
app.config["MONGO_URI"]= environment.MONGO_URL
config.mongo.init_app(app)
CORS(app)

# JWT
app.config["SECRET_KEY"] = environment.SECRET_JWT

# Rutas
app.register_blueprint(institutional_rest, url_prefix='/auth/institutional')
app.register_blueprint(administrative_rest, url_prefix='/auth/administrative')
app.register_blueprint(student_rest, url_prefix='/students')
app.register_blueprint(teacher_rest, url_prefix='/teachers')
app.register_blueprint(boss_rest, url_prefix='/boss')
app.register_blueprint(chat_rest, url_prefix='/chat')
app.register_blueprint(notification_rest, url_prefix='/notification')
app.register_blueprint(wellness_rest, url_prefix='/wellness')
app.register_blueprint(meet_rest, url_prefix='/meet')

@app.route("/auth/renew")
@token_required
def renew(current_user):
    return jwt.renewToken(current_user)

@app.route("/ping")
def ping():
    return "Todo ok!"

# Lanzar servidor
if __name__ == "__main__":
    app.run(debug=True, port=environment.PORT, host="0.0.0.0")
