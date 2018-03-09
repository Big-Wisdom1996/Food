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

def main():            
    line = grabLine(1)  
    x = 1 
    dish,ingredient, AInv, WInv = "","","",""
    
    while(line != "END END"): #Surf through entire document
        line = grabLine(x)
        if(len(line) != 1):
            prefix = line.split(" ")[0]
            content = line.split(" ")[1]
        if(prefix == "D"): #Sort content
            dish = content
        elif(prefix == "I"):
            ingredient = content
        elif(prefix == "AInv"):
            AInv = eval(content[0])#store as integer
        elif(prefix == "WInv"):
            WInv = eval(content[0])#store as integer
            
        if(ingredient!="" and AInv!="" and WInv!=""): #When all content is full print and reset content
            need = WInv - AInv
            print("You need",need,ingredient)
            ingredient, AInv, WInv = "","",""
            
        x += 1
main()

