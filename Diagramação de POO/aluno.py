from pessoa import PessoaIFRO


class Aluno(PessoaIFRO):
    def __init__(self, nome, matricula, senha, turma):
        super().__init__(nome, matricula, senha)
        self.turma = turma


    @classmethod
    def registrar(cls):
        return super().registrar()