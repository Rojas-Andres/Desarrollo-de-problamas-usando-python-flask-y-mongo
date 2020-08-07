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
def index():
    return render_template('index.html' )

@app.route('/contactos')
def contactos():
    #Realizamos la consulta a la base de datos para enviar los clientes
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM CLIENTES')
    data = cur.fetchall()
    #Le envio los clientes al index para que los muestre 
    return render_template('contactos.html',clientes = data )

@app.route('/add_cliente',methods=['POST'])
def add_cliente():
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
        return redirect(url_for('contactos'))

@app.route('/edit_contact/<int:cedula>')
def get_cliente(cedula):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM CLIENTES WHERE cedula = {0} ".format(cedula))
    dato = cur.fetchall()
    return render_template('editar_contacto.html',cliente = dato[0] )

@app.route('/actualizar/<int:cedula>',methods=['POST'])
def actualizar(cedula):
    cur = mysql.connection.cursor()
    nombre = request.form["Nombre"]
    cedula_cli = request.form["Cedula"]
    direccion = request.form["Direccion"]
    telefono = request.form["Telefono"]
    foto = request.form["Foto"]
    cur.execute("""
    UPDATE CLIENTES SET CEDULA = %s ,nombre =%s,direccion =%s,telefono =%s,foto=%s 
    where cedula=%s
     """,(cedula_cli,nombre,direccion,telefono,foto,cedula))
    mysql.connection.commit()
    flash("El contacto fue actualizado satisfactoriamente")
    return redirect(url_for('contactos')) 

#Le envio la cedula 
@app.route('/delete/<int:cedula>')
def delete_cliente(cedula):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM CLIENTES WHERE cedula = {0} ".format(cedula))
    mysql.connection.commit()
    flash("Contacto borrado satisfactoriamente")
    return redirect(url_for('contactos'))


#Productos

@app.route('/productos')
def productos():
    #Realizamos la consulta a la base de datos para enviar los clientes
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM PRODUCTOS')
    data = cur.fetchall()
    #Le envio los clientes al index para que los muestre 
    return render_template('productos.html',productos = data )

@app.route('/add_productos',methods=['POST'])
def add_productos():
    if request.method == 'POST':
        #Nos referimos al name del formulario del index
        codigo = request.form["Codigo"]
        categoria = request.form["Categoria"]
        nombre = request.form["Nombre"]
        precio = request.form["Precio"]
        cantidad = request.form["Cantidad"]
        estado = request.form["Estado"]
        #Establecemos un cursor para la conexion a la bd
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO productos (codigo_producto ,categoria,nombre ,precio,cantidad_bodega,estado) values (%s,%s,%s,%s,%s,%s)", (codigo,categoria,nombre,precio,cantidad,estado))
        #cur.execute("Select * from contacts")
        mysql.connection.commit()
        #Flash permite enviar mensajes entre vistas
        flash("Producto ha sido agregado satisfactoriamente")
        #Redireccionamos a la principal
        return redirect(url_for('productos'))

@app.route('/edit_producto/<int:producto>')
def get_producto(producto):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM PRODUCTOS WHERE codigo_producto = {0} ".format(producto))
    dato = cur.fetchall()
    return render_template('editar_producto.html',producto = dato[0] )

@app.route('/actualizar_producto/<int:producto>',methods=['POST'])
def actualizar_producto(producto):
    cur = mysql.connection.cursor()
    codigo = request.form["Codigo"]
    categoria = request.form["Categoria"]
    nombre = request.form["Nombre"]
    precio = request.form["Precio"]
    cantidad = request.form["Cantidad"]
    estado = request.form["Estado"]
    cur.execute("""
    UPDATE PRODUCTOS SET codigo_producto = %s ,categoria =%s,nombre =%s,precio =%s,cantidad_bodega=%s ,estado=%s
    where codigo_producto=%s
     """,(codigo,categoria,nombre,precio,cantidad,estado,producto))
    mysql.connection.commit()
    flash("El producto fue actualizado satisfactoriamente")
    return redirect(url_for('productos')) 


#Le envio el producto 
@app.route('/delete_producto/<int:producto>')
def delete_producto(producto):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM PRODUCTOS WHERE codigo_producto = {0} ".format(producto))
    mysql.connection.commit()
    flash("Producto borrado satisfactoriamente")
    return redirect(url_for('productos'))

#El debug significa que cada vez que hagamos un cambio se reinicie el server
if __name__== '__main__': 
    app.run(port = 3000 ,debug = True)
    