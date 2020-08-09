Colecciones creadas:
	-clientes
	-productoss
	-proveedores
	-productos_vendidos
	-vendedor

Explicacion de las colecciones creadas:
Se crearon las diferentes colecciones ya que si se tenia toda la informacion en una coleccion ,si a un cliente se le añadia un nuevo campo se debia editar cada 
documento asimismo pasaria con los proveedores e venededores.
	
Explicacion de cada coleccion:
	1. Clientes: Esta coleccion tiene los campos de cliente,nombre,cedula,ciudad . Con el fin de si se desea agregar el barrio del cliente pueda ser añadido sin 
	problema ademas si el cliente cambia de ciudad es solo cambiarlo en esta coleccion o otro tipo de campo.
	2. Productos: Esta coleccion tiene una lista de productos que dentro contiene un diccionario por cada producto , ya que cada producto pertenece a una tienda
		 en especifico, no se le añadio el precio al producto ya que si el precio cambia pueden tener problemas en el sistema por ende se le añadio este 
		campo a productos_vendidos.
	3. Proveedores: Esta coleccion contiene proveedor, ciudad y el codigo del proveedor. Con el fin de si se añade un nuevo campo solo seria en esta coleccion.
	4. productos_vendidos: Esta coleccion contiene cada producto que fue vendido al cliente seria asi como una factura que se realizo en un dia , por otra parte
	se creo venta que contiene un diccionario por cada producto que fue vendido dentro de este contienen varias llaves que son el codigo del producto,la cantidad
	de productos vendidos,si el producto en mencion fue devuelto(el valor de esta llave solo tiene dos valores el cual es 'S' para Si y 'N' para No ) 
	y el precio con el que se compro ese producto en ese dia, por otro lado se tiene el codigo de la tienda, la fecha de la venta, codigo del cliente y por ultimo
	el codigo del vendedor.
	5.vendedor : Esta coleccion almacena los datos del vendedor como lo es el codigo,nombre,ciudad,cedula.

Los siguientes .json contienen la informacion mas descriptiva
	- clientes.json
	- productos.json
	- proveedores.json
	- productos_vendidos.json
	- vendedor.json

Los siguientes documentos contienen los insert que se realizaron para las pruebas (Se recomienda abrirlos en sublime):

	- insertmany_clientes
	- insertmany_productos
	- insertmany_productosvendidos
	- insertmany_proveedores
	- insertmany_vendedor
	
Ver datos registrados (El pretty es para que se vea cada documento mas ordenado y legible):

db.clientes.find().pretty()
db.productoss.find().pretty()
db.proveedores.find().pretty()
db.productos_vendidos.find().pretty()
db.vendedor.find().pretty()