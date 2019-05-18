from passlib.hash import lmhash
from passlib.hash import nthash

myPass = "Napier"
mySecPass = "Foxtrot"

lmhash1 = lmhash.hash(myPass)
nthash1 = nthash.hash(myPass)
lmhash2 = lmhash.hash(mySecPass)
nthash2 = nthash.hash(mySecPass)

print("LM Hash of {}: {}".format(myPass, lmhash1))
print("NT Hash of {}: {}\n".format(myPass, nthash1))

print("LM Hash of {}: {}".format(mySecPass, lmhash2))
print("NT Hash of {}: {}".format(mySecPass, nthash2))
