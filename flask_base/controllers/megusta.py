from flask import redirect, render_template, request, flash, session
from flask_base import app
from flask_base.models.pensamientos import Pensamiento
from flask_base.models.usuario import Usuario

@app.route("/procesar_megusta/<id>")
def procesar_megusta(id):

    data = {
        'pensamiento_id' : id,
        'usuario_id': session['usuario_id'],
    }

    resultado = Pensamiento.megusta(data)

    if not resultado and resultado != 0:
        flash("error al crear me gusta", "error")
        return redirect("/")

    flash("Me gusta creado correctamente", "success")
    return redirect("/")

@app.route("/procesar_no_megusta/<id>")
def procesar_no_megusta(id):

    data = {
        'pensamiento_id' : id,
        'usuario_id': session['usuario_id'],
    }

    Pensamiento.nomegusta(data)

    flash("Me gusta eliminado correctamente", "success")
    return redirect("/")
