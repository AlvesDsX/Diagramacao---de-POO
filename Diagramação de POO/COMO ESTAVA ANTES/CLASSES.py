
class Aluno(PessoaIFRO):
  def __init__(self, nome, matricula, senha, turma):
      super().__init__(nome, matricula, senha)
      self._turma = turma

  @property
  def turma(self):
      return self._turma
  
  @turma.setter
  def turma(self, turma):
      self._turma = turma

#Classe intermediária
class Professor(PessoaIFRO):
    def __init__(self, nome, matricula, senha, departamento, especialização, carga_horaria_semanal):
        super().__init__(nome, matricula, senha)
        self._departamento = departamento  #Atributo comum a todos os professores.
        self._especializacao = especialização
        self._carga_horaria_semanal = carga_horaria_semanal #Até aqui.

    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento

    @property
    def especializacao(self):
        return self._especializacao
    
    @especializacao.setter
    def especializacao(self, especializacao):
        self._especializacao = especializacao

    @property
    def carga_horaria_semanal(self):
        return self._carga_horaria_semanal
    
    @carga_horaria_semanal.setter
    def carga_horaria_semanal(self, carga_horaria_semanal):
        self._carga_horaria_semanal = carga_horaria_semanal

class ProfessorTecnico(Professor):
  def __init__(self, nome, matricula, senha, departamento,especialização, carga_horaria_semanal): #Adicionar um atributo específico
      super().__init__(nome, matricula, senha, departamento, especialização, carga_horaria_semanal) #Reutilizando atributo da classe intermediária "professor".
      #implementar ele aqui


class ProfessorMateria(Professor):
  def __init__(self, nome, matricula, senha, departamento, especialização, carga_horaria_semanal): #Adicionar um atributo específico
      super().__init__(nome, matricula, senha, departamento, especialização, carga_horaria_semanal) #Reutilizando novamente.
      #implementar ele aqui