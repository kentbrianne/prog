import time
import random
import matplotlib.pyplot as plt

recorder = []
num = []

tstart = time.time()

def msort(nums): 

   
 
    if len(nums) > 1: 
        mid = len(nums)//2  
        L = nums[:mid]  
        R = nums[mid:] 

        msort(L) 
        msort(R) 

        i = j = k = 0
        

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                nums[k] = L[i] 
                i+=1
            else: 
                nums[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L): 
            nums[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            nums[k] = R[j] 
            j+=1
            k+=1
    


def printer(nums): 
    for i in range(len(nums)):        
        print(nums[i],end=" ") 
    print() 


def main(): 
    n = 10
    nums = random.sample(range(0, n), n)
    msort(nums)
    printer(nums) 
    num.append(n)

main()
tend = time.time()
timelapse = tend-tstart
print("Runtime:", timelapse)

recorder.append(timelapse)

tstart = time.time()

def msort(nums): 

   
 
    if len(nums) > 1: 
        mid = len(nums)//2  
        L = nums[:mid]  
        R = nums[mid:] 

        msort(L) 
        msort(R) 

        i = j = k = 0
        

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                nums[k] = L[i] 
                i+=1
            else: 
                nums[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L): 
            nums[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            nums[k] = R[j] 
            j+=1
            k+=1
    


def printer(nums): 
    for i in range(len(nums)):        
        print(nums[i],end=" ") 
    print() 


def main(): 
    n = 100
    nums = random.sample(range(0, n), n)
    msort(nums)
    printer(nums) 
    num.append(n)

main()
tend = time.time()
timelapse = tend-tstart
print("Runtime:", timelapse)

recorder.append(timelapse)

tstart = time.time()

def msort(nums): 

   
 
    if len(nums) > 1: 
        mid = len(nums)//2  
        L = nums[:mid]  
        R = nums[mid:] 

        msort(L) 
        msort(R) 

        i = j = k = 0
        

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                nums[k] = L[i] 
                i+=1
            else: 
                nums[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L): 
            nums[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            nums[k] = R[j] 
            j+=1
            k+=1
    


def printer(nums): 
    for i in range(len(nums)):        
        print(nums[i],end=" ") 
    print() 


def main(): 
    n = 1000
    nums = random.sample(range(0, n), n)
    msort(nums)
    printer(nums) 
    num.append(n)

main()
tend = time.time()
timelapse = tend-tstart
print("Runtime:", timelapse)

recorder.append(timelapse)

tstart = time.time()

def msort(nums): 

   
 
    if len(nums) > 1: 
        mid = len(nums)//2  
        L = nums[:mid]  
        R = nums[mid:] 

        msort(L) 
        msort(R) 

        i = j = k = 0
        

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                nums[k] = L[i] 
                i+=1
            else: 
                nums[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L): 
            nums[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            nums[k] = R[j] 
            j+=1
            k+=1
    


def printer(nums): 
    for i in range(len(nums)):        
        print(nums[i],end=" ") 
    print() 


def main(): 
    n = 10000
    nums = random.sample(range(0, n), n)
    msort(nums)
    printer(nums) 
    num.append(n)

main()
tend = time.time()
timelapse = tend-tstart
print("Runtime:", timelapse)

recorder.append(timelapse)

print(recorder)

plt.plot(num,recorder, 'ro')
plt.axis([0, 10000, 0, 0.5])
plt.ylabel('Merge Sort')
plt.show()