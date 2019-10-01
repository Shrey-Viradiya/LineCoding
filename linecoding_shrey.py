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
        
        for y in tempstr:
            if y!= '0':
                break
        
        if (y == '1'):
            output.append("0001-10-11")
        elif(y== '-1'):
            output.append("000-1101-1")

    return "".join(output)

print(B8ZS("10000000001010111010000001000000000001"))