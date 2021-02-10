import numpy as np
from random import randint 
from name_generation import name_gen as ng  
class Map: 
    def __init__(self, x_size = 10, y_size = 10):
        self.x_size = x_size
        self.y_size = y_size
        self.map = []
        #self.resources = {'water' : randint(0, 100), 'metals' : randint(0, 100), 'temp' : randint(0, 100)}
        self.nameGen = ng.nameGen('name_generation/data_files/cities500.csv', 3)
        self.build(self.x_size, self.y_size)
    def build(self, x_size, y_size):
        for x in range(x_size):
            for y in range(y_size):
                self.map.append({self.nameGen.generate(self.nameGen.chain): {}, 'resources': {'water' : randint(0, 100), 'metals' : randint(0, 100), 'temp' : randint(0, 100)}})
                #appends properties to each point on the map
         
    

                        
        
test = Map()
print(test.map)        
        