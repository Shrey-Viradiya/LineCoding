  
def NRZ_L(b):
    output1 =[] 
    for i in range(0,len(input)):
        if b[i]==0:
            output1.append(1)
        else:
            output1.append(-1)
    return output1
    
def NRZ_I(b):
    output2 = []
    flag = 1

    for i in b:
        if(i == 1):
            if(flag == 1):
                flag = -1
            else:
                flag = 1
            output2.append(flag)
        else:
            output2.append(flag)
    return output2


        