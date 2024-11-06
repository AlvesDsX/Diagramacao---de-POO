class Mensagem:
  def __init__(self, remetente , destinatario , campeonato, data , motivo):
      self.remetente = remetente                #Aluno que irá justificar a sua falta     '------> Professor Técnico(by: Vava)'
      self.destinatario = destinatario          #A quem irá se dirigir, o qual irá receber a notifcação por parte do remetente
      self.campeonato = campeonato              #Campeonato que irá intervir no horário de aula
      self.data = data                          #Data do evento
      self.motivo = motivo                      #Motivo da mensagem

  def enviarNotificacao(self):
      print(f"Notificação de {self.remetente.nome} para {self.destinatario}:")
      print(f"Campeonato: {self.campeonato.nome}")
      if self.data:
        print(f"Data do evento: {self.data}")
      print(f"Motivo: {self.motivo}")

  def preencherMensagem(self, motivo):
     self._motivo = motivo
     print("Mensagem exlarecida com o devido motivo:", self.motivo)

  def compararHorarios(self, horarios_aula):
     if self.data in horarios_aula:
        print("Conflito detectado entre horários de aula e evento.")
        return True
     print("Nenhum conflito de horário detectado.")
     return False