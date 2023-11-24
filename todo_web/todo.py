
from flask import Flask, render_template, request, redirect, url_for # Importamos la clase Flask

app = Flask(__name__) # Instancia de Flask

# Lista para almacenar tareas. Cada tarea es un diccionario con 'id', 'titulo' y 'descripcion'
tareas = [] 
id_actual = 1 # Variable para asignar un id a cada tarea

@app.route('/') # Indicamos la ruta de la página
def index(): # Definimos la función que se ejecutará cuando se entre a la ruta
    return render_template('index.html', tareas=tareas) # Retornamos el template 'index.html' con las tareas

@app.route('/add', methods=['GET', 'POST']) # Indicamos la ruta de la página
def add(): # Definimos la función que se ejecutará cuando se entre a la ruta
    global id_actual # Indicamos que usaremos la variable global id_actual
    if request.method == 'POST': # Si se hace una petición POST
        titulo = request.form['titulo'] # Obtenemos el título de la tarea
        descripcion = request.form['descripcion'] # Obtenemos la descripción de la tarea
        tareas.append({'id': id_actual, 'titulo': titulo, 'descripcion': descripcion}) # Agregamos la tarea a la lista
        id_actual += 1 # Incrementamos el id actual
        return redirect(url_for('index')) # Redireccionamos a la ruta index
    return render_template('add.html') # Retornamos el template 'add.html'

@app.route('/edit/<int:id>', methods=['GET', 'POST']) # Indicamos la ruta de la página
def edit(id): # Definimos la función que se ejecutará cuando se entre a la ruta
    tarea = next((t for t in tareas if t['id'] == id), None) # Obtenemos la tarea con el id indicado
    if request.method == 'POST': # Si se hace una petición POST
        tarea['titulo'] = request.form['titulo'] # Obtenemos el título de la tarea
        tarea['descripcion'] = request.form['descripcion'] # Obtenemos la descripción de la tarea
        return redirect(url_for('index')) # Redireccionamos a la ruta index
    return render_template('edit.html', tarea=tarea) # Retornamos el template 'edit.html' con la tarea

@app.route('/delete/<int:id>') # Indicamos la ruta de la página
def delete(id): # Definimos la función que se ejecutará cuando se entre a la ruta
    global tareas # Indicamos que usaremos la variable global tareas
    tareas = [t for t in tareas if t['id'] != id] # Eliminamos la tarea con el id indicado
    return redirect(url_for('index')) # Redireccionamos a la ruta index

if __name__ == '__main__': # Iniciamos la aplicación
    app.run(debug=True) # Ejecutamos la aplicación en modo debug
