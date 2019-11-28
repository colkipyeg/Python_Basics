number=100
#if number > 50:
   # print("i am satisfied.")
if number > 150:
    print("i am satisfied")
else:
    print("I am not satisfied.")


number=20
if number>0:
    print("{}is greater than 0".format(number))
elif number==10:
    print("{}is ==to 10".format(number))
else:
    print("{}is a negative number".format(number))



kis=int(input("enter marks for Kiswahili:"))
eng=int(input("enter marks for English:"))
mat=int(input("enter marks for Maths:"))
scie=int(input("enter marks for Science:"))
sst=int(input("enter marks for Biology:"))

sum=int(kis)+int(eng)+int(mat)+int(scie)+int(sst)
print(sum)

average=(kis+eng+mat+scie+sst)/5
print(average)

