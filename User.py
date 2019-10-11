# -*- coding: utf-8 -*-

class User:
    
    def __init__(self, id):
        self.id = id
        self.ticksCount = 0
        
    def __str__(self):
        return str(self.id)
    
    def printUser(self):
        print('UserID = '+str(self.id)+', ticks = '+str(self.ticksCount))
        
    def incrementTicks(self):
        self.ticksCount += 1


#------------------------------------------------------------------------