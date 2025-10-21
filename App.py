from flask import Flask, request, jsonify
from models.Usuario import Usuario
from models.Instituicoes import InstituicaoEnsino
from helpers.data import getInstituicoesEnsino

app = Flask(__name__)

usuario = Usuario(1, "João", "00011122233", "2025-10-09")
usuarios = [usuario]

instituicoesEnsino = getInstituicoesEnsino()


@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200


# Usuarios.

@app.get("/usuarios")
def getUsuarios():
    return jsonify([u.to_json() 
                    for u in usuarios]), 200


@app.get("/usuarios/<int:id>")
def getUsuariosById(id: int):
    usuario = next((u for u in usuarios if u.id == id), None)
    if usuario:
        return jsonify(usuario.to_json()), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404


@app.post("/usuarios")
def setUsuarios():
    data = request.get_json()
    usuario = Usuario(len(usuarios) + 1,
                      data["nome"], data["cpf"], data["data_nascimento"])
    usuarios.append(usuario)
    return jsonify(usuario.to_json()), 201


@app.put("/usuarios/<int:id>")
def updateUsuario(id: int):
    data = request.get_json_()
    usuario = Usuario(id,
                      data["nome"], data["cpf"], data["data_nascimento"])
    usuarios[id] = usuario
    return jsonify(usuario.to_json()), 200


@app.delete("/usuarios/<int:id>")
def deleteUsuario(id: int):
    usuario = usuarios.pop(id)
    return jsonify({"mensagem": f"Usuário {usuario.nome} removido"}), 200


# Instituições.

@app.get("/instituicoesensino")
def getInstituicoesEnsinoRoute():
    instituicoesEnsinoJson = [ie.to_json()
                              for ie in instituicoesEnsino]
    return jsonify(instituicoesEnsinoJson), 200


@app.get("/instituicoesensino/<int:id>")
def getInstituicoesEnsinoById(id: int):
    ieDict = instituicoesEnsino[id].to_json()
    return jsonify(ieDict), 200


@app.post("/instituicoesensino")
def setInstituicao():
    data = request.get_json()
    instituicao = InstituicaoEnsino(
        data["codigo"],
        data["nome"],
        data["co_uf"],
        data["co_municipio"],
        data["qt_mat_bas"],
        data["qt_mat_prof"],
        data["qt_mat_eja"],
        data["qt_mat_esp"]
    )
    instituicoesEnsino.append(instituicao)
    return jsonify(instituicao.to_json()), 201


@app.put("/instituicoesensino/<int:id>")
def updateInstituicao(id: int):
    data = request.get_json()
    instituicao = InstituicaoEnsino(
        data["codigo"],
        data["nome"],
        data["co_uf"],
        data["co_municipio"],
        data["qt_mat_bas"],
        data["qt_mat_prof"],
        data["qt_mat_eja"],
        data["qt_mat_esp"]
    )
    instituicoesEnsino[id] = instituicao
    return jsonify(instituicao.to_json()), 200


@app.delete("/instituicoesensino/<int:id>")
def deleteInstituicao(id: int):
    instituicao = instituicoesEnsino.pop(id)
    return jsonify({"mensagem": f"Instituição {instituicao.nome} removida"}), 200
