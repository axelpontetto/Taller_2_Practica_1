from flask import Flask
from flask import render_template
from flask import request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'simulacion'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

ultimaLeida = 0		# ID de la ultima muestra leida
muestreo = 0

@app.route('/')
def index():
	return render_template('medidas.html', muestreo=5)

@app.route('/promedios')
def promedios():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute('SELECT AVG(temperatura), AVG(humedad), AVG(presion), AVG(viento) from Medidas ORDER BY idMedida desc LIMIT 10')
	prom = cursor.fetchone()
    
	string = '<th scope="row">Últimas 10 muestras:</th>'
	string = string + '<td>' + str( round( prom[0] , 2) ) + ' °C</td>'
	string = string + '<td>' + str( round( prom[1] , 2) ) + ' % </td>'
	string = string + '<td>' + str( round( prom[2] , 2) ) + ' hPa </td>'
	string = string + '<td>' + str( round( prom[3] , 2) ) + ' km/h </td>'
	
	return string

@app.route('/ultima')
def ultima():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute('SELECT * from Medidas ORDER BY idMedida desc LIMIT 1')
	lastData = cursor.fetchone()
    
	string = '<th scope="row">' + str( round( lastData[0] , 2) ) + '</th>'
	string = string + '<td>' + str( round( lastData[1] , 2 ) ) + ' °C</td>'
	string = string + '<td>' + str( round( lastData[2] , 2 ) ) + ' % </td>'
	string = string + '<td>' + str( round( lastData[3] , 2 ) ) + ' hPa </td>'
	string = string + '<td>' + str( round( lastData[4] , 2 ) ) + ' km/h </td>'
	
	return string

@app.route('/historico')
def historico():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute('SELECT * from Medidas')
	allData = cursor.fetchall()

	string =''
	for row in allData:
		string = string +'<tr> <th scope="row">' + str( round( row[0], 2 ) ) + '</th>'
		string = string + '<td>' + str( round( row[1] , 2 ) ) + ' °C </td>'
		string = string + '<td>' + str( round( row[2] , 2 ) ) + ' % </td>'
		string = string + '<td>' + str( round( row[3] , 2 ) ) + ' hPa </td>'
		string = string + '<td>' + str( round( row[4] , 2 ) ) + ' km/h </td> </tr>'
	
	return string

if __name__ == "__main__":
    app.run( debug = True , port = 7000)