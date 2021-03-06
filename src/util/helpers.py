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

def parseColor(note):
    if not note:
      return "empty"
    color = ""
    if note < 3:
      color = "bad"
    elif note >= 3 and note < 4:
      color = "regular"
    else:
      color = "good"
    return color

def updateSemestersRegistered(semesters):
    return list(map(lambda semester: {**semester, "promedio" : parseColor(semester["promedio"])}, semesters))

def countSemesters(semesters):
    registered = list(filter(lambda semester: semester["promedio"] != "empty", semesters))
    return len(registered)