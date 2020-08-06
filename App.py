from flask import Flask
#Esta seria la clase que vamos a configurar
app = Flask(__name__)
#Decorador cada vez que un usuario entre a la ruta principal le responda algo
@app.route('/')
def Index():
    return 'Bienvenido'
#El debug significa que cada vez que hagamos un cambio se reinicie el server
if __name__== '__main__': 
    app.run(port = 3000 ,debug = True)
    