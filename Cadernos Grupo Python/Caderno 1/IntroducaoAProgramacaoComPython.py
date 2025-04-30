#Instalação (Windows)- Primeira execução do python
print("Hello World")


#Instalação (Windows)- Hello World no Jupyter 
print("Hello World")
print("Esse")
print("É meu segundo programa")
print("Em python")


#Entendendo melhor o print
print("Hello World")
print("Esse", end="")
print("é meu terceiro programa", end="")
print("em Python")


#Variáveis
print("Ciência de dados!")
print("Ciência de dados!")
print("Ciência de dados!")
print("Ciência de dados!")

x = "Ciência de dados!"
print(x)
print(x)
print(x)
print(x)

x = "O meu filme favorito é troll 2!"
print(x)
print(x)
print(x)
print(x)

#Tipos de dados
x = 4

x = 4
y = "4"
print(x)
print(y)

x = 4
y = "4"
print(x + x)
print(y + y)

#Tipos de dados - Função type()
x = 4
print(type(x))

#Tipos de dados - Principais tipos de variáveis - int
x = 4
print(x)
print(type(x))

#Tipos de dados - Principais tipos de variáveis - str
texto1 = "Ciência de dados!"
texto2 = 'O meu filme favorito é "troll 2"!'
texto3 = """Minha terra tem palmeiras
Onde canta o Sabiá,
As aves, que aqui gorjeiam,
Não gorjeiam como lá."""

print(texto1)
print(type(texto1))
print(texto2)
print(type(texto2))
print(texto3)
print(type(texto3))


#Tipos de dados - Principais tipos de variáveis - float
numeroRacional1 = 1.0
numeroRacional2 = 56.133000
print(numeroRacional1)
print(type(numeroRacional1))
print(numeroRacional2)
print(type(numeroRacional2))


#Tipos de dados - Principais tipos de variáveis - bool
chovendo = True
calor = False
vascoEMaisCampeaoQueOFlamengo = 4 > 7
print(chovendo)
print(type(chovendo))
print(calor)
print(type(calor))
print(vascoEMaisCampeaoQueOFlamengo)
print(type(vascoEMaisCampeaoQueOFlamengo))


#Tipos de dados - Principais tipos de variáveis - list
vetorDeNumeros = [1, 2, 3, 4]
vetorDeFrutas = ["Morango", "Pera", "Banana"]
vetorVazio = [ ]
print(vetorDeNumeros)
print(type(vetorDeNumeros))
print(vetorDeFrutas)
print(type(vetorDeFrutas))
print(vetorVazio)
print(type(vetorVazio))


#Tipos de dados - Principais tipos de variáveis - function
print(type(print))


#Operandos - + e - - int e float
x = 1 + 3
print(x - 2)

x = 1 + 3.0
print(x - 2)


#Operandos - + e - - str
texto = "ketchup"
print(texto + " e mostarda")


#Operandos - + e - - bool
print(True + True + False)


#Operandos - * e / - int e float
x = 4 * 8
print(x / 3)


#Operandos - * e / - str
textoOriginal = "Ciência de dados!\n"
print(textoOriginal*5)


#Operandos - // e %
nAmigos = 25
nEquipes = 25//11
amigosNaDeFora = 25%11
print("Amigos na de fora:")
print(3)
print("Equipes formadas:")
print(2)


#Operandos - **
x = 9
xAoQuadrado = 9 ** 2
raizQuadradaDeX = 9 ** 0.5
print(xAoQuadrado)
print(raizQuadradaDeX)


#Operandos - ( e )
expressaoAlgebrica = (((2+3)/2)+4**2)**(1/2)
print("Resultado da expressão algébrica (((2+3)/2)+4**2)**(1/2):")
print(expressaoAlgebrica)


#Operandos - ( e ) - funções
print("Olá Mundo!")


#Operandos - Operadores condicionais - >, <, >=, <=
print(4 > 7)
print(5 <= 10.4)
print("Mostarda" >= "Maionese")


#Operandos - Operadores condicionais - == e !=
print(4 == 7)
print(5 == 5)
print(4 != "4")
print(True != True)


