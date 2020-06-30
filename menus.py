from function import *
	
eu = Conta()

def menu1():
 clear()
 printl('Menu!'.center(32), 32, '-')
 print('[0] Logar')
 print('[1] Registrar')
 print('[2] Sair')
 print('-'*32)
 x = input('E: ')
 clear()
 if x == '0':
  if eu.login() is False:
   menu1()
  menulog()
 elif x == '1':
  Conta.register()
  x = input('Enter para continuar.')
  clear()
  menu1()
 elif x == '2':
  print('Deslogando...')
  sleep(3)
  exit()
 else:
  printl('Opção Inválida!')
  sleep(2)
  menu1()

def menulog():
 clear()
 printl('Configurações de Conta!')
 print('[0] Transferir Dinheiro')
 print('[1] Ver informações')
 print('[2] Trocar Senha')
 print('[3] Deletar Conta')
 print('[4] Deslogar')
 x = input('E: ')
 
 
 if x == '0':
  clear()
  eu.mtransfer()
  printl('Pressione Enter para voltar.')
  x = getpass('')
  menulog()
 elif x == '1':
  eu.ficha()
  printl('Pressione Enter para voltar.')
  x = getpass('')
  menulog()
 elif x == '2':
  eu.newpass()
  printl('Pressione Enter para voltar.')
  x = getpass('')
  menulog()
 elif x == '3':
  eu.delete_ac()
  printl('Pressione Enter para voltar.')
  x = getpass('')
  menu1()
 elif x == '4':
  eu.logout()
  menu1()
 else:
  printl('Opção Inválida!')
  speep(2)
  menulog()
