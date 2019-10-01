from utilities import text2binary

def polarRZ(message):
    output = []
    for x in text2binary(message):
        if (x == '0'):
            output.append(-1)
            output.append(0)
        else:
            output.append(+1)
            output.append(0)

    return output

def AMI(message):
    output = []
    change = 1
    for x in text2binary(message):
        if (x == '0'):
            output.append(0)
        else:
            output.append(change)
            if(change == 1):
                change = -1
            else:
                change = 1
    return output

def pseudoternary(message):
    output = []
    change = 1
    for x in text2binary(message):
        if (x == '1'):
            output.append(0)
        else:
            output.append(change)
            if(change == 1):
                change = -1
            else:
                change = 1
    return output

def B8ZS(message):
    output = []
    change = 1
    # for x in text2binary(message):
    for x in message:
        if (x == '0'):
            output.append('0')
        else:
            output.append(str(change))
            if(change == 1):
                change = -1
            else:
                change = 1

    temp = "".join(output)
    temp = temp.split("00000000")

    output = []
    for x in temp:
        output.append(x)
        tempstr = x[::-1]
        
        if(len(tempstr) > 1):
            for _ in range(len(tempstr)):
                if tempstr[_]!= '0':
                    if tempstr[_+1] == '-1':
                        y='-1'
                        break
                    else:
                        y = '1'
                        break
        else:
            y = tempstr
        
        if (y == '1'):
            output.append("0001-10-11")
        elif(y== '-1'):
            output.append("000-1101-1")

    return "".join(output[:-1])
print(B8ZS("1 0000 00 00 0 1010 11 101000000 1 0000 00 00 01"))
#           1 0001-10-11 0-1010-11-101000000-1 0001-10-11 01
# print(B8ZS("1 0000 0000  0 1010 11 101000000 1 0000 00 00 0001"))
#           1 0001-10-11 0-1010-11-101000000-1 0001-10-11 0001