#######################################################################################
#                                                                                     #
#     Source file must be formatted correctly                                         #
#     1) if line has anything, it must only have two things separated by one space    #
#     2) must end with "END END"                                                      #
#                                                                                     #
#######################################################################################


def grabLine(line):
    source = open(r"/users/elihermann/documents/github/food/source.txt",'r')
    for x in range (0,line):
        data = source.readline()
    source.close()
    return data

def main():            
    line = grabLine(1)  
    x = 1 
    dish,ingredient, AInv, WInv = "","","",""
    
    while(line != "END END"): #Surf through entire document
        line = grabLine(x)
        
        #sort content of a line by its prefix
        if(len(line) != 1):
            prefix = line.split(" ")[0]
            content = line.split(" ")[1]
        if(prefix == "D"): #right now this is pointless
            dish = content
        elif(prefix == "I"):
            ingredient = content
        elif(prefix == "AInv"):
            AInv = eval(content[0])#store as integer, and you have to put the [0] here because
        elif(prefix == "WInv"):    #the string actually has a \n charachter in it which screws it up
            WInv = eval(content[0])#store as integer
            
        #When all content is full print and reset content
        if(ingredient!="" and AInv!="" and WInv!=""): 
            need = WInv - AInv
            print("You need",need,ingredient)
            ingredient, AInv, WInv = "","",""
            
        x += 1
main()

