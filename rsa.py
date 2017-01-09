#!/usr/bin/env python3.5
#-*-coding:UTF-8-*-

from math import sqrt

#####################################################################################
#                                       Variable Globale                            #
#####################################################################################




#####################################################################################
# Test si un nombre est premier     							                    #
# @param intA : un nombre                                                           #
# @return result : Retourne vrai ou faux		                                    #
#####################################################################################

def IsFirst(intA):
    result=True
    racine=int(sqrt(intA))
    for i in range(1,racine):
        reste=intA%i
        if reste==0 and i!=1:
            result=False
    return result


#####################################################################################
# Description de la fonction									                    #
# @param param : le paramètre                                                       #
# @return return : le paramètre de retour		                                    #
#####################################################################################

# def SontPremierEntreEux(intA, intB):


#####################################################################################
# Description de la fonction									                    #
# @param param : le paramètre                                                       #
# @return return : le paramètre de retour		                                    #
#####################################################################################

# def TrouvePremier(max):



#####################################################################################
# Description de la fonction									                    #
# @param param : le paramètre                                                       #
# @return return : le paramètre de retour		                                    #
#####################################################################################

def CalculInverse(intA, intMod):
    for i in range(intMod):
        if (intA*i)%intMod==1:
            return i
    return -1
if __name__ == '__main__':
    # test pour la fonction IsFirst
    assert(IsFirst(40)==False)
    assert(IsFirst(7)==True)
    assert(IsFirst(517)==False)
    assert(IsFirst(173)==True)

    # Test pour la fonction CalculInverse
    assert(CalculInverse()==)
    assert(CalculInverse()==)
    assert(CalculInverse()==)
    assert(CalculInverse()==)
