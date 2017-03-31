import math
import random

import constante as c
import physicFunction


def genAlpha():
    return random.uniform(c.ALPHA_MIN, c.ALPHA_MAX)


def genLongBras():
    return random.uniform(c.ARM_LENGTH_MIN, c.ARM_LENGTH_MAX)


def genSectionBase():
    return random.uniform(c.SECTION_BASE_MIN, c.SECTION_BASE_MAX)


def genSectionHauteur():
    return random.uniform(c.SECTION_HEIGHT_MIN, c.SECTION_HEIGHT_MAX)


def genLongCorde():
    return random.uniform(c.ROPE_LENGTH_MIN, c.ROPE_LENGTH_MAX)


def genLongFleche():
    return random.uniform(c.ARROW_LENGTH_MIN, c.ARROW_LENGTH_MAX)


def genDiametreFleche():
    return random.uniform(c.ARROW_DIAMETER_MIN, c.ARROW_DIAMETER_MAX)


def genRhoFleche():
    return random.uniform(c.ARROW_RHO_MIN, c.ARROW_RHO_MAX)


def genYoungModule():
    return random.uniform(c.YOUNG_MODUL_MIN, c.YOUNG_MODUL_MAX)


def genPoissonCoeff():
    return random.uniform(c.POISSON_COEF_MIN, c.POISSON_COEF_MAX)

mutateGen=[
    genAlpha(),
    genLongBras(),
    genSectionBase(),
    genSectionHauteur(),
    genLongCorde(),
    genLongFleche(),
    genDiametreFleche(),
    genRhoFleche(),
    genYoungModule(),
    genPoissonCoeff()]


def createIndividual():
    # return [51, 29.9, 9.7, 9.1, 2, 0.5,0.2,7850,210,0.27]
    return [genAlpha(),             # 0 51
            genLongBras(),          # 1 29.9
            genSectionBase(),       # 2 9.7
            genSectionHauteur(),    # 3 9.1
            genLongCorde(),         # 4 2
            genLongFleche(),        # 5 0.5
            genDiametreFleche(),    # 6 0.2
            genRhoFleche(),         # 7 7850
            genYoungModule(),       # 8 210
            genPoissonCoeff()]      # 9 0.27
def tnt(individual):
    ressort = physicFunction.ressort(individual[8], individual[9])
    longVide = physicFunction.longueurVide(individual[1], individual[4])
    longDeplacement = physicFunction.longueurDeplacement(individual[5], longVide)
    masse = physicFunction.masseProjectile(individual[7], individual[6], individual[5])
    velocity = physicFunction.velocite(ressort, longDeplacement, masse)
    energie = physicFunction.energieImpact(masse, velocity)
    tnt = physicFunction.energieTNT(energie)
    return tnt

def distanceCible(individual):
    masse = physicFunction.masseProjectile(individual[7], individual[6], individual[5])
    longVide = physicFunction.longueurVide(individual[1], individual[4])
    longDeplacement = physicFunction.longueurDeplacement(individual[5], longVide)
    ressort = physicFunction.ressort(individual[8], individual[9])
    velocity = physicFunction.velocite(ressort, longDeplacement, masse)
    portee = physicFunction.portee(velocity, c.EARTH, individual[0])
    distance = abs(c.DISTANCE - portee)


    return distance

def scoreIndividual(distance,tnt):
    # score=-3*distance+900
    # if distance>300 or score<1:
    #     score=1
    # print(distance,score)
    # return math.pow(score,2)
    print(distance,(1000/(1+math.pow(distance/10,2)))+tnt*0.0001)
    print(tnt)
    return (1000/(1+math.pow(distance/10,2)))+tnt*0.0001



def getIndividuByCursor(cursor, offset, score):
    for i in range(1, c.NB_POP+1):
        if offset < score[cursor] and offset > score[cursor - 1]:
            return int(cursor)
        cursor = math.fmod(cursor + 1, c.NB_POP + 1)
        if cursor == 0:
            cursor = 1


def genererCouple(score):
    totalScore = score[c.NB_POP]
    offset = random.uniform(0, totalScore)
    cursor = getIndividuByCursor(1, offset, score)

    pas = random.randint(400, 700)
    parentA = 0
    parentB = 0

    couple = {}
    countCouple = 1
    while countCouple < c.NB_POP / 2 + 1:
        offset = math.fmod(offset + pas, totalScore)

        if parentA == 0:
            parentA = getIndividuByCursor(cursor, offset, score)
            cursor = parentA
        else:
            parentB = getIndividuByCursor(cursor, offset, score)
            cursor = parentB

        if parentB != parentA and parentB != 0:
            couple[countCouple] = [parentA, parentB]
            parentA = 0
            parentB = 0
            countCouple += 1
    return couple

    [parentA,paraentB ],[ parentA,paraentB ]