## Basics Part 2

__Note: Skipping questions that I don't find useful, or which require me to print sensitive information (operating system, file paths, etc.)__

1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other. 

1. 
def alldiffnum(*arg):
    numl = []
    for x in arg:
        numl.append(x)
    if len(set(numl)) == len(numl):
        print('all numbers unique')
    else:
        print('not all numbers are unique')

2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

2. 
from itertools import permutations as perms
vowels = ['a', 'e', 'i', 'o', 'u']
list(perms(vowels, 5))

3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

3.
numl = [1,2,3,4,5,6]

while len(numl) > 0:
    if len(numl) <= 2:
        print(numl[-1])
        del numl[-1]
    else:
        print(numl[2])
        del numl[2]

5. Write a Python program to create the combinations of 3 digit combo. 

5.
from itertools import combinations as combos

vowels = [1, 2, 3, 4, 5, 6]
list(combos(vowels, 3))

6. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies. 

6.
import pandas as pd

longstring = "The river is famous to the fish. The loud voice is famous to silence, which knew it would inherit the earth before anybody said so."

longstring = longstring.replace('.', '')
longstring = longstring.replace(',', '')

longstring = longstring.split()

longstring = pd.Series(data = longstring)

longstring.value_counts()

7. Write a Python program to count the number of each character of a given text of a text file. 

7.
longstring = "The river is famous to the fish. The loud voice is famous to silence, which knew it would inherit the earth before anybody said so."

longstring = longstring.replace('.', '')
longstring = longstring.replace(',', '')

longstring =[x for x in longstring]

edict = {}

for x in longstring:
    edict[x] = 0
    
for x in longstring:
    edict[x] += 1

12. Write a Python program to create all possible permutations from a given collection of distinct numbers.

12.
from itertools import permutations as perms

def permer(n):
    return list(perms(n))

16. Write a Python program to get the third side of right angled triangle from two given sides. 

16.
import math 

def ratri(a, b):
    return math.sqrt(a**2 + b**2)

18. Write a Python program to find the median among three given numbers. 

18.
def findmed(l):
    l.sort()
    if len(l) % 2 == 0:
        rpoint = int((len(l) / 2))
        lpoint = int(rpoint - 1)
        return (l[lpoint] + l[rpoint]) / 2
    else:
        return l[math.floor(len(l) / 2)]

24. Write a Python program to find the number of divisors of a given integer is even or odd. 

24.
def signofdiv(n):
    nlist = []
    for x in range(1, n + 1):
        if n % x == 0:
            nlist.append(x)
    if len(nlist) % 2 == 0:
        return 'divisor count is even'
    if len(nlist) % 2 == 1:
        return 'divisor count is odd'

25. Write a Python program to find the digits which are absent in a given mobile number. 

25.
def mobilecheck(n):
    validnumber = True
    for place, nums in enumerate(n.split('-')):
        if place <= 1:
            if len(nums) < 3:
                print('not enough numbers in at least one section of mobile number')
                validnumber = False
        if place == 2:
            if len(nums) < 4:
                print('not enough numbers in at least one section of mobile number')
                validnumber = False
    if validnumber == True:
        print('Phone number is missing no numbers')

29. Write a Python program to find common divisors between two numbers in a given pair. 

29.
def comdiv(a , b):
    anums = [x for x in range(1, a + 1) if a % x == 0]
    bnums = [x for x in range(1, b + 1) if b % x == 0]
    cds = [x for x in anums if x in bnums]
    return cds

30. Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure. 
Note: A palindrome is a word, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.

30.
def palcheck(n):
    while n != int(str(n)[::-1]):
        n = n + int(str(n)[::-1])
    return n

32. Write a python program to find heights of the top three building in descending order from eight given buildings. 
Input:
0 <= height of building (integer) <= 10,000
Input the heights of eight buildings:
25
35
15
16
30
45
37
39
Heights of the top three buildings:
45
39
37

32.
def findmaxh(l):
    l.sort(reverse = True)
    return l[0:3]

34. Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No". 
Input:
Integers separated by a single space.
1 <= length of the side <= 1,000
Input three integers(sides of a triangle)
8 6 7
No

34.
def rtricheck(a, b, c):
    if (a**2 + b**2) == c**2:
        return "Yes"
    else:
        return "No"

41. Write a Python program to compute and print sum of two given integers (more than or equal to zero). If given integers or the sum have more than 80 digits, print "overflow". 
Input first integer:
25
Input second integer:
22
Sum of the two integers: 47

