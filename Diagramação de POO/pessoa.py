from abc import ABC, abstractmethod

class PessoaIFRO(ABC):
  def __init__(self, nome, matricula, senha, turma):
      self.nome = nome              #será verifcado com o setter
      self.matricula = matricula    #será verifcado com o setter
      self.senha = senha  
      self.turma = turma          #será verifcado com o setter

  @property
  def nome(self):
      return self._nome

  @nome.setter
  def nome(self, nome):
      if len(nome.strip()) > 0: #Verificação do nome, remove os espaços e analisa o comprimento do nome e quant. de strings
        self._nome = nome
      else:
          raise ValueError("\033[3mO nome não pode está vazio.\033[0m")
 
  @property
  def matricula(self):
      return self._matricula

  @matricula.setter
  def matricula(self, matricula):
      if matricula.isdigit() and len(matricula) == 13: #Verificando se a matrícula contém N° IR inteiros > 0 e se o seu comprimento é igual a 13.
        self._matricula = matricula
      else:
          raise ValueError("\033[3mA matrícula deve conter 13 dígitos*\033[0m")

  @property
  def senha(self):
      return self._senha

  @senha.setter
  def senha(self, senha):
      if len(senha) >= 8 and any(c.isdigit() for c in senha):
        self.senha = senha
      else:
          raise ValueError("\033[3mA senha deve conter pelo menos 8 caracteres com ao menos um número*\033[0m")
      
  def verificar_senha(self, senha):
      return self._senha == senha
 
  @property
  def turma(self):
     return self._turma
  

  @classmethod
  def registrar(cls):
     nome = input("Favor, digite o seu nome: ").strip()
     matricula = input("Digite sua matrícula (13 dígitos): ").strip()
     senha = input("Digite sua senha (mínimo 8 caracteres): ").strip()

     return cls(nome, matricula, senha)