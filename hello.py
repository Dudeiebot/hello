#import random
#x = "baed"
#def orange():
y = int(10)
#print(bool(y))
#print(bool(x))
shii = "HELLO WORLD"
print(shii.lower())  # to lower case
print(isinstance(y, bool))


#x = y = z = Orange
#print (random.randrange(2,20))


#orange()
#print("let talk about" + x )



#class myclass():
 #   def _len_(self):
  #      return 0

#myobj = myclass
#print(bool(myobj))


thislist = list(("pen", "mirror", "school", "people"))
mylist = ["show", "aeyan", "rabbit", "inter"]
#thislist[2]= "negro"
#thislist.insert(4, "banana")
#mylist.pop(2)
#del thislist[4]
thislist.remove("pen")
mylist.append(thislist)
print(mylist)
#mylist.clear()
#thislist.extend(mylist)
#[print(show) for show in mylist]
#print(thislist)


SchoolList = ["20", "50", "70", "100"]
SchoolList.sort(reverse = True)
print(SchoolList)
#i = 0
#while i < len(SchoolList):
 #   print(SchoolList[i])
  #  i = i + 1

tuplePersona = ("chill", "aggressive", "sherah", "loom")
#y = "rant",
#tuplePersona += y
#x = list(tuplePersona)
#x.remove("loom")
for chill in tuplePersona:
    print(tuplePersona)

LetTalkSet = {"yuno", "pro", "agbavi", "shill"}
steel_set = {"30", "40", "50", "70"}
x = LetTalkSet.union(steel_set)
#x = LetTalkSet.pop()
print(x)
#print(LetTalkSet)


Dict_ionaary = {"black" : "police",
                "house" : "duplex",
                "type" : "prodigy",
                "parent" : "assistance" }

#print(Dict_ionaary["house"])
y = Dict_ionaary.values()
Dict_ionaary.update({"color" : "blue"})
print(Dict_ionaary)
print(y)

a = "50"
b = "100"
print("shiit") if b != a else print("LFG")


if a > b:
    print("biish")
elif b == a:
    print("it goes down")
else:
    print("the other report")

a = 1
while a < 6:
    print(a)
    if a == 3:
        break
    a += 1
 
b = 3
while b < 11:
    b += 2
    if b == 7:
        continue
    print(b)

#i = 1
#while i < 5:
#    print (i)
#    if i == 3:
#       break
#    i += 1


for x in range(3, 7):
    print(x)

footballer = ["pele", "neymar", "ronaldo", "messi"]
country = ["brazil", "brazil2", "portugal", "argentina"]
for x in footballer:
    for y in country:
        print(x, y)

def function_main(fname):
   print(fname + "peculiar")
    
function_main("siddiq")
function_main("penny")
function_main("tally")
function_main("yeats")

#these practically add up all the factorial value of n up but you can check up the one that lsit them all in fn.py
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("The factorial of 5 is", factorial(5))

