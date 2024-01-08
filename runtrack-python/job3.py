class Operation:
    
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

        
    def adition(self):
        return self.nombre1 + self.nombre2
    
    
    
Ope = Operation(12,3)
print(Ope.adition())


print(Ope)