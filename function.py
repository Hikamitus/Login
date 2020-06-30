md5 = lambda txt: m((txt.encode())).hexdigest()

clear = lambda: system('clear')

def printl(txt, n = 32, symb = '~'):
 print(symb*32)
 print(txt)
 print(symb*32)

class Conta(object):
 def __init__(self):
  self.__id = None
  self.__login = None
  self.__senha = None
  self.__username = None
  self.__dinheiro = None
  self.__bio = None
  
 def __update(self):
   id = str(self.__id)
   c.execute("SELECT * FROM logins WHERE id = ?", id)
   row = c.fetchone()
   self.__id, self.__login, self.__username, self.__senha, self.__bio, self.__dinheiro = row

 def login(self):
  printl('Sessão de Login.')
  login = md5(str(input('Login: ')))
  senha = md5(str(getpass('Senha: ')))
  c.execute("SELECT * FROM logins WHERE login = ? and senha = ?", (login, senha))
  try:
   row = c.fetchone()
   self.__id, self.__login, self.__username, self.__senha, self.__bio, self.__dinheiro = row
  except:
   print(f"""{'~'*32}
Ouve um Erro ao Logar!
{'~'*32}""")
   sleep(2)
   self.logout()
   return False
  else:
   printl("Logado com Sucesso!")
   sleep(2)
   clear()
   return True


 def logout(self):
  self.__login = None
  self.__senha = None
  self.__username = None
  self.__bio = None


 def register():
  printl('Sessão de Registro.')
  login = md5(input('Novo login: '))
  senha = md5(getpass('Nova senha: '))
  s2 = md5(getpass('Confirme a Senha: '))
  username = input('Username: ')
  bio = input('Biografia(opicional): ')
  if senha != s2:
   print('Senha não são iguais!')
   return
  try:
   c.execute("""
INSERT INTO logins (username, login, senha, bio) VALUES
(?, ?, ?, ?)""", (username, login, senha, bio))
  except:
   printl("O login já está em uso.")
  else:
   conn.commit()
  
  
 def newpass(self):
  if self.__login == None:
   print('• Você precisa estar logado para trocar de senha.')
   return
  printl('Sessão de troca de senha.')
  senha = md5(getpass('Senha Atual: '))
  newsenha = md5(getpass('Nova senha:'))
  ns2 = md5(getpass('Confirme a nova senha: '))
  if senha != self.__senha:
      print()
      print('Sua senha a sua senha atual não é valida.')
      return
  printl('Senha alterada com Sucesso!')
  c.execute("""UPDATE logins
set senha = ?
where login = ? AND senha = ?
""", (newsenha, self.__login, senha))
  conn.commit()
  self.__update()
  
  
 def delete_ac(self):
  if self.__login == None:
   print('Você precisa estar logado!')
   return
  print('~'*32)
  print('Sessão de deletação conta.')
  print('~'*32)
  senha = md5(getpass('Digite sua senha: '))
  confirm = bool(input('Digite True para apagar sua conta: '))
  if not senha == self.__senha:
   print('Senha incorreta!')
   return
  if confirm != True:
   return
  c.execute("""DELETE FROM logins
where login = ? and senha = ?""", (self.__login, self.__senha))
  conn.commit()
  self.logout()
  
 def ficha(self):
  self.__update()
  if not self.__login == None:
   print(f"""{'~'*45}
Minhas Informações
{'~'*45}
ID: {self.__id}
Username: {self.__username}
Dinheiro: ${self.__dinheiro}
Login: {self.__login}
Senha: {self.__senha}
Biografia: {self.__bio}
{'~'*45}""")
   return
  print('• Você não está logado.')

 def mtransfer(self):
  if self.__login == None:
      print('Você precisa estar Logado!')
      sleep(2)
      clear()
      return
  id = input('ID da pessoa para transferir: ')
  c.execute('SELECT username, dinheiro FROM logins \
  	WHERE id = ?', id)
  row = c.fetchone()
  
  if id == self.__id:
   printl('Não se faça de puta.')
  
  print()
  
  if len(row) == 0:
   printl('Não há pessoas vom este ID.')
   return
  
  i = row[0]
  dinheiro = row[1]
  print()
  while True:
   print(f'Você quer transferir para {i}?')
   print('[S/N]')
   d = input('')
   if d.lower() == 'n':
    printl('Saindo...')
    sleep(3)
   elif d.lower() == 's':
    break
   clear()
   return
   
  print()
  
  amount = input('Quantidade para transferir: ')
  
  while True:
   x = input('Tem certeza?[S/N]\n')
   if x.lower() == 's':
    break
   elif x.lower() == 'n':
    print('Ok')
    return
   else:
    continue   
  
  try:
   amount = int(amount)
  except:
   printl('Precisa ser um número!')
   sleep(3)
   return
  if amount > self.__dinheiro:
   printl('Você nem tem esse dinheiro.')
   return
  if amount < 0:
   printl('Não se transfere números negativo.')
   print('Engraçadinho.')
   return
  
  self.__dinheiro -= amount
  c.execute('''UPDATE logins
  	set dinheiro = ?
  	where id = ?''', ((dinheiro + amount), id))

  c.execute('''UPDATE logins
  	set dinheiro = ?
  	where id = ?''', ((self.__dinheiro), self.__id))
  	
  conn.commit()
  self.__update()

import sqlite3 as sql3
from hashlib import md5 as m
from getpass import getpass
from os import system
from time import sleep

#aqui = "./A_Login/"
conn = sql3.connect('database.db')
c = conn.cursor()