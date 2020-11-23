#13. print numbers using for loop and range method

#For loop and range fuction

mynum = [9,10,11,12,13,14]
for num in range(1,5):
    print(num)
    print('hello')
mynum2 = [1,2,3,4,2,12,]
for nums in range(1,6):
    print (nums)
    
#13. If condition is true it stops printing numbers(using if-elif-else)
 
#if-elif-else
#if any stmet is correct it stops and never continue to another stamt

a = 110
b = 10
c = 1
d = 2
e = 3
f = 4
g = 5
h = 6
i = 7
j = 8
k = 0
l = 0
m = 1
n = 2
o = 3
p = 4
q = 5
r = 6
s = 7
t = 2

if a < b:
    print('B is greater than A')
elif b < c:
    print('C is greater than B')
elif c < d:
    print('D is greater than C')
elif e < f:
    print('F is greater than E')
elif f < g:
    print('G is greater than F')
elif g < h:
    print('H is greater than I')
elif h < i:
    print (' I is greater than H')
elif i < j:
    print('j is greater than I')
elif j < i:
    print ('I is greater than J')
elif k < l:
    print('L is greater than K')
elif m < n:
    print('N is greater than M')
elif o < p:
    print('P is greater than O')
elif q < r:
    print('R is greater than Q')
elif s < r:
    print('R is greater than S')
elif t < s:
    print('S is greater than T')
else:
    print(' Nothing is greater than any thing here')

#14. printing numbers till condition false using while loop
condition = 1
condition1 = 2
condition2 = 3
condition3 = 4
condition4 = 5
condition5 = 6
condition6 =6
condition7 = 7
condition8 = 8
condition9 = 9
condition10 = 10
condition11 = 11
condition12 = 12
condition13 = 13
condition14 = 14

while condition < 10:
    print(condition)
    condition +=1
while condition1 < 10:
    print(condition1)
    condition1 +=1
while condition2 < 20:
    print (condition2)
    condition2 +=1
while condition3 < 30:
    print (condition3)
    condition3 +=1
while condition4 < 30:
    print (condition4)
    condition4 +=1
while condition5 < 40:
    print (condition5)
    condition5 +=1
while condition6 < 50:
    print(condition6)
    condition6 +=1
while condition7 < 33:
    print(condition7)
    condition7 +=1
while condition8 < 22:
    print (condition7)
    condition8 +=1
while condition9 < 12:
    print  (condition9)
    condition9 +=1
while condition10 < 13:
    print(condition10)
    condition10 +=1
while condition11 < 14:
    print (condition11)
    condition11 +=1
while condition12 < 15:
    print (condition12)
    condition12 +=1
while condition13 < 16:
    print (condition13)
    condition13 +=1
while condition14 < 17:
    print  (condition14)
    condition14 +=1
#15. print names using break & continue statements.

print ("Printing statrs from 0")
users = ["sravan","kumar","vasam", "A350","A330","A380","M400"]
for i in users:
    if (i == 'vasam'):
        continue
    print i
print("Printing ending with 45")

#16. Open text file -Exception handling using try-except-else-finally

try:
    f = open('test.txt')
except Exception:
    print ("sorry file not there")
else:
    print(f.read())
    f.close()
finally:
    print ("its opened")

#17.print correct name using if elif else
name ="sravans"

if name is "sravan":
    print("hi i am sravan")
elif name is "vasam":
    print("hi i am not sravan")
elif name is "kumar":
    print("hi i am not kumar")
else:
    print("not true")

#18.print names using for loop
name ="sravans"

if name is "sravan":
    print("hi i am sravan")
elif name is "vasam":
    print("hi i am not sravan")
elif name is "kumar":
    print("hi i am not kumar")
else:
    print("not true")
#19.using continue statement not to print given integer value in the range function

magicnumers = 55
for maggi in range(202):
    if maggi is magicnumers:
        print(maggi,"Bonjour a tous, Je suis ici, vous pouvez regardez mon nouvelle video. merci")
        continue
    else:
         print(maggi)

#20. using break statement, terminate the program. Print interger value
magicnumers = 55
for maggi in range(202):
    if maggi is magicnumers:
        print(maggi,"Bonjour a tous, Je suis ici, vous pouvez regardez mon nouvelle video. merci")
        break
    else:
         print(maggi)
#
