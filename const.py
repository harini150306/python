# constructor 
class car:
    def __init__(self):
        print("this is an constructor")
        self.wheels = 23
        self.miliage =12
        self.airbags =77.089
    
car1 = car()
print(car1.miliage)

car2 =car()
print(car2.wheels)
print(car2.miliage)
car2.miliage =2.5
print(car2.miliage)

