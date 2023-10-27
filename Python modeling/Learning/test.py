arr = [] #- масив
set =  set() # - невпорядкований масив без індексів та дублікатів
tuple = (3,2,4,5) # - масив з незмінними елементами  

comprehension = [i**2 for i in range(0,100)]
generator = (i**3 for i in range(0,100))

print(next(generator))

class ComputationalModel():
    def __init__(self,betta,gamma,delta):
        self.betta = betta
        self.gamma = gamma
        self.delta = delta
    @staticmethod # - метод, що не може змінювати сам об'єкт та його властивості 
    def hi():
        print("Hi!")

class ImportantFunc():
    def __init__(self) -> None:
        pass
    def importantFunc(self):
        ...

class SIRModel(ComputationalModel,ImportantFunc): # - моде наслідувати більше ніж один клас
    def __init__(self, betta, gamma, delta):
        super().__init__(betta, gamma, delta) # - поінтер на батьківський клас 