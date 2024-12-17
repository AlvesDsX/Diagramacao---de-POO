from pessoa import PessoaIFRO
from mensagem import Mensagem  

class ProfessorMateria(PessoaIFRO):
    def __init__(self, nome, matricula, senha, turma, disciplina):
        super().__init__(nome, matricula, senha, turma)
        self.disciplina = disciplina

    @property
    def disciplina(self):
        return self._disciplina

    @disciplina.setter
    def disciplina(self, disciplina):
        # O setter pode fazer alguma validação ou transformação se necessário
        self._disciplina = disciplina

    def receberMensagem(self, mensagem):
        print(f"Mensagem recebida de {mensagem.remetente} para {mensagem.destinatario}")
        print(f"Motivo: {mensagem.motivo}")
        print(f"Data do Evento: {mensagem.data}")
        print(f"Campeonato: {mensagem.campeonato.nomecamp}")


    def abdicarFalta(self, aluno, campeonato):
        # Aqui o professor de matéria pode abdicar da falta do aluno
        print(f"Falta negada para o aluno {aluno.nome} por participação no campeonato {campeonato.nomecamp}")


class ProfessorTecnico(PessoaIFRO):
    def __init__(self, nome, matricula, senha, turma, modalidade):
        super().__init__(nome, matricula, senha, turma)
        self.modalidade = modalidade  # A modalidade associada ao professor técnico

    def preencherMensagem(self, professor_materia, aluno, campeonato, data_evento, motivo):
        # Preenche uma instância de Mensagem com os dados necessários
        mensagem = Mensagem(
            remetente=self.nome,
            destinatario=professor_materia.nome,
            campeonato=campeonato,
            data=data_evento,
            motivo=motivo
        )
        # A mensagem preenchida pode ser retornada ou processada conforme necessário
        return mensagem

    def notificarProfessor_Materia(self, professor_materia, aluno, campeonato, data_evento, motivo):
        try:
            mensagem = self.preencherMensagem(professor_materia, aluno, campeonato, data_evento, motivo)
            professor_materia.receberMensagem(mensagem)
            print(f"Notificação enviada para o professor de {professor_materia.disciplina}: {professor_materia.nome}")
        except Exception as e:
            print(f"Erro ao notificar o professor: {e}")
        finally:
            print("Processo de notificação finalizado.")

#PROFESSORTEC e PROFESSORMAT (PESSOAIFRO) OK
