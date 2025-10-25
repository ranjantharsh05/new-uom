#sum of the multiples of 3 and 5
count=0
num=int(input("enter the number : "))
for i in range (1,num):
    if i%3==0 or i%5==0:
        count+=i
    i+=1
print(f'total = {count}')