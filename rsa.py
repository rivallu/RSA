#!/usr/bin/env python3.5
#-*-coding:UTF-8-*-

import math
import random as rd

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
    racine=int(math.sqrt(intA))
    for i in range(1,racine):
        reste=intA%i
        if reste==0 and i!=1:
            result=False
    return result


#####################################################################################
# Fonction déterminant si deux nombres sont premiers entre eux	                    #
# @param param : deux entiers intA et intB                                          #
# @return return : retourne True s'ils sont premiers entre eux, False sinon         #
#####################################################################################

def SontPremierEntreEux(intA, intB):
    a = intA
	b = intB
	reste = 1
	while reste != 0 :
		reste = a%b
		a = b
		b = reste
	if a == 1 :
		return True
	else :
		return False


#####################################################################################
# Trouve un nombre premier aléatoire inférieur à une borne supérieure max           #
# @param param : la borne supérieure max (entier)                                   #
# @return return : le nombre premier généré (variable : entier premier)             #
#####################################################################################

def TrouvePremier(max):
	valid = False
	while valid == False :
		premier = rd.randint(2, max-1)
		valid = IsFirst(premier)
	return premier



#####################################################################################
# Description de la fonction									                    #
# @param param : le paramètre                                                       #
# @return return : le paramètre de retour		                                    #
#####################################################################################

# def CalculInverse(inta, intMod):


if __name__ == '__main__':
    assert(IsFirst(40)==False)
    assert(IsFirst(7)==True)
    assert(IsFirst(517)==False)
    assert(IsFirst(173)==True)
    assert(SontPremierEntreEux(13,15)==True)
	assert(SontPremierEntreEux(22,10)==False)
	assert(SontPremierEntreEux(33,19)==True)
	assert(SontPremierEntreEux(8,24)==False)
