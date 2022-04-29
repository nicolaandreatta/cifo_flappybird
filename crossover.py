from random import randint, uniform
from charles import Individual

def single_point_co(p1, p2, crossoverProbab):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    #print(p1)
    #print(p2)
    # decide whether to perform crossover
    if crossoverProbab > uniform(0, 1):
        # select the index where to cut the dna s 
        co_point = randint(1, len(p1)-2)
        #print('copoint:', co_point)
        newRepr1 = p1.representation[:co_point] + p2.representation[co_point:]
        #print('newRepr1:', newRepr1)
        offspring1 = Individual(representation = newRepr1, size=len(p1), valid_set=p1.valid_set)
        newRepr2 = p2.representation[:co_point] + p1.representation[co_point:]
        #print('newRepr2:', newRepr2)
        offspring2 = Individual(representation = newRepr2, size=len(p1), valid_set=p1.valid_set)
        #print('o1', offspring1)
        #print('o2', offspring2)
    else: 
        offspring1, offspring2 = p1, p2

    return offspring1, offspring2
