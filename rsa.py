#!/usr/bin/env python3.5
#-*-coding:UTF-8-*-


from math import sqrt
import random as rd

#####################################################################################
#                                       Variable Globale                            #
#####################################################################################
p=7
q=11
Phin=(p-1)*(q-1)
e=13
d=37
n=p*q
Alphabet = [chr(65 + i) for i in range(0, 26)]
codageAlphabet=[]

#####################################################################################
# Test si un nombre est premier     							                    #
# @param intA : un nombre                                                           #
# @return result : Retourne vrai ou faux		                                    #
#####################################################################################

def IsFirst(intA):
    result=True
    racine=int(sqrt(intA))+1
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

def initialiseCodageAlphabet():
    for i in range(0,215):
        if SontPremierEntreEux(i,215):
            if len(codageAlphabet)==26:
                return codageAlphabet
            if not( i in codageAlphabet):
                codageAlphabet.append(i)

def DecodageAlphabet(intA):
    for i in range(0, len(codageAlphabet)) :
        if intA == codageAlphabet[i]:
            return i

def EntierLettre(lettre):
    i=ord(lettre)-65
    return codageAlphabet[i]

def aPuisBModuloN(intA,intB,intMod):
   # mod = intA%intMod
   # result=(mod**intB)%intMod
   result=(intA**intB)%intMod
   return result

def chiffre(message):
    messageChiffre = []
    for i in message :
        chiffre = EntierLettre(i)
        chiffre = aPuisBModuloN(chiffre, e, n)
        messageChiffre.append(chiffre)
    return messageChiffre

def dechiffre(intA):
    message=''
    for i in intA :
        i = (i**d)%n
        i = DecodageAlphabet(i)
        message += Alphabet[i]
    return message


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
    assert(IsFirst(35)==False)

    #Test de la fonction SontPremierEntreEux
    assert(SontPremierEntreEux(13,15)==True)
    assert(SontPremierEntreEux(22,10)==False)
    assert(SontPremierEntreEux(33,19)==True)
    assert(SontPremierEntreEux(8,24)==False)

    # Test pour la fonction CalculInverse
    assert(CalculInverse(5,7)==3)
    assert(CalculInverse(3,11)==4)

    #test pour la fonction aPuisBModuloN
    assert(aPuisBModuloN(10,1,11)==10)
    assert(aPuisBModuloN(10,3,11)==10)
    assert(aPuisBModuloN(5,2,25)==0)

    initialiseCodageAlphabet()
    assert(dechiffre(chiffre('ALEXANDRE'))=='ALEXANDRE')
    print('codageAlphabet => {}'.format(codageAlphabet))
    print('message chiffré => {}'.format(chiffre('ALEXANDRE')))
    print('message déchiffré => {}'.format(dechiffre(chiffre('ALEXANDRE'))))
	# #test pour les fonctions chiffre et dechiffre
