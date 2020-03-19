
import random

data = ["Enter Password: ","%s","Wrong","Correct!!!"]
code = ["0x01020000","0x0c220002","0x01020001","0x0c230002","0x0900000D","0x01020002","0x0c220002",
        "0x010200FF","0x0c240002","0x01020003","0x0c220002","0x01020000","0x0c250002"]

codeCounter     = 0                                      
linecodeCounter = 13
opCode          = ["XOR","SUB","MUL","DIV","ADD"]
opCodeSig       = ["^","-","*","/","+"]
opCodeHex       = ["0x04","0x03","0x05","0x06","0x00"]
flag            = "REB{VM_P4CK3R5_AR3_S0_TRICKY_MR_L337}"

print ".TEXT"
print "0\tMOV\tR2 0x0"
print "1\tTRAP\tOUT R2"
print "2\tMOV\t R2 0x1"
print "3\tTRAP\tIN R2"
print "4\tJMP\t 0xD"
print "5\tMOV\t R2 0x2"
print "6\tTRAP\tOUT R2"
print "7\tMOV\t R2 0xFF"
print "8\tTRAP\tHALT R2"
print "9\tMOV\t R2 0x3"
print "10\tTRAP\tOUT R2"
print "11\tMOV\t R2 0x0"
print "12\tTRAP\tHALT R2"

for i in flag:
    rand0 = random.randint(2,30)
    rand1 = random.randint(30,60)
    while True:
        randop0 = random.randint(0,4)
        randop1 = random.randint(0,4)
        if not randop0 == randop1:
            if opCode[randop0] == "DIV" or opCode[randop0] == "SUB":
                randop1 = 4
                rand1 = random.randint(2,6)
            if opCode[randop1] == "DIV" or opCode[randop1] == "SUB":
                randop0 = 4
                rand1 = random.randint(2,6)
            if opCode[randop1] == "MUL":
                rand1 = random.randint(2,6)
            if opCode[randop0] == "MUL":
                rand0 = random.randint(2,6)                                    
            break
    print str(linecodeCounter) + "\tLOAD\tR1 " + str(hex(codeCounter))
    linecodeCounter+=1
    print str(linecodeCounter) + "\tMOVR\tR0 R1"
    linecodeCounter+=1
    print str(linecodeCounter) + "\t" + opCode[randop0] + "\t" + "R0 " + str(hex(rand0))
    linecodeCounter+=1
    print str(linecodeCounter) + "\t" + opCode[randop1] + "\t" + "R0 " + str(hex(rand1))
    linecodeCounter+=1
    res = eval("hex((" + str(ord(i)) + " " + opCodeSig[randop0] + str(rand0) + ")" + opCodeSig[randop1] + str(rand1) + ")" )
    print str(linecodeCounter) + "\tCMP\tR0 " +  res
    linecodeCounter+=1
    print str(linecodeCounter) + "\tJNE\t0x5"
    r = str(hex(codeCounter)).replace("0x","")
    if len(r) == 1:
      r = "0" + r
    code.append("0x070100" + r)
    code.append("0x02000001")
    t = str(hex(rand0)).replace("0x","")
    if len(t) == 1:
        t = "0" + t
    code.append(opCodeHex[randop0] + "0000" + t)
    t = str(hex(rand1)).replace("0x","")
    if len(t) == 1:
        t = "0" + t
    code.append(opCodeHex[randop1] + "0000" + t)
    res = str(res).replace("0x","")
    if len(res) == 1:
        res = "000" + res
    if len(res) == 3:
        res = "0" + res
    if len(res) == 2:
        res = "00" + res
    code.append("0x0800" + res)
    code.append("0x0b000005")
    linecodeCounter+=1
    codeCounter+=1
print "JE 0x9"
code.append("0x0a000009")

print "\n.DATA"
for i in range(len(data)):
   print '{} "{}"'.format(i,data[i])

file = open("code.r","w")
file.write(str(code).replace("'","").replace("[","{").replace("]","}"))
file.close()