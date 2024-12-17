
class Jogo:
    def __init__ (self, data, turno, local):
        self.data = data
        self.turno = turno
        self.local = local
        self.jogadores = []

    def adicionarJogador(self, aluno):
        if aluno.modalidade == "Futsal" and self.turno == "Vespertino":  #Simulando
            if aluno not in self.jogadores:
                self.jogadores.append(aluno)
                print(f'Jogador "{aluno.nome}" adicionado ao jogo com sucesso!')
            else:
                print(f'O aluno "{aluno.nome}" já está inscrito neste jogo.')
        else:
            print(f'O aluno "{aluno.nome}" não pode ser adicionado ao jogo, pois a modalidade ou turno não são compatíveis.')
    
    def mostrarJogadores(self):
        if self.jogadores:
            for jogador in self.jogadores:
                print(f"Jogador: {jogador.nome}")
        else:
            print("Não há registro de nenhum jogador inscrito no jogo.")

#JOGO OK