#Operandos - Operadores condicionais - not, and, or
expressao1 = (1 < 4) and (1 == 0.0)
expressao2 = (expressao1) or ("Mostarda" == "Mostarda")
expressao3 = (not expressao1) and ("Mostarda" == "Mostarda")
print(expressao1)
print(expressao2)
print(expressao3)


#Operandos - Operadores condicionais - in
listaDeCodimentos = ["Ketchup", "Mostarda", "Maionese"]
print("Pimenta" in listaDeCodimentos)
print("Mostarda" in listaDeCodimentos)
print("ostar" in listaDeCodimentos[1])


#Métodos e funções padrão - Transformação de tipo (casting)
print(int("4") == 4)

print("4" == str(4))
numeroInteiro = 4
numeroRacional = 3.0
print(int(numeroRacional))
print(float(numeroInteiro))
print(bool(numeroInteiro))

listaDeCodimentos = ["Mostarda", "Ketchup", "Maionese"]
print(tuple(listaDeCodimentos))


#Métodos e funções padrão - Principais funções de inteiros (int) - range()
de0a4 = range(5)
numerosDeUmADez = range(1, 11)
numerosParesDeZeroAVinte = range(0, 21, 2)
print(list(de0a4))
print(list(numerosDeUmADez))
print(list(numerosParesDeZeroAVinte))


#Métodos e funções padrão - Principais funções de inteiros (int) - random.randint()
import random
numeroAleatorio1 = random.randint(3, 9)
numeroAleatorio2 = random.randint(3, 9)
numeroAleatorio3 = random.randint(3, 9)
numeroAleatorio4 = random.randint(3, 9)
print(numeroAleatorio1)
print(numeroAleatorio2)
print(numeroAleatorio3)
print(numeroAleatorio4)


#Métodos e funções padrão - Principais funções de floats (float) - round()
print(round(3.3))
print(round(2.5))
print(round(4.7))


#Métodos e funções padrão - Principais funções de floats (float) - math.ceil()
import math
print(math.ceil(3.3))
print(math.ceil(2.5))
print(math.ceil(4.7))


#Métodos e funções padrão - Principais funções de floats (float) - math.floor()
import math
print(math.floor(3.3))
print(math.floor(2.5))
print(math.floor(4.7))


#Métodos e funções padrão - Principais funções de floats (float) - math.trunc()
import math
print(math.trunc(3.3))
print(math.trunc(2.5))
print(math.trunc(-4.7))


#Métodos e funções padrão - Principais métodos e funções de strings (str) - len
nome = input("Digite seu nome: \n")
idade = int(input("Digite sua idade: \n"))
print("Você se chama " + nome + " e fará " + str((idade + 1)) + " anos")


#Métodos e funções padrão - Principais métodos e funções de strings (str) - .replace()
frase = "Meu filme favorito é troll 2!"
print(len(frase))


#Métodos e funções padrão - Principais métodos e funções de strings (str) - .strip()
frase = "     Meu filme    favorito é troll 2!                  "
print(frase.strip())


#Métodos e funções padrão - Principais métodos e funções de strings (str) - .replace()
frase = "Meu filme favorito é troll 2 e o meu segundo filme favorito é troll 1!"
print(frase.replace("troll", "sharknado"))


#Métodos e funções padrão - Principais métodos e funções de strings (str) - split()
frase = "Ketchup Maionese Mostarda"
listaDeCodimentosGastronomicos = frase.split(" ")
print(listaDeCodimentosGastronomicos)


#Métodos e funções padrão - Principais métodos e funções de strings (str) - .format()
listaDeCodimentosGastronomicos = ['Ketchup', 'Maionese', 'Mostarda']
frase = "Codimento Gastronomico 1: {}\nCodimento Gastronomico 2: {}\nCodimento Gastronomico 3: {}".format(listaDeCodimentosGastronomicos[0], listaDeCodimentosGastronomicos[1], listaDeCodimentosGastronomicos[2])
print(frase)