41.
def overflow(a, b):
    if len(str(a + b)) > 80:
        print ('overflow')
    else:
        print (a + b)
        
41.
def sortnums(*args):
    arglist = []
    for x in args:
        arglist.append(x)
    arglist.sort()
    return arglist

42. Write a Python program that accepts six numbers as input and sorts them in descending order. 
Input:
Input consists of six numbers n1, n2, n3, n4, n5, n6 (-100000 <= n1, n2, n3, n4, n5, n6 <= 100000). The six numbers are separated by a space.
Input six integers:
15 30 25 14 35 40
After sorting the said integers:
40 35 30 25 15 14

42.
def sortnums(*args):
    arglist = []
    for x in args:
        arglist.append(x)
    arglist.sort()
    return arglist

47. Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters. 

Note: A word is a sequence of letters which is separated by the spaces.

Input: 
A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text.
Input text: Thank you for your comment and your participation.
Output: your participation.

47.
import pandas as pd

longstring = "The river is famous to the fish The loud voice is famous to silence which knew it would inherit the earth before anybody said so"

lengthdict = {}

for x in longstring.split():
    lengthdict[x] = len(x)

for key, value in lengthdict.items():
    if value == max(lengthdict.values()):
        print(key)
        
longstringser = [x for x in longstring.split() if x != ' ']

longstringser = pd.Series(data = longstringser)

lser = pd.DataFrame(longstringser.value_counts()) 

lser.columns = ['wcount']

lser[lser.wcount == 2]

50. Write a Python program to replace a string "Python" with "Java" and "Java" with "Python" in a given string. 
Input:
English letters (including single byte alphanumeric characters, blanks, symbols) are given on one line. The length of the input character string is 1000 or less.
Input a text with two words 'Python' and 'Java'
Python is popular than Java
Java is popular than Python

50.
def replang(s):
    s = s.replace('Python', 'J')
    s = s.replace('Java', 'Python')
    s = s.replace('J', 'Java')
    return s


72. Write a Python program to check whether a given integer is a palindrome or not. 
Note: An integer is a palindrome when it reads the same backward as forward. Negative numbers are not palindromic.
Sample Input:
(100)
(252)
(-838)
Sample Output:
False
True
False

72.
def palcheck2(n):
    if n == n[::-1]:
        print('palindome')
    else:
        print('not palindrome')


73. Write a Python program to remove the duplicate elements of a given array of numbers such that each element appear only once and return the new length of the given array. 
Sample Input:
[0,0,1,1,2,2,3,3,4,4,4]
[1, 2, 2, 3, 4, 4]
Sample Output:
5
4

73.
def duprem(a, i):
    for x in a:
        if x == i:
            a.remove(i)
    return a

75. Write a Python program to remove all instances of a given value from a given array of integers and find the length of the new array. 
Sample Input:
([1, 2, 3, 4, 5, 6, 7, 5], 5)
([10,10,10,10,10], 10) 
([10,10,10,10,10], 20) 
([], 1)
Sample Output:
6
0
5
0

75.
def duprem(a, i):
    for x in a:
        if x == i:
            a.remove(i)
    return len(a)

80. Write a Python program to find the first missing integer that does not exist in a given list. 
Sample Input:
[2, 3, 7, 6, 8, -1, -10, 15, 16]
[1, 2, 4, -7, 6, 8, 1, -10, 15]
[1, 2, 3, 4, 5, 6, 7]
[-2, -3, -1, 1, 2, 3]
Sample Output:

4
3
8
4

80.
def numlist(l):
    l.sort()
    allnums = []
    for x in range(l[0],l[-1]+1):
        allnums.append(x)
    for y in allnums:
        if y not in l:
            return y

81. Write a Python program to randomly generate a list with 10 even numbers between 1 and 100 inclusive. 
Note: Use random.sample() to generate a list of random values.
Sample Input:
(1,100)
Sample Output:

[4, 22, 8, 20, 24, 12, 30, 98, 28, 48]

81.
import random

print(random.sample([n for n in range(1, 100) if n % 2 == 0], 10))

82. Write a Python program to calculate the median from a list of numbers. 
Sample Input:
[1,2,3,4,5]
[1,2,3,4,5,6]
[6,1,2,4,5,3]
[1.0,2.11,3.3,4.2,5.22,6.55]
[1.0,2.11,3.3,4.2,5.22]
[2.0,12.11,22.3,24.12,55.22]
Sample Output:
3
3.5
3.5
3.75
3.3
22.3

import math

