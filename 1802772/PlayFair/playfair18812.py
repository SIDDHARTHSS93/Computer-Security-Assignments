import time
choose=input("Plese enter 'E' if you want to Encrypt and 'D' if you want to Decrypt:")
#We will ask User to Enter E for Encryption and D for Decryption into variable Choose
if choose=='E':
    key=input("Please Enter the secret Key:")
    key=key.upper()
    keylist=[]
    ciphertext=[]
    keymatrix=[]
    value1=0
    value2=0
    value3=0
    value4=0
    alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    #We will make alist Key List,that will take the input we provide at Key and enter unique characters once followed by the remaining characters in alphabet except J
    message=input("Please Enter your Plaintext")
    
    for i in range(len(key)):
        if key[i]=='\s':
            i+=1
        if key[i] not in keylist:
            keylist.append(key[i])
    for i in range(len(alpha)):
        if alpha[i] not in keylist:
            keylist.append(alpha[i])

    print(keylist)
    #We will Use Keymatrix to display keylist as 5*5 Matrix
    keymatrix.insert(0,keylist[0:5])
    keymatrix.insert(1,keylist[5:10])
    keymatrix.insert(2,keylist[10:15])
    keymatrix.insert(3,keylist[15:20])
    keymatrix.insert(4,keylist[20:25])
    #We will Enter the Plain Text Message into message
    print("The Plain Text is:",message)
    message=message.upper()
    count=0
    #We remove spaces and make Key and Message Upper Case 
    messagelist=list(message)
    for i in range(len(messagelist)):
        if message[i]=='\s':
            del messagelist[i]
    x=len(messagelist)
    print(x)
    i=0
    #We use count variable to denote odd or even number of blocks 0=even, 1=odd
    while i<x:
        count=count+1
        if count%2==0:
            count=0
        #If last character makes Message into odd number of characters add Z to make the message even.
        if i==(x-1) and count%2==1:
            if messagelist[i]=='Z':
                messagelist.insert(i+1,'Q')
            else:
                messagelist.insert(i+1,'Z')
                
            x=x+1
        #If the ith and i+1th Character is same, insert X after ith character   
        if count%2==1 and (messagelist[i]==messagelist[i+1]):
            messagelist.insert(i+1,'X')
            x+=1
        #If the ith and i+1th Character is X, insert Y after ith character   
        
        if count%2==1 and (messagelist[i]==messagelist[i+1] and messagelist[i]=='X'):
            messagelist.insert(i+1,'Y')
            x+=1
        #Replace J with I
        if messagelist[i]=='J':
            messagelist[i]=='I'

        i+=1
    message=''.join(messagelist)
    print("The Plain Text is:",message)
    #Traverse through the message, if message is found in key, take the values of ith and i+1th Character into values value 1, value2,and value 3,value4 Respectively
    for i in range(0,len(message),2):   
        for j in range(5):
            for k in range(5):
                if message[i]==keymatrix[j][k]:
                    value1=j
                    value2=k
                if message[i+1]==keymatrix[j][k]:
                   value3=j
                   value4=k
                   
        #if both characters fall in same Row in Key Matrix, if value is not the last column, take value2+1th and value4+1th Column into ciphertext
        if value1==value3:
            if value2==4 and value4!=4: 
                value2=0
                value4+=1
            elif value4==4 and value2!=4:
                value4=0
                value2+=1
            
            else:
                value2+=1
                value4+=1
        #if both characters fall in same Column in Key Matrix, if value is not the last Row, take value1+1th and value3+1th Row into ciphertext
        if value2==value4:
            if value1==4 and value3!=4: 
                value1=0
                value3+=1
            elif value3==4 and value1!=4: 
                value3=0
                value1+=1
            
            else:
                value1+=1
                value3+=1
        #if both characters are in different rows and columns of the key matrix, form a rectange, and take the other ends of the rectangle into ciphertext
        if value1!=value3 and value2!=value4:
            temp=value2
            value2=value4
            value4=temp

            

        
        
    
           
        ciphertext.append(keymatrix[value1][value2])
        ciphertext.append(keymatrix[value3][value4])

    #Display Cipher Text 
    ciphertext=''.join(ciphertext)   
    print("The Cipher Text is:",ciphertext)

elif choose=='D':
    #If Choose=D,
    #We will make alist Key List,that will take the input we provide at Key and enter unique characters once followed by the remaining characters in alphabet except J
    #We will Use Keymatrix to display keylist as 5*5 Matrix
    #We will Enter the Cipher Text Message into ciphertext
    #We remove spaces and make Key and ciphertext Upper Case 

    key=input("Please Enter the secret Key:")
    key=key.upper()
    keylist=[]
    message=[]
    keymatrix=[]
    value1=0
    value2=0
    value3=0
    value4=0
    alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for i in range(len(key)):
        if key[i] not in keylist:
            keylist.append(key[i])
    for i in range(len(alpha)):
        if alpha[i] not in keylist:
            keylist.append(alpha[i])

    keymatrix.insert(0,keylist[0:5])
    keymatrix.insert(1,keylist[5:10])
    keymatrix.insert(2,keylist[10:15])
    keymatrix.insert(3,keylist[15:20])
    keymatrix.insert(4,keylist[20:25])
    print(keymatrix)
    
    ciphertext=input("Please Enter your ciphertext:")
    ciphertext=ciphertext.upper()

    #We will search ciphertext's ith and i+1th value with key matrix, and if found store the 1st value positions into value 1 and value 2 and 2nd value's positions into value3 and value4
    for i in range(0,len(ciphertext),2):   
        for j in range(5):
            for k in range(5):
                if ciphertext[i]==keymatrix[j][k]:
                    value1=j
                    value2=k
                if ciphertext[i+1]==keymatrix[j][k]:
                   value3=j
                   value4=k
                   
        #if both characters fall in same Row in Key Matrix, if value is not the last column, take value2-1th and value4-1th Column into message

        if value1==value3:
            if value2==0 and value4!=0: 
                value2=4
                value4-=1
            elif value4==0 and value2!=0:
                value4=4
                value2-=1
            
            else:
                value2-=1
                value4-=1
        #if both characters fall in same Column in Key Matrix, if value is not the last Row, take value111th and value311th Row into message

        if value2==value4:
            if value1==0 and value3!=0: 
                value1=4
                value3-=1
            elif value3==0 and value1!=0: 
                value3=4
                value1-=1
            
            else:
                value1-=1
                value3-=1
        #if both characters are in different rows and columns of the key matrix, form a rectange, and take the other ends of the rectangle into message

        if value1!=value3 and value2!=value4:
            temp=value4
            value4=value2
            value2=temp

            

        
        
    
            
        message.append(keymatrix[value1][value2])
        message.append(keymatrix[value3][value4])
    
    message=''.join(message)   
   

    messagelist=list(message)
    x=len(messagelist)
    print(x)
    count=0
    for i in range(x):
        count=count+1
        #If last character is Q and the 2nd last character is  Z remove Q, if last character is Z and 2nd last character is something else, remove Z
        if messagelist[-1]=='Q' and messagelist[-2]=='Z' and count%2==0:
            messagelist.pop()
            x=x-1
        if messagelist[-1]=='Z' and messagelist[-2]!='Z' and count%2==0:
            messagelist.pop()
            x=x-1
        if count%2==0:
           count=0
        #If ith value and i+2th value is same and X lies in i+1th value remove X
        if(i+2<x-2 and messagelist[i]==messagelist[i+2] and messagelist[i+1]=='X'):
            del messagelist[i+1]
    message=''.join(messagelist)
    #print message
    print("The Plain Text is:",message)
            
time.sleep(100)
