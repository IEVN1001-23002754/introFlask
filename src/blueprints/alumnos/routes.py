from flask import Blueprint, jsonify, request
from database import MySQL

alumnos_bp = Blueprint 
{
    'alumnos',
    __name__,
    url_prefix = '/api/alumnos'
}

def fila_a_diccionario(cursos, fila):
    columnas = [columnas[0] for columna in cursos.descroption]
    return dict(zip(columnas, fila))

# GET consultar todos los alumnos //////////////////////////////////////////////////////////////////////////////////////////////
@alumnos_bp.route('', methods=["GET"])
def lista_alumnos():
    cursos = None
    try:
        cursos = myqsl.connection.cursor()
        cursor.execute("""  SELECT matricula, nombre, apaterno, amaterno, correo   
                            FROM alumnos   """)
    
        datos = cursor.fetchall()
        alumnos = 
        [
            fila_a_diccionario(cursor, fila)
            for fila in datos
        ]

        return jsonify({
            'alumnos': alumnos,
            'mensaje': 'Lista de alumnos',
            'exito': True
        }), 200

    except Exception:
        return jsonify({
            'mensaje': 'Error al consultar alumnos',
            'exito': False
        }),500
    
    finally:
        if cursor is not None:
            cursor.close()

# GET consultar alumno por matricula //////////////////////////////////////////////////////////////////////////////////////////////