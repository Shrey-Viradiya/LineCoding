input = [0,1,0,0,1,1,1,0,1,0]    # only to test
 

output1 =[]     # only to test
def NRZ_L(b):
    for i in range(0,len(input)):
        if b[i]==0:
            output.append(1)
        else:
            output.append(-1)
    

output2 =[]   # only to test
flag = 0
def NRZ_I(b):
    for i in range(0,len(input)):
        if(b[0]==0):
            output2.append(1)
        elif(b[0]==1):
            output2.append(-1)
        elif(b[i]==0):
            output2.append(flag)
        elif(b[i]==1):
            if(flag==0):
                flag=1
            else:
                flag=0

            output2.append(flag)

NRZ_L(input)         
NRZ_I(input)

        