from utilities import text2binary
def NRZ_L(message):
    output1 =[] 
    for i in text2binary(message):
        if b[i]==0:
            output1.append(1)
        else:
            output1.append(-1)
    return output1
    
def NRZ_I(message):
    output2 = []
    flag = 1
    for i in text2binary(message):
        if(i == 1):
            if(flag == 1):
                flag = -1
            else:
                flag = 1
            output2.append(flag)
        else:
            output2.append(flag)
    return output2
        