#Métodos e funções padrão - Principais métodos e funções de strings (str) - isalum(), .isalpha() e .isnumeric()
print("Troll2".isalnum())
print("Ketchup".isalpha())
print("Ciência de dados!".isalpha())
print("2024".isnumeric())
print("Sharknado 5 e troll 2!".isalnum())
print("ano de 2024".isnumeric())


#Métodos e funções padrão - Principais métodos e funções de strings (str) - .upper(), .lower() e .capitalize()
print("Hello World!".lower())
print("ketchup, maionese, mostarda".upper())
print("ketchup, maionese, mostarda".capitalize())


#Métodos e funções padrão - Principais métodos e funções de strings (str) - .join()
listaDeCodimentos = ["Ketchup", "Maionese", "Mostarda"]
print(", ".join(listaDeCodimentos))


#Métodos e funções padrão - Principais métodos e funções de strings (str) - .find()
print("Melhores filmes: Troll 2 e Troll 1".find("Troll"))
print("Melhores filmes: Troll 2 e Troll 1".find("Sharknado"))


#Métodos e funções padrão - Principais métodos e funções de strings (str) - .count()
print("Sharknado 1, Sharknado 2, Sharknado 3, Sharknado 4, Sharknado 5, Sharknado 6".count("Sharknado"))


#Métodos e funções padrão - Principais métodos e funções de listas (list) - max()
print(max([1, 2, 7, 3, 4]))


#Métodos e funções padrão - Principais métodos e funções de listas (list) - min()
print(min([1, 2, 7, 3, 4]))

#Métodos e funções padrão - Principais métodos e funções de listas (list) - sum()
print(sum([1, 2, 7, 3, 4]))

#Métodos e funções padrão - Principais métodos e funções de listas (list) - len()
print(len([1, 2, 7, 3, 4]))

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .append()
codimentosGastronomicos = ["Ketchup", "Maionese"]
codimentosGastronomicos.append("Mostarda")
print(codimentosGastronomicos)

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .extend()
codimentosGastronomicos = ["Ketchup", "Maionese"]
codimentosGastronomicos.extend(["Mostarda"])
print(codimentosGastronomicos)

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .insert()
codimentosGastronomicos = ["Ketchup"]
codimentosGastronomicos.insert(231, "Mostarda")
codimentosGastronomicos.insert(1, "Maionese")
print(codimentosGastronomicos)

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .remove()
codimentosGastronomicos = ["Ketchup", "Maionese", "Mostarda"]
codimentosGastronomicos.remove("Ketchup")
print(codimentosGastronomicos)

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .pop()
codimentosGastronomicos = ["Ketchup", "Maionese", "Mostarda"]
codimentosGastronomicos.pop(1)
print(codimentosGastronomicos)
print(codimentosGastronomicos.pop())
print(codimentosGastronomicos)

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .index()
codimentosGastronomicos = ["Ketchup", "Maionese", "Mostarda"]
print(codimentosGastronomicos.index("Ketchup"))

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .count()
lista = ["Ciência de dados!", "Ciência de dados!", "Ciência de dados!", "Ciência de dados!"]
print(lista.count("Ciência de dados!"))

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .sort() ou sorted()
numeros1 = [5, 1, 77, 8, 2, 3, 3213, 23, -3, -7]
numeros1.sort(reverse=True)
numeros2 = [5, 1, 77, 8, 2, 3, 3213, 23, -3, -7]
numeros2 = sorted(numeros2)
listaDeCodimentos = ["Ketchup", "Mostarda", "Maionese"]
print(numeros1)
print(numeros2)
print(sorted(listaDeCodimentos))

#Métodos e funções padrão - Principais métodos e funções de listas (list) - .reverse()
listaDeCodimentos = ["Ketchup", "Maionese", "Mostarda"]
listaDeCodimentos.reverse()
print(listaDeCodimentos)


#Comentários - Comentários com hashtag
#Lista de codimentos mais utilizados na cozinha brasileira
listaDeCodimentos = ["Maionese", "Mostarda", "Ketchup"]
#Organiza em ordem alfabética
listaDeCodimentos.sort()
#Inverte a ordem dos codimentos (não vou utilizar agora)
#listaDeCodimentos.reverse()
print(listaDeCodimentos)


