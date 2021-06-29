import requests
from flask import request
from util import jwt, response, helpers

class Administrative:
    
    def login(self):
        document = request.json["document"]
        password = request.json["password"]
        req = requests.get('https://simulador-divisist.herokuapp.com/administrativo')
        data = req.json()
        user = helpers.validateUser(data, document, password, "administrative")
        if user:
            del user["contrasena"]
            token = jwt.generateToken(user, 60)
            return response.success("Bienvenido!!", user, token)
        else:
            return response.error("Revise los datos ingresados", 401) 
        
         
         
