'''''class Car:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def max_speed(self,speed):
        return f'the {self.color} runs at the speed of{speed} km/hr'

vehicle = Car("skoda","cyan")
print(vehicle.max_speed(100))'''

'''deck = [str(x)+y for x in range(1,14) for y in ["S","H","C","D"]]
val=[]
for i in range(3,16):
    for j in range(0,4):
        val.append(i)
print(val)
print(deck)
print(dict(zip(deck,val)))
player1 = str(input('enter the player1 name:'))
player2 = str(input('enter the player2 name:'))'''

'''v=[]
for x in range (1,10):
    v.append(x)
    print(x)
c = v[1::2]
print(c)'''

'''import random

list = [1,2,3,4]
random.shuffle(list)
print(list)'''

''''import random
list =[1,2,3,4]
for x in range(5):
    random.shuffle(list)
    print(list)'''

''''list = [[1,2],[2,3],[3,4]]
list1=[]
list2=[]
for x in (list):
    list1.append(x[0])
    list2.append(x[1])
print(list1)
print(list2)   seperating  the numberslist within in the list into seperate lists'''

'''list = [[1,2],[2,3],[3,4]]
list1,list2 = zip(*list)
print(list1)
print(list2)''' # unzipping method



import random

suits =["hearts","spades","clubs","diamonds"]
ranks =["2","3","4","5","6","7","8","9","10","j","q","k","a"]
deck=[]
for suit in suits:
    for rank in ranks:
       deck.append(f'{rank} of {suit}')
    print(deck)
str(input('enter the player1 name:'))
str(input('enter the player2 name:'))
player1=[]
player2=[]

while len(player1)<26:
   card = random.choice(deck)
   deck.remove(card)
   player1.append(card)
   card2 = random.choice(deck)
   deck.remove(card2)
   player2.append(card2)
print(player1)
print(player2)
def val(sum):
    count =0
    for i in sum:
        ch = i[0]
        if ch=='a':
            count+=14
        elif ch=='k':
            count+=13
        elif ch=='q':
            count+=12
        elif ch=='j':
            count+=11
        elif (ch=='1'):
            count+=10
        else:
            count+=int(ch)
    return count

def final(player1,player2):
  count1 =  val(player1)
  count2 = val(player2)
  if (count1>count2):
      print('player1 is the winner')
  elif(count1==count2):
      print('tie up')
  else:
      print('player2 is the winner')

print('player1 has cards:',val(player1))
print('player2 has cards:',val(player2))

final(player1,player2)


