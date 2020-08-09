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
        mysql.connection.commit()
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
#Inactivar producto /inactivar
#Le envio el producto 
@app.route('/inactivar/<int:producto>')
def inactivar(producto):
    cur = mysql.connection.cursor()
    cur.execute("update PRODUCTOS set estado = %s WHERE codigo_producto =%s ",('INACTIVAR',producto))
    mysql.connection.commit()
    flash("Producto ha sido inhabilitado satisfactoriamente")
    return redirect(url_for('productos'))
@app.route('/delete_producto/<int:factura>')
def delete_producto(producto):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM PRODUCTOS WHERE codigo_producto = {0} ".format(producto))
    mysql.connection.commit()
    flash("Producto borrado satisfactoriamente")
    return redirect(url_for('productos'))

#Facturas

@app.route('/facturas')
def facturas():
    #Realizamos la consulta a la base de datos para enviar las facturas
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM FACTURAS')
    data = cur.fetchall()
    #Le envio los clientes al index para que los muestre 
    return render_template('facturas.html',facturas = data )


@app.route('/add_facturas',methods=['POST'])
def add_facturas():
    if request.method == 'POST':
        #Nos referimos al name del formulario del index
        codigo = request.form["Codigo"]
        print(codigo)
        cedula = request.form["Cedula"]
        productos = request.form["Productos"].split(',')
        cantidad = request.form["Cantidad"].split(',')
        fecha = request.form["Fecha"]
        metodo = request.form["Metodo"]
        print(productos)
        print(cantidad)
        #Valido que los productos digitados sea igual a la cantidad de productos 
        if len(cantidad)==len(productos):
            #Establecemos un cursor para la conexion a la bd
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO FACTURAS (codigo_factura,cedula_cliente ,fecha_compra, metodo_pago ) values (%s,%s,%s,%s)", (codigo,cedula,fecha,metodo))
            for i in range(len(cantidad)):
                cur.execute(" INSERT INTO FACTURA_PRODUCTO (codigo_factura,producto,cantidad_producto) values(%s,%s,%s)",(codigo,productos[i],cantidad[i]))
            #cur.execute("INSERT INTO FACTURAS (codigo_factura  ,cedula_cliente ,producto  ,cantidad_prod ,fecha_compra ,metodo_pago ) values (%s,%s,%s,%s,%s,%s)", (codigo,cedula,producto,cantidad,fecha,metodo))
            mysql.connection.commit()
            flash("La factura ha sido agregada satisfactoriamente")
            #Redireccionamos a la principal
        else:
            flash("No se ha ingresado la factura porque la cantidad de productos es diferente a los productos")
        return redirect(url_for('facturas'))

@app.route('/edit_facturas/<int:factura>')
def get_facturas(factura):
    cur = mysql.connection.cursor()
    #Hacemos esto para sacar los productos
    cur.execute(""" SELECT b.producto FROM FACTURAS a ,FACTURA_PRODUCTO b WHERE 
    a.codigo_factura=b.codigo_factura and a.codigo_factura = {0} order by a.codigo_factura
    """.format(factura))
    dato_productos = cur.fetchall()
    print(dato_productos[0][0])
    productos=""
    for i in dato_productos:
        for j in i:
            productos+="{},".format(j)
    #Eliminamos el ultimo caracter de la cadena
    productos=productos[:len(productos)-1]
    
    #Sacamos la cantidad de los productos
    cur.execute(""" SELECT b.cantidad_producto FROM FACTURAS a ,FACTURA_PRODUCTO b WHERE 
    a.codigo_factura=b.codigo_factura and a.codigo_factura = {0} order by a.codigo_factura
    """.format(factura))
    #Guardamos todos los registros para luego recorrerlos uno a uno y enviarlo a editar_factura todo junto 
    dato_cantidad_producto = cur.fetchall()
    #print(dato_productos[0][0])
    cantidad_producto=""
    for i in dato_cantidad_producto:
        for j in i:
            cantidad_producto+="{},".format(j)
            #productos=''.join(j)
    #Eliminamos el ultimo caracter de la cadena
    cantidad_producto=cantidad_producto[:len(cantidad_producto)-1]
    print("Cantidad productso",cantidad_producto)
    
    #Sacamos el resto de los campos
    cur.execute("""SELECT a.codigo_factura,a.cedula_cliente,a.fecha_compra,a.metodo_pago,       b.cantidad_producto
     FROM FACTURAS a ,FACTURA_PRODUCTO b 
    WHERE a.codigo_factura=b.codigo_factura and a.codigo_factura = {0} """.format(factura,productos))
    dato = cur.fetchall()
    print(dato[0])

    return render_template('editar_factura.html',factura = dato[0] , productos = productos ,cantidad = cantidad_producto)



