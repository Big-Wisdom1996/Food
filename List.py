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

def newDish(dishName):
    outfile = open("/users/elihermann/documents/github/food/pickle.dat","wb")
    pickle.dump(dishName,outfile)
    outfile.close()
    
def readFile():
    infile = open("/users/elihermann/documents/github/food/pickle.dat","rb")
    print(pickle.load(infile))
    infile.close()
    
newDish("Eli")
newDish("Soup")
readFile()
readFile()

