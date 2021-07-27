from flask import Flask
from flask import send_from_directory
from flask import render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from datetime import datetime
import os


app = Flask(__name__)

mysql = MySQL()

CARPETA = os.path.join('uploads')
app.config['CARPETA'] = CARPETA

app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-04.cleardb.com'
app.config['MYSQL_DATABASE_USER'] = 'ba69f91b5bbe8a'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ec3a01d0'
app.config['MYSQL_DATABASE_Db'] = 'heroku_8a079106560b065'
mysql.init_app(app)


@app.route('/')
def index():
    '''Visualización del index.html'''
    return render_template('servicios/index.html')


@app.route('/nails')
def nails():
    '''Se muestran en la página todos aquellos servicios cargados en la base de datos, cuyo spa sea "uñas"'''
    sql = "SELECT * FROM `heroku_8a079106560b065` . `servicios` WHERE spa = 'uñas';"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    servicios_nails = cursor.fetchall()
    conn.commit()
    return render_template('servicios/nails.html', servicios_nails=servicios_nails)


@app.route('/browsandlashes')
def browsandlashes():
    '''Se muestran en la página todos aquellos servicios cargados en la base de datos, cuyo spa sea "cejas" o "pestañas'''
    sql = "SELECT * FROM `heroku_8a079106560b065` . `servicios` WHERE spa = 'cejas' OR spa = 'pestañas';"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    servicios_browsandlashes = cursor.fetchall()
    conn.commit()
    return render_template('servicios/browsandlashes.html', servicios_browsandlashes=servicios_browsandlashes)


@app.route('/turnos')
def turnos():
    '''Muestra el formulario de turnos'''
    return render_template('servicios/turnos.html')


@app.route('/faq')
def faq():
    '''Muestra la seccion de preguntas frecuentes'''
    return render_template('servicios/faq.html')


@app.route('/gestion', methods=['POST', 'GET'])
def gestion():
    '''Desde acá se listan los servicios actuales y se pueden crear y editar servicios'''
    sql = "SELECT * FROM `heroku_8a079106560b065` . `servicios`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    servicios = cursor.fetchall()
    conn.commit()
    return render_template('servicios/gestion.html', servicios=servicios)


@app.route('/create')
def create():
    '''Desde acá se ingresan servicios nuevos'''
    return render_template('servicios/create.html')


@app.route('/store',  methods=['POST'])
def storage():
    '''Guarda los datos cargados en el formulario cuando se crea un servicio nuevo'''
    _spa = request.form['txtSpa']
    _nombre = request.form['txtNombre']
    _tiempo = request.form['txtTiempo']
    _duracion = request.form['txtDuracion']
    _precio = request.form['txtPrecio']
    _foto = request.files['txtFoto']

    if _nombre == '' or _nombre.isspace() == True:
        return redirect('/create')
    if _tiempo == '' or _tiempo.isspace() == True:
        return redirect('/create')
    if len(_precio) == 0 or _precio.isdigit() == False:
        return redirect('/create')
    if _foto.filename == '':
        return redirect('/create')

    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

     # Si hay una foto cargada, se le modifica el nombre
    if _foto.filename != '':
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save("uploads/" + nuevoNombreFoto)

        sql = "INSERT INTO `heroku_8a079106560b065`.`servicios` (`id`,`spa`,`nombre`,`proceso`,`duracion`,`precio`,`foto`) VALUES (NULL,%s,%s,%s,%s,%s,%s)"
        datos = (_spa, _nombre, _tiempo, _duracion, _precio, nuevoNombreFoto)
        conn = mysql.connect()
        cursor = conn.cursor()
        conn.commit()

    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/gestion')


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''En esta página el administrador se loguea para poder ingresar al sistema de gestión'''
    '''Funciona con username='admin' y password=admin' '''

    if request.method == 'POST':
        _username = request.form['username']
        _password = request.form['password']
        datos = (_username, _password)
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM `heroku_8a079106560b065`.`usuarios` WHERE `username` =%s AND `password`=%s;"
        cursor.execute(sql, datos)
        users = cursor.fetchall()
        username = users[0][1]
        # Si trae una coincidencia, redirecciona a Gestión, sino queda en login hastq ue ingrese username y password correctos
        if len(users) == 1:
            return redirect(url_for('gestion'))
        else:
            return redirect(url_for('login'))

    return render_template('servicios/login.html')


@app.route('/destroy/<identificador>')
def destroy(identificador):
    '''Esta ruta se encarga de eliminar servicios'''
    datos = identificador
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "DELETE FROM `heroku_8a079106560b065` . `servicios` WHERE `id` =%s;"

    cursor.execute("SELECT foto FROM `heroku_8a079106560b065` . `servicios` WHERE id=%s", datos)
    fila = cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))

    cursor.execute(sql, datos)
    conn.commit()
    return redirect(url_for('gestion'))


@app.route('/edit/<int:id>')
def edit(id):
    sql = "SELECT * FROM `heroku_8a079106560b065` . `servicios` WHERE `id` =%s;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    servicios = cursor.fetchall()
    conn.commit()
    return render_template('servicios/edit.html', servicios=servicios)


@app.route('/update', methods=['POST'])
def update():

    _spa = request.form['txtSpa']
    _nombre = request.form['txtNombre']
    _tiempo = request.form['txtTiempo']
    _duracion = request.form['txtDuracion']
    _precio = request.form['txtPrecio']
    _foto = request.files['txtFoto']
    id = request.form['txtID']

    sql = "UPDATE `heroku_8a079106560b065`.`servicios` SET `spa`=%s, `nombre`=%s, `proceso`=%s, `duracion`=%s, `precio`=%s WHERE `id`=%s;"
    datos = (_spa, _nombre, _tiempo, _duracion, _precio, id)

    conn = mysql.connect()
    cursor = conn.cursor()

    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if _foto.filename != '':
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save("uploads/" + nuevoNombreFoto)

        cursor.execute("SELECT foto FROM `heroku_8a079106560b065` . `servicios` WHERE id=%s", datos)
        fila = cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
        cursor.execute("UPDATE `heroku_8a079106560b065`.`servicios` SET `foto`=%s WHERE id=%s;", (nuevoNombreFoto, id))
        conn.commit()

    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/gestion')


@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    '''Se muestra en el html la foto asociada al servicio'''
    return send_from_directory(app.config['CARPETA'], nombreFoto)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
