from flask import Flask, request
from flask_cors import CORS

def salvar_contato(pessoa:dict):
    #print(type(pessoa),'\t',pessoa,'\t')
    try:
        with open(f'db/base.txt') as file:
            arquivo = file.read()
        
        print("antes: ",arquivo)
        
        arquivo += f"\nnome: {pessoa['nome']}\nemail: {pessoa['email']}\nmensagem: {pessoa['mensagem']}\n"
        
        print("depois: ", arquivo)
        
        with open(f'db/base.txt', 'w') as file:
            file.writelines(arquivo)
        
        return True
    
    except Exception as _:
        return False


app = Flask(__name__)
CORS(app)

@app.route('/contato', methods=['POST'])
def criar_usuario():
    novo_contato = request.json
    stts = salvar_contato(novo_contato)
    return '', 200 if stts else 500


if __name__ == '__main__':
    app.run(debug=True)


'''
Para consumir a API no front

const dados = { nome: nome_preenchido, email: email_preenchido, mensagem: msg_preenchida}

fetch('http://127.0.0.1:5000/contato',{method: "POST", headers:{"Content-Type":"application/json",},body: JSON.stringify(dados),}).then((response) => response.json()).then((data) => console.log(data)).catch((error) => console.error("Erro:
",error));
'''