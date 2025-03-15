## Écrivez votre code ici !
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return f"Je m'appele {self.name} et j'ai {self.age} ans !"


class Employee(Person):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        base = super().display_details()
        return base + f" et je gagne {self.salary}€ par mois"


employee = Employee("arthur", "25", 2000)
print(employee.display_details())
