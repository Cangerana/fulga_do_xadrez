import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from deap.tools.support import History
from utils.moves import flip
from utils.colision import is_coliding
from deap import creator, base, tools, algorithms


def ga(state):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=103)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    toolbox.register("evaluate", lambda ind:  evaluation(ind, state))
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=10)
    # toolbox.register("mate", tools.cxTwoPoints)
    # toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3) 
    # toolbox.register("select", tools.selRoulette, k=15)

    population = toolbox.population(n=400)  # 700

    def hstd(data): return data['std']

    NGEN = 400  # 300
    history = []
    for gen in range(NGEN):
        if 1 > 1 - (gen/NGEN) > 0.2 and history[-1]['max'] == history[-1]['min']:
            offspring = algorithms.varAnd(
                population, toolbox, cxpb=0.9, mutpb=1.0 - (gen/NGEN))
        else:
            offspring = algorithms.varAnd(
                population, toolbox, cxpb=0.6, mutpb=0.35)
        fits = toolbox.map(toolbox.evaluate, offspring)

        for fit, ind in zip(fits, offspring):
            ind.fitness.values = (fit,)
        population = toolbox.select(offspring, k=len(population))

        history.append(stats.compile(population))
        print(f'GEN ({gen:^3}){history[-1]}')

    result = tools.selBest(population, k=1)
    print(result[0])
    del toolbox
    plot(history)
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


def plot(history):
    avg = [h['avg'] for h in history]
    std = [h['std'] for h in history]
    min = [h['min'] for h in history]
    max = [h['max'] for h in history]

    x_axis = range(1, len(history)+1)

    # First Plot
    plt.subplot(2, 1, 1)

    plt.plot(x_axis, avg)
    blue_patch = mpatches.Patch(color='blue', label='AVG')

    plt.plot(x_axis, min)
    green_patch = mpatches.Patch(color='green', label='Max')

    plt.plot(x_axis, max)
    orange_patch = mpatches.Patch(color='orange', label='Min')
    plt.legend(handles=[blue_patch, green_patch, orange_patch])

    plt.title("Genetic Algorithm")
    plt.xlabel("Generations")
    plt.ylabel("Score")

    # Second Plot
    plt.subplot(2, 1, 2)

    plt.plot(x_axis, std, color='red')
    red_patch = mpatches.Patch(color='red', label='STD')
    plt.legend(handles=[red_patch])

    plt.xlabel("Generations")
    plt.ylabel("Score")

    plt.show()


"""
BASE:
    - toolbox.register("mate", tools.cxTwoPoint)
    - toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
    - toolbox.register("select", tools.selTournament, tournsize=10)

            700 | 300 -> 835 ('TUNADO')
            700 | 300 -> 480 ('NORMAL')
            
            1000 | 400 -> 835 ('TUNADO')
            1000 | 400 -> 835  ('Normal')
            
            400 | 400 -> 470.0 ('Normal')
            400 | 400 ->   ('tunado')


1000 | 400
P1:
    - toolbox.register("mate", tools.cxUniform, indpb=0.5)
    - toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
    - toolbox.register("select", tools.selRoulette, k=15)

P2
    - toolbox.register("mate", tools.cxUniform, indpb=1)
    - toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
    - toolbox.register("select", tools.selRoulette, k=15)

P3
    - toolbox.register("mate", tools.cxPartialyMatched) 
    - toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3) 
    - toolbox.register("select", tools.selStochasticUniversalSampling, k=5) 

P4 - 835.0
    - toolbox.register("mate", tools.cxTwoPoints)
    - toolbox.register("mutate", tools.mutFlipBit, indpb=0.15)
    - toolbox.register("select", tools.selTournament, k=5, tournsize=3)

p5 - 835.0
    - toolbox.register("mate", tools.cxTwoPoints)
    - toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3) 
    - toolbox.register("select", tools.selTournament, k=5, tournsize=3)

p6 - 265.0
    - toolbox.register("mate", tools.cxTwoPoints)
    - toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3) 
    - toolbox.register("select", tools.selRoulette, k=15)

p7 - 310.0
    - toolbox.register("mate", tools.cxPartialyMatched)
    - toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3) 
    - toolbox.register("select", tools.selRoulette, k=15)
"""