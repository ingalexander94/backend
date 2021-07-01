import requests
from flask import request
from util import jwt, response, helpers

class Institutional:
    
    def login(self):
        code = request.json["code"]
        document = request.json["document"]
        password = request.json["password"]
        req = requests.get('https://simulador-divisist.herokuapp.com/institucional')
        data = req.json()
        user = helpers.validateUser(data, document, password, code)
        if user:
            del user["contrasena"]
            token = jwt.generateToken(user, 60)
            return response.success("Bienvenido!!", user, token)
        else:
            return response.error("Revise los datos ingresados", 401) 
        
    def getByCode(self, code):
        if(not code or not code.isdigit() or len(code) != 7):
            return response.error("Se necesita un código de 7 caracteres", 400)
        req = requests.get("https://simulador-divisist.herokuapp.com/institucional")
        data = req.json()
        for user in data:
          if user["codigo"] == code:
            return response.success("Todo Ok!", user, "")
        return response.error("No se encontraron resultados", 400)
    
    def getMyCoursesStudent(self, code):
        if(not code or not code.isdigit() or len(code) != 7):
            return response.error("Se necesita un código de 7 caracteres", 400)
        req = requests.get("https://simulador-divisist.herokuapp.com/cursos")
        data = req.json()
        req2 = requests.get("https://simulador-divisist.herokuapp.com/materias")
        data2 = req2.json()
        courses = []
        indexed = helpers.indexedCourses(data2)
        for course in data:
          if course["estudiante"] == code:
              aux = {
                  **course,
                  "materia" : indexed[course["materia"]]
              }
              del aux["estudiante"]
              courses.append(aux)
        return response.success("Todo ok!", courses, "")
    
    def getMyCoursesTeacher(self, code):
        if(not code or not code.isdigit() or len(code) != 7):
           return response.error("Se necesita un código de 7 caracteres", 400)
        req = requests.get("https://simulador-divisist.herokuapp.com/materias")
        data = req.json()
        courses = []
        for course in data:
          if course["docente"] == code:
              del course["docente"]
              courses.append(course)
        return response.success("Todo ok!", courses, "")

        
        
              
        
         