def findmed(l):
    l.sort()
    if len(l) % 2 == 0:
        rpoint = int((len(l) / 2))
        lpoint = int(rpoint - 1)
        return (l[lpoint] + l[rpoint]) / 2
    else:
        return l[math.floor(len(l) / 2)]

83. Write a Python program to test whether a given number is symmetrical or not. 
A number is symmetrical when it is equal of its reverse.
Sample Input:
(121)
(0)
(122)
(990099)
Sample Output:
True
True
False
True

83.
def symcheck(n):
    if len(str(n)) % 2 == 1:
        halfp = int(math.ceil(len(str(n)) / 2))
        firsth = str(n)[:halfp]
        secondh = str(n)[halfp - 1:]
        if secondh[::-1] != firsth:
            print('not symmetrical')
        else:
            print('symmetrical')
        print(firsth, secondh)
    else:
        halfp = int(len(str(n)) / 2)
        firsth = (str(n)[0: halfp]) 
        secondh = (str(n)[halfp:])
        if (secondh[::-1]) != (firsth):
            print('not symmetrical')
        else:
            print('symmetrical')


84. Write a Python program that accept a list of numbers and create a list to store the count of negative number in first element and store the sum of positive numbers in second element. 
Sample Input:
[1, 2, 3, 4, 5]
[-1, -2, -3, -4, -5]
[1, 2, 3, -4, -5]
[1, 2, -3, -4, -5]
Sample Output:
[0, 15]
[5, 0]
[2, 6]
[3, 3]


