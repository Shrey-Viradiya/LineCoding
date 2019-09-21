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
        
def _2B1Q(b):
    output3 = []
 
    for i in range(0,len(b)-1,2):
        if(b[0]=='0' & b[1]=='0'):
            output3.append(1)   # we can also appent only one bit ,  we have to understand the graph_plot in that way
            output3.append(1)
            
        elif(b[0]=='0' & b[1]=='1'):
            output3.append(2)
            output3.append(2)
            
        elif(b[0]=='1' & b[1]=='0'):
            output3.append(-1)
            output3.append(-1)
            
        elif(b[0]=='1' & b[1]=='1'):
            output3.append(-2)
            output3.append(-2)
            

        elif(b[i]=='0' & b[i+1]=='0'):
            if(output3[i-1]>0):
                output3.append(1)
                output3.append(1)     
            else:
                output3.append(-1)
                output3.append(-1)
            
        elif(b[i]=='0' & b[i+1]=='1'):
            if(output3[i-1]>0):
                output3.append(2)
                output3.append(2)   
            else:
                output3.append(-2)
                output3.append(-2)
            
        elif(b[i]=='1' & b[i+1]=='0'):
            if(output3[i-1]>0):
                output3.append(-1)
                output3.append(-1)
                
            else:
                output3.append(1)
                output3.append(1)
            
        elif(b[i]=='1' & b[i+1]=='1'):
            if(output3[i-1]>0):
                output3.append(-2)
                output3.append(-2)
                
            else:
                output3.append(2)
                output3.append(2)
            
    return output3    
            

