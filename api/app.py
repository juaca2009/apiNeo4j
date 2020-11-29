import json
from flask import Flask, request, Response
from api.dto import createConceptoDto, createGrupoDto


app = Flask(__name__)

@app.route('/grupo/crear', methods=['POST'])
def crear_grupo():
    datos = request.json
    gdto = createGrupoDto(datos["nombre"], datos["descripcion"])


@app.route('/concepto/crear', methods=['POST'])
def crear_concepto():
    datos = request.json
    cdto = createConceptoDto(datos["nombre"], datos["descripcion"])


@app.route('/grupoConcepto',  methods=['POST'])
def asociar_grupoConcepto():
    datos = request.json


@app.route('/grupoGrupo',  methods=['POST'])
def asociar_grupoGrupo():
    datos = request.json






if __name__ == '__main__':
    app.run(debug=True)