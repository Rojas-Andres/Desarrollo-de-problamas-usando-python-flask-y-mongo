from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#Esta seria la clase que vamos a configurar

app = Flask(__name__)
#Conexion a mysql
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flask_contact'

#Configuraciones
#Inicializamos una sesion al server , lo guardamos dentro de la memoria de la app
app.secret_key="mysecretkey"


#Conexion a la base de datos
mysql = MySQL(app)
#Decorador cada vez que un usuario entre a la ruta principal le responda algo
@app.route('/')
def Index():
    #Realizamos la consulta a la base de datos para enviar los clientes
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM CLIENTES')
    data = cur.fetchall()
    #Le envio los clientes al index para que los muestre 
    return render_template('index.html',clientes = data )
@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method == 'POST':
        #Nos referimos al name del formulario del index
        nombre = request.form["Nombre"]
        cedula = request.form["Cedula"]
        direccion = request.form["Direccion"]
        telefono = request.form["Telefono"]
        foto = request.form["Foto"]
        #print(nombre)
        #Establecemos un cursor para la conexion a la bd
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clientes (nombre,cedula,direccion,telefono,foto) values (%s,%s,%s,%s,%s)", (nombre,cedula,direccion,telefono,foto))
        #cur.execute("Select * from contacts")
        mysql.connection.commit()
        #Flash permite enviar mensajes entre vistas
        flash("Contacto agregado satisfactoriamente")
        #Redireccionamos a la principal
        return redirect(url_for('Index'))
@app.route('/edit_contact')
def edit_contact():
    return 'Editar contacto'
#Le envio la cedula 
@app.route('/delete/<int:cedula>')
def delete_contact(cedula):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM CLIENTES WHERE cedula = {0} ".format(cedula))
    mysql.connection.commit()
    flash("Contacto borrado satisfactoriamente")
    return redirect(url_for('Index'))
#El debug significa que cada vez que hagamos un cambio se reinicie el server
if __name__== '__main__': 
    app.run(port = 3000 ,debug = True)
    