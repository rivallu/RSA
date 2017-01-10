#!/usr/bin/env python3.5
#-*-coding:UTF-8-*-


from math import sqrt
import random as rd
import time

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

#####################################################################################
# Initialise une liste contenant l'alphabet						                    #
# @return codageAlphabet : la liste contenant je sais quoi                          #
#####################################################################################

def initialiseCodageAlphabet(max):
    while(len(codageAlphabet)<26):
        i=rd.randint(1,214)
        if SontPremierEntreEux(i,n) and i not in codageAlphabet:
            codageAlphabet.append(i)

    # for i in range(0,215):
    #     if SontPremierEntreEux(i,n):
    #         if len(codageAlphabet)==26:
    #             return codageAlphabet
    #         if not( i in codageAlphabet):
    #             codageAlphabet.append(i)

#####################################################################################
# Retourne la position de la lettre donnée						                    #
# @param intA : le chiffre à chercher dans codageAlphabet                           #
# @return i : la position de la lettre  		                                    #
#####################################################################################

def DecodageAlphabet(intA):
    for i in range(0, len(codageAlphabet)) :
        if intA == codageAlphabet[i]:
            print("l'indice trouvé: {}".format(i))
            return i

#####################################################################################
# Fait corespondre à une lettre son codage alphabet				                    #
# @param lettre : la lettre a cherché                                               #
# @return codageAlphabet : son codage associé	                                    #
#####################################################################################

def EntierLettre(lettre):
    i=ord(lettre)-65
    return codageAlphabet[i]

#####################################################################################
# génère le modulo du chiffre donnée							                    #
# @param intA : le chiffre                                                          #
# @param intB : la clé publique                                                     #
# @param intMod : Le modulo                                                         #
# @return return : le paramètre de retour		                                    #
#####################################################################################

def aPuisBModuloN(intA,intB,intMod):
   mod = intA%intMod
   result=(mod**intB)%intMod
   return result

#####################################################################################
# chiffre un message donnée   									                    #
# @param message : le message a chiffré                                             #
# @return messageChiffre : le message chiffré	                                    #
#####################################################################################

def chiffre(message):
    messageChiffre = []
    for i in message :
        chiffre = EntierLettre(i)
        chiffre = aPuisBModuloN(chiffre, e, n)
        messageChiffre.append(chiffre)
    print('message chiffré => {}'.format(messageChiffre))
    return messageChiffre

#####################################################################################
# Déchiffre le message donnée									                    #
# @param intA : le message a déchiffré                                              #
# @return message : le message déchiffré		                                    #
#####################################################################################

def dechiffre(intA):
    message=''
    for i in intA :
        print('le chiffre à déchiffré: {}'.format(i))
        i = (i**d)%n
        print('le chiffre à chercher dans le codageAlphabet: {}'.format(i))
        i = DecodageAlphabet(i)
        print("la lettre déchiffré est : {}".format(Alphabet[i]))
        message += Alphabet[i]
    print('message déchiffré => {}'.format(message))
    return message


#####################################################################################
# Calcule l'inverse d'un nombre par rapport à un modulo			                    #
# @param intA : le chiffre                                                          #
# @param intMod : le modulo                                                         #
# @return i : l'inverse du chiffre voulu		                                    #
#####################################################################################

def CalculInverse(intA, intMod):
    for i in range(intMod):
        if (intA*i)%intMod==1:
            return i
    return -1

#####################################################################################
# Mesure le temps d'execution d'une fonction            		                    #
# @param function : la fonction à mesuré                                            #
# @param *args : les arguments de la fonction à mesuré                              #
#####################################################################################

def mesureTemps(function, *args):
    tmp1=time.clock()
    function(*args)
    tmp2=time.clock()
    tmp=tmp2-tmp1
    print("le temps d'execution de la fonction {function} est de {tmp}".format(function=function.__name__,tmp=tmp))

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

    #test pour les fonctions chiffre et dechiffre
    initialiseCodageAlphabet(n)
    print(codageAlphabet)
    print('p = {p} q={q} e={e} d={d} n={n}'.format(p=p,q=q,e=e,d=d,n=n))
    assert(dechiffre(chiffre('ALEXANDRE'))=='ALEXANDRE')
    # assert(dechiffre(chiffre('LUCAS'))=='LUCAS')
    # assert(dechiffre(chiffre('XYLOPHONE'))=='XYLOPHONE')
    #
    # print('codageAlphabet => {}'.format(codageAlphabet))
    # print('message chiffré => {}'.format(chiffre('ALEXANDRE')))
    # print('message déchiffré => {}'.format(dechiffre(chiffre('ALEXANDRE'))))


    p=TrouvePremier(50)
    q=TrouvePremier(50)
    n=p*q
    Phin=(p-1)*(q-1)
    e=rd.randint(2, Phin)
    while not(SontPremierEntreEux(e,Phin)):
        e=rd.randint(2,Phin)
    d=CalculInverse(e,Phin)
    assert(d!=-1)
    initialiseCodageAlphabet(n)
    print('p = {p} q={q} e={e} d={d} n={n}'.format(p=p,q=q,e=e,d=d,n=n))
    print('codageAlphabet => {}'.format(codageAlphabet))
    dechiffre(chiffre('ALEXANDRE'))
