import fn      #import from fn.py and when you run it import all the output of fn.py and also the last line of fn.py(ln 57 & 58)
fn.greetings("morning")

import datetime
x = datetime.datetime.now()
print(x)
print(x.strftime("%H"))  #strftime() inputs some certain format code in. just like these

import platform
x = platform.system()
b = platform.machine()
print(x)
print(platform.platform())
print(b)

#import re

import camelcase  #regarding pip and installation of camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))


import matplotlib
print(matplotlib.__version__)

