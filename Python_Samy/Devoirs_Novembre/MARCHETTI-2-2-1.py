# Samy Marchetti

def CalculSomme():
	a = input("Indiquez le premier nombre :")
	b = input("\nIndiquez le deuxième nombre :")
	resultat = int(a) + int(b)

	print("\nLa somme de",a, "et", b, "est", resultat,". Recommencer ?")
	choix = input()

	if (choix == "O"):
		CalculSomme()
		
CalculSomme()