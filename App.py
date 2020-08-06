from flask import Flask
from flask_mysqldb import MySQL
#Esta seria la clase que vamos a configurar
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskcontact'
#Conexion a la base de datos
mysql = MySQL(app)
#Decorador cada vez que un usuario entre a la ruta principal le responda algo
@app.route('/')
def Index():
    return 'Bienvenido'
@app.route('/add_contact')
def add_contact():
    return 'Añadir contacto'
@app.route('/edit_contact')
def edit_contact():
    return 'Editar contacto'
@app.route('/delete')
def delete_contact():
    return 'Borrar contacto'

#El debug significa que cada vez que hagamos un cambio se reinicie el server
if __name__== '__main__': 
    app.run(port = 3000 ,debug = True)
    