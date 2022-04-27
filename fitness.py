

def build_neural_network(weightList):
    
    return 0

def play_flappy_bird(nn):

    return 0

def get_fitness(self, numberOfRepeats = 10):
    avgScore = 0
    weightList = self.representation
    for repeat in range(numberOfRepeats): 
        currentScore = 0
        nn = build_neural_network(weightList)
        currentScore = play_flappy_bird(nn)
        avgScore += currentScore
    
    return avgScore / numberOfRepeats