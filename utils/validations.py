import re, filetype

def validar_datos_contacto(nombre, mail, telefono, region, comuna):
    #validar nombre
    if (not nombre) or not (3 <= len(nombre) <= 80): print("mal nombre");return False
    #validar mail
    regex_mail = r'^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
    if (not mail) or (not re.match(regex_mail, mail)): print("mal mail");return False

    #validar telefono
    regex_tel = r'^[0-9]+$'
    if (not telefono) or (not len(telefono) >= 8) or (not re.match(regex_tel, telefono)): 
        # print("mal telefono")
        # print(not telefono)
        # print(not len(telefono) >= 8)
        # print(not re.match(regex_tel, telefono))
        return False

    #validar region
    if (region == "nada"): print("mal region");return False

    #validar comuna
    if (comuna == "nada"): print("mal comuna");return False

    return True

def validar_datos_disp(nombre, tipo, años, funcionamiento):
    #validar nombre dispositivo
    if not 3 <= len(nombre) <= 80: 
        print("error con el nombre")
        return False

    #validar tipo
    if tipo == "nada": 
        print("error con el tipo")
        return False

    #validar años de uso
    try:
       if not 0 < int(años) < 100: 
        print("error con el años uso")
        return False
    except ValueError:
       print("error con el años uso")
       return False
    
    #validar funcionamiento
    if funcionamiento == "nada": 
        print("error con el estado")
        return False

    # print("todo bien")
    return True

def validate_conf_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if conf_img is None:
        return False
    

    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True