85. From Wikipedia:
An isogram (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter. It is also used by some people to mean a word or phrase in which each letter appears the same number of times, not necessarily just once. Conveniently, the word itself is an isogram in both senses of the word, making it autological.
Write a Python program to check whether a given string is an "isogram" or not. 
Sample Input:
("w3resource")
("w3r")
("Python")
("Java")
Sample Output:
False
True
True
False


86. Write a Python program to count the number of equal numbers from three given integers. 
Sample Input:
(1, 1, 1)
(1, 2, 2)
(-1, -2, -3)
(-1, -1, -1)
Sample Output:
3
2
0
3


87. Write a Python program to check whether a given employee code is exactly 8 digits or 12 digits. Return True if the employee code is valid and False if it's not. 
Sample Input:
('12345678')
('1234567j')
('12345678j')
('123456789123')
('123456abcdef')
Sample Output:
True
False
False
True
False


88. Write a Python program that accept two strings and test if the letters in the second string are present in the first string. 
Sample Input:
["python", "ypth"]
["python", "ypths"]
["python", "ypthon"]
["123456", "01234"]
["123456", "1234"]
Sample Output:
True
False
True
False
True


89. Write a Python program to compute the sum of the three lowest positive numbers from a given list of numbers. 
Sample Input:
[10, 20, 30, 40, 50, 60, 7]
[1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5]
Sample Output:
37
6
6


90. Write a Python program to replace all but the last five characters of a given string into "*" and returns the new masked string. 
Sample Input:
("kdi39323swe")
("12345abcdef")
("12345")
Sample Output:
******23swe
******bcdef
12345


91. Write a Python program to count the number of arguments in a given function. 
Sample Input:
()
(1)
(1, 2)
(1, 2, 3)
(1, 2, 3, 4)
[1, 2, 3, 4]
Sample Output:
0
1
2
3
4
1


92. Write a Python program to compute cumulative sum of numbers of a given list. 
Note: Cumulative sum = sum of itself + all previous numbers in the said list.
Sample Input:
[10, 20, 30, 40, 50, 60, 7]
[1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5]
Sample Output:
[10, 30, 60, 100, 150, 210, 217]
[1, 3, 6, 10, 15]
[0, 1, 3, 6, 10, 15]


93. Write a Python program to find the middle character(s) of a given string. If the length of the string is odd return the middle character and return the middle two characters if the string length is even. 
Sample Input:
("Python")
("PHP")
("Java")
Sample Output:
th
H
av


94. Write a Python program to find the largest product of the pair of adjacent elements from a given list of integers. 
Sample Input:
[1,2,3,4,5,6]
[1,2,3,4,5]
[2,3]
Sample Output:
30
20
6


95. Write a Python program to check whether every even index contains an even number and every odd index contains odd number of a given list. 
Sample Input:
[2, 1, 4, 3, 6, 7, 6, 3]
[2, 1, 4, 3, 6, 7, 6, 4]
[4, 1, 2]
Sample Output:
True
False
True


96. Write a Python program to check whether a given number is a narcissistic number or not. 

If you are a reader of Greek mythology, then you are probably familiar with Narcissus. He was a hunter of exceptional beauty that he died because he was unable to leave a pool after falling in love with his own reflection. That's why I keep myself away from pools these days (kidding).
In mathematics, he has kins by the name of narcissistic numbers - numbers that can't get enough of themselves. In particular, they are numbers that are the sum of their digits when raised to the power of the number of digits.
For example, 371 is a narcissistic number; it has three digits, and if we cube each digits 33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
153 = 13 + 53 + 33
370 = 33 + 73 + 03
407 = 43 + 03 + 73.
There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
1634 = 14+64+34+44
8208 = 84+24+04+84
9474 = 94+44+74+44
It has been proven that there are only 88 narcissistic numbers (in the decimal system) and that the largest of which is
115,132,219,018,763,992,565,095,597,973,971,522,401
has 39 digits.

Ref.: //https://bit.ly/2qNYxo2
Sample Input:
(153)
(370)
(407)
(409)
(1634)
(8208)
(9474)
(9475)
Sample Output:
True
True
True
False
True
True
True
False


97. Write a Python program to find the highest and lowest number from a given string of space separated integers. 
Sample Input:
("1 4 5 77 9 0")
("-1 -4 -5 -77 -9 0")
("0 0")
Sample Output:
(77, 0)
(0, -77)
(0, 0)


98. Write a Python program to check whether a sequence of numbers has an increasing trend or not. 
Sample Input:
[1,2,3,4]
[1,2,5,3,4]
[-1,-2,-3,-4]
[-4,-3,-2,-1]
[1,2,3,4,0]
Sample Output:
True
False
False
True
False


99. Write a Python program to find the position of the second occurrence of a given string in another given string. If there is no such string return -1. 
Sample Input:
("The quick brown fox jumps over the lazy dog", "the")
("the quick brown fox jumps over the lazy dog", "the")
Sample Output:
-1
31


100. Write a Python program to compute the sum of all items of a given array of integers where each integer is multiplied by its index. Return 0 if there is no number. 
Sample Input:
[1,2,3,4]
[-1,-2,-3,-4]
[]
Sample Output:
20
-20
0


101. Write a Python program to find the name of the oldest student from a given dictionary containing the names and ages of a group of students. 
Sample Input:
{"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
{"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4, "Joannie Archibald": 12.6, "Becki Saunder": 12.7}
Sample Output:
Nidia Dominique
Becki Saunder


102. Write a Python program to create a new string with no duplicate consecutive letters from a given string. 
Sample Input:
("PPYYYTTHON")
("PPyyythonnn")
("Java")
("PPPHHHPPP")
Sample Output:
PYTHON
Python
Java
PHP


103. Write a Python program to check whether two given lines are parallel or not. 
Note: Parallel lines are two or more lines that never intersect. Parallel Lines are like railroad tracks that never intersect.
The General Form of the equation of a straight line is: ax + by = c
The said straight line is represented in a list as [a, b, c]
Example of two parallel lines: 
x + 4y = 10 and x + 4y = 14
Sample Input:
([2,3,4], [2,3,8])
([2,3,4], [4,-3,8])
Sample Output:
True
False


104. Write a Python program to find the lucky number(s) in a given matrix. 
Sample Input:
Original matrix: [[1, 2], [2, 3]]
Lucky number(s) in the said matrix: [2]
Original matrix: [[1, 2, 3], [3, 4, 5]]
Lucky number(s) in the said matrix: [3]
Original matrix: [[7, 5, 6], [3, 4, 4], [6, 5, 7]]
Lucky number(s) in the said matrix: [5]


105. Write a Python program to check whether a given sequence is linear, quadratic or cubic. 
Sequences are sets of numbers that are connected in some way.
Linear sequence:
A number pattern which increases or decreases by the same amount each time is called a linear sequence. The amount it increases or decreases by is known as the common difference.
Quadratic sequence:
In quadratic sequence, the difference between each term increases, or decreases, at a constant rate.
Cubic sequence:
Sequences where the 3rd difference are known as cubic sequence.
Sample Input:
[0,2,4,6,8,10]
[1,4,9,16,25]
[0,12,10,0,-12,-20]
[1,2,3,4,5]
Sample Output:
Linear Sequence
Quadratic Sequence
Cubic Sequence
Linear Sequence


106. Write a Python program to test whether a given integer is pandigital number or not. 
From Wikipedia,
In mathematics, a pandigital number is an integer that in a given base has among its significant digits each digit used in the base at least once.
For example, 
1223334444555556666667777777888888889999999990 is a pandigital number in base 10.
The first few pandigital base 10 numbers are given by:
1023456789, 1023456798, 1023456879, 1023456897, 1023456978, 1023456987, 1023457689
Sample Input:
(1023456897)
(1023456798)
(1023457689)
(1023456789)
(102345679)
Sample Output:
True
True
True
True
False


107. Write a Python program to check whether a given number is Oddish or Evenish. 
A number is called "Oddish" if the sum of all of its digits is odd, and a number is called "Evenish" if the sum of all of its digits is even.
Sample Input:
(120)
(321)
(43)
(4433)
(373)
Sample Output:
Oddish
Evenish
Oddish
Evenish
Oddish


108. Write a Python program that takes three integers and check whether the last digit of first number * the last digit of second number = the last digit of third number. 
Sample Input:
(12, 22, 44)
(145, 122, 1010)
(0, 22, 40)
(1, 22, 40)
(145, 122, 101)
Sample Output:
True
True
True
False
False


109. Write a Python program find the indices of all occurrences of a given item in a given list. 
Sample Input:
([1,2,3,4,5,2], 2)
([3,1,2,3,4,5,6,3,3], 3)
([1,2,3,-4,5,2,-4], -4)
Sample Output:
[1, 5]
[0, 3, 7, 8]
[3, 6]


110. Write a Python program to remove two duplicate numbers from a given number of list. 
Sample Input:
([1,2,3,2,3,4,5])
([1,2,3,2,4,5])
([1,2,3,4,5])
Sample Output:
[1, 4, 5]
[1, 3, 4, 5]
[1, 2, 3, 4, 5]


111. Write a Python program to check whether two given circles (given center (x,y) and radius) are intersecting. Return true for intersecting otherwise false. 
Sample Input:
([1,2, 4], [1,2, 8])
([0,0, 2], [10,10, 5])
Sample Output:
True
False


112. Write a Python program to compute the digit distance between two integers. 
The digit distance between two numbers is the absolute value of the difference of those numbers.
For example, the distance between 3 and -3 on the number line given by the |3 - (-3) | = |3 + 3 | = 6 units
Digit distance of 123 and 256 is
Since |1 - 2| + |2 - 5| + |3 - 6| = 1 + 3 + 3 = 7
Sample Input:
(123, 256)
(23, 56)
(1, 2)
(24232, 45645)
Sample Output:
7
6
1
11


113. Write a Python program to reverse all the words which have even length. 
Sample Input:
("The quick brown fox jumps over the lazy dog")
("Python Exercises")
Sample Output:
The quick brown fox jumps revo the yzal dog
nohtyP Exercises


114. Write a Python program to print letters from the English alphabet from a-z and A-Z. 
Sample Input:
("Alphabet from a-z:")
("\nAlphabet from A-Z:")
Sample Output:
Alphabet from a-z:
a b c d e f g h i j k l m n o p q r s t u v w x y z 
Alphabet from A-Z:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 


115. Write a Python program to generate and prints a list of numbers from 1 to 10. 
Sample Input:
range(1,10)
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6', '7', '8', '9']


116. Write a Python program to identify nonprime numbers between 1 to 100 (integers). Print the nonprime numbers. 
Sample Input:
range(1, 101)
Sample Output:
Nonprime numbers between 1 to 100:
4
6
8
9
10
..
96
98
99
100


117. Write a Python program to make a request to a web page, and test the status code, also display the html code of the specified web page. 
Sample Output:
Web page status: <Response [200]>
HTML code of the above web page:
<!doctype html>
<html>
<head>
<title>Example Domain</title>
<meta charset="utf-8" />
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
</head>
<body>
<div>
<h1>Example Domain</h1>
<p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>
<p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>



118. In multiprocessing, processes are spawned by creating a Process object. Write a Python program to show the individual process IDs (parent process, process id etc.) involved. 
Sample Output:
Main line
module name: __main__
parent process: 23967
process id: 27986
function f
module name: __main__
parent process: 27986
process id: 27987
hello bob


119. Write a Python program to check if two given numbers are coprime or not. Return True if two numbers are coprime otherwise return false. 
Sample Input:
(17, 13)
(17, 21)
(15, 21)
(25, 45)
Sample Output:
True
True
False
False


120. Write a Python program to calculate Euclid's totient function of a given integer. Use a primitive method to calculate Euclid's totient function. 
Sample Input:
(10)
(15)
(33)
Sample Output:
4
8
20
