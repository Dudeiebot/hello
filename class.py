class myLanguage:
    def __init__(languagename, exhibit1, exhibit2):
      languagename.exhibit1 = exhibit1
      languagename.exhibit2 = exhibit2                  #GG the most perfect example to understand the init and assigning of the variables.

learn = myLanguage ("yoruba", "igbo")
print("my languages are: " + learn.exhibit1 + " and " + learn.exhibit2 )
#print(learn.exhibit2)


class Dude:
    def __init__(me, myName, myAge, myCity):
        me.myName = myName
        me.myAge = myAge
        me.myCity = myCity

    def __str__(me):            #GG exhibit __str__ pushing in with other variables put in.
        return f"{me.myName} is my name and my age is {me.myAge} and i also live in {me.myCity}"
dude1 = Dude("excel", 23, "abuja")
print(dude1)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + " and my age is " + str(self.age))

p1 = Person("John", 30)
p2 = Person("Jane", 30)
p1.myfunc()
p2.myfunc()




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " and my age is " + str(self.age))

p1 = Person("John", 36)
p1.myfunc()

class Student(Person):      #deriv/child class to Person above.
    pass

s1 = Student("paul", 28)
s1.myfunc()


