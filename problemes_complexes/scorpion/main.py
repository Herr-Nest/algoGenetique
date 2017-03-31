import random

import time

import matplotlib.pyplot as plt
import constante as c
import geneticFunction

debut=time.time()
# initialisation de la population

individual = {}
score = {}
score[0] = 0
distance=[]

for generation in range(0,c.NB_GENERATION):
    if len(individual)==0:
        for i in range(1, c.NB_POP + 1):
            individual[i] = geneticFunction.createIndividual()

            score[i] = geneticFunction.scoreIndividual(geneticFunction.distanceCible(individual[i])) + score[i - 1]
    couple = geneticFunction.genererCouple(score)
    sommeDistance=0
    for i in range(1,c.NB_POP +1):
        sommeDistance += geneticFunction.distanceCible(individual[i])
    distance.append(sommeDistance/c.NB_POP)
    children = {}
    for i in range(1, len(couple)+1):
        cut=c.HEIGHT_CUT
        if random.randint(1, 11)<=c.CHANGE_CUT:
            cut=random.randint(1, 10)

        children[2 * i - 1] = individual[couple[i][0]][:cut] + individual[couple[i][1]][cut:]
        children[2 * i] = individual[couple[i][1]][:cut] + individual[couple[i][0]][cut:]
        if random.randint(1,101)<c.MUTATION:
            geneMute = random.randint(0, 9)
            children[2 * i - 1][geneMute] = geneticFunction.mutateGen[geneMute]
        if random.randint(0,101)<c.MUTATION:
            geneMute=random.randint(0, 9)
            children[2 * i][geneMute] = geneticFunction.mutateGen[geneMute]
        score[2 * i - 1] = geneticFunction.scoreIndividual(geneticFunction.distanceCible(children[2 * i - 1]))+score[2 * i - 2]
        score[2 * i] = geneticFunction.scoreIndividual(geneticFunction.distanceCible(children[2 * i]))+ score[2 * i - 1]

    individual = children
    del children
    # print(individual)

plt.plot(distance)
plt.show()
fin=time.time()
print(fin-debut)
