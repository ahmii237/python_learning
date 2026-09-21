
principal= 0
rate =0
time=0

while principal<=0 or rate <= 0 or time <= 0:
    principal=int(input("Enter Principal Amount: "))
    rate=int(input("enter rate of interest: "))
    time=int(input("enter the time.: "))

total=principal * pow((1+ rate/100),time)
print(f"New Balance is ${total}")