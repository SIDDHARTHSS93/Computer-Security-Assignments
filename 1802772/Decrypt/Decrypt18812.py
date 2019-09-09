plaintext=[]
import time
#Input the Cipher Text 
ciphertext="te td fyvyzhy szh pqqpnetgp esp nlpdlc ntaspc hld le esp etxp, mfe te td wtvpwj ez slgp mppy cpldzylmwj dpnfcp, yze wplde mpnlfdp xzde zq nlpdlc'd pypxtpd hzfwo slgp mppy twwtepclep lyo zespcd hzfwo slgp lddfxpo esle esp xpddlrpd hpcp hcteepy ty ly fyvyzhy qzcptry wlyrflrp. "
print("\n\nThe Cipher Text is:\n",ciphertext)
for i in range(len(ciphertext)):
    #while traversing through Ciphertext, we will take ASCII Value of characters into aascii
    aascii=ord(ciphertext[i])
    #If Ascii value not [a-z] i.e. less than 97, if ascii is 46(.) or 32(space) print as it is.
    #Else subtract 65, this gives value of Capitsl letter, and subtract 11 to show, 11 backward shifts are needed to decipher this text, if text greater than Z use modulus to repeat A
    if(aascii<97):
        if aascii==46:
            plaintext.append('.')
        elif aascii==32:
            plaintext.append(' ')
        else: 
            aascii=aascii-65
            aascii=(aascii-11)%26
            aascii=aascii+65
            plain=chr(aascii)
            plaintext.append(plain)
            
    #If Ascii is small letter i.e. greater than 97, subtract 97 and subtract -11 to get character of plain text
    else:
        aascii=aascii-97
        aascii=(aascii-11)%26
        aascii=aascii+97
        plain=chr(aascii)
        plaintext.append(plain)
str2=''.join(plaintext)
print("\n\nYour New Plaintext is:\n"+str2)
time.sleep(100)
