class Campeonato:
    def __init__(self, nome, modalidade, dataInicial, dataFinal):
        self.nomecamp = nome                    #Nome do campeonato
        self.modalidade = modalidade            #Modalidade referente ao campeonato
        self.dataInicial = dataInicial          #Data inicial do campeonato
        self.dataFinal = dataFinal              #Data final do campeonato
        self.jogos = []                         #Lista de jogos do campeonato

    def inscreverAluno(self, aluno):
        if aluno.modalidade == self.modalidade:
            print(f'Aluno "{aluno.nome}" está inscrito no campeonato "{self.nomecamp}".')
        else:
            print(f'O aluno não pode ser inscrito no campeonato "{self.nomecamp}", pois a modalidade não é correspondente com o campeonato.')
            return
        
    def adicionarJogo(self, jogo):
        self.jogos.append(jogo)
        print(f'Jogo adicionado ao campeonato "{self.nomecamp}".')

    def consultarJogo(self):
        if self.jogos:
            for jogo in self.jogos:
                print(f'Consulta: Jogo marcado para {jogo.data} no turno da {jogo.turno} no local "{jogo.local}".')
        else:
            print("Nenhum jogo registrado para este campeonato.")