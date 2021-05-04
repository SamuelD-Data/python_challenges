__Note: Skipping questions that I don't find useful, or which require me to print sensitive information (operating system, file paths, etc.)__

1. Write a Python program to print the following string. 
Sample String : "Twinkle, twinkle, little star':

1.
print('Twinkle, twinkle, little star')

2. Write a Python program to get the Python version you are using. 

2.
import sys
print(sys.version)

3. Write a Python program to display the current date and time.
Sample Output : 
Current date and time : 
2014-07-05 14:34:14

3.
from datetime import datetime
print('Current date and time : ', datetime.now())

4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
Sample Output : 
r = 1.1
Area = 3.8013271108436504

4.
def calc_area(r):
    return math.pi * r ** 2

5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 

5.
def name_swap(fn, ln):
    print(ln, fn)

6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
Sample data : 3, 5, 7, 23
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23')

6.
def lt(*arg):
    numlist = []
    for i in arg:
        numlist.append(i)
    print (numlist, tuple(numlist))

7. Write a Python program to accept a filename from the user and print the extension of that. 
Sample filename : abc.java 
Output : java

7.
def checkext(file):
    print(file.split('.')[1])

8. Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]

8.
def firstlast(colors):
    print(colors[0], ',', colors[-1])

9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

9.
def examsched(nums):
    print(nums[0],'/', nums[1],'/', nums[2])

10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
Sample value of n is 5 
Expected Result : 615

10.
def prodsum(n):
    n = str(n)
    print(int(n) + int(n * 2) + int(n * 3))

11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.

11.
def docs(f):
    print(f.__doc__)

12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. 

12. 
import calendar 

def calendarmaker(m, y):
    print(calendar.month(y, m))
    
calendarmaker(12, 2020)

13. Write a Python program to print the following 'here document'. 
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

13.
print('a string that you "don\'t" have to escape\nThis\nis a  ....... multi-line\nheredoc string --------> example')

14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 

14.
from datetime import date

def datedifference(d1, d2):
    print((date(d2[0], d2[1], d2[2]) - date(d1[0], d1[1], d1[2])).days)
    
datedifference((2014, 7, 2), (2014, 7, 11))

15. Write a Python program to get the volume of a sphere with radius 6.

15.
print(4/3 * math.pi * 6**3)

16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. 

16.
def nprob(n):
    if n <= 17:
        print(17 - n)
    else:
        print(abs(17 - n) * 2)

17. Write a Python program to test whether a number is within 100 of 1000 or 2000. 

17.
def rangecheck(n):
    if n >= 900 and n <= 1100:
        print('close to 1000')
    elif n >= 1900 and n <= 2100:
        print('close to 2000')
    else:
        print('close to neither 1000 or 2000')

18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. 

18.
def combothree(a, b, c):
    if a == b and b == c:
        print((a + b + c) * 3)
    else:
        return 'not equal'

19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. 

19.
def addis(s):
    if s[:1] == 'Is':
        print(s)
    else:
        print('Is' + s)

20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. 

20.
def ncopy(n, s):
    print(n * s)

21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. 

21.
def evenodd(n):
    if n % 2 == 1:
        print(n, 'is odd')
    else:
        print(n, 'is even')

22. Write a Python program to count the number 4 in a given list. 

22.
def countfour(l):
    return len([x for x in l if x == 4])

23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. 

23.
def twocopy(n, s):
    print(s[:2] * n)

24. Write a Python program to test whether a passed letter is a vowel or not. 

24.
def isvowel(l):
    return l.lower() in ['a', 'e', 'i', 'o', 'u']

25. Write a Python program to check whether a specified value is contained in a group of values. 
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

25.
def valcheck(v, l):
    return v in l

26. Write a Python program to create a histogram from a given list of integers. 

import matplotlib.pyplot as plt

def histplotter(l):
    plt.hist(l)
    plt.show()

27. Write a Python program to concatenate all elements in a list into a string and return it. 

def concatlist(l):
    a = ''
    for x in l:
        a += str(x)
    return a

28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. 
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

28.
[x for x in numbers if x % 2 == 0 and x < 237]

29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
Expected Output : 
{'Black', 'White'}

29.
[x for x in color_list_1 if x not in color_list_2]

30. Write a Python program that will accept the base and height of a triangle and compute the area. 

30.
def triarea(b, h):
    print((b * h) / 2)

31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 

31.
def gcdfinder(a, b):
    smallnum = min([a, b])
    divnums = []
    for x in range(1,smallnum + 1):
        if a % x == 0 and b % x == 0:
            divnums.append(x)
    return(max(divnums))

32. Write a Python program to get the least common multiple (LCM) of two positive integers. 

32.
def lcmfinder(a, b):
    gcd = gcdfinder(a, b)
    numerator = abs(a * b)
    print(numerator / gcd)

33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

33.
def triplesum(a, b, c):
    if a == b or a == c or b == c:
        print(0)
    else:
        print(a + b + c)

34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 

34.
def sumtwo(a, b):
    summed = a + b
    if summed >= 15 and summed <= 20:
        return 20
    else:
        return summed

35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

