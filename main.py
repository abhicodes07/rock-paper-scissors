# Rock paper scissor game

# Class that stores choices and points
class Participant:
    # Constructor function storing choice, name and points
    def __init__(self, name: str):
        self.name = name
        self.points: int = 0
        self.choice: str = " "

    # Making a choice
    def choose(self):
        self.choice = input(f"{self.name}, Select Between rock, paper and scissor: ")
        print(f"{self.name} selects {self.choice}")
    
    # Converting choices to numeric values 
    def toNumericalChoice(self):
        switcher = {
            "rock" : 0,
            "paper" : 1,
            "scissor" : 2
        }
        return switcher[self.choice]
    
    # Incrementing Points Whenever a certain Participant wins
    def incrementPoint(self):
        self.points += 1

# Game Structure
class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
        self.result = self.compareChoices(p1, p2)
        print(f"Round resulted in a {self.result}")
        if self.result > 0:
            p1.incrementPoint()
        elif self.result < 0:
            p2.incrementPoint()
    
    # Comparing chocies of participant 1 and participant 2 with provided rules
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    
    def getResultAsString(self, result):
        res = {
            0: "Draw",
            1: "Win",
            -1: "Loss"
        }
        return res[result]

# Play Game
class Game:
    def __init__(self):
        self.endGame: bool = False # while this is false game will continue 
        self.participant = Participant(input("Enter First Participant Name: ")) # Object using above class
        self.secondParticipant = Participant(input("Enter The Second Name: ")) # Second object for second participant

    # Once the participant information is filled, the game starts 
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
    
    # Play again?
    def checkEndCondition(self):
        self.answer = input("Continue Game y/n: ")
        if self.answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print(f"Game ended, {self.participant.name} has {self.participant.points} and {self.secondParticipant.name} has {self.secondParticipant.points}")
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        self.resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = f"Winner is {self.participant.name}"
        elif self.participant.points < self.secondParticipant.points:
            resultString = f"Winner is {self.secondParticipant.name}"
        print(resultString)

if __name__ == "__main__":
    game = Game()
    game.start()
