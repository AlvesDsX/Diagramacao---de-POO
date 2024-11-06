from pessoa import PessoaIFRO
from mensagem import Mensagem

class Aluno(PessoaIFRO):
    def __init__(self, nome, matricula, senha, turma, modalidade):
        super().__init__(nome, matricula, senha, turma)
        self.modalidade = modalidade #Atributo adicional da classe, essa  é a modalidade referente a qual o aluno participa.

    @classmethod
    def registrar(cls):
        pessoa = super().registrar()
        turma = input("Digite seu turno: ").strip()
        modalidade = input("Digite sua modalidade: ").strip()
        return cls(pessoa.nome, pessoa.matricula, pessoa._senha, turma, modalidade)

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
        print(f"Conversa agendada com sucesso!\nAssunto: {assuntos}.\n")