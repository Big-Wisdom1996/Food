import pickle
    
    
'''
#Serialize data
outfile = open("/users/elihermann/documents/github/food/pickle.dat","wb")
pickle.dump(eli, outfile)
pickle.dump(thomas, outfile)
outfile.close()

#deserialize data
infile = open("pickle.dat","rb")
print(pickle.load(infile))
print(pickle.load(infile))
infile.close()
'''          
from tkinter import *

def openLists():
    infile = open("/users/elihermann/documents/github/food/pickle.dat","rb")
    temp = (pickle.load(infile))
    infile.close()
    return temp

def saveLists(dishName):
    outfile = open("/users/elihermann/documents/github/food/pickle.dat","wb")
    pickle.dump(dishName,outfile)
    outfile.close()
    
def addDish(dishName):
    list.append([dishName])
    
def addIngredient(dishName,ingredient):
    for i in range(0,len(list)):
        if(dishName in list[i]):
            list[i].append(ingredient)
        
def printEntry():
    print(name.get())



list = []
addDish("Pizza")
addIngredient("Pizza","Cheese")
addIngredient("Pizza","Pepperoni")
addDish("Cereal")
addIngredient("Cereal","Milk")
addIngredient("Cereal","Cereal")

#interface to display the dish and ingredients
window = Tk()
window.title("Food!")

#create a frame for dishes and add it to window
frame1 = Frame(window, bg = "Yellow") 
frame1.grid(row = 1, column = 1)

#create a dish label
dish1 = Label(frame1,text = list[0][0])
dish1.grid(row= 1, column = 1)

dish2 = Label(frame1, text = list[1][0])
dish2.grid(row = 2,column = 1)

#create a frame for ingredients
frame2 = Frame(window)
frame2.grid(row = 1, column = 2)

#create ingredient label
ingredient = Label(frame2, text = list[0][1:])
ingredient.grid(row = 1, column = 1)

#create ingredient label
ingredient2 = Label(frame2, text = list[1][1:])
ingredient2.grid(row = 2, column = 1)




window.mainloop()


