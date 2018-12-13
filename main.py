from database import BancoDeDados

#testa se executou pelo terminal se é o modulo principal
#para executar as func desse modulo elas tem que ser escrita explicitamente 
if __name__ == "__main__": 
	banco = BancoDeDados()
	banco.conecta()
	banco.criar_tabelas()
	banco.inserir_cliente('Marcos','python', '11111111111','mcastrosouza@live.com')
	banco.inserir_cliente('Thomas', 'java','22222222222', 'thomas@gmail.com')
	print (banco.login('Marcos', 'python'))
	#banco.buscar_email('mcastrosouza@live.com')
	#banco.remover_cliente('22222222222')
	banco.buscar_cliente('22222222222')
	banco.desconecta()



