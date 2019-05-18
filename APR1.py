from passlib.hash import apr_md5_crypt as apr

myPass1 = "changeme"
myPass2 = "123456"
myPass3 = "password"
salt1 = "RVVoTUuX"
salt2 = "G.raku4o"
salt3 = "ouhEhI3L"

apr1 = apr.hash(myPass1, salt=salt1)
apr2 = apr.hash(myPass2, salt=salt2)
apr3 = apr.hash(myPass3, salt=salt3)

print("APR Hash of {}: {}".format(myPass1, apr1))
print("APR Hash of {}: {}".format(myPass2, apr2))
print("APR Hash of {}: {}\n".format(myPass3, apr3))

print("APR Verification of Hash {}: {}".format(myPass1, apr.verify(myPass1, apr1)))
print("APR Verification of Hash {}: {}".format(myPass2, apr.verify(myPass2, apr2)))
print("APR Verification of Hash {}: {}\n".format(myPass3, apr.verify(myPass3, apr3)))

print("Dummy test of Hash {}: {}".format(myPass3, apr.verify("passward", apr3)))
