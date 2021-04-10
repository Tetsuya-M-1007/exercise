class Living:
    def __init__(self):
        self.oneself = None
        self.dog = None
        self.cat = None

    def name(self):
        print(f"My name is {self.oneself}") 
        print(f"My dog is {self.dog}")
        print(f"My cat is {self.cat}")     

class LivingAdd(Living):
    def __init__(self):
        super().__init__()
        self.father = None
        self.mother = None
        self.brother = None
        self.sister = None

    def name(self):
        print(f"My father is {self.father}")
        print(f"My mother is {self.mother}")
        print(f"My brother is {self.brother}")
        print(f"My sister is {self.sister}")
        print(f"My name is {self.oneself}")
        print(f"My dog is {self.dog}")
        print(f"My cat is {self.cat}")