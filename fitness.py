#import flappy_update
#from flappy import play_game

def build_neural_network(weightList):
    
    return 0

def play_flappy_bird(nn):
    #return play_game()
    return 0


def calc_fitness(self, numberOfRepeats = 10):
    avgScore = 0
    weightList = self.representation
    for _ in range(numberOfRepeats): 
        currentScore = 0
        nn = build_neural_network(weightList)
        currentScore = play_flappy_bird(nn)
        avgScore += currentScore
    
    #return avgScore / numberOfRepeats

    # for test purposes 1 - to be deleted once the fitness can be calculated by playing the game
    #dummyFitness = sum(self.representation)

    # for test purposes 2 - to be deleted once the fitness can be calculated by playing the game
    dummyFitness = sum(self.representation[:3]) - sum(self.representation[3:])


    return dummyFitness

    