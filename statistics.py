import matplotlib.pyplot as plt
import numpy as np

def calculateAverage(arr):
    average=sum(arr)/len(arr)
    return average
def findMedian(arr,n):
    arr.sort()
    if n % 2 ==0:
        
        index=int(n/2)
        median=(arr[index-1]+arr[index])/2
    else:
        index=int((n-1)/2)
        median= arr[index]
    return median 
def findModus(arr):
    
    modus= max(set(arr), key = arr.count)
    return modus
def findSampleVariance(arr,n,average):
    sum=0
    for x in arr:
        sum += (x - average)**2
    sampleVariance= (1/(n-1))*sum 
    return sampleVariance
def subIntervals(arr):
 
    groups=[]
    space=np.linspace(1500000, 8500000,15)
    for i in range(14):
        counter=0
        L=[]
        for j in arr:
            if(j >= space[i] and j< space[i+1]):
                counter+=1
                L.append(j)
                
        if counter==0:
            L.append(0)
        groups.append(L)
    
    return groups

listingPrices= 
[2195000,3975000,2375000,6220000,2450000,7180000,4495000,6000000,5800000,8250000,42
50000,7500000,1990000,2900000,2080000,3500000,3650000,8250000,3700000,2390000]
print(listingPrices)
n = len(listingPrices)
maxPrice = np.amax(listingPrices)
space = np.linspace(1500000, 8500000,15)
groups = subIntervals(listingPrices)
            
print("Interval           frequency            relative frequency             
cumulative relative frequency")
cum = 0
sumf = 0
sumr = 0
tableInfo=[]
for i in range(14):
    if groups[i][0] == 0:
        frequency = 0
    else:
        frequency = len(groups[i])
    
    relative = float("{:.2f}".format(frequency/n))
    cum += relative
    print(f'{space[i]/1000000} _ {float("{:.2f}".format((space[i+1]/1000000)-
0.01))} mil   |      {frekvens}          |          {"{:<4}".format(relative)}      
|             {float("{:.2f}".format(cum))}')
    sumf += frequency
    sumr += relative
    tableInfo.append(relative)
    if i == 13:
        
print("____________________________________________________________________________
__________")
        print(f'Total                   {sumf}                    
{float("{:.2f}".format(sumr))}')    
print("")
print("")
print ("the average is ",calculateAverage(listingPrices))
print ("median is   ", findMedian(listingPrices, n))
print ("mode is   ",findModus(listingPrices))
average=calculateAverage(listingPrices)
sampleVariance=findSampleVariance(listingPrices, n , average)
print ("The sample variance is   ", sampleVariance)
standardDeviation = np.sqrt(sampleVariance)
print ("The sample standard deviation   ",float("{:.2f}".format(standardDeviation)))
print("")
print("")
L=[]
for i in space:
    L.append(i)
plt.figure()
plt.hist(listingPrices,bins=L,edgecolor='black')
plt.show()
