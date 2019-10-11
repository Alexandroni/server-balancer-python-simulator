# Load Balancing

- read a file containg all users enter in each clock 'tick'

- each server can handle 'Umax' users

- each user can handle one task

- each task consumes Ttask 'ticks' to finish

- each task that finishs leaves the server


## algorithm

- create a server list

- read the file and iterate each line

- for each line add users to available servers

    - if there are no server
    
        - create a server object per iten inside the list
        
        - create a user object per iten inside the list of users
    
    - else
        
        - create a user object per iten, inside the list of users, of an 
          available server
        
    - increment ticks
    
    - write the output file line for that tick
    
- finish


## Comments

- There are print functions commented that can show the current status of the 
  servers: which server is on, how many users and which users are inside    

- There are 3 classes:
    - A User class that contain the tickCount for this user and an ID just for 
      control purpose
     
    - A Server class that contain a list with Users and an ID, again, just for 
      control purpose
      
    - A Servers class that is a list of Server 
    
- The run.py is the file that can execute the algorithm. 
  Since there are no recommendations for this simulation that should be a class, I just created a function

- The example.txt is a file with the inputs example inside de PDF of this test

- The output file always change for each running test 
