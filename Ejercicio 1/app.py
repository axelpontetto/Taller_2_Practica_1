# Librerías para importar en el proyecto
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# Definimos la ruta destinada para ingresar con un navegador web
# Request por defecto: GET
@app.route('/')
# Función destinada para controlar la ruta defina anteriormente
def index():
	# Retornamos el template formulario ubicado en la carpeta templates
    return render_template('formulario.html')

# Definimos la ruta destinada al request POST enviado por el metodo anterior GET
@app.route('/formulario', methods = ['POST'])
# Definimos la Funcion asociada al request anteriormente mencionado
def action_form():
	# Comprobamos que el request haya sido un POST y retornamos los valores ingresados
    if request.method == 'POST':
        data = request.form
        nombre = data["nombre"]
        apellido = data["apellido"]
        return render_template('respuesta.html', nombre = nombre, apellido = apellido)

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run( debug = True , port = 8000)