import os

from flask import flash
from flask_base.config.mysqlconnection import connectToMySQL
from flask_base.models.modelo_base import ModeloBase
from flask_base.utils.regex import REGEX_CORREO_VALIDO

class Pensamiento(ModeloBase):

    modelo = 'pensamientos'
    campos = ['texto','usuario_creador']

    def __init__(self, data):
        self.id = data['id']
        self.texto = data['texto']
        self.usuario_creador = data['usuario_creador']
        self.nombre_usuario = data['nombre_usuario']
        self.numero_likes = data['numero_likes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def update(cls,data):
        query = """UPDATE pensamientos 
                        SET texto = %(texto)s,
                        updated_at=NOW() 
                    WHERE id = %(id)s"""
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def validar(cls, data):
        is_valid = True
        is_valid = cls.validar_largo(data, 'texto', 5)
        return is_valid

    @classmethod
    def get_all(cls):
        query = f"""SELECT p.*, u.nombre as nombre_usuario, count(m.pensamiento_id) as numero_likes FROM pensamientos p 
                    JOIN usuarios u ON u.id = p.usuario_creador LEFT JOIN megusta m ON m.pensamiento_id = p.id
                    group by p.id;"""
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def get_all_by_user(cls, usuario):
        query = f"""SELECT p.*, u.nombre as nombre_usuario, count(m.pensamiento_id) as numero_likes FROM pensamientos p 
                    JOIN usuarios u ON u.id = p.usuario_creador LEFT JOIN megusta m ON m.pensamiento_id = p.id WHERE p.usuario_creador = %(usuario)s
                    group by p.id;"""
        data = {
            'usuario': usuario
        }
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @classmethod
    def megusta(cls, data):
        query = """
                INSERT INTO megusta (usuario_id, pensamiento_id)
                VALUES (%(usuario_id)s, %(pensamiento_id)s);
                """

        print("PRINT DE PRUEBA:", data, query)
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def nomegusta(cls, data):
        query = """
                DELETE FROM megusta WHERE usuario_id =  %(usuario_id)s and pensamiento_id = %(pensamiento_id)s;
                """
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado
