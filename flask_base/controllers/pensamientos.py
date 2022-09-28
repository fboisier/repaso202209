from flask import redirect, render_template, request, flash, session
from flask_base import app
from flask_base.models.pensamientos import Pensamiento
from flask_base.models.usuario import Usuario


@app.route("/")
def index():

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')

    return render_template("index.html", pensamientos=Pensamiento.get_all())
    
@app.route("/usuarios/<id>")
def usuarios(id):

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')

    return render_template("usuario.html", pensamientos=Pensamiento.get_all_by_user(id))

@app.route("/procesar_pensamiento", methods=["POST"])
def procesar_pensamiento():

    if not Pensamiento.validar(request.form):
        return redirect('/')

    data = {
        'texto' : request.form['texto'],
        'usuario_creador': session['usuario_id'],
    }

    resultado = Pensamiento.save(data)

    if not resultado:
        flash("error al crear el pensamiento", "error")
        return redirect("/")

    flash("Pensamiento creado correctamente", "success")
    return redirect("/")


@app.route("/eliminar/pensamiento/<id>")
def eliminar(id):

    Pensamiento.delete(id)
    flash("Pensamiento eliminado", "success")
    return redirect("/")