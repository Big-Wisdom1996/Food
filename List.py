
source = open(r"/users/elihermann/documents/github/food/source.txt",'w')

source.write("Eli\n")
source.write("Rules\n")
source.write("schools\n")
source.write("fools")

source.close()

def grabLine(line):
    source = open(r"/users/elihermann/documents/github/food/source.txt",'r')
    for x in range (0,line):
        data = source.readline()
    return data

print(grabLine(2))