import numpy
import random
import time
#We will store the values of private keys into private 1 and 2, private 1 and 2
#will be the output of combined congruential method.
#We will have alpha and q to obtain the public keys(x1 and x2) for the Diffie
#Hellman's Algorithm.
#we will use public keys x1 and x2 to generate secret key.
#variables y1 and y2 2 random numbers intermediate values in the combined
#congruential algorithm.
#variables a1,a2,m1 and m2 are used to generate y1, y2, and x.
#x holds the list of each generator value, or eachprivate key in this case.
private1=0
private2=0
alpha=3
q=353
x=numpy.zeros(3)
y1=numpy.zeros(3)
y2=numpy.zeros(3)
m1=2147483642
m2=2147483423
a1=450
a2=234
while True:
    y1[0]=random.randint(1, 2147483641)
    y2[0]=random.randint(1, 2147483422)
    i=0
    x[0]=0

    for i in range(2):
        y1[i+1]=(a1*y1[i])%m1
        y2[i+1]=(a2*y2[i])%m2
        x[i+1]=(y1[i+1]-y2[i+1])%(m1-1)

        private1=int(x[1]%500)
        private2=int(x[2]%500)

    if private1<q and private2<q:
        break

print("The first Private Key is:",private1)
print("The second Private Key is:",private2)

#Once the private keys are generated. We will use private keys in the formula
#X=a**privatekey mod q, where X is the public key x1 and x2,and
#the private keys are what we generated earlier.

x1=(alpha**private1)%q
x2=(alpha**private2)%q

#Once we generate public keys x1 and x2 we will use them to generate secret keys,
#we will use secret key=X**opp private mod q.
#where opp private key is the opposite private key used. 

secretkey=(x2**private1)%q
print("The Secret Key is:",secretkey)
#Once Secret key is generate, we will divide it into its individual characters.
#This is going to be used to generate list T.
#We will ask user to enter a file name. This file will contain plain text which
#we will convert to cipher text.
#Also the 2nd user will enter the secret key, this is used to confirm that the
#2nd user is genuine. 
l=len(str(secretkey))
count=0
f=input("Please Enter the file Name:")
secretkey=input("Please Enter the Secret Key:")
file=open(f,"r")
cont=file.read()
#We will take the plaintext from the block and divide it into 64 bit blocks
#In this case 8 characters, as each character is 8 bits in length.
#if all blocks are of equal sizes, we will take the last block, else we will take the 2nd last block. 
for i in range(len(cont)):
    count+=1
block=[]
count2=count/8-count//8
if count2>0:
    count=(count//8)+1
else:
    count=count//8

for i in range(count
               ):
    block.append([])

i=0
block[i].append(cont[0])
for j in range(1,len(cont)):
    if i<count:
        block[i].append(cont[j])
        if(j%8==0):
            block[i]=''.join(block[i])
            i+=1
        if(j==(len(cont)-1)):
            block[i]=''.join(block[i])
            i+=1

while(j-1<8*i):
    block[i-1]=block[i-1]+'0'
    j+=1
if count2>0:
    print("\n\nThe Block of plain text is:\n",block[i-2])
else:
    print("\n\nThe Block of plain text is:\n",block[i-1])
#We will create list s contsining a range from 0-255, and t which will
#contain our secret key value as discussed earlier.  
secretkeylist=numpy.zeros(l)
s=numpy.zeros(256)
t=numpy.zeros(256)
secretkey=str(secretkey)
for i in range(l):
    secretkeylist[i]=int(secretkey[i])
for i in range(256):
    s[i]=i
    t[i]=secretkeylist[i%l]

j=0
#we will find j as a value of j+s[i]+t[i] mod 256 and swap s[i] and s[j]
for i in range(255):
    j=int((j+s[i]+t[i])%256)
    temp=s[i]
    s[i]=s[j]
    s[j]=temp

#In the end we get a new s array. Now we will give new values for i and j and again swap s[i] and s[j]
#we will take the last value as s[t] and store it in k. This k will be used to encrypt the block of plaintext
i=0
j=0
k=0
count3=0
while True:
    i=int((i+1)%256)
    if(i==0):
        count3+=1
    if(count3==2):
        break
    j=int((j+s[i])%256)
    
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    t=int(s[i]+s[j])%256
    k=int(s[t])
    
if count2>0:
    count=count-2
    pt=block[count]
else:
    count=count-1
    pt=block[count]
    
#We will then take key k and xor with the ascii value of plain text, and convert the new integer list to a character string
#This new character String is the cipher text.
ptascii=numpy.zeros(len(pt))
ct=numpy.zeros(len(pt))
cipher=[]

for i in range(len(pt)):
    ptascii[i]=ord(pt[i])
    ct[i]=int(ptascii[i])^k
    cipher.append(chr(int(ct[i]%26)+97))
cipher="".join(cipher)
print("The Encrypted Text is:",cipher)
cipher=input("Please enter the ciphertext:")
#We will ask the user to provide cipher text. We will use the cipher text to generatean integer matrix.
#We will use the key k to xor the cipher text back to plain text. 
ctq=numpy.zeros(len(pt))
ctr=numpy.zeros(len(pt))
for i in range(len(pt)):
    ctq[i]=ct[i]//26
    ctr[i]=int((ord(cipher[i])-97)%26)
plain=[]
pt1=numpy.zeros(len(ct))
for i in range(len(ct)):
    pt1[i]=ctq[i]*26+ctr[i]
    pt1[i]=int(pt1[i])^k
    plain.append(chr(int(pt1[i])))
plain="".join(plain)
print("The decrypted text is:",plain)
time.sleep(1000)
