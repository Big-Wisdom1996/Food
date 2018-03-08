import pickle

eli = 5
thomas = 6

outfile = open("/users/elihermann/documents/github/food/pickle.dat","wb")
pickle.dump(eli, outfile)
pickle.dump(thomas, outfile)
outfile.close()

infile = open("pickle.dat","rb")
print(pickle.load(infile))
print(pickle.load(infile))
infile.close()
            
