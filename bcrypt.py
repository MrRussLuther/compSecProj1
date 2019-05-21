from passlib.hash import md5_crypt, sha1_crypt, sha256_crypt, sha512_crypt, des_crypt

var = "Hello"

salt = "ZDzPE45C"
desSalt = "e4"

md5 = md5_crypt.hash(var, salt=salt)
sha1 = sha1_crypt.hash(var, salt=salt)
sha256 = sha256_crypt.hash(var, salt=salt)
sha512 = sha512_crypt.hash(var, salt=salt)
des = des_crypt.hash(var, salt=desSalt)

print("MD5 Hash of {}: {}...    Length = {}".format(var, md5[12:18], len(md5)))
print("SHA1 Hash of {}: {}...    Length = {}".format(var, sha1[13:19], len(sha1)))
print("SHA256 Hash of {}: {}...    Length = {}".format(var, sha256[26:32], len(sha256)))
print("SHA512 Hash of {}: {}...    Length = {}".format(var, sha512[26:32], len(sha512)))
print("Des hash of {}: {}...    Length = {}".format(var, des, len(des)))
