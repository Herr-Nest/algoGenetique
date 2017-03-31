import random

import time

import matplotlib.pyplot as plt
import constante as c
import geneticFunction

debut=time.time()
# initialisation de la population

individual = {}
scoreCumul = {}
scoreCumul[0] = 0
distance=[]
moyenneNote=[]
tnt=[]
variance=[]
for generation in range(0,c.NB_GENERATION):

    score=[]
    if len(individual)==0:
        for i in range(1, c.NB_POP + 1):
            individual[i] = geneticFunction.createIndividual()
            score.append(geneticFunction.scoreIndividual(geneticFunction.distanceCible(individual[i]), geneticFunction.tnt(individual[i])))
            scoreCumul[i] = score[i-1] + scoreCumul[i - 1]
    couple = geneticFunction.genererCouple(scoreCumul)

    sommeDistance=0
    sommeTnt = 0
    deltaScore=0
    moyenneNote.append(scoreCumul[c.NB_POP] / c.NB_POP)
    for i in range(1,c.NB_POP +1):
        sommeDistance += geneticFunction.distanceCible(individual[i])
        sommeTnt+= geneticFunction.tnt(individual[i])
        deltaScore+=score[i-1]-moyenneNote[generation]
    variance.append(deltaScore/c.NB_POP)
    distance.append(sommeDistance/c.NB_POP)
    tnt.append(sommeTnt/c.NB_POP)
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
        scoreCumul[2 * i - 1] = geneticFunction.scoreIndividual(geneticFunction.distanceCible(children[2 * i - 1]), geneticFunction.tnt(children[2 * i - 1])) + scoreCumul[2 * i - 2]
        scoreCumul[2 * i] = geneticFunction.scoreIndividual(geneticFunction.distanceCible(children[2 * i]), geneticFunction.tnt(children[2 * i])) + scoreCumul[2 * i - 1]

    individual = children
    del children
    # print(individual)
plt.xlabel('nombre de generation')
plt.subplot(221)
plt.ylabel("Distance à la cible")
plt.plot(distance)
plt.subplot(222)
plt.ylabel("Puissance en tnt")
plt.plot(tnt)
plt.subplot(223)
plt.ylabel("Note Moyenne")
plt.plot(moyenneNote)
plt.subplot(224)
plt.ylabel("Variance")
plt.plot(variance)
plt.show()
fin=time.time()
print(fin-debut)
