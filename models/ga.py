import random
import statistics
from utils.moves import flip
from utils.colision import is_coliding
from deap import creator, base, tools, algorithms


def ga(state):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=115)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)


    toolbox.register("evaluate", lambda ind:  evaluation(ind, state))
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=10)


    population = toolbox.population(n=700)

    NGEN=300
    buffer = [9999999]
    for gen in range(NGEN):
        if statistics.pstdev(buffer[-10:]) > 5:
            offspring = algorithms.varAnd(population, toolbox, cxpb=0.6, mutpb=0.3)
        else:
            print('Bora acelerar esse processo!!')
            offspring = algorithms.varAnd(population, toolbox, cxpb=0.9, mutpb=0.9)
        fits = toolbox.map(toolbox.evaluate, offspring)

        for fit, ind in zip(fits, offspring):
            ind.fitness.values = (fit,)
        population = toolbox.select(offspring, k=len(population))

        score = (lambda ind: evaluation(ind, state))(population[0])
        print(score)
        
        buffer.append(score)
        
        if len(buffer) > 100:
            if statistics.pstdev(buffer) <= 150 and gen/NGEN > 0.6:
                break
            buffer.pop(0)


    result = tools.selBest(population, k=10)
    print(result[0])
    del toolbox
    return result[0]


def evaluation(individual, state):
    player = state['player']
    state = state['state']
    score = 0
    steps = 0

    for action in individual:
        if action == 1:
            score -= 5
            player = flip[player]

        if is_coliding(player, state, steps=steps):
            return score - 200
        score += 10
        steps += 1

    return score
