from person import *
from nation import *
import random

def askConfiguration(nation: Nation) -> Nation:
    educationSpending = int(input("Spending on education per student (100$: low education level,  2'000$: high education level) ($$) : "))
    incomeTax = int(input("Income tax (%) : "))
    nation.educationSpending = educationSpending
    nation.incomeTax = incomeTax

    return nation

def randomAge() -> int:
    groups = [
        (0, 14, 0.25),
        (15, 24, 0.15),
        (25, 54, 0.40),
        (55, 64, 0.10),
        (65, 100, 0.10),
    ]
    
    age_group = random.choices(groups, weights=[g[2] for g in groups], k=1)[0]
    
    age = random.randint(age_group[0], age_group[1])
    
    return age

import random

def randomSalaireBrut(age, formationLevel):
    formationFactor = (formationLevel / 100) + 0.005

    if age < 25:
        mean, stddev = 25000, 8000 
    elif 25 <= age < 35:
        mean, stddev = 40000, 12000
    elif 35 <= age < 50:
        mean, stddev = 55000, 15000
    elif 50 <= age < 65:
        mean, stddev = 70000, 18000
    else:
        mean, stddev = 50000, 15000 

    salaire = max(0, random.gauss(mean, stddev))
    salaire *= formationFactor

    return int(salaire)

# Exemple d'utilisation
age = 30
formationLevel = 80
salaire = randomSalaireBrut(age, formationLevel)
print(f"Âge: {age}, Niveau de formation: {formationLevel}, Salaire brut estimé: {salaire} €")


def randomEducationLevel(educationSpending) -> int:

    moyenne = max(5, 0.05 * educationSpending)
    gap = 10  
    print(moyenne)
    level = random.gauss(moyenne, gap)
    
    level = max(0, int(level))
    
    return level

def newPerson(nation: Nation) -> Person:
    age = randomAge()
    fortune = randomFortune(age)


def start():
    INITIAL_POPULATION = 100
    INITIAL_BUDGET = 1000000
    nation = Nation(budget=INITIAL_BUDGET, persons=[], educationSpending=0, incomeTax=0)
    for i in range(INITIAL_POPULATION):


        nation.persons.append(Person())

    nation = askConfiguration(nation)
    print(nation)

# start()