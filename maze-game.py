import random

green='\033[0;32m'
yellow='\033[0;93m'
red='\033[0;31m'
purple ='\033[0;35m'
blue='\033[0;34m'
orange='\033[0;34m'
cyan='\033[0;36m'
white='\033[1;37m'
lightblue='\033[1;34m'

'''
Black        0;30     Dark Gray     1;30
Red          0;31     Light Red     1;31
Green        0;32     Light Green   1;32
Brown/Orange 0;33     Yellow        1;33
Blue         0;34     Light Blue    1;34
Purple       0;35     Light Purple  1;35
Cyan         0;36     Light Cyan    1;36
Light Gray   0;37     White         1;37
'''


maze=[
  #0123456789
  'xxxxxxxxxx',#0
  'x    x x x',#1
  'x  x x   x',#2
  'xx x   xxx',#3
  'x  x x   x',#4
  'xxxx x xxx',#5
  'x  x x x x',#6
  'x xx x   x',#7
  'x    x x x',#8
  'xxxxxxxxxx' #9
  #0123456789
]
# maze=[
# "xxxx",
# "x  x",
# "x  x",
# "xxxx"
# ]
placebeen= "+"
placebeenoutput= "[]"
you="p"
yououtput="pp"
barrier="x"
barrieroutput="\u2588\u2588"
end = "e"
endoutput= "ee"
space= " "
spaceoutput="  "
pmaze= [" "*len(maze[0])]*len(maze)

px = 8
py = 8
ex = 1
ey = 1
def printin():
  print("\x1B[0;0H")
  print("\x1B[2J")

  print(yellow +"\nThis is The Maze Game.\nYour goal is to get to the end.\npp represents you, the player.\n[] represents the places you have already been.\n" + barrieroutput+" represents a wall that you can't go through.\n"+white)
printin()
def setcoordpp():
  global px
  global py
  badspot = True
  while badspot:
    px=random.randint(1,len(maze[0])-2)
    py=random.randint(1,len(maze)-2)
    badspot= maze[py][px] == barrier
setcoordpp()

def setcoordee():
  global ex
  global ey
  badspot = True
  while badspot:
    ex=random.randint(1,len(maze[0])-2)
    ey=random.randint(1,len(maze)-2)
    badspot= maze[ey][ex] == barrier or (px==ex and py==ey)
setcoordee()



def printmaze(mazearray,printee= False):
  printin()
  for ind in range(0,len(mazearray)):
    newl = ""
    #for ch in maze[ind]:
    for chnum in range(0,len(mazearray[ind])):
      if ind == py and chnum == px:
        a= yououtput
      #if ch == 'x':
      elif mazearray[ind][chnum] == barrier:
        a=white + barrieroutput
      elif mazearray[ind][chnum]==placebeen:
        a= placebeenoutput
      elif ind == ey and chnum == ex:
        if printee:
          a= endoutput
        else:
          a=spaceoutput  
      else:
        #a= ch+ch
        a= mazearray[ind][chnum]+mazearray[ind][chnum] 
      newl += a
    print(newl)
    

def changechar(pmaze,px,py,ch):
  z=pmaze[py]
  z1= z[0:px]
  z2= ch
  z3= z[px+1:]
  
  pmaze[py] = z1 + z2 + z3 

def movedir(move):
  z= movevals[move]
  dx = z["dx"]
  dy = z["dy"]
  global px
  global py
  if maze[py+dy][px+dx] == " ":
    changechar(pmaze,px,py,placebeen)
    px+=dx
    py+=dy
    return True
  else:
    changechar(pmaze,px+dx,py+dy,'x')
    return False

movevals={
  's': {'dx': 0,'dy': 1},
  'w': {'dx': 0,'dy':-1},
  'a': {'dx':-1,'dy': 0},
  'd': {'dx': 1,'dy': 0}
}
  
finished = False


def badinp(inp):
  if inp=="":
    return True
  inp= inp.strip()
  inp=inp[0]
  inp= inp.lower()
  if not (inp in "wasd"):
    return True
  else:
    return False



while not finished:
  direc= "xyz"
  badmess=""
  while badinp(direc):
    printmaze(pmaze)
    print(red+badmess)
    direc = input(white+"What direction do you want to move? (w,a,s,d ) ")
    badmess= "badinput"
  firstch= direc[0]    
  if not movedir(firstch):
    print("You've hit a wall ")
    printmaze(pmaze)
  else: 
    # printmaze(maze,True)
    printmaze(pmaze)
  if px == ex and py == ey:
    finished = True
    print(green+"Congradulations, You've won")

# printmaze(pmaze)




    












 