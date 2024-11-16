from person import *
class Nation:
    def __init__(self, budget: int, incomeTax: int, educationSpending: int, persons: list[Person], retirementAge: int, retirement):
        self.budget = budget
        self.incomeTax = incomeTax
        self.educationSpending = educationSpending
        self.persons = persons

    def __str__(self):
        return (f'Nation(budget={self.budget}, incomeTax={self.incomeTax}, '
                f'educationSpending={self.educationSpending}, persons={self.persons})')