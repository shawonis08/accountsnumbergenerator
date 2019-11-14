import random
startVal = "210"
firstendVal = "00"
with open ("file.txt","w") as out:
    for i in range(0,500):
        lastendval = str(random.randint(1,2))
        middlevalue = str(random.randint(1111111,9999999))
        val = startVal+middlevalue+firstendVal+lastendval+str("\n")
        out.write(val)