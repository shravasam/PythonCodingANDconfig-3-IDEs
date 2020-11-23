

a, b = 3, 4
x,y,z,e,r,t,y = 1,2,3,4,5,6,7
print(a,b)
print(x,y,z,e,r,t,y)


a, b = 3, 4
x,y,z,e,r,t,y = 1,2,3,4,5,6,7
print(a,b)
print(x,y,z,e,r,t,y)


#2. calling integer and floating variables

mystring = "hello"
name ="vasam"
country = "france"
myfloat = 10.0
myint = 20
myfloat1 = 30.00

if mystring == "hello":
    print("String: %s" % mystring)

if country == "france":
    print ("welcome %s" %country)

if name == "vasam":
    print("my name is %s"%name)
    
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("integer is %d"% myint)
if isinstance(myfloat1, float) and myfloat1 == 30.00:
    print("floating is %f" %myfloat1)
  
#appending and removing strings

names = ["sravan", "vasam"]
names.append("kumar")
names.remove("vasam")
print (names)


#4.using lists appending String & integer values 

rollno =[]
empnames = []
countrys = []

planeInfo = ["A350","A380","M400"]


rollno.append(1)
rollno.append(2)
rollno.append(3)
rollno.append(4)

countrys.append("france")
countrys.append("india")
countrys.append("china")
countrys.append("ukrain")

empnames.append("sravan")
empnames.append("vasam")
empnames.append("kumar")

Craft = planeInfo[1]

print("roll number info %s" %rollno)
print("emp details%s"%empnames)
print("countrys info %s" %countrys)
print("its about plane info %s" % Craft)


#5.printing string multiple times

lotsofhellos = "hello" * 10
print(lotsofhellos)

myname = "VASAM " * 200 
place = "Toulouse \n" * 100
print(myname+place)

#6.multiplication, arrays, appending
numbers = ([1,2,3]*33)
print(numbers)
num = ([12,34,33,55] * 54)
print(num)

rollNums = ([343434,343434] * 88)
print(rollNums)

TRS = []

TRS.append("LINKED MODIFICATION")
print(TRS*4)

TRS.append("MIXIBILITY")
print(TRS*5)

