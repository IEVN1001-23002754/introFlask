from flask import Blueprint, jsonify, request
from database import MySQL

maestros_bp = Blueprint 
{
    'maestros',
    __name__,
    url_prefix = '/api/maestros'
}

def fila_a_diccionario(cursos, fila):
    columnas = [columnas[0] for columna in cursos.descroption]
    return dict(zip(columnas, fila))

# GET consultar todos los maestros //////////////////////////////////////////////////////////////////////////////////////////////
maestros_bp.route('', methods=["GET"])
def lista_maestros():
    cursos = None
    try:
        cursos = myqsl.connection.cursor()
        cursor.execute("""  SELECT id_maestro, nombre, apaterno, amaterno, correo   
                            FROM maestros   """)
    
        datos = cursor.fetchall()
        maestros = 
        [
            fila_a_diccionario(cursor, fila)
            for fila in datos
        ]

        return jsonify({
            'maestros': maestros,
            'mensaje': 'Lista de maestros',
            'exito': True
        }), 200

    except Exception:
        return jsonify({
            'mensaje': 'Error al consultar maestros',
            'exito': False
        }),500
    
    finally:
        if cursor is not None:
            cursor.close()

# GET consultar maestro por id //////////////////////////////////////////////////////////////////////////////////////////////