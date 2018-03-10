'''
    Source file must be formatted correctly
    1) if you want to put .5 you have to put 0.5
    2) if a line has anything it must have two things separated by one space
    3) File must end with END END
    4) type a space after every unit
'''
import math

def grabLine(line):
    source = open(r"/users/elihermann/documents/github/food/source.txt",'r')
    for x in range (0,line):
        data = source.readline()
    source.close()
    return data

def main():            
    line = grabLine(1)  
    x = 1 
    dish,ingredient, AInv, WInv, unit= "","","","",""
    
    while(line != "END END"): #Surf through entire document
        line = grabLine(x) #grab line
        x += 1
        
        #sort content of a line by its prefix
        if(len(line) != 1):
            prefix = line.split(" ")[0]
            content = line.split(" ")[1]
            if(prefix == "D"): #right now this is pointless
                dish = content
            elif(prefix == "I"):
                ingredient = content
            elif(prefix == "AInv"):
                AInv = float(content)
            elif(prefix == "WInv"):    
                WInv = float(content)#store as integer
            elif(prefix == "Unit"):
                unit = content
                        
        #When all content is full print and reset content
        if(ingredient!="" and AInv!="" and WInv!="" and unit!=""): 
            need = WInv - AInv
            if(need > 0): #You don't need any if you have more than you need
                print("You need",math.ceil(need),unit,"of",ingredient) #round up how much you need
            ingredient, AInv, WInv,unit = "","","",""
            
main()

