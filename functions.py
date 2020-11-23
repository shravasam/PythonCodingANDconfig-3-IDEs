#6.call funciotns simple

def main():
    print("hello world")
def first():
    print("france")
def two():
    print("india")
def three():
    print("A330")
    
main()
first()
two()
three()





#7.Passing variables  & return values using fuctions
#return values
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return  num1*num2
def div(num1,num2):
    return num1/num2
def module(num1,num2):
    return num1%num2
def mainAdd():
    myresult = add(1,1)
    print(myresult)
def mainSub():
    mySubResult = sub(1,1)
    print(mySubResult)
def mainMul():
    myMulResult = mul(1,2)
    print(myMulResult)
def mainDiv():
    myDivResult = div(1,2)
    print (myDivResult)
def mainModul():
    myModResult = module(5,3)
    print(myModResult)
mainAdd()
mainSub()
mainMul()
mainDiv()
mainModul()

#8.Calling single method, returning all variable values
#return values
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return  num1*num2
def div(num1,num2):
    return num1/num2
def module(num1,num2):
    return num1%num2
def mainAdd():
    num1 = int(input("enter 1 number"))
    num2 = int(input("enter 2 number"))
    print(add(num1,num2))
    print(sub(num1,num2))
    print(mul(num1,num2))
    print(div(num1,num2))
    print(module(num1,num2))
mainAdd()

#Problem statement: i wanted inherit result into monthstotal method for that i need classes

def div(num1,num2):
    return num1/num2

def months(num1):
    return num1
def mainAdd():
    num1 = int(input("enter 1 number"))
    num2 = int(input("enter 2 number"))
    result = div(num1, num2)
    print(result)
def monthsTotal():
    num1 = int(input("months"))
    total = result*num1
    print(total)
mainAdd()
monthsTotal()


#9. using operators if match found return values and print.

#Enter values
#return values
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return  num1*num2
def div(num1,num2):
    return num1/num2
def module(num1,num2):
    return num1%num2
def main():
    num1 = int(input("enter 1 number"))
    num2 = int(input("enter 2 number"))

    operation = int(input("what do you want 1.addition, 2.subtraction, 3.multiplication, 4.divisin, 5.mod"))
    if(operation == 1):
        print(add(num1,num2))
    elif(operation == 2):
        print(sub(num1,num2))
    elif(operation == 3):
        print(mul(num1,num2))
    elif(operation == 4):
        print(div(num1,num2))
    elif(operation ==5):
        print(module(num1,num2))
    else:
        print("i dont undersstand")
main()

#10. using try except block, Boolean, return “integer” values

#return values
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return  num1*num2
def div(num1,num2):
    return num1/num2
def module(num1,num2):
    return num1%num2
def main():
    validInput = False
    while not validInput:
        try:
            num1 = int(input("enter 1 number"))
            num2 = int(input("enter 2 number"))
            #operation = input("what do you want(add,substration,multiplication,division,mod)")
            operation = int(input("what do you want 1.addition, 2.subtraction, 3.multiplication, 4.divisin, 5.mod"))
            validInput = True
        except:
            print ("invalid input")

    if(operation == 1):
        print(add(num1,num2))
    elif(operation == 2):
        print(sub(num1,num2))
    elif(operation == 3):
        print(mul(num1,num2))
    elif(operation == 4):
        print(div(num1,num2))
    elif(operation ==5):
        print(module(num1,num2))
    else:
        print("i dont undersstand")
main()


#11. using try except block, Boolean, return “integer” values, repeating application

#return values
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return  num1*num2
def div(num1,num2):
    return num1/num2
def module(num1,num2):
    return num1%num2
def addAgain(num1,num2):
    return num1+num2
def main():
    user_continue = True
    while user_continue:
        validInput = False
        while not validInput:
            try:
                num1 = int(input("enter 1 number"))
                num2 = int(input("enter 2 number"))
                #operation = input("what do you want(add,substration,multiplication,division,mod)")
                operation = int(input("what do you want 1.addition, 2.subtraction, 3.multiplication, 4.divisin, 5.mod , 6.extra"))
                validInput = True
            except:
                    print ("invalid input")
        if(operation == 1):
            print(add(num1,num2))
        elif(operation == 2):
            print(sub(num1,num2))
        elif(operation == 3):
            print(mul(num1,num2))
        elif(operation == 4):
            print(div(num1,num2))
        elif(operation ==5):
            print(module(num1,num2))
        elif(operation == 6):
            print(addAgain(num1,num2))
        else:
            print("i dont undersstand")
        user_y = str(input('would you continue any other calculations1."Y" to yes' ))
        if(user_y ==True):
            continue
main()

#12. using boolean operators, one main method return all arithmetic operations and ask to repeat application.
#return values
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return  num1*num2
def div(num1,num2):
    return num1/num2
def module(num1,num2):
    return num1%num2
def main():
    user_continue = True
    while user_continue:
        validInput = False
        while not validInput:
            try:
                num1 = int(input("enter 1 number"))
                num2 = int(input("enter 2 number"))
                #operation = input("what do you want(add,substration,multiplication,division,mod)")
                operation = int(input("what do you want 1.addition, 2.subtraction, 3.multiplication, 4.divisin, 5.mod"))
                validInput = True
            except:
                    print ("invalid input")
        if(operation == 1):
            print(add(num1,num2))
        elif(operation == 2):
            print(sub(num1,num2))
        elif(operation == 3):
            print(mul(num1,num2))
        elif(operation == 4):
            print(div(num1,num2))
        elif(operation ==5):
            print(module(num1,num2))
        else:
            print("i dont undersstand")
        user_y = int(input('Press 1 to continue press any number to exit' ))
        if(user_y !=1):
            user_continue = False
            break
        else:
             continue
main()

#21. funcitons, program to multiply USD using 2 functions.
def poulet():
    print("cost of poulet in usa")
def costofpoulet(usd):
    amount = usd*44
    print(amount,"$")
poulet()
costofpoulet(67)

#22. return stament
def allowed_dating_age(my_age):
    girls_age=my_age/2+7
    return girls_age
buck_limit = allowed_dating_age(27)
creepy_limit = allowed_dating_age(27)
print("buck can date girls",buck_limit,"or orders")
print("creepy limits ",creepy_limit,"or orders")

#23. default values for arguments
def get_genders(sex='unknown'):
    if sex is 'm':
        sex = "male"
    elif sex is 'f':
        sex = "female"
    print(sex)
get_genders('m')
get_genders('f')
get_genders()
#24.variable scope
#CORRECT
a=1234
def corn():

    print(a)
def fudge():
    print(a)
corn()
fudge()
#INCORRECT

def corn():
    a = 1234
    print(a)
def fudge():
    print(a)
corn()
fudge()

#25. keyboard arugments

def dump_sentece(name='sravan',action='ate',item='banana'):
    print(name,action,item)
def mme (name='langlois',age='29',bank='lcl'):
    print(name,age,bank)
dump_sentece()
dump_sentece("vasam","farts","gently")
dump_sentece(item='awesome')
dump_sentece(item='awesome',action='finish')
dump_sentece(item='sss',action='sjksdkd')
mme()

#26.Flexible number of arguments, addition with given first value
def add_numers(*args):
    total=0
    for a in args:
        total+=a
        print(total)
add_numers(3,4,333,24,223,34)


