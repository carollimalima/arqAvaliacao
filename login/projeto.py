import psycopg2
from datetime import datetime
from funcionario import Funcionario
from Dao import *

class Projeto:
    
    def __init__(self,nome,dataPrevista):
        self._nome = nome
        self._dataPrevista = format(datetime.strptime(str(dataPrevista),"%d/%m/%Y"),"%d/%m/%Y")
        self._funcionarios= []

    def _get_nome(self):
        return self._nome
    
    def _get_dataPrevista(self):
        return self._dataPrevista
    
    def _get_id(self):
        return self._id
    
    def _get_funcionarios(self):
        return self._funcionarios

    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_id(self, id):
        self._id = id
    
    def _set_dataPrevista(self, data):
        self._dataPrevista = datetime.strptime(data,'%d/%m/%Y')
    
    def _set_funcionarios(self, f):
        try:
            self._funcionarios.append(f)
        except:
            self._funcionarios = []
            self._funcionarios.append(f)
    

    nome = property(_get_nome,_set_nome)
    dataPrevista = property(_get_dataPrevista,_set_dataPrevista)
    id = property(_get_id,_set_id)
    funcionarios = property(_get_funcionarios,_set_funcionarios)





class projetoDao(dao):

    def __init__(self):
        #self._conexao = "dbname=funcionario user=postgres password=postgres host=localhost port=5432"
        super().__init__()

    def listar(self):
        con = psycopg2.connect(self._conexao)
        v=[]
        with con as c:
            cursor = c.cursor()
            cursor.execute('select * from projeto')
            for l in cursor.fetchall():
                dt=l[2].strftime("%d/%m/%Y")
                p = Projeto(l[1],dt)
                p.id=int(l[0])
                v.append(p)
            
        cursor.close()
        return v
    

    
    def salvar(self, p):

        verifica=hasattr(p, 'id')

        if (verifica):
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('UPDATE projeto SET nome = %s, dtPrevista = %s WHERE idProjeto = %s',(p.nome,p.dataPrevista,int(p.id)))
                con.commit()
                cursor.close()


        else:
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('insert into projeto (nome,dtPrevista) values (%s,%s) RETURNING idProjeto', (p.nome,p.dataPrevista))
                cod = (cursor.fetchone())[0]
                con.commit()
                p.id = cod
                cursor.close()



    def buscar(self,cod):
        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM projeto WHERE idProjeto = %s',[cod])
        l = cursor.fetchone()
        dt=l[2].strftime("%d/%m/%Y")
        p = Projeto(l[1],dt)
        p.id=int(l[0])
        cursor.close()
        return p


    def excluir(self,id):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('DELETE FROM projeto WHERE idProjeto = %s',[id])
        con.commit()
        cursor.close()
    

    def buscar_vinculo(self,cod):
        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        with con as c:
            cursor = c.cursor()
            cursor.execute('select f.idFuncionario,f.nome,f.email,f.login,f.admin,p.idProjeto,p.nome,p.dtPrevista from funcionario f right outer join FuncProj fp on f.idFuncionario=fp.idFuncionarioFK left outer join projeto p on fp.idProjetoFK=p.idProjeto WHERE p.idProjeto = %s',[cod])
            #cursor.execute('select f.idFuncionario,f.nome,f.email,f.login,f.admin from funcionario f right outer join FuncProj fp on f.idFuncionario=fp.idFuncionarioFK')
            ln=cursor.fetchall()
            p = projetoDao().buscar(cod)
                
            for l in ln:
                f=Funcionario(l[1],l[2],'a',l[3])
                f.id=int(l[0])
                p.funcionarios=f

           
        con.commit()
        return p



    #def vincula_func(self,)




p=Projeto("projeto 3","20/06/2019")
f=Funcionario("kkk","emailoi","senha","login")
#pdao=projetoDao()
#p.funcionarios=f
#print(p.funcionarios[0].nome)
#print(pdao.listar())