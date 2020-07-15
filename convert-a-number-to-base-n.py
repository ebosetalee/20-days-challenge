import random
number = int(random.random()*1000000000)
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
base_number = int(random.choice(my_list)) 
print(base_number)

def calculate_base():
    res=""
    a = number
    while (a > 0):
      c = a % base_number
      d = a // base_number
      res+=str(c)
      a = d
    print("{0} to base {1:2} is {2}".format(number,base_number,res[::-1]))

def calclulate_base_16():
    print("{0} to base 16 is {0:>04x}".format(number))

def base_11_to_15():
    base_value = "0123456789abcde"
    res=""
    a = number
    while (a > 0):
      c = a % base_number
      d = a // base_number
      res+= base_value[c]
      a = d
    print("{0} to base {1} is {2}".format(number,base_number,res[::-1]))

if base_number < 10:
    calculate_base()
elif (base_number == 16):
    calclulate_base_16()
else:
    base_11_to_15()