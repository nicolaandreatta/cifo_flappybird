from random import randint, uniform

def binary_mutation(individual, mutationProbab):
    """Binary mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    # decide whether to perform mutation
    if mutationProbab > uniform(0, 1):
        # select the index of the weight to be mutated
        mutationPoint = randint(0, len(individual) - 1)
        # generate random new weight 
        individual[mutationPoint] = round(uniform(individual.valid_set[0], individual.valid_set[1]), 4)
        # update fitness of indiv after mutation
        individual.update_fitness()
    return individual


