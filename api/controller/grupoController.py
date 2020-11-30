import json
from flask import Flask, request, Response, Blueprint, jsonify
from dto import createConceptoDto, createGrupoDto
from app import app
from service.groupService import groupServicie
from service.conceptosService import conceptoServicie

grupos_api = Blueprint('grupos_api', __name__)

service_group = groupServicie()
service_concept = conceptoServicie()


@app.route('/grupo/crear', methods=['POST'])
def crear_grupo():
    datos = request.json
    code = service_group.crear_grupo(datos)
    return Response(json.dumps({'status_code': code}), mimetype='application/json')


@app.route('/concepto/crear', methods=['POST'])
def crear_concepto():
    datos = request.json
    code = service_concept.crear_concepto(datos)
    return Response(json.dumps({'status_code': code}), mimetype='application/json')


@app.route('/grupo/grupo',  methods=['POST'])
def asociar_grupoGrupo():
    datos = request.json
    code = service_group.asociar_grupogrupo(datos)
    return Response(json.dumps({'status_code': code}), mimetype='application/json')


@app.route('/grupo/<string:nombre>', methods=['GET'])
def obtener_grupo(nombre):
    info = service_group.obtener_infoGrupo(nombre)
    if len(info) != 0:
        return Response(json.dumps(info), mimetype='application/json')
    else:
        Response(json.dumps({'status_code': 409}), mimetype='application/json')

