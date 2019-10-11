# -*- coding: utf-8 -*-

from User import User

class Server:
    
    def __init__(self, id, Umax, Ttmax):
        self.users = []
        self.id= id
        self.Umax = Umax
        self.Ttmax = Ttmax
    #----------------------------------------------------------
    
    
    def addUser(self, id):
        
        #create user
        newUser = User(id)
        
        if (len(self.users) < self.Umax):
            #append
            self.users.append(newUser)
            return True
        else:
            #raise Exception('The server is full')
            print('Try to add user '+str(id)+', but the Server id= '+str(self.id)+', The server is full')
            return False

    #----------------------------------------------------------
    
    def incrementTick(self):
        #loop to increment
        for u in self.users:
            u.incrementTicks()
        
        #remove users done
        self.removeUsersFinished()
    #----------------------------------------------------------
        
    def removeUsersFinished(self):
        #interate the list and get only the users that have ticks less than Ttmax
        newList = [x for x in self.users if x.ticksCount < self.Ttmax]
        self.users = newList
        del(newList)
    #----------------------------------------------------------
    
    
    def printServerUsers(self):
        
        if (len(self.users) == 0):
            print('Serverid = '+str(self.id)+'No more users left on server')
        else:
            print('------------------------')
            print('Serverid = '+str(self.id))
            for u in self.users:
                u.printUser()
    #----------------------------------------------------------
    
    def getNumberOfUsers(self):
        return len(self.users)
    #----------------------------------------------------------

#------------------------------------------------------------------------  
        
    
#s = Server(1,2,4)

#s.addUser(1)
#s.addUser(2)
#s.addUser(3)

#s.printServerUsers()
    