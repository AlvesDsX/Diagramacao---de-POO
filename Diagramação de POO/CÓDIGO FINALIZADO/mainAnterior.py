'''from aluno import Aluno
from professor import ProfessorTecnico, ProfessorMateria
from campeonato import Campeonato
from jogo import Jogo

#Lista para armazenar todos os usuários registrados.
usuarios = []

#Funções para personalizar linhas e textos
def titulo(txt):
    print("-"*30)
    print(txt)
    print("-"*30)   

def tipoUser(tipotxt):
    print(tipotxt)

usuarios = []
#Primeiro, coletar a info. dos usuários com as devidas validações, pois elas serão usadas durante o restante do programa.
def coletarInformacoesUsers():
    while True:
        nome = input("Digite seu nome: ").strip()
        if len(nome) == 0:
            print("\033[3mO campo obrigatório está vazio*\033[0m")

        #Verificando se a matrícula possui exatamente 13 dígitos.
        while True:
            matricula = input("Digite sua matrícula (13 dígitos): ").strip()
            if not matricula.isdigit():
                print("\033[3mA matrícula deve conter apenas números*\033[0m")
            elif len(matricula) != 13:
                print("\033[3mA matrícula deve conter exatamente 13 dígitos*\033[0m")
            else:
                break
        #Verificando se a senha possui ao menos 8 dígitos.
        while True:
            senha = input("\nDigite sua senha (mínimo 8 caracteres, ao menos um número.): ").strip()
            if len(senha) < 8 or not any(char.isdigit() for char in senha):
                print("\033[3mA senha deve conter pelo menos 8 caracteres com ao menos um número*\033[0m")
            else:
                break

        return{"Nome": nome, "Matrícula": matricula, "Senha": senha}

#Escolher o tipo de usuário do sistema.
def escolherTipoUser():
    opcoes = {
        '1': "Aluno",
        '2': "Professor Técnico",
        '3': "Professor Matéria"
    }

    while True:
        titulo("   Categorias de Usuários:")
        for opcao, descricao in opcoes.items():
            print(f"{opcao}. {descricao}")

        escolha = input("\nPor favor, insira seu tipo de usuário: ").strip().lower()

#Verificação de número ou nome
        if escolha in opcoes: #caso seja números
            return opcoes[escolha]
        elif escolha.capitalize() in opcoes.values():
            return escolha.capitalize()
        
        print("\n\033[3mTipo de usuário inválido, tente novamente.\033[0m\n")

#Fazer o registro desse usuário com base na escolha realizada no "escolherTipoUser()".
# Função para registrar o usuário
def registrarUser():
    escolha = escolherTipoUser()
    titulo("    Registro de Usuário:")
    tipoUser(f"Opção \033[1m{escolha}\033[0m escolhido com sucesso!\n")

    while True:
        try:
            # Coletar informações do usuário
            infoUsers = coletarInformacoesUsers()
            matricula = infoUsers["Matrícula"]

            # Verificação da matrícula.
            if any(usuario.matricula == matricula for usuario in usuarios):
                print("\nErro: Matrícula já cadastrada.")
                return

            if escolha == 'Aluno':
                turma = input("Digite seu turno: ").strip()
                modalidade = input("Digite sua modalidade esportiva: ").strip()  # Solicitar modalidade
                usuario = Aluno(infoUsers["Nome"], matricula, infoUsers["Senha"], turma, modalidade)  # Passar modalidade
            elif escolha == 'Professor Técnico':
                aulas = input("Digite as aulas: ").strip()
                departamento = input("Digite seu departamento (Matemática, Filosofia ou Educ. Financeira): ").strip()
                usuario = ProfessorTecnico(infoUsers["Nome"], matricula, infoUsers["Senha"], departamento, aulas)
            elif escolha == 'Professor Matéria':
                aulas = input("Digite as aulas: ").strip()
                usuario = ProfessorMateria(infoUsers["Nome"], matricula, infoUsers["Senha"], aulas)
            else:
                print("\n\033[3mTipo de usuário inválido.\033[0m")
                return

            # Adiciona o usuário à lista de usuários
            usuarios.append(usuario)
            titulo("Registro de Usuário:")
            print("\n\033[3mUsuário registrado com sucesso!\033[0m")
            break
        except ValueError as erro:
            print(f"Erro correspondente: {erro}")  # Exibindo a mensagem correspondente ao erro com base nas validações

def fazer_login():
  titulo("       Realizar login:")
  matricula = input("\nDigite sua matrícula: ").strip()
  senha = input("Digite sua senha: ").strip()
  
  for usuario in usuarios:
      if usuario.matricula == matricula and usuario.verificar_senha(senha):
          print("\n\033[1m\033[3mLogin perfeitamente efetuado.\033[0m")
          return usuario
  print("\n\033[3mFalha no login: Senha ou matrícula incorretas.\033[0m")
  return None

def menuUsuario(usuarioLogado):
    #campeonato e jogo instanciados
    campeonato_futebol = Campeonato("Campeonato de Futebol", "Futebol", "01/12/2024", "15/12/2024")
    jogo_futebol = Jogo("03/12/2024", "manhã", "Ginásio Claúdio Coutinho")

    while True:
            titulo(f"Seja muito bem-vindo, {usuarioLogado.nome}!")
            print("1. Inscrever-se em campeonato")
            print("2. Participar de jogo")
            print("3. Sair")
            opcao = input("\nEscolha uma opção: ").strip()
            if opcao == '1':
                #Inscrevendo o aluno no campeonato
                aluno = Aluno(usuarioLogado.nome, usuarioLogado.matricula, usuarioLogado.senha, "Vespertino", "Futsal")
                campeonato_futebol.inscreverAluno(aluno)
            elif opcao == '2':
                #Adicionando o aluno no jogo
                aluno = Aluno(usuarioLogado.nome, usuarioLogado.matricula, usuarioLogado.senha, "Vespertino", "Futsal")
                jogo_futebol.adicionarJogador(aluno)      # Josmith será adicionado ao jogo
                jogo_futebol.mostrarJogadores()           # Exibindo os jogadores do jogo
            elif opcao == '3':
                print("\nSaindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente.")


def menu():
  while True:
      titulo("  Sistema de Jogos Externos")
      print("1. Registrar novo usuário")
      print("2. Fazer login")
      print("3. Sair do sistema")
      opcao = input("\nEscolha uma opção: ").strip()

      if opcao == '1':
          registrarUser()
      elif opcao == '2':
          usuario_logado = fazer_login()
          if usuario_logado:
              print(f"\033[1m\033[3mBem-vindo, {usuario_logado.nome}!\033[0m")
      elif opcao == '3':
          print("\nSaindo do sistema...")
          break
      else:
          print("Opção inválida. Tente novamente.")

#Instâncias de Aluno para simular a validação de inscrição do aluno
campeonato_futebol = Campeonato("Campeonato de Futebol", "Futebol", "01/12/2024", "15/12/2024")
aluno_josmith = Aluno("Herwing Josmith", "1234567890123", "senha123", "Vespertino", "Futsal")
aluna_marta = Aluno("Marta da Silva", "9876543210987", "senha456", "Matutino", "Vôlei")


#Tentando inscrever os alunos
campeonato_futebol.inscreverAluno(aluno_josmith)  #Josmtih irá  ser inscrito
campeonato_futebol.inscreverAluno(aluna_marta)    #Marta não irá ser inscrita


#Criando um jogo e adicionando um aluno como jogador
jogo_futebol = Jogo("03/12/2024", "manhã", "Campo Principal")
jogo_futebol.adicionarJogador(aluno_josmith)      #Adicionar Josmith ao jogo
jogo_futebol.mostrarJogadores()                   #Exibir os jogadores do jogo

#Executando o menu
menu()'''          #Em virtude do tempo., não conseguimos conciliar o código com as classes do sistema. :D