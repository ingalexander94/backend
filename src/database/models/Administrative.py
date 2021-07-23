import requests
from flask import request
from util import jwt, response, environment

class Administrative:
    
    def login(self):
        info = request.get_json()
        document = info["document"]
        role = info["role"]
        endpoint =  f"{role}_{document}"
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
        
    def getFaculties(self):
        req = requests.get(f"{environment.API_URL}/facultades")
        data = req.json()
        return response.success("Todo ok!", data, "")
         
