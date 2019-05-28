import psycopg2
from datetime import datetime
from funcionario import *
#from dao import *

class Departamento:
    def __init__(self,nome):
        self._nome = nome
        self._vinculo = []

    def _get_nome(self):
        return self._nome
    
    def _get_vinculo(self):
        return self._vinculo
    
    def _get_dtAtualizacao(self):
        return self._dtAtualizacao
    
    def _get_funcionario(self):
        return self._funcionario
    
    def _get_id(self):
        return self._id
    
    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_id(self, id):
        self._id = id
    
    def _set_dtAtualizacao(self, data):
        self._dtAtualizacao = data
    
    def _set_funcionario(self, funcionario):
        self._funcionario = funcionario

    def _set_vinculo(self, f):
        try:
            self._vinculo.append(f)
        except:
            self._vinculo = []
            self._vinculo.append(f)
    

    nome = property(_get_nome,_set_nome)
    funcionario = property(_get_funcionario,_set_funcionario)
    id = property(_get_id,_set_id)
    dtAtualizacao = property(_get_dtAtualizacao,_set_dtAtualizacao)
    vinculo = property(_set_vinculo,_get_vinculo)









class departamentoDao():

    def __init__(self):self._conexao = "dbname=funcionario user=postgres password=postgres host=localhost port=5432"

    def listar(self):
        con = psycopg2.connect(self._conexao)
        v=[]
        with con as c:
            cursor = c.cursor()
            cursor.execute('select * from departamento')
            for l in cursor.fetchall():
                d = Departamento(l[1])
                d.dtAtualizacao=l[3]
                d.funcionario=l[2]
                d.id=int(l[0])
                v.append(d)
            
        cursor.close()
        return v
    

    
    def salvar(self, d):

        verifica=hasattr(d, 'id')

        if (verifica):
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('UPDATE departamento SET nome = %s, idGerente = %s,dataatualizacao=NOW() WHERE idDepartamento = %s',(d.nome,d.funcionario,int(d.id)))
                con.commit()
                cursor.close()


        else:
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('insert into departamento (nome) values (%s) RETURNING idDepartamento', [d.nome])
                cod = (cursor.fetchone())[0]
                con.commit()
                d.id = cod
                cursor.close()



    def buscar(self,cod):
        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM departamento WHERE idDepartamento = %s',[cod])
        l = cursor.fetchone()
        f = funcionarioDao().buscar(l[2])
        d = Departamento(l[1])
        d.funcionario=l[2]
        d.dtAtualizacao=l[3]
		
        cursor.close()
        return d


    def excluir(self,id):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('DELETE FROM departamento WHERE idDepartamento = %s',[id])
        con.commit()
        cursor.close()


ddao=departamentoDao()
#print(ddao.listar())


 
