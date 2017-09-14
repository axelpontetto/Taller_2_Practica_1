import pymysql.cursors
from random import uniform
from time import sleep

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='simulacion',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

for x in range(1,100):
	temperatura = str(uniform(-100,100))
	humedad = str(uniform(0,100))
	presion = str(uniform(600,1200))
	viento = str(uniform(0,400))

	cursor = connection.cursor()

	cursor.execute('SELECT * from Muestreo')
	muestreo = cursor.fetchone()
	cursor.execute('SELECT MAX(idMedida) FROM simulacion.medidas')
	maxId = cursor.fetchone()
	id = maxId['MAX(idMedida)'] + 1

	cursor.execute('''INSERT INTO simulacion.medidas(idMedida, temperatura, humedad, presion, viento) VALUES (%s, %s, %s, %s, %s)''', (id , temperatura , humedad, presion, viento ) )
	connection.commit()

	print(muestreo['periodo'])
	sleep(muestreo['periodo'])

connection.close()