def check3cons(a, b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False

36. Write a Python program to add two objects if both objects are an integer type. 

36.
def addobj(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        return ('one or more arguments are not int type')

37. Write a Python program to display your details like name, age, address in three different lines. 

37.
def naa(name, age, address):
    print(name,'\n', age, '\n', address)

38. Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49

38.
def xyprob(x, y):
    print ((x+y) * (x+y))
    
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. 
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79

39.
def intcalc(amt, i, yrs):
    print(amt * i * yrs)

40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 

40.
def distcalc(x1, y1, x2, y2):
    print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

58. Write a python program to find the sum of the first n positive integers. 

def sum_ints(num):
    num_sum = 0
    for x in range(0, num + 1):
        num_sum += x
    return num_sum

59. Write a Python program to convert height (in feet and inches) to centimeters. 

def height_convert(ft, inches):
    return (ft * 30.48) + (inches * 2.54)

height_convert(1,3)

60. Write a Python program to calculate the hypotenuse of a right angled triangle. 

def hypot_right(a, b):
    return math.sqrt((a ** 2) + (b ** 2))

61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. 

def convert_ft(ft):
    print('inches:', ft * 12, '\nyards:', ft * 3, '\nmiles:', ft * 5280)

62. Write a Python program to convert all units of time into seconds. 

def convert_to_sec(t):
    print(t,'hour(s) =', t * 3600, 'seconds\n', t, 'minute(s) =', t * 60, 'seconds')

65. Write a Python program to convert seconds to day, hour, minutes and seconds. 

def second_conv(s):
    print('seconds:', s)
    print('minutes:', s / 60)
    print('hours:', s / 3600)
    print('days:', s / 86400)

66. Write a Python program to calculate body mass index. 

def calc_bmi(h, w):
    return (w / (h**2))

67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure. 

def conv_kp(kp):
    print('psi:', kp * 0.145038)
    print('mmhg:', kp * 7.50062)
    print('atmospheric pressure:', kp * 0.00986923)

68. Write a Python program to calculate the sum of the digits in an integer. 

def digit_sum(i):
    digits = [int(d) for d in str(i)]
    return sum(digits)

69. Write a Python program to sort three integers without using conditional statements and loops. 

def sort_ints(a, b, c):
    numlist = [a, b, c]
    numlist.sort()
    return numlist

81. Write a Python program to concatenate N strings. 

81.
def concat_n(n, s):
    print(s * n)

82. Write a Python program to calculate the sum over a container. 

82.
def sumcon(con):
    print(sum(con))

83. Write a Python program to test whether all numbers of a list is greater than a certain number. 

83.
def check_greater(l, n):
    check = False
    for x in l:
        if x > n:
            check = True
    return check

84. Write a Python program to count the number occurrence of a specific character in a string. 

84.
def occ_count(s, c):
    counter = 0
    for x in s:
        if x == c:
            counter += 1
    return counter

88. Given variables x=30 and y=20, write a Python program to print "30+20=50". 

88.
x = 30
y = 20
print(x, '+', y, '=', x + y)

89. Write a Python program to perform an action if a condition is true. 
Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.

89.
def val_check(v):
    if v == 1:
        print('First day of a Month!')

91. Write a Python program to swap two variables. 

91.
def vswap(a, b):
    c = a
    a = b
    b = c
    return a, b

95. Write a Python program to check whether a string is numeric. 

95.
def sign_check(n):
    if n == 0:
        print('zero')
    elif n > 0:
        print('positive')
    else:
        print('negative')

109. Write a Python program to check if a number is positive, negative or zero. 

109.
def sign_check(n):
    if n == 0:
        print('zero')
    elif n > 0:
        print('positive')
    else:
        print('negative')
        
112. Write a Python program to remove the first item from a specified list. 

112.
def drop_first(l):
    return l[1:]


113. Write a Python program to input a number, if it is not a number generate an error message.

113.
def numcheck(n):
    if type(n) not in [int, float]:
        print('error')
    else:
        print('is numerical')

114. Write a Python program to filter the positive numbers from a list. 

def allpos(l):
    return [n for n in l if n < 0]

115. Write a Python program to compute the product of a list of integers (without using for loop). 

from numpy import product

def lprod(l):
    return product(l)
    
120. Write a Python program to format a specified string to limit the number of characters to 6. 

120.
def trim_string(s):
    return s[0:6]

121. Write a Python program to determine whether variable is defined or not.

121.
try:
    v
except NameError:
    print("variable has not been assigned any value")
else:
    print("variable has been assigned value:", v)

124. Write a Python program to check whether multiple variables have the same value. 

124.
a = 2
b = 3

if a == b:
    print('variables have matching value')
else:
    print('variables have different values')

128. Write a Python program to check whether lowercase letters exist in a string. 

128.
def lowerccheck(s):
    val = False
    for x in s:
        if x.islower() == True:
            print('lowercase letter found:', x)

129. Write a Python program to add trailing and leading zeroes to a string. 

129.
def addzeros(s):
    return '0' + s + '0'

138. Write a Python program to convert true to 1 and false to 0. 

138.
def swapbool(b):
    if b == True:
        return 1
    else:
        return 0

139. Write a Python program to valid a IP address. 

139.
def ipvalidate(i):
    splitl = []
    status = True
    for x in i.split('.'):
        splitl.append(x)
    if len(splitl) != 4:
        print('octet amount not equal to 4')
        status = False
    elif len(splitl) == 4:
        for o in splitl:
            if len(o) > 3:
                print('too many numbers in octect:', o)
                status = False
    if status == True:
        print('Ip Valid')

144. Write a Python program to check whether variable is of integer or string. 

144.
def typecheck(v):
    if type(v) == str:
        print('is string')
    elif type(v) == int:
        print('is integer')
    else:
        print('not integer or string')

145. Write a Python program to test if a variable is a list or tuple or a set. 

145.
def varcheck2(v):
    if type(v) == list:
        print('is list')
    elif type(v) == tuple:
        print('is tuple')
    elif type(v) == set:
        print('is set')
    else:
        print('is not list, tuple or set')

147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user. 

147.
def divcheck(a, b):
    if a % b != 0:
        print('not evenly divisible')
    else:
        print('evenly divisible')

148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. 

148.
def maxmin(l):
    return max(l), min(l)

149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. 


150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values. 
