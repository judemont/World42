class Person:
    def __init__(self, fortune: int, age: float, income: int, educationLevel: int):
        self.fortune = fortune
        self.age = age
        self.educationLevel = educationLevel
        self.income = income
    
    def __str__(self):
        return f"Person(fortune={self.fortune}, age={self.age}, income={self.income}, educationLevel{self.educationLevel})"