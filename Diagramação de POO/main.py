from CLASSES import *

# Lista para armazenar todos os usuários registrados.
usuarios = []

usuarios = []
def registrar_usuario():
    tipo = input("\n------------------------\nDigite o tipo de usuário\n------------------------\n\naluno\n\nprofessor_tecnico\n\nprofessor_materia\n\n------------------------\nDigite o tipo de usuário\n------------------------\n\nEscolha sua opção: ").strip().lower()
    print("\n-----------------\nRegistrar usuário\n-----------------\n")
    nome = input("Digite o nome: ").strip()
    matricula = input("Digite a matrícula: ").strip()
    senha = input("Digite a senha: ").strip()


    if any(usuario.matricula == matricula for usuario in usuarios):
        print("\nErro: Matrícula já cadastrada.")
        return

    if tipo == 'aluno':
        turma = input("Digite o turno: ").strip()
        usuario = Aluno(nome, matricula, senha, turma)
    elif tipo == 'professor_tecnico':
        modalidade = input("Digite a modalidade: ").strip()
        aulas = input("Digite as aulas: ").strip()
        usuario = ProfessorTecnico(nome, matricula, senha, modalidade, aulas)
    elif tipo == 'professor_materia':
        aulas = input("Digite as aulas: ").strip()
        usuario = ProfessorMateria(nome, matricula, senha, aulas)
    else:
        print("Tipo de usuário inválido.")
        return

    usuarios.append(usuario)
    print("\n-----------------\nRegistrar usuário\n-----------------")
    print("\nUsuário registrado com sucesso.")

def fazer_login():
  print("\n-----------------\n   Fazer login   \n-----------------")
  matricula = input("\nDigite a matrícula: ").strip()
  senha = input("Digite a senha: ").strip()
  

  for usuario in usuarios:
      if usuario.matricula == matricula and usuario.verificar_senha(senha):
          print("\nLogin bem-sucedido.\n")
          return usuario
  print("\nLogin falhou: matrícula ou senha incorretos.")
  print("\n-----------------\n   Fazer login   \n-----------------")
  return None

def menu():
  while True:
      print("\n-------------------------\nSistema de Jogos Externos\n-------------------------\n")
      print("1 - Registrar novo usuário")
      print("2 - Fazer login")
      print("3 - Sair")
      opcao = input("\nEscolha uma opção: ").strip()

      if opcao == '1':
          registrar_usuario()
      elif opcao == '2':
          usuario_logado = fazer_login()
          if usuario_logado:
              print(f"Bem-vindo, {usuario_logado.nome}!")
      elif opcao == '3':
          print("\nSaindo do sistema...")
          break
      else:
          print("Opção inválida. Tente novamente.")

# Executando o menu
menu()