import requests
from flask import request
from util import jwt, response, environment

class Institutional:
    
    def login(self):
        info = request.get_json()
        code = info["code"]
        role = info["role"]
        endpoint =  f"estudiante_{code}" if role == "estudiante" else f"docente_{code}"
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
        req = requests.get(f"{environment.API_URL}/{role}_{code}")
        data = req.json()
        if(data["ok"]):
            user = data["data"]
            del user["contrasena"]
            return response.success("Todo Ok!", user, "")
        else: 
            return response.error("No se encontraron resultados", 400)
    
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

        
              
        
         


