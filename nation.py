from person import *
class Nation:
    def __init__(self, budget: int, incomeTax: int, educationSpending: int, persons: List[Person]):
        self.budget = budget
        self.incomeTax = incomeTax
        self.educationSpending = educationSpending
        self.persons = persons