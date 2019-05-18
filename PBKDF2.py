from passlib.hash import pbkdf2_sha512 as pbkdf2

myPass1 = "changeme"
myPass2 = "123456"
myPass3 = "password"
salt = b'ZDzPE45C'

myHash1 = pbkdf2.hash(myPass1, rounds=8000, salt=salt)
myHash2 = pbkdf2.hash(myPass2, rounds=8000, salt=salt)
myHash3 = pbkdf2.hash(myPass3, rounds=8000, salt=salt)

print("PBKDF2 Hash of {}: {}...    (salt= {})".format(myPass1, myHash1[32:38], myHash1[20:31]))
print("PBKDF2 Hash of {}: {}...    (salt= {})".format(myPass2, myHash2[32:38], myHash2[20:31]))
print("PBKDF2 Hash of {}: {}...    (salt= {})\n".format(myPass3, myHash3[32:38], myHash3[20:31]))

print("PBKDF2 Verification of {}: {}".format(myPass1, pbkdf2.verify(myPass1, myHash1)))
print("PBKDF2 Verification of {}: {}".format(myPass2, pbkdf2.verify(myPass2, myHash2)))
print("PBKDF2 Verification of {}: {}\n".format(myPass3, pbkdf2.verify(myPass3, myHash3)))

print("Dummy Test of {}: {}".format(myPass2, pbkdf2.verify("654321", myHash2)))
