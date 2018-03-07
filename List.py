
source = open(r"/users/elihermann/documents/github/food/source.txt",'w')

source.write("Eli\n")
source.write("Rules\n")
source.write("schools\n")
source.write("fools")

source.close()

source = open(r"/users/elihermann/documents/github/food/source.txt",'r')

line1 = source.readline()
line2 = source.readline()

print(line1)
print(line2)

source.close()
