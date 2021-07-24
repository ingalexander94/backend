import math
from flask import request, Response
from util import response, emails
from database import config
from bson import json_util
from pymongo import DESCENDING

mongo = config.mongo

class Postulation: 
    
    def generatePostulation(self):
        data = request.get_json()
        postulate = self.searchValidation(data["student"], True)
        if postulate:
            return response.error("Ya se encuentra postulado", 401)
        else:
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
        postulation = self.searchValidation(data["student"], data["isActive"])
        res = json_util.dumps(postulation)
        return Response(res, mimetype="applicaton/json")
    
    def searchValidation(self, student, isActive):
        data = {
            "student": student,
            "isActive":isActive
        }
        postulation = mongo.db.postulation.find_one(data)
        return postulation
    
    def paginatePostulations(self, userAuth):
        totalPostulations = mongo.db.postulation.count_documents({"isActive":True})
        page = request.args.get("page", default=1, type= int)
        perPage = request.args.get("perPage", default=5, type= int)
        totalPages = math.ceil(totalPostulations/perPage)
        offset = ((page-1) * perPage) if page > 0 else 0
        program = userAuth["programa"]
        print("programa ",program) 
        data = mongo.db.postulation.find({"student.programa":program}).sort("date", DESCENDING).skip(offset).limit(perPage)
        postulations = json_util.dumps({
            "totalPages": totalPages,
            "data": data
        })
        return Response(postulations, mimetype="applicaton/json")
    
    def filterPostulations(self):
        code = request.json["code"]
        data = mongo.db.postulation.find_one({"student.codigo": {"$eq": code} })
        postulations = json_util.dumps(data)
        return Response(postulations, mimetype="applicaton/json")
    
    def countPostulationUnattended(self):
        unattended = mongo.db.postulation.count_documents({"state":"SIN ATENDER"})
        return response.success("todo ok!", unattended, "")
    