@app.route('/actualizar_facturas/<int:factura>',methods=['POST'])
def actualizar_facturas(factura):
    cur = mysql.connection.cursor()
    codigo = request.form["Codigo"]
    cedula = request.form["Cedula"]
    producto = request.form["Producto"]
    #Dividimos los productos para hacer el update
    producto=producto.split(',')
    #print(producto)
    #Dividimos la cantidad
    cantidad = request.form["Cantidad"]
    cantidad=cantidad.split(',')
    #print(cantidad)
    fecha = request.form["Fecha"]
    metodo = request.form["Metodo"]
    #No se hace update los borramos y lo volvemos a llenar con los nuevos valores 
    cur.execute(""" DELETE FROM FACTURA_PRODUCTO where codigo_factura ={0} """.format(factura))
    cur.execute(""" DELETE FROM FACTURAS where codigo_factura = {0} """.format(factura))
    cur.execute(""" INSERT INTO FACTURAS (codigo_factura,cedula_cliente,fecha_compra,metodo_pago) 
    values (%s,%s,%s,%s)
    """,(codigo,cedula,fecha,metodo))
    for i in range(len(cantidad)):
        cur.execute(""" INSERT INTO FACTURA_PRODUCTO (codigo_factura,producto,cantidad_producto)
        values (%s,%s,%s)
        """,(codigo,producto[i],cantidad[i]))
    mysql.connection.commit()
    flash("La factura fue actualizado satisfactoriamente")
    '''
    cur.execute("""
    UPDATE FACTURAS SET codigo_factura = %s ,cedula_cliente =%s,producto =%s,cantidad_prod =%s,fecha_compra=%s ,metodo_pago=%s
    where codigo_factura=%s
     """,(codigo,cedula,producto,cantidad,fecha,metodo,factura))
    mysql.connection.commit()
    flash("La factura fue actualizado satisfactoriamente")
    '''
    return redirect(url_for('facturas')) 

#Le envio la factura 
@app.route('/delete_facturas/<int:factura>')
def delete_factura(factura):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM FACTURA_PRODUCTO WHERE codigo_factura = {0} ".format(factura))
    cur.execute("DELETE FROM FACTURAS WHERE codigo_factura = {0} ".format(factura))
    mysql.connection.commit()
    flash("La factura borrado satisfactoriamente")
    return redirect(url_for('facturas'))
#Reporte clientes , facturas y producto
@app.route('/reporte')
def reporte():
    cur = mysql.connection.cursor()
    cur.execute("""  
    SELECT d.cedula,d.nombre,a.codigo_factura,sum(b.cantidad_producto*c.precio) as valor
    FROM FACTURAS a, FACTURA_PRODUCTO b ,PRODUCTOS c ,CLIENTES d
    where a.codigo_factura=b.codigo_factura and b.producto=c.codigo_producto and a.cedula_cliente=d.cedula 
    group by a.codigo_factura,d.cedula order by valor
    """)
    data = cur.fetchall()
    return render_template('reporte.html',reportes = data )
#El debug significa que cada vez que hagamos un cambio se reinicie el server
if __name__== '__main__': 
    app.run(port = 3000 ,debug = True)
    