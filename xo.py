##name:thomas waheed hanna
##id:20170081
##group (4)
## X O with computer
import random
board=[0,1,2,3,4,5,6,7,8]
def show():
    print (board[0],"|",board[1],"|",board[2])
    print ("---------------")
    print (board[3],"|",board[4],"|",board[5])
    print ("---------------")
    print (board[6],"|",board[7],"|",board[8])
show()
def checkline (char,spot1,spot2,spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3]==char:
        return True
def checkall(char):
    if checkline (char,0,1,2):
        return True
    if checkline (char,1,4,7):
        return True
    if checkline (char,6,7,8):
        return True
    if checkline (char,3,4,5):
        return True
    if checkline (char,0,3,6):
        return True
    if checkline (char,2,5,8):
        return True
    if checkline (char,2,4,6):
        return True
    if checkline (char,0,4,8):
        return True

while True :
    y= int (input("select a spot:"))
    if (board[y]!= "x") and (board[y]!="o"):
        board[y]="x"

        if checkall("x")== True:
            show()
            print ("<< X WINS>>")            
            break;
        
        while True:
              random.seed()
              opponent = random.randint(0,8)
        

              if (board[opponent]!="o") and (board[opponent]!="x"):
                  board[opponent] = "o"
               
                  if checkall("o")== True:
                      print ("<< O WINS>>")
                      break;
                  break;
                
    else:
        print ("this spot is taken")

    show()
            
        
        
