# Proyecto Flask de Donación de Dispositivos

Este es un proyecto web construido con Flask que permite a los usuarios donar dispositivos electrónicos y ver los dispositivos donados por otros usuarios. La aplicación incluye funcionalidad para validar entradas, subir imágenes, gestionar datos a través de una base de datos, y visualizar gráficos de los datos.

## Estructura del Proyecto

- **app.py**: Archivo principal que maneja las rutas y la lógica principal de la aplicación.
- **templates/**: Carpeta que contiene las plantillas HTML.
  - **index.html**: Página principal que ahora incluye botones para visualizar gráficos.
- **static/**: Carpeta para archivos estáticos, dividida en subcarpetas:
  - **css/**: Archivos CSS para el estilo de la aplicación.
  - **js/**: Archivos JavaScript, incluyendo scripts para manejar AJAX y gráficos.
  - **uploads/**: Carpeta donde se guardan las imágenes de los dispositivos donados.
- **utils/**: Contiene el archivo `validations.py` para validar las entradas de los usuarios.
- **database/**: Contiene el archivo `db.py` con todas las funciones de interacción con la base de datos.
- **requirements.txt**: Lista de módulos de Python necesarios para el proyecto.

## Funciones Principales en `app.py`

### `agregar_donacion()`

- Maneja la validación y almacenamiento de los datos de contacto y dispositivos.
- Guarda las imágenes subidas de los dispositivos.

### `ver_dispositivos(num)`

- Recupera y muestra dispositivos por página.

### `info_dispositivo(disp_id)`

- Muestra información detallada de un dispositivo específico y permite agregar comentarios.

### `grafico_tipo_dispositivos()`

- Genera y muestra un gráfico de los tipos de dispositivos donados.

### `grafico_contactos_comuna()`

- Genera y muestra un gráfico de la cantidad de contactos por comuna.

### Botones de Gráficos en `index.html`

En la página principal (`index.html`), se han agregado dos nuevos botones:

- **Gráfico Tipo de Dispositivos**: Lleva a una página que muestra un gráfico con la distribución de tipos de dispositivos donados.
- **Gráfico Contactos por Comuna**: Lleva a una página que muestra un gráfico con la distribución de contactos por comuna.

### AJAX y Fetch en JavaScript

Estos graficos utilizan AJAX con `fetch` para recuperar los datos del servidor y mostrarlos sin necesidad de recargar la página.

