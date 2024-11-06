class Aulas:
    def __init__(self, horarios_semanal):
        self.horarios_semanal = horarios_semanal    #Diminuindo a redundância em apenas 1 só atributo, pois antes repetia: seg, ter..sex.
    
    def obterHorarioDia(self, dia: str):
        return self.horarios_semanal(dia.capitalize(), "Nenhuma aula encontrada durante esse dia.")
        
    def verificarConflitoEvento(self, jogo):              #Verificando se há conflito entre o horário do jogo e o horário de aulas.
        for dia, horario in self.horarios_semanal.items():
            if jogo.data == dia:
                print(f"Conflito detectado: {dia} às {horario}")
                return True
        return False

class Turma:
    def __init__(self, curso, turno, alunos, serie, horarios):
        self.curso = curso
        self.turno = turno                                               
        self.alunos = []
        self.serie = serie
        self.horario: Aulas
       
    def listarAlunos(self):
        if self.alunos:
            for aluno in self.alunos:
                print(f"Nome: {aluno.nome}")

    def verificarConflitoComJogo(self, jogo):
        return self.horario.verificarConflitoComEvento(jogo)
    
#AULAS E TURMA OK