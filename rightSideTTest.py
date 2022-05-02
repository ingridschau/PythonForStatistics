import matplotlib.pyplot as plt 
import numpy as np 
 
def finnUtvalgetsVarians(arr,n,gjennomsnitt): 
    sumen=0 
    for x in arr: 
        sumen += (x - gjennomsnitt)**2 
    UV= (1/(n-1))*sumen  
    return UV 
def RegnGjennomsnitt(arr): 
    gjennomsnitt=sum(arr)/len(arr) 
    return gjennomsnitt 
datasett= [213, 250, 204, 216, 242, 209, 168, 197, 175, 308, 197, 206] 
 
n=len(datasett) 
 
gjennomsnitt=RegnGjennomsnitt(datasett) 
uv=finnUtvalgetsVarians(datasett, n ,gjennomsnitt) 
print ("utvalgets varians er lik   ",uv) 
usa=np.sqrt(uv) 
print ("utvalgets standardavvik er lik   ",float("{:.2f}".format(usa)))
