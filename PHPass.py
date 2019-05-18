from passlib.hash import phpass

var1 = "changeme"
var2 = "123456"
var3 = "password"
salt1 = "ZDzPE45C"
salt2 = "C54EPzDZ"
salt3 = "PEzS45CZ"

myHash1 = phpass.hash(var1, salt=salt1)
myHash2 = phpass.hash(var2, salt=salt2)
myHash3 = phpass.hash(var3, salt=salt3)

print("PHPPass Hash of {}: {}".format(var1, myHash1))
print("PHPPass Hash of {}: {}".format(var2, myHash2))
print("PHPPass Hash of {}: {}\n".format(var3, myHash3))

print("PHPPass Verification of Hash {}: {}".format(var1, phpass.verify(var1, myHash1)))
print("PHPPass Verification of Hash {}: {}".format(var1, phpass.verify(var2, myHash2)))
print("PHPPass Verification of Hash {}: {}\n".format(var1, phpass.verify(var3, myHash3)))

print("Dummy Test of {} Hash: {}".format(var3, phpass.verify("passward", myHash3)))
