from charles import Population, Individual
from fitness import get_fitness
from selection import fps, tournament
from crossover import single_point_co
from mutation import binary_mutation

print('Hello World')
print('ipdfvunőd')
print('ifubsf')

# Monkey Patching
Individual.get_fitness = get_fitness

# define population params
popSize = 20
problemType = 'max'
solSize = 5
validSet = [0, 1]
replacement = True

# initialize population
pop = Population(size = popSize, optim = problemType, sol_size = solSize, valid_set = validSet, replacement = replacement)

print(pop)

# define evolution params
numberOfGenerations = 100
selectionAlg = tournament
crossoverAlg = single_point_co
crossoverProbab = 0.7
mutationAlg = binary_mutation
mutationProbab = 0.2
elitism = False

# do evolution
#pop.evolve(gens = numberOfGenerations, select = selectionAlg, crossover = crossoverAlg,
#            mutate = mutationAlg, co_p = crossoverProbab, mu_p = mutationProbab, elitism = elitism)
