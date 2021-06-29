import functools

def indexedCourses(data):
        return functools.reduce(lambda acc, curr: {**acc, curr["codigo"] : curr }, data , {})
    
def validateUser(users, document, password, code):
    aux = None
    if code:
        aux = list(filter(lambda user: user["codigo"] == code and user["documento"] == document and user["contrasena"] == password, users))
    else:
        aux = list(filter(lambda user: user["documento"] == document and user["contrasena"] == password, users))
    if aux:
        aux = aux[0]
    return aux