from abc import ABC, abstractmethod

class PessoaIFRO(ABC):
  def __init__(self, nome, matricula, senha, turma):
      self.nome = nome              #será verificado com o setter
      self.matricula = matricula    #será verificado com o setter
      self.senha = senha            #será verificado com o setter
      self.turma = turma            #será verificado com o setter

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
        self._senha = senha
      else:
          raise ValueError("\033[3mA senha deve conter pelo menos 8 caracteres com ao menos um número*\033[0m")
      
  @property
  def turma(self):
     return self._turma
  
  @turma.setter
  def turma(self, turma):
     if len(turma.strip()) > 0: #Verificando se o que for escrito for > 0 caracteres para validar que o campo não fique vazio.
        self._turma = turma
     else: 
        raise ValueError('O campo "Turma" não pode estar vazio.')
      
  def verificar_senha(self, senha):
      return self._senha == senha
  
  @classmethod
  def registrar(cls):
     nome = input("Favor, digite o seu nome: ").strip()
     matricula = input("Digite sua matrícula (13 dígitos): ").strip()
     senha = input("Digite sua senha (mínimo 8 caracteres): ").strip()
     turma = input("Digite sua turma: ").strip()

     return cls(nome, matricula, senha, turma)
  
#PESSOAIFRO(ABC) OK
