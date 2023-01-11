# MARCHETTI Samy, Fiche 3, Exercice 2

import sys

# Exercice A
def exerciceA():
	result = int()

	for i in range(1, len(sys.argv)):
		a = int(sys.argv[i])
		result = result + a

	print(result)

# Exercice B
def exerciceB():
	result = int(1)

	for i in range(1, len(sys.argv)):
		a = int(sys.argv[i])
		result = result * a

	print(result)

# Exercice C
def exerciceC():
	result = int()

	for i in range(1, len(sys.argv)):
		a = int(sys.argv[i])
		result = result + a

	print(result / (len(sys.argv) - 1))

# Exercice D
def exerciceD():
	result = []

	for i in range(1, len(sys.argv)):
		result.append(int(sys.argv[i]))

	print(max(result))

# Exercice E
def exerciceE():
	result = []

	for i in range(1, len(sys.argv)):
		result.append(int(sys.argv[i]))

	print(min(result))

# Exercice F
def exerciceF():
	search = int(input("Please enter a number:"))
	result = []

	for i in range(1, len(sys.argv)):
		result.append(int(sys.argv[i]))

	print(result.count(search))

#Exercice G
def exerciceG():
	result = []

	for i in range(1, len(sys.argv)):
		result.append(int(sys.argv[i]))

	print(max(result))

	print(result.index(max(result)) + 1)

# Espace essai
#exerciceF()
