from flask import session

import hashlib

hashlib.md5("senha".encode()).hexdigest()

def main():
    app.secret_key = 'minha chave'
    app.env = 'development'
    app.run(debug=True, port=2001)


from flask import redirect

session['var']='oi'
app.run()

app.secret_key = 'minha chave' (vai no main, tem q fazer isso antes de dar app.run)

def  __str__(self):
        return "Nome do Funcionário: {}, Id do Funcionário: {}, Email: {}, Departamento: {} ".format(self._nome,self._codigo,self._email,self._departamento)


#lista de funcionarios no depto
#objeto de depto no funcionario
#inserir admin no formulario (criar um admin padrao com TRUE ja)
#listar projetos > ver detalhes do projeto > (lista de funcionarios do projeto)
#> check box com os funcionarios, selecionar os funcionarios que quer vincular
#> enviar

#> ver detalhes > desvincular/adicionar
#> tratar erros pra ver se ja tem repetido....

def vincularFunc(self,projeto):
        conn = self.conectar()
        cur = conn.cursor()
        try:
            cur.execute('SELECT codFuncionario FROM funcionarioprojeto WHERE codProjeto = %s', [projeto.obterCodigo()])
            vinculados = []
            for linha in cur.fetchall():
                codfuncionario = linha[0]
                vinculados.append(codfuncionario)
            cadastrados = []
            for linha in projeto.obterFuncionarios():
                cadastrados.append(linha[0])
            aux = []
            for linha in cadastrados:
                if linha not in vinculados:
                    aux.append(linha)
            for linha in aux:
                cur.execute('INSERT INTO funcionarioprojeto (codfuncionario,codprojeto) values (%s,%s)',[int(linha),int(projeto.obterCodigo())])
                conn.commit()
            cur.close()
            return "Vinculo concluido!"
        except:
            return 'Deu erro!'

"""
@app.before_first
def before_first_request(): 
    print('ndsjkd')

@app.before_request
def before_request():
    print(request.path)
    print('jdklajskd')


#executa smp qndo da uma exceção
@app.after_request
def after_request(response):
    print('jdklsa')
    return response
"""