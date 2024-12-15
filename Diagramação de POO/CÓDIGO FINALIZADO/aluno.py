from pessoa import PessoaIFRO
from mensagem import Mensagem

class Aluno(PessoaIFRO):
    def __init__(self, nome, matricula, senha, turno, modalidade):
        super().__init__(nome, matricula, senha, turno)
        self.modalidade = modalidade  #Atributo adicional
    # ALTERAÇÂO TESTE1 15.12.2024 13:15
    # ALTERAÇÃO TESTE2 15.12.2024 13:17
    # ALTERAÇÃO TESTE3 15.12.2024 13:22
    @classmethod
    def registrar(cls):
        nome = input("Favor, digite o seu nome: ")
        matricula = input("Digite sua matrícula (13 dígitos): ")
        senha = input("Digite sua senha (mínimo 8 caracteres): ")
        turno = input("Digite seu turno: ")                #Se é de manhã, tarde, noite
        modalidade = input("Digite sua modalidade: ")      #Coleta a modalidade do aluno

        #Cria e retorna uma instância da classe Aluno
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