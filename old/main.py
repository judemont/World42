import math
import random
import time
import copy

class Person:
    def __init__(self, netSalary: int, grossSalary: int, age: int, intellectualCapacities: int, health: int):
        self.netSalary = netSalary
        self.grossSalary = grossSalary
        self.age = age
        self.intellectualCapacities = intellectualCapacities,
        self.health = health

class Nation:
    def __init__(self, name: str, budget: int, incomeTax: int, educationSpending: int, otherRevenues: int, persons: list[Person]):
        self.name = name
        self.budget = budget
        self.incomeTax = incomeTax
        self.otherRevenues = otherRevenues
        self.educationSpending = educationSpending
        self.persons = persons

class Stats:
    def __init__(self, averageSalary, unemployedCount):
        self.averageSalary = averageSalary
        self.unemployedCount = unemployedCount

def start():
    INITIAL_NATIONAL_BUDGET =  100
    INITIAL_POPULATION = 100
    OTHER_NATION_REVENUES = 0
    nation = newNation(INITIAL_NATIONAL_BUDGET, OTHER_NATION_REVENUES)
    
    for i in range(INITIAL_POPULATION):
        newPerson(nation, random.randint(0, 80))
        
    monthNum = 0
    stats = Stats(0,0)
    while nation.budget >= 0:
        oldNation = copy.copy(nation)
        cycle(nation, monthNum)
        stats = printStats(nation, monthNum, stats, oldNation)
        time.sleep(3)
        monthNum +=1 

    print("Game Over")


def newPerson(nation: Nation, age: int):

    educationSpendingPerResident = (nation.budget * nation.educationSpending / 100) / (len(nation.persons)+1)

    intellectualCapacities = round(random.gauss(50, 20))

    salary = educationSpendingPerResident * 11 + intellectualCapacities * 7 + random.gauss(0, 300)
    if(salary < 0):
        salary = 0
   
    nation.persons.append(Person(
        grossSalary=salary,
        netSalary=salary,
        age=age,
        intellectualCapacities=intellectualCapacities,
        health=100
    ))



def updatePopulation(factor: int, nation: Nation):
    populationCount = len(nation.persons) 
    for i in range(math.ceil(populationCount * factor - populationCount)):
        newPerson(nation, 0)



def cycle(nation: Nation, monthNum: int):

    i=0
    for person in nation.persons:
        # Collect tax to national budget
        nation.budget += person.grossSalary * nation.incomeTax / 100
        # Pay taxes
        person.netSalary = person.grossSalary - (person.grossSalary * nation.incomeTax / 100)
        # increase age
        if(monthNum % 12 == 0):
            person.age += 1

            # death
            if(person.age > random.gauss(70, 20)):
                del nation.persons[i]

        if(person.netSalary < 100 and random.randint(1, 4) == 1):
            del nation.persons[i]

        i += 1




    # Finance education :
    nation.budget -=  nation.budget * nation.educationSpending / 100

    # data["editable"]["education spending"]["value"] = round(data["national budget"]["value"] / data["editable"]["education spending"]["value"] * 100

    return nation


def newNation(initialBudget: int, otherNationRevenues: int) -> Nation:
    nationName = ""
    incomeTax = None
    educationSpending = None

    while nationName == "":
        nationName = input("Nation name : ")
    while incomeTax == None or incomeTax < 0 or incomeTax > 100:
        try:
            incomeTax = int(input("Income tax %: "))
        except:
            pass
    while educationSpending == None or educationSpending < 0 or educationSpending > 100:
        try:
            educationSpending = int(input("Education spending (% of budget): "))
        except:
            pass

    nation = Nation(
        name=nationName,
        budget=initialBudget,
        incomeTax=incomeTax,
        educationSpending=educationSpending,
        otherRevenues=otherNationRevenues,
        persons=[],
    )

    return nation


def humanReadableNumber(num: int) -> str:
    num_str = '{:,}'.format(round(num))
    return num_str.replace(',', "'")



def printStats(nation: Nation, monthNum: int, oldStats: Stats, oldNation: Nation):
    averageSalary = 0
    unemployedCount = 0
    
    if(len(nation.persons)  > 0 ):
        for people in nation.persons:
            if(people.netSalary < 50):
                unemployedCount += 1
            averageSalary += people.netSalary

        averageSalary = averageSalary / len(nation.persons)

        print("Month : " + str(monthNum))

        if oldNation.budget > nation.budget:
            printRed("national budget : " + humanReadableNumber(nation.budget) + " $$")
        else:
            printGreen("national budget : " + humanReadableNumber(nation.budget) + " $$")
        if (oldNation.budget * oldNation.educationSpending) > (nation.budget * nation.educationSpending):
            printRed("education spending : " + humanReadableNumber(nation.budget * nation.educationSpending / 100) + " $$")
        else:
            printGreen("education spending : " + humanReadableNumber(nation.budget * nation.educationSpending / 100) + " $$")
        if (oldNation.budget * oldNation.educationSpending / len(oldNation.persons)) > (nation.budget * nation.educationSpending / len(nation.persons)):
            printRed("education spending per resident : " + humanReadableNumber(nation.budget * nation.educationSpending / 100 / len(nation.persons)) + " $$")
        else:
            printGreen("education spending per resident : " + humanReadableNumber(nation.budget * nation.educationSpending / 100 / len(nation.persons)) + " $$")
        print()
        if len(oldNation.persons) > len(nation.persons):
            printRed("total population : " + humanReadableNumber(len(nation.persons)))
        else:
            printGreen("total population : " + humanReadableNumber(len(nation.persons)))
        if oldStats.unemployedCount / len(oldNation.persons) > unemployedCount / len(nation.persons):
            printRed("unemployment rate : " + str(round(unemployedCount / len(nation.persons) * 100, 2)) + "%")
        else:
            printGreen("unemployment rate : " + str(round(unemployedCount / len(nation.persons) * 100, 2)) + "%")
        if(oldStats.averageSalary > averageSalary):
            printRed("average salary : " + humanReadableNumber(averageSalary) + " $$")
        else:
            printGreen("average salary : " + humanReadableNumber(averageSalary) + " $$")


    return Stats(
        averageSalary=averageSalary,
        unemployedCount=unemployedCount
    )
    # print("number of unemployed : " + str(countUnemployed(peoples)))





def printRed(value): print("\033[41m{}\033[0m ▼▼" .format(value))
def printGreen(value): print("\033[42m{}\033[00m ▲▲" .format(value))
def printBlue(value): print("\033[44m{}\033[00m" .format(value))

start()