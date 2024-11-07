for number in range(1,1000001):# number in range of 1000000
    sum=0
    for i in range(1,number):
        if number%i==0:#to check perfect number
            sum+=i
    if sum==number:#sum of divisor of number must be equal to that number
        print(f"perfect number is between 1 and 1M are: ",number) 
print(number)   