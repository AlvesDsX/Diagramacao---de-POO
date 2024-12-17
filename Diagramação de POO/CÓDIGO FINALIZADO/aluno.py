from pessoa import PessoaIFRO
from mensagem import Mensagem

class Aluno(PessoaIFRO):
    def __init__(self, nome, matricula, senha, turno, modalidade):
        super().__init__(nome, matricula, senha, turno)
        self.modalidade = modalidade  #Atributo adicional

    @classmethod
    # Adicionar try: (Matricula ser int); (Senha ter verificação de digitos) 
    def registrar(cls):
        try:
            nome=input("Favor, digite o seu nome: ") # Verifica se a entrada contém apenas letras e espaços
            if not all(c.isalpha() or c.isspace() for c in nome):
                raise ValueError("Um erro foi encontrado")
                print(f"Você digitou: {nome}")
        except Exception as erro:
            print(erro)

        try: # VERIFICAÇÃO DE Nº INTEIRO EM MATRICULA
            matricula = int(input("Digite sua matrícula (13 dígitos): "))
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}.')

        try: # VERIFICAÇÃO DE CARACTER DE SENHA
            senha = str(input("Digite sua senha (mínimo 8 caracteres): "))
        except:
            print('Um erro foi encontrado.')
            
        turno = input("Digite seu turno: ")                #Se é de manhã, tarde, noite
        modalidade = input("Digite sua modalidade: ")      #Coleta a modalidade do aluno

        aluno = cls(nome, matricula, senha, turno, modalidade)
        return aluno

    def justificarFalta(self, campeonato, motivo):
        mensagem = Mensagem(self, "Professor", campeonato, motivo)
        mensagem.enviarNotificacao()
        print("Justificativa de falta enviada com sucesso.")
    
        def conversarProf(self):
        assuntos = [
            "1. Justificativa de faltas",
            "2. Pedido de prorrogação de prazo para entrega de trabalhos",
            "3. Outros"
        ]
        print("Lista de assuntos para tratar com o professor:")
        for assunto in assuntos:
            print(assunto)

        escolha = input("Escolha o número do assunto sobre o qual você gostaria conversar (1-3): ").strip()
            
        if escolha == "1":
            assunto = "Justificativa de faltas"
        elif escolha == "2":
            assunto = "Pedido de prorrogação de prazo para entrega de trabalhos"
        elif escolha == "3":
            assunto = input("Por favor, especifique o assunto: ").strip()
        else:
            print("A opção escolhida é inválida! Tente novamente.")
            return
        print(f"Conversa agendada com sucesso!\nAssunto: {assunto}.\n")

#ALUNO(PESSOAIFRO) OK
