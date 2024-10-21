# Proyecto Flask de Donación de Dispositivos

Este es un proyecto web construido con Flask que permite a los usuarios donar dispositivos electrónicos y ver los dispositivos donados por otros usuarios. La aplicación incluye funcionalidad para validar entradas, subir imágenes, y gestionar datos a través de una base de datos.


## Estructura del Proyecto

- **app.py**: Archivo principal que maneja las rutas y la lógica principal de la aplicación.
- **templates/**: Carpeta que contiene las plantillas HTML.
- **static/**: Carpeta para archivos estáticos, dividida en subcarpetas:
  - **css/**: Archivos CSS para el estilo de la aplicación.
  - **js/**: Archivos JavaScript.
  - **uploads/**: Carpeta donde se guardan las imágenes de los dispositivos donados.
- **utils/**: Contiene el archivo `validations.py` para validar las entradas de los usuarios.
- **database/**: Contiene el archivo `db.py` con todas las funciones de interacción con la base de datos.
- **requirements.txt**: Lista de módulos de Python necesarios para el proyecto.


## Funciones Principales en `app.py`

### `agregar_donacion()`

- Maneja la validación y almacenamiento de los datos de contacto y dispositivos.
- Guarda las imágenes subidas de los dispositivos.

### `ver_dispositivos(num)`

- Recupera y muestra dispositivos por pagina.

### `info_dispositivo(disp_id)`

- Muestra información detallada de un dispositivo específico y permite agregar comentarios.

## Validaciones

Las validaciones de los datos se realizan en el archivo `utils/validations.py`.

## Interacción con la Base de Datos

Las interacciones con la base de datos se gestionan en `database/db.py`, que incluye funciones para crear contactos, dispositivos, y almacenar imágenes y comentarios.
