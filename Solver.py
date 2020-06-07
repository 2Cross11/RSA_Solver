from Crypto.Util.number import inverse
from Crypto.Util.number import long_to_bytes

p = int(input("Enter p value : "))
q =  int(input("Enter q value : "))
c = int(input("Enter c value : "))
n = p*q
phi = (p-1)*(q-1)
e = 65537
d = inverse(e,phi)
m = pow(c,d,n)
Message = (long_to_bytes(m))
print ("Flag : ",Message)
