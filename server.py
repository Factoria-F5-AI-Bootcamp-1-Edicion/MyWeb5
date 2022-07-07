from flask import Flask, render_template
import sqlite3

# Carpeta raiz
app = Flask(__name__, template_folder='home')

# Conexion a base de datos
bd = sqlite3.connect("db.sqlite")
cursor = bd.cursor()


# consulta a base de datos
cursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=cursor.fetchall()

for i in range(len(variosProductos)):
	print('''
        {
            "PRODUCTOS": "''' + str(variosProductos[i][0]) + '''",
            "PRECIO": ''' + str(variosProductos[i][1]) + ''' 
        },         
    ''')

#update datos
#bd.commit()

#Cerramos conexion a la base de datos
bd.close()

# Rutas del servidor web
@app.route('/')
def home():
    return render_template("/index.html")

@app.route('/api')
def api():
    for i in range(len(variosProductos)):
	    lee = '''
        {
            "PRODUCTOS": "''' + str(variosProductos[i][0]) + '''",
            "PRECIO": ''' + str(variosProductos[i][1]) + ''' 
        },         
        '''
    return str(lee)
print("Servidor levantado !!! ")
app.run(debug=True,port=5000)
