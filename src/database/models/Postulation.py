from flask import request, Response
from util import response, emails
from database import config
from bson import json_util

mongo = config.mongo

class Postulation: 
    
    def generatePostulation(self):
        data = request.get_json()
        # Obtener información de quíen postulo
        data["postulator"] = data["postulator"] if data["postulator"] else data["student"]
        data = {
            **data,
            "state":"SIN ATENDER",
            "isActive": True
        }
        id = mongo.db.postulation.insert(data)
        namePostulator = f'{data["postulator"]["rol"]} {data["postulator"]["nombre"]}'
        program = data["student"]["programa"]
        message = f"Cordial saludo\nSe le informa que ha sido postulado por el {namePostulator} y se ha enviado la solicitud al jefe del programa de {program} para continuar con el proceso de seguimiento.\nEstado de la Postulación: SIN ATENDER"
        subject = "Postulación generada en el sistema de alertas de la UFPS"
        emails.sendEmail(data["student"]["correo"], message, subject)
        return response.success("Estudiante Postulado", {**data, "_id": str(id)}, "")
    
    def validatePostulation(self):
        data = request.get_json()
        postulation = mongo.db.postulation.find_one(data)
        res = json_util.dumps(postulation)
        return Response(res, mimetype="applicaton/json")