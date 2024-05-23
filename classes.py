import random
class Jogo():
    def __init__(self):
        self.player = None
        self.computer = None
        self.answer = None

    def decisaoJogo(self):
        self.computer = random.choice(["Pedra", "Papel", "Tesoura"])
        if self.player == "Pedra":
            if self.computer == "Pedra":
                self.answer = "Empate"

            elif self.computer == "Papel":
                self.answer = "Computador"

            elif self.computer == "Tesoura":
                self.answer = "Jogador"

        elif self.player == "Papel":
            self.player = "Papel"
            if self.computer == "Pedra":
                self.answer = "Jogador"

            elif self.computer == "Papel":
                self.answer = "Empate"

            elif self.computer == "Tesoura":
                self.answer = "Computador"

        elif self.player == "Tesoura":
            if self.computer == "Pedra":
                self.answer = "Computador"

            elif self.computer == "Papel":
                self.answer = "Jogador"

            elif self.computer == "Tesoura":
                self.answer = "Empate"

    def resultadoJogo(self):
        if self.answer == 'Empate':
            return (f"O jogador jogou {self.player}. O Computador jogou {self.computer}."
                  f"\nAmbos se Anulam. EMPATE")
        elif self.answer == "Jogador":
            return (f"O jogador jogou {self.player}. O Computador jogou {self.computer}."
                  f"\n{self.player} ganha de {self.computer}."
                  f"\nVitória do {self.answer}.")
        elif self.answer == "Computador":
            return (f"O jogador jogou {self.player}. O Computador jogou {self.computer}."
                  f"\n{self.computer} ganha de {self.player}."
                  f"\nVitória do {self.answer}.")
