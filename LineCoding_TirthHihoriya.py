from utilities import text2binary

def NRZ_L(message):
    output1 =[] 
    for b in text2binary(message):
        if b=='0':
            output1.append(1)
        else:
            output1.append(-1)
    return output1
    
def NRZ_I(message):
    output2 = []
    flag = 1
    for b in text2binary(message):
        if(b == '1'):
            if(flag == 1):
                flag = -1
            else:
                flag = 1
            output2.append(flag)
        else:
            output2.append(flag)
    return output2
        
def _2B1Q(message):   # `b` (bit)  is `message`
    output3 = []
    b = text2binary(message)        # pls check the output of 2b1q  !!!
    for i in range(0,len(b)-1,2):
        if(i==0):
            if(b[0]=='0' and b[1]=='0'):
                output3.append(1)   
                output3.append(1)
            elif(b[0]=='0' and b[1]=='1'):
                output3.append(2)            
                output3.append(2)
            elif(b[0]=='1' and b[1]=='0'):
                output3.append(-1)            
                output3.append(-1)
            elif(b[0]=='1' and b[1]=='1'):
                output3.append(-2) 
                output3.append(2)

        elif(b[i]=='0' and b[i+1]=='0'):
            if(output3[i-1]>0):
                output3.append(1)
                output3.append(1)     
            else:
                output3.append(-1)
                output3.append(-1)
            
        elif(b[i]=='0' and b[i+1]=='1'):
            if(output3[i-1]>0):
                output3.append(2)
                output3.append(2)   
            else:
                output3.append(-2)
                output3.append(-2)
            
        elif(b[i]=='1' and b[i+1]=='0'):
            if(output3[i-1]>0):
                output3.append(-1)
                output3.append(-1)
                
            else:
                output3.append(1)
                output3.append(1)
            
        elif(b[i]=='1' and b[i+1]=='1'):
            if(output3[i-1]>0):
                output3.append(-2)
                output3.append(-2)
                
            else:
                output3.append(2)
                output3.append(2)
            
    return output3  


def manchester(message):
    output = []
    for x in text2binary(message):
        if (x == '0'):
            output.append(1)
            output.append(-1) 
        else:
            output.append(-1) 
            output.append(1)
    return output                          
            

def diff_manchester(message):
    output = []
    c=-1
    b = text2binary(message)
    for i in range(len(b)):
        if i==0:
            if b[0]=='0':
                output.append(1)
                output.append(-1)
                c+=2
            elif b[0]=='1':
                output.append(-1)
                output.append(1)
                c+=2    
        elif b[i] == '0':
            if output[c]==-1:
                output.append(-1)
                output.append(1)
                c+=2
            elif output[c]==1:
                output.append(1)
                output.append(-1)
                c+=2
        elif b[i] == '1':
            if output[c]==1:
                output.append(-1)
                output.append(1)
                c+=2
            elif output[c]==-1:
                output.append(1)
                output.append(-1)
                c+=2            
    return output


def MLT_3(message):
    output = []
    b = text2binary(message)
    flag =1
    for i in range(len(b)):
        
        if i==0:
            if b[0]=='0':
                output.append(0)
            else:
                output.append(1)
        elif b[i]=='0':
            output.append(output[i-1])
        else:
            if output[i-1]==1 or output[i-1]==-1:
                output.append(0)
            else:
                if flag==1:
                    output.append(-1)
                    flag=-1
                else:
                    output.append(1)
                    flag=1
    return output


def  B8ZS(message):
    output = []
    # b = text2binary(message)
    b = message
    change = 1
    i=0
    while(i<len(b)):
        if(i<(len(b)-8) and b[i]=='0' and b[i+1]=='0' and b[i+2]=='0' and b[i+3]=='0' and b[i+4]=='0' and b[i+5]=='0' and b[i+6]=='0' and b[i+7]=='0' and i!=0  ):
            print(i)
            if b[i-1]=='1':
                
                output.append(0)
                output.append(0)
                output.append(0)
                output.append(1)
                output.append(-1)
                output.append(0)
                output.append(-1)
                output.append(1)
                
                i+=9
                
            else:
                
                output.append(0)
                output.append(0)
                output.append(0)
                output.append(-1)
                output.append(1)
                output.append(0)
                output.append(1)
                output.append(-1)
                
                i+=9
                   
        elif (b[i] == '0'):
            output.append(0)
            i+=1
        else:
            output.append(change)
            i+=1
            if(change == 1):
                change = -1
            else:
                change = 1
    return output
    

    
    




print("1000000000 1010111010000001 00000000000 1")
print(B8ZS("10000000001010111010000001000000000001"))