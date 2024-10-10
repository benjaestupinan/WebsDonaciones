from flask import Flask, render_template, url_for, request, redirect
from database import db
from utils import validations
import hashlib
import filetype
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agregar_donacion", methods=["GET", "POST"])
def agregar_donacion():
    # comuna = db.get_comuna_id_by_name("Arica")
    # print(comuna)
    if request.method == "POST":
        disp_count = request.form.get("disp_count")
        contact_name = request.form.get("nombre")
        contact_mail = request.form.get("mail")
        contact_phonenumber = request.form.get("celular")
        contact_region = request.form.get("region")
        contact_comuna = request.form.get("comuna")

        # print(f"hay {disp_count} dispositivos")
        # print(f"nombre: {contact_name}")
        # print(f"mail: {contact_mail}")
        # print(f"telefono: {contact_phonenumber}")
        # print(f"region: {contact_region}")
        # print(f"comuna: {contact_comuna}")

        if not validations.validar_datos_contacto(contact_name, contact_mail, contact_phonenumber, contact_region, contact_comuna):
           error="Error con los datos de contacto"
           return render_template("agregar_donacion.html", error=error) # Error con los input de usuario
        
        _email = db.get_contact_by_mail(contact_mail)
        if _email is None:
          status, msg = db.create_contact(contact_name, contact_mail, contact_phonenumber, contact_comuna)
          if not status:
            error=msg
            return render_template("agregar_donacion.html", error=error)

        for i in range(int(disp_count)):
          #  print("#################################")
           disp_name = request.form.get(f"nombre-disp{i}")
           disp_tipo = request.form.get(f"tipo{i}")
           disp_años = request.form.get(f"años-de-uso{i}")
           disp_desc = request.form.get(f"description{i}")
           disp_funcionamiento = request.form.get(f"estado-funcionamiento{i}")
           disp_img = request.files.get(f"foto-producto{i}")

          #  print(f"imagen: {disp_img}")
          #  print(f"nombre disp {i}: {disp_name}")
          #  print(f"descripcion disp {i}: {disp_desc}")
          #  print(f"tipo disp {i}: {disp_tipo}")
          #  print(f"años disp {i}: {disp_años}")
          #  print(f"estado disp {i}: {disp_funcionamiento}")

           if not validations.validar_datos_disp(disp_name, disp_tipo, disp_años, disp_funcionamiento):
              error=f"Error con los datos de dispositivo N°{i+1}"
              return render_template("agregar_donacion.html", error=error) # Error con los input de dispositivo
           
           if not validations.validate_conf_img(disp_img):
              error=f"Error con los archivos de dispositivo N°{i+1}"
              return render_template("agregar_donacion.html", error=error) # Error con las fotos
           
           statusNew, msgNew = db.create_disp(contact_mail, disp_name, disp_desc, disp_tipo, disp_años, disp_funcionamiento)
           if not statusNew:
             error=msgNew
             return render_template("agregar_donacion.html", error=error)

           _filename = hashlib.sha256(
               secure_filename(disp_img.filename) # nombre del archivo
               .encode("utf-8") # encodear a bytes
               ).hexdigest()
           _extension = filetype.guess(disp_img).extension
           img_filename = f"{_filename}.{_extension}"

           disp = db.get_disp_id(contact_mail, disp_name, disp_desc, disp_tipo, disp_años, disp_funcionamiento)
 
           # 2. save img as a file
           disp_img.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))            
           statusImg, msgImg = db.create_img(img_filename, disp_img.filename, disp[0])
           if not statusImg:
              error=msgImg
              return render_template("agregar_donacion.html", error=error)
           
          
        return render_template("index.html", gracias="Gracias por agregar su donacion!!!")
        
        # return redirect(url_for("exito")) # inicio con mensaje de aceptacion
    else:
        return render_template("agregar_donacion.html")

@app.route("/ver_dispositivos/<num>")
def ver_dispositivos(num):
    data = db.get_disps((int(num)-1)*5, 5)

    # data[i][4] = tipo
    # data[i][2] = nombre
    # data[i][6] = estado
    
    newData = []
    for i in range(len(list(data))):
        dato = []
        user = db.get_contact_by_id(data[i][1])
        comuna = db.get_comuna_by_id(user[4])[0]

        archivo = db.get_files_by_disp_id(data[i][0])[0][0]

        dato.append(data[i][4])
        dato.append(data[i][2])
        dato.append(data[i][6])
        dato.append(comuna)
        dato.append(f"uploads/{archivo}")
        dato.append(i)
        dato.append(data[i][0])

        newData.append(dato)

    if len(list(db.get_disps(int(num)*5, 5))) == 0:
       return render_template("ver_dispositivos.html", num=int(num), data=newData, last="true")
       
    return render_template("ver_dispositivos.html", num=int(num), data=newData)

@app.route("/info_dispositivo/<disp_id>", methods=["GET", "POST"])
def info_dispositivo(disp_id):
   
    if request.method == "POST":

        nombre = request.form.get("autor")
        texto = request.form.get("comment")

        status, msg = db.create_comment(nombre, texto, disp_id)
        if not status:
              error=msg
              return render_template("info_dispositivo.html", data=data, comentarios=comentarios, error=error)

        return redirect(url_for("info_dispositivo", disp_id=disp_id))
    elif request.method == "GET":
        data = []
        comentarios = db.get_commentarios_by_disp_id(disp_id)
        
        # Nombre donante = data[0]
        # Mail donante = data[1]
        # Telefono donante = data[2]

        # Tipo = data[3]
        # Nombre = data[4]
        # Descripcion = data[5]
        # Estado = data[6]
        # Años de uso = data[7]
        # Comuna = data[8]
        # Imagen = data[9]


        disp = db.get_disp_by_id(disp_id)
        
        # print("##############################################")
        # print(comentarios)
        # print("##############################################")
        
        donante_id = disp[1]

        donante = db.get_contact_by_id(donante_id)

        comuna = db.get_comuna_by_id(donante[4])[0]

        archivo = db.get_files_by_disp_id(disp_id)[0][0]

        data.append(donante[1]) # data[0]
        data.append(donante[2]) # data[1]
        data.append(donante[3]) # data[2]

        data.append(disp[4]) # data[3]
        data.append(disp[2]) # data[4]
        data.append(disp[3]) # data[5]
        data.append(disp[6]) # data[6]
        data.append(disp[5]) # data[7]
        data.append(comuna) # data[8]
        data.append(f"uploads/{archivo}") # data[9]

        return render_template("info_dispositivo.html", data=data, comentarios=comentarios)