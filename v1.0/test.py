# #!/usr/bin/python

# for num in range(10,50):  #to iterate between 10 to 20
#   for i in range(2,num): #to iterate on the factors of the number
#      if num%i == 0:      #to determine the first factor
#         j=num/i          #to calculate the second factor
#         print '%d equals %d * %d' % (num,i,j)
#         break #to move to the next number, the #first FOR
#   else:                  # else part of the loop
#      print num, 'is a prime number'

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1

# print "Good bye!"
# for letter in 'Python':     # First Example
#    if letter == 'h':
#       pass
#       print 'this block is passed'
#    print 'Current Letter :', letter
  
# var = 10                    # Second Example
# while var > 0:              
#    print 'Current variable value :', var
#    var = var -1
#    if var == 5:
#       break
import math ;
import random ;
random.seed()
print random.randrange(1,100,7)
ls=[1,2,3,6,4]
random.shuffle(ls)
print ls
print random.uniform(5,20)
print math.hypot(3, 4)
print math.e
# print (random.random())
# print math.sqrt(25)
print "Good by"
print "mohamed hakeem"