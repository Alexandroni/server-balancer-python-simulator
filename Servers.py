# -*- coding: utf-8 -*-

from Server import Server

class Servers:
    
    def __init__(self, Umax, Ttmax):
        self.sList = []
        self.Umax = Umax
        self.Ttmax = Ttmax
        self.serverIdCount = 0
        self.userIdCount = 0
        self.costs = 0
        self.serverListPerTick = []
        self.tickCount = 0
    #----------------------------------------------------------
    
    def createServer(self, id):
        #create server
        s = Server(id, self.Umax, self.Ttmax)
        
        #append to the list
        self.sList.append(s)
    #----------------------------------------------------------
    
    def addUser(self):
        #verify if there are any server
        if (len(self.sList) == 0):
            
            self.serverIdCount += 1
            self.userIdCount += 1
            
            self.createServer(self.serverIdCount)
            
            self.sList[-1].addUser(self.userIdCount)
            
        else:
            tryToAdd = None
            self.userIdCount += 1
            
            for s in self.sList:
                tryToAdd = s.addUser(self.userIdCount)
                
                if (tryToAdd == True):
                    break
            
            if (tryToAdd != True):
                self.serverIdCount += 1
                
                self.createServer(self.serverIdCount)
                
                self.sList[-1].addUser(self.userIdCount)                
    #----------------------------------------------------------
    
    def incrementTicks(self):
        
        self.tickCount += 1
        
        if (len(self.sList) == 0):
            print('There are no servers o increment')
        else:
            for s in self.sList:
                s.incrementTick()
                
        #increment costs
        self.costs += len(self.sList)
        
        self.serverListPerTick.append(len(self.sList))
        
        #loop to get the useless server
        for s in self.sList:
            newList = [x for x in self.sList if len(x.users) != 0]
            self.sList = newList
            del(newList)
            
        
        
        #print('\n')
        #print('--------------')
        #print('TickCount = '+str(self.tickCount))
        #print('--------------')
    
    def printServers(self):
        if (len(self.sList) == 0):
            print('There are no servers')
        else:
            for s in self.sList:
                s.printServerUsers()
    #----------------------------------------------------------
    
    def printCosts(self):
        print ('Costs = $'+str(self.costs))
        
    
    def printServersForOutput(self):
        
        if (len(self.sList) == 0):
            return "0"
        
        line = ""
        
        for s in self.sList:
            if (line == ""):
                line = str(s.getNumberOfUsers())
            else:
                line = line+","+str(s.getNumberOfUsers())
                
        return line
        
         
#------------------------------------------------------------------------
                

#s = Servers(2, 4)



#print(s.sList)

#1
#3
#0
#1
#0
#1
#0
#0
#0
#0

#s.incrementTicks()
#s.addUser()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.addUser()
#s.addUser()
#s.addUser()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.addUser()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.addUser()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.incrementTicks()
#s.printServers()
#s.printServersForOutput()
#
#s.printCosts()
#
#print(s.ss)
#
#print(sum(s.ss))
