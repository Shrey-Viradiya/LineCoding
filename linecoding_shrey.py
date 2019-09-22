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