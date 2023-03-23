#C:\Users\ygoetgheluck\OneDrive - UPEC\M1\Programmation python\Python-2023-M2

"""
#Exercice 1 class
class tall:
    def __init__(self, list):
        self.liste = list
        self.plus_grand = self.grand()
    def grand(self):
            plus_grand = self.liste[0]  # On suppose que le premier élément est le plus grand
            for element in self.liste:
                if element > plus_grand:
                    plus_grand = element
            return(plus_grand)


my_list = [5, 2 , 5 , 6,10,5]
Cherche = tall(my_list)
print(Cherche.plus_grand)
"""

#Exercice 1 class
class Restau:
    def __init__(self,restau_name,cuisine_type):
        self.restau_name = restau_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The cuisine type of {self.restau_name} is {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.restau_name} is open.")
        
    def restau (self) : 
        print(f"{self.number_served} client was served.")
        self.number_served += 1
        print(f"{self.number_served} client was served.")
    def set_number_served(self, clients) :
        if clients >= self.number_served:
            self.number_served = clients
        else:
            print("You can't delete clients")
    def inscrement_number_served(self, clientsMore):
        if clientsMore >= 0 : 
            self.number_served += clientsMore
        else :
            print("Erreur")

"""
restaurant1 = Restau('Pizzeria', 'Italien')
restaurant1.describe_restaurant()
restaurant1.set_number_served(2)
restaurant1.restau()
restaurant1.inscrement_number_served(3)
restaurant1.restau()

restaurant2 = Restau('Gastronomique', 'French')
restaurant2.describe_restaurant()

restaurant3 = Restau('Tapas', 'Spanish')
restaurant3.describe_restaurant()
"""


class user : 
    def __init__(self, first_name, last_name, adress, number):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.number = number
        self.login_attemps = 0
        
    def describe_user (self):
        print(f"User {self.first_name} {self.last_name} live at {self.adress} and his phone number is {self.number}.")
    def greet_user (self):
        print(f"The restaurant welcome you {self.first_name} {self.last_name}")

    def increment_login_attemps (self):
        self.login_attemps += 1 

    def reset_login_attempts(self):
        self.login_attemps = 0
        
        

C1 = user("Yann", "Goet", "Genas", "15852")
C1.describe_user()
C1.greet_user()
C1.increment_login_attemps()
C1.increment_login_attemps()
C1.increment_login_attemps()
print(C1.login_attemps)
C1.reset_login_attempts()
print(C1.login_attemps)



