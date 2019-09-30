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
    flag = 1
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
            if output[c]=='-1':
                output.append(-1)
                output.append(1)
                c+=2
            elif output[c]=='1':
                output.append(1)
                output.append(-1)
                c+=2
        elif b[i] == '1':
            if output[c]=='1':
                output.append(-1)
                output.append(1)
                c+=2
            elif output[c]=='-1':
                output.append(1)
                output.append(-1)
                c+=2




            
    return output