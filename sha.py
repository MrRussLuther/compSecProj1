from passlib.hash import sha256_crypt as sha256

salt = "8sFt66rZ"
myPass1 = "changeme"
myPass2 = "123456"
myPass3 = "password"

myHash1 = sha256.using(rounds="12345").hash(myPass1, salt=salt)
myHash2 = sha256.using(rounds="12345").hash(myPass2, salt=salt)
myHash3 = sha256.using(rounds="12345").hash(myPass3, salt=salt)

print("SHA256 Hash of {}: {}".format(myPass1, myHash1))
print("SHA256 Hash of {}: {}".format(myPass2, myHash2))
print("SHA256 Hash of {}: {}\n".format(myPass3, myHash3))
print("Verification of {} Hash: {}".format(myPass1, sha256.verify(myPass1, myHash1)))
print("Verification of {} Hash: {}".format(myPass2, sha256.verify(myPass2, myHash2)))
print("Verification of {} Hash: {}\n".format(myPass3, sha256.verify(myPass3, myHash3)))

print("Dummy Test of {}: {}".format(myPass1, sha256.verify("chungeme", myHash1)))
