import requests
from flask import request
from util import jwt, response, environment
from database import config

mongo = config.mongo

class Institutional:
    
    def login(self):
        info = request.get_json()
        code = info["code"]
        role = info["role"]
        endpoint =  f"{role}_{code}"
        try:
            req = requests.get(f"{environment.API_URL}/{endpoint}")
            data = req.json()
            if data["ok"]:
                user = data["data"]
                del user["contrasena"]
                token = jwt.generateToken(user, 60)
                return response.success("Bienvenido!!", user, token)
            else:
                return response.error("Revise los datos ingresados", 401) 
        except:
          return response.error("Revise los datos ingresados", 401) 
        
    def getByCode(self, code, role):
        if(not code or not code.isdigit() or len(code) != 7):
            return response.error("Se necesita un código de 7 caracteres", 400)
        try:
            req = requests.get(f"{environment.API_URL}/{role}_{code}")
            data = req.json()
            if(data["ok"]):
                user = data["data"]
                del user["contrasena"]
                return response.success("Todo Ok!", user, "")
            else: 
                return response.error("No se encontraron resultados", 400)
        except:
          return response.success("No se encontraron resultados", None, "")
    
    def getMyCoursesStudent(self, code):
        if(not code or not code.isdigit() or len(code) != 7):
            return response.error("Se necesita un código de 7 caracteres", 400)
        req = requests.get(f"{environment.API_URL}/materias_{code}")
        courses = req.json()
        return response.success("Todo ok!", courses, "")
    
    def getMyCoursesTeacher(self, code):
        if(not code or not code.isdigit() or len(code) != 7):
           return response.error("Se necesita un código de 7 caracteres", 400)
        req = requests.get(f"{environment.API_URL}/cursos_{code}")
        courses = req.json()
        # Borrar el docente
        return response.success("Todo ok!", courses, "")

    def getStudentsOfCourse(self, code, group):
        if(not code or not code.isdigit() or len(code) != 7):
           return response.error("Se necesita un código de 7 caracteres", 400)
        req = requests.get(f"{environment.API_URL}/listado_{code}_{group}")
        students = req.json()
        return response.success("Todo ok!", students, "")

    def getProfits(self, code, risk):
        if(not code or not code.isdigit() or len(code) != 7):
            return response.error("Se necesita un código de 7 caracteres", 400)
        req = requests.get(f"{environment.API_URL}/beneficios_{code}")
        data = list(req.json())
        profits = list(mongo.db.profit.find({"riesgo" : risk}, {"nombre":1, "_id": False}))
        array = []
        for key in profits:
            array.append(key["nombre"])
        aux = list(filter(lambda profit: profit["nombre"] in array, data ))
        return response.success("todo ok", aux , "")
    
    def getNumberSemesters(self, user):
        program = user["programa"]
        program = "sistemas"
        semesters = requests.get(f"{environment.API_URL}/semestre_{program}");
        data = semesters.json()
        quantity = data["cantidadSemestres"]
        return response.success("todo ok!", quantity, "")
      
    def studentsOfSemesters(self, user, semester):
        if not semester:
          return response.error("El semestre es obligatorio", 400)
        program = user["programa"]
        program = "sistemas"
        students = requests.get(f"{environment.API_URL}/{program}_{semester}");
        data = students.json()
        return response.success("todo ok!", data, "")
        
              
        
         


