import sqlite3

class BancoDeDados: 
	"""Classe que representa o banco de dados (database) da aplicacao"""
	def __init__(self, nome='banco.dp' ):#inicializa o banco de dados 
		self.nome, self.conexao = nome, None
		print ("DANIIII")
	def conecta(self):
		"""Conecta passando o nome do arquivo"""
		self.conexao = sqlite3.connect(self.nome)

	def desconecta(self):
		"""DEsconecta do banco de dados"""
		try:
			self.conexao.close()
		except AttributeError:
			pass

	def criar_tabelas(self):
		"""Cria as tabelas do banco de dados"""
		try:
			cursor = self.conexao.cursor()

			cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes(
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
					nome TEXT NOT NULL,
					senha VARCHAR(20) NOT NULL,
					cpf VARCHAR(11) UNIQUE NOT NULL,
					email TEXT NOT NULL
			);
			""")
		except AttributeError:
			print ("Faca a conexao do banco antes de criar as tabelas")


	def inserir_cliente(self, nome, senha, cpf, email):
		"""Insere cliente no banco"""
		try:
			cursor = self.conexao.cursor()

			try:
				cursor.execute("""
					INSERT INTO clientes (nome, senha, cpf, email) VALUES (?,?,?,?)
				""", (nome, senha, cpf, email))
			except sqlite3.IntegrityError:
				print('O cpf %s já existe!' % cpf)

			self.conexao.commit()

		except AttributeError:
			print('Faça a conexão do banco antes de inserir clientes.')

	def buscar_cliente(self,cpf):
		"""Busca um cliente pelo cpf"""
		try:
			cursor = self.conexao.cursor()

			#obtem todos os dados 
			cursor.execute("SELECT *FROM clientes WHERE cpf=?", [(cpf)])
			
			cliente = cursor.fetchone()
			
			if cliente:
				return True
			return False
						
		except AttributeError:
			print('Faça a conexão do banco antes de buscar clientes.')

			'''
			for linha in cursor.fetchall():#retorna o resultado do select
			#O retorn eh uma lista
				if linha[2] == cpf:
					print ('Cliente %s encontrado.' %linha[1])
					break
				else:
					print ('Cliente nao encontrad0')
			'''

		except AttributeError:
			print ('Faca a conexao do banco antes de buscar cliente.')

	def remover_cliente(self, cpf):
		"""Remove um cliente pelo cpf """
		try:
			cursor = self.conexao.cursor()

			#obtem todos os dados 
			cursor.execute("""SELECT *FROM clientes;""")

			cursor = self.conexao.cursor()
			pessoa  = self.buscar_cliente(cpf)	

			cursor.execute("""DELETE FROM clientes WHERE cpf = %d""" % int(cpf))
			
			self.conexao.commit()
		except AttributeError:
			print ('Faca a conexao do banco antes de buscar cliente.')


	"""Se achar o cliente com esse email return true, senao return false"""
	def buscar_email(self, email):

		try:
			cursor = self.conexao.cursor()

			#obtem todos os dados 
			cursor.execute("""SELECT *FROM clientes;""")

			for linha in cursor.fetchall():#retorna o resultado do select
			#O retorn eh uma lista
				if linha[3] == email:
					return True
				else:
					return False
		except AttributeError:
			print ('Faca a conexao do banco antes de buscar cliente.')


	def login(self,username, senha):
		"""Para ver se o usuario pode logar o nao n sistema"""
		try:
			cursor = self.conexao.cursor()
			sql = 'SELECT *FROM clientes WHERE nome=? and senha=?'
			cliente = cursor.execute(sql, [username, senha]).fetchone()
			if cliente:
				return True
			return False
			
		except AttributeError:
			print ('Faca a conexao do banco antes de buscar cliente.')
