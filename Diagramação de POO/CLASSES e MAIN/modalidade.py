from typing import List
from aluno import Aluno

class Modalidade():
    def __init__(self, modalidade: str):
        self.modalidade = modalidade
        self.time = List[Aluno] = []

    def adicionarAluno(self, aluno: Aluno):
        if aluno not in self.time:
            self.time.append(aluno)
            print(f'Aluno {aluno.nome} foi adicionado ao time de {self.modalidade}.')

    def visualizarTime(self):
        for aluno in self.time:
            print(f"Aluno: {aluno.nome}, Matrícula: {aluno.matricula}")
        return self.time