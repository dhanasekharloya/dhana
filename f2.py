num1=int(input("enter num1 value:"))
num2=int(input("enter num2 value:"))
for i in range(num1,num2+1):
    no_of_digits=len(str(i))
    temp=i
    s=0
    dig=temp%10
    s+=dig**no_of_digits
    temp//=10
if i==s:
    print()
