def function_main(fname):
    print(fname +  "peculiar")
function_main("siddiq")
function_main("penny")
function_main("tally")
function_main("yeats")


def myfunction(gname, sname):
 print(gname + " " + sname)
myfunction("tunde", "shammah")

def my_children(child1, child2, child3, child4 ):
    print("here are my children: " + child1 + ", " + child2 + ", " + child3 + ", " + child4)
my_children(child1 = "fat", child2 = "slim", child3 = "cool" , child4 = "obese") 


def multiplying(learn):
    return 10 * learn

print(multiplying(3))
print(multiplying(2))
print(multiplying(1))


#these practically list all the factorial of a number added

def tri_recursion(n):
    if(n > 0):
       result = n + tri_recursion(n-1)
       print (result)
    else:
      result = 0
    return result

print("recursion example:")
tri_recursion(7)



def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(5))

def functn(b):
    return lambda x : b + x

myaddition = functn(100)
addbro = functn(20)
print(myaddition(10))
print(addbro(10))

def greetings(name):
    print("good" + name)
