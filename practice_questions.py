#Check Prime Number 
def prime_number(n):
    if n > 1 :
        for i in range(2,n):
            if n % i == 0:
                print("Not Prime")
                return
            else:
                print("Prime")
                return
        

prime_number(3)
                

#List Uniqueness Checker and where duplicates found break the loop 
def uniqueness_checker(item):
    unique_items = set()
    for items in item:
        if items in unique_items:
            print("Duplicate :" , items)
            break
        unique_items.add(items)

item = ["apple","bnana","melon","orange","apple"]
print(uniqueness_checker(item))

#Write a code where used time method and implement the waittime duble logic:
import time
wait_time = 1
attempt = 0 
retries = 77679
while attempt < retries:
    print("Attempts:",attempt+1 ,"Wait Time:",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempt+=1