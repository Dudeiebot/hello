#import random
#x = "baed"
#def orange():
shii = "HELLO WORLD"
y = int(10)
#print(bool(y))
#print(bool(x))
print(shii.lower())
print(isinstance(y, bool))


#x = y = z = Orange
#print (random.randrange(2,20))


#orange()
#print("let talk about" + x )



class myclass():
    def _len_(self):
        return 0

myobj = myclass
print(bool(myobj))


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

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
 
