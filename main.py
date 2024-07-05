# Rock paper scissor game

# Phase - input
# Actor - Participant --> Performer
# Behaviour - Chooses Symbol 
# Data - Symbol saved as choice on Participant

# Symbol saved as choice on Participants, Phase: Input
class Participant:
    def __init__(self: None) -> str:
        self.points: int = 0
        self.choice: str = " "

class GameRound:
    pass

class Game:
    def __init__(self: bool) -> bool:
        self.endGame: bool = False
        self.Participant = Participant() # Object using above class
        self.secondParticipant = Participant() # Second object for second participant

