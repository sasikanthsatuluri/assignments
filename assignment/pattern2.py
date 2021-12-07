#PRINT
'''        *
          ***
         *****
        *******
       *********
      ***********
'''
no_of_stars = 1
for x in range(6,0,-1):    #line creating
    for y in range(x):
        print(" ",end = "") #space creating
    for z in range(no_of_stars):
        print("*",end = " ")
    print("\n")
    no_of_stars +=1