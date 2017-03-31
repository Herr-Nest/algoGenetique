import math


def ressort(E, v):
    """

    :param E: module de young
    :param v: coefficient de poisson
    :return: ressort
    """
    return (E / (1 - 2 * v)) / 3


def longueurVide(lb, lc):
    """

    :param lb: longueur du bras
    :param lc: longueur de la corde
    :return:
    """
    a = math.pow(lb,2)-math.pow(lc,2)
    return math.sqrt(a)/2 if a >= 0 else 0


def longueurDeplacement(lf, lv):
    """

    :param lf: longueur de la fleche
    :param lv: longueur a vide
    :return: longueur de deplacement
    """
    return lf - lv


def masseProjectile(rho, d, lf):
    """

    :param rho: masse volumique de la fleche
    :param d: base de la section
    :param lf: longueur fleche
    :return: masse de la fleche
    """
    return rho * math.pi*math.pow((d/2), 2) * lf


# Param float K : ressort
# Param float ld : longueur du deplacement
# Param float mp : masse du projectile
# return float velocite
def velocite(K,ld,mp):
    """

    :param K: ressort
    :param ld: longueur du deplacement
    :param mp: masse du projectile
    :return: velocite
    """
    return math.sqrt(K*math.pow(ld, 2)/mp)


def portee(V, g, alpha):
    """

    :param V: Velocite
    :param g: gravite
    :param alpha: angle de hausse
    :return:
    """
    return math.pow(V, 2)/g*math.sin(math.radians(alpha)*2)


def energieImpact(mp, V):
    return 1/2*mp*math.pow(V, 2)


def energieTNT(ej):
    return ej/4184
