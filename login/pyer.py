from datetime import datetime
import psycopg2

class Funcionario:
    def __init__(self,nome,email):

        self._nome = nome
        self._email = email

    def _get_nome(self):
        return self._nome
    
    def _get_email(self):
        return self._email

    def _get_id(self):
        return self._id
    
    def _get_departamento(self):
        return self._departamento
    
    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_email(self, email):
        self._email = email
    
    def _set_id(self, id):
        self._email = id
    
    def _set_departamento(self, departamento):
        self._departamento = departamento

    nome = property(_get_nome,_set_nome)
    email = property(_get_email,_set_email)
    id = property(_get_id,_set_id)
    departamento = property(_get_departamento,_set_departamento)

"""
class Departamento:
    def __init__(self,nome):

        self._nome = nome


    def _get_nome(self):
        return self._nome
    
    def _get_funcionario(self):
        return self._funcionario
    
    def _get_id(self):
        return self._id
    
    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_id(self, id):
        self._id = id
    
    def _set_funcionario(self, funcionario):
        self._funcionario = funcionario
    

    nome = property(_get_nome,_set_nome)
    funcionario = property(_get_funcionario,_set_funcionario)
    id = property(_get_id,_set_id)



class Projeto:
    
    def __init__(self,nome,dataPrevista):
        self._nome = nome
        self._dataPrevista = format(datetime.strptime(str(dataPrevista),"%d/%m/%Y"),"%d/%m/%Y")
    
    def _get_nome(self):
        return self._nome
    
    def _get_dataPrevista(self):
        return self._dataPrevista
    
    def _get_id(self):
        return self._id

    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_id(self, id):
        self._id = id
    
    def _set_dataPrevista(self, dataPrevista):
        self._dataPrevista = format(datetime.strptime(str(dataPrevista),"%d/%m/%Y"),"%d/%m/%Y")
    

    nome = property(_get_nome,_set_nome)
    dataPrevista = property(_get_dataPrevista,_set_dataPrevista)
    id = property(_get_id,_set_id)


"""

class funcionarioDao:

    def __init__(self):
        self._conexao = "dbname=funcionario user=postgres password=postgres host=localhost port=5432"

    def listar(self):
        con = psycopg2.connect(self._conexao)
        v=[]
        with con as c:
            cursor = c.cursor()
            cursor.execute('select * from funcionario')
            for linha in cursor.fetchall():
                f = Funcionario(linha[1],linha[2])
                f.id=int(linha[0])
                v.append(f)
            
        cursor.close()
        return v





#f.departamento=d
#d.funcionario=f

#print(fdao.listar())
#print(f.departamento.id)
"""
fdao = funcionarioDao().listar()
for f in fdao:
    print(f.nome)
"""

#depto nao precisa de gerente



 





