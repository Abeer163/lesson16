def cube(number):
   return number*number*number
def calc(number):
   if number %3 ==0:
      print("your number is divisible by 3")
      return cube(number)
   else:
      print("false")
print(calc(9))

