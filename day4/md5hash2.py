import hashlib
from hashlib import md5

key = "iwrupvqb"
count = 1

while(True):
    hexm = md5((key + str(count)).encode()).hexdigest()
    
    if(hexm[0:6] != "000000"):
        count += 1
    if(hexm[0:6] == "000000"):
        print(count)
        break