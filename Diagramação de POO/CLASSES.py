from abc import ABC, abstractmethod
class PessoaIFRO(ABC):
  def __init__(self, nome, matricula, senha):
      self.nome = nome
      self.matricula = matricula
      self.senha = senha

  def _str_(self):
      return f"{self.nome} (Matrícula: {self.matricula})"

  def verificar_senha(self, senha):
      return self.senha == senha

  def getnome(self):
      return self.nome

  def setnome(self):
      self.nome = nome

  def getmatricula(self):
      return self.matricula

  def setmatricula(self):
      self.matricula = matricula    

  def getsenha(self):
      return self.senha

  def setsenha(self):
      self.senha = senha




class Aluno(PessoaIFRO):
  def __init__(self, nome, matricula, senha, turma):
      super().__init__(nome, matricula, senha)
      self.turma = turma
  def getturma(self):
      return self.turma

  def setturma(self):
      self.turma = turma


class ProfessorTecnico(PessoaIFRO):
  def __init__(self, nome, matricula, senha, modalidade, aulas):
      super().__init__(nome, matricula, senha)
      self.modalidade = modalidade
      self.aulas = aulas

  def getmodalidade(self):
      return self.modalidade

  def setmodalidade(self):
      self.modalidade = modalidade

  def getaulas(self):
      return self.aulas

  def setaulas(self):
      self.aulas = aulas


class ProfessorMateria(PessoaIFRO):
  def __init__(self, nome, matricula, senha, aulas):
      super().__init__(nome, matricula, senha)
      self.aulas = aulas

  def getaulas(self):
      return self.aulas

  def setaulas(self):
      self.aulas = aulas



