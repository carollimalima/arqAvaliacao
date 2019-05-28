import psycopg2
from datetime import datetime

class Funcionario:
    def __init__(self,nome,email,senha,login):
        self._nome = nome
        self._email = email
        self._login = login
        self._senha = senha

    def _get_nome(self):
        return self._nome
    
    def _get_email(self):
        return self._email

    def _get_id(self):
        return self._id
    
    def _get_departamento(self):
        return self._departamento
    
    def _get_login(self):
        return self._login
    
    def _get_senha(self):
        return self._senha
    
    def _get_admin(self):
        return self._admin
    
    def _set_nome(self, nome):
        self._nome = nome
    
    def _set_email(self, email):
        self._email = email
    
    def _set_id(self, id):
        self._id = id
    
    def _set_departamento(self, departamento):
        self._departamento = departamento
    
    def _set_login(self,login):
        self._login = login
    
    def _set_senha(self,senha):
        self._senha = senha
    
    def _set_admin(self,admin):
        self._admin = admin


    nome = property(_get_nome,_set_nome)
    email = property(_get_email,_set_email)
    id = property(_get_id,_set_id)
    departamento = property(_get_departamento,_set_departamento)
    login = property(_get_login,_set_login)
    senha = property(_get_senha,_set_senha)
    admin = property(_get_admin,_set_admin)


class funcionarioDao:

    def __init__(self):
        self._conexao = "dbname=funcionario user=postgres password=postgres host=localhost port=5432"

    def listar(self):
        con = psycopg2.connect(self._conexao)
        v=[]
        with con as c:
            cursor = c.cursor()
            cursor.execute('select * from funcionario')
            for l in cursor.fetchall():
                f = Funcionario(l[1],l[2],l[4],l[6])
                f.admin=l[5]
                f.departamento=int(l[3])
                f.id=l[0]
                v.append(f)
            
        cursor.close()
        return v
    

    
    def salvar(self, f):

        verifica=hasattr(f, 'id')

        if (verifica):
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('UPDATE Funcionario SET nome = %s, email = %s, idDepartamento = %s, login = %s, senha=%s, admin=FALSE WHERE idFuncionario = %s',(f.nome,f.email,f.departamento,f.login,f.senha,f.id))
                con.commit()
                cursor.close()


        else:
                con = psycopg2.connect(self._conexao)
                cursor = con.cursor()
                cursor.execute('insert into Funcionario (nome,email,idDepartamento,login,senha,admin) values (%s,%s,%s,%s,%s,FALSE) RETURNING idFuncionario', (f.nome,f.email,f.departamento,f.login,f.senha))
                cod = (cursor.fetchone())[0]
                con.commit()
                f.id = int(cod)
                cursor.close()



    def buscar(self,cod):
        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Funcionario WHERE idFuncionario = %s',[cod])
        l = cursor.fetchone()
        f = Funcionario(l[1],l[2],l[4],l[6])
        f.admin=l[5]
        f.departamento=int(l[3])
		
        f.id = int(l[0])
        cursor.close()
        return f


    def excluir(self,id):

        con = psycopg2.connect(self._conexao)
        cursor = con.cursor()
        cursor.execute('DELETE FROM Funcionario WHERE idFuncionario = %s',[id])
        con.commit()
        cursor.close()


    def login(self,login,senha):
        try:
            con = psycopg2.connect(self._conexao)
            cursor = con.cursor()
            cursor.execute('SELECT * FROM Funcionario WHERE login = %s and senha= %s ',(login,senha))
            l = cursor.fetchone()
	        #nome,email,idDepartamento,senha,admin,login
            f = Funcionario(l[1],l[2],l[4],l[6])
            f.admin=l[5]
            f.departamento=int(l[3])
            cursor.close()
            return f
        except TypeError:
            return "O login e senha não correspondem às informações em nossos registros. Tente Novamente"



 

#f.departamento=d
#d.funcionario=f

#print(fdao.listar())
#print(f.departamento.id)

f1 = funcionarioDao()
f=Funcionario("oi","emailoi","senha","login")
f.id=6
f.departamento=2
#f1.salvar(f)
#f1.oi()
#f = f1.login("adm","adm")
#print(f)

#f = f1.buscar(1)
#print(f.nome)
#print(f.email)
#print(f.departamento)

#depto nao precisa de gerente



 





