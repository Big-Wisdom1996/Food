'''
source = open(r"/users/elihermann/documents/github/food/source.txt",'w')

source.write("Eli\n")
source.write("Rules\n")
source.write("schools\n")
source.write("fools")

source.close()
'''
def grabLine(line):
    source = open(r"/users/elihermann/documents/github/food/source.txt",'r')
    for x in range (0,line):
        data = source.readline()
    source.close()
    return data

def findInventory(ingredient):
    done = 0
    x = 1
    while(done == 0):
        #grab the type of line
        type = grabLine(x).split(" ")
        #compare type to desired type
        if(type[0] == ingredient):
            print("Yes")
            done = 1
        else:
            x += 1 
        
    #return line
    return type[1]
    
def placeDish(content):
    source = open(r"/users/elihermann/documents/github/food/source.txt",'a')
    source.write("\nD "+content)
    source.close()
    
def placeIngredient(content):
    source = open(r"/users/elihermann/documents/github/food/source.txt",'a')
    source.write("\nI "+content)
    source.close()
    
def placeInventory(content):
    source = open(r"/users/elihermann/documents/github/food/source.txt",'a')
    source.write("\nWInv "+content)
    source.close()
    
def placeActual(content):
    source = open(r"/users/elihermann/documents/github/food/source.txt",'a')
    source.write("\nAInv "+content)
    source.close()
    
def newDish():
    placeDish(input("What's the dish?: "))
    done = 0
    while(done == 0):
        answer = input("Ingredient: ")
        if (answer == "no"):
            done = 1
        else:
            placeIngredient(answer)
            placeActual("")
            placeInventory(input("Weekly Inventory: "))
            
newDish()