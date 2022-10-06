#2.11
#a
total = 0
negative = [-7,-6,-5,-4,-3,-2,-1]
for i in negative:
    total = total + negative[i]
print(total)

#2.11
#b

x=[17*9,24*10,21*11,27*12]
y=[17,24,21,27]

average_age = sum(x)/sum(y)
print(round(average_age))


#2.11
#c

res = 2**-20
print(res)

#2.11
#d

result = 4356/61
print(result)

#2.11
#e

result = 4356//61
print(result)

#2.12
s1 = '-'
s2 = '+'

#a
print(s1+s2)
#b
print(s1+s2+s1)
#c
print(s2+s1+s1)
#d
print(s2+s1+s1+s2+s1+s1)
#e
print(s2+(s1*2)+s2+(s1*2)+s2+(s1*2)+s2+(s1*2)+s2+(s1*2)+s2+(s1*2)+s2+(s1*2)+s2+(s1*2)+s2+(s1*2)+s2+(s1*2)+s2)

#2.13
s = 'abcdefghijklmnopqrstuvwxyz'
#a
for i in s:
    if i=='a':
        print(i)
#c
print(s[2])
#z
print(s[25])
#y
print(s[24])
#q
for i in s:
    if i=='q':
        print(i)


#2.14
s = 'goodbye'

#a
if s[0]=='g':
    print('True')
else:
    print('False')
#b
if s[6]=='g':
    print('True')
else:
    print('False')
#c
if s[0]=='g' and s[1]=='a':
    print('True')
else:
    print('False')
# # #d
# if s[6]=='x':
#     print('True')
# else:
#     print('False')
#e
middle = s[len(s)//2]
if middle == 'd':
    print('True')
else:
    print('False')

#f
if s[0] == s[-1]:
    print('True')
else:
    print('False')

#g
if s[-4:] == 'tion':
    print('True')
else:
    print('False')

#2.15
#a
string1 = 'anachronistically'
string2 = 'counterintuitive'

if len(string1) > len(string2):
    print('The word anachronistically is 1 more than the numbers of characters in the word counterintuitive.')
else:
    print('The statement is false.')

#b 
string1 = 'misinterpretation'
string2 = 'misrepresentation'
if string1 < string2:
    print('The word misinterpretation appears earlier in the dictionary than the word misrepresentation.')
else:
    print('False')

#c
string1 = 'floccinaucinihilipilification'
if 'e' not in string1:
    print('The letter e does not appear in the word floccinaucinihilipilification.')
else:
    print('The statement is False, e is present in the string')

#d
string1 = "counterrevolution"
string2 = 'counter'
string3 = 'resolution'

if len(string1) == (len(string2)+len(string3)):
    print('The number of characters in the word counterrevolution is equal to the sum of the number of characters in words counter and resolution.')
else:
    print('The statement is false')
    
#2.16
#a
a = 6
b = 7
print(a,b)

#b
c = (a+b)/2
print(c)

#c
inventory = ['paper','staples','pencils']
print(inventory)

#d
first,middle,last = 'John','Fitzgerald','Kennedy'
print(first,middle,last)

#e
fullname = first+' '+middle+' '+last
print(fullname)

#2.17
#a
if (17+9) < 10:
    print('True')
else:
    print('False')

#b
if len(inventory) > (5*len(fullname)):
    print('True')
else:
    print('False')

#c
if c<=24:
    print('True')
else:
    print('False')

#d
if a < 6.75 and b> 6.75:
    print('True')
else:
    print('False')

#e
if len(middle)>len(first) and len(middle)<len(last):
    print('True')
else:
    print('False')

#f
if len(inventory) == 0 or len(inventory) > 10:
    print('True')
else:
    print('False')

#2.18
#a
flowers = ['rose','bougainvillea','yucca', 'marigold', 'daylilly','lilly of the valley']
print(flowers)

#b
if 'potato' in flowers:
    print('True')
else:
    print('False')

#c
thorny = flowers[:3]
print(thorny)

#d
poisonous = flowers[-1:]
print(poisonous)

#e
dangerous = thorny+poisonous
print(dangerous)

#2.19
answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']

#a
yeslist = []
for i in answers:
    if i == 'Y':
        yeslist.append(i)
numYes = len(yeslist)
print(numYes)

#b
nolist = []
for i in answers:
    if i == 'N':
        nolist.append(i)
numNo = len(nolist)
print(numNo)

#c
length_answers = len(answers)
percentYes = (numYes/length_answers)*100
print(percentYes)

#d
answers.sort()
print(answers)
        
#e
f=answers.index('Y')
print(f)

#2.20
s = 'top'
reverse_s = s[::-1]
print(reverse_s)

#2.21
s = 'Louis'
t = 'Peter'
print(s[0]+t[0])

#2.22
lst = [3,7,-2,12]
range_lst = max(lst)-min(lst)
print(range_lst)

#2.23
monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')

#a
monthsL.insert(-1,'April')
print(monthsL)
monthsT_lst = list(monthsT)
monthsT_lst.insert(-1,'April')
print(tuple(monthsT_lst))

#b
monthsL.append('June')
print(monthsL)
monthsT_lst.append('June')
print(tuple(monthsT_lst))

#c
monthsL.pop()
print(monthsL)
monthsT_lst.pop()
print(tuple(monthsT_lst))

#d
monthsL.pop(1)
print(monthsL)
monthsT_lst.pop(1)
print(tuple(monthsT_lst))

#e
monthsL = monthsL[::-1]
print(monthsL)
monthsT_lst  =monthsT_lst[::-1]
print(tuple(monthsT_lst))

#f
monthsL.sort()
print(monthsL)
monthsT_lst.sort()
print(tuple(monthsT_lst))

#2.24
grades = ['B','B','F','C','B','A','A','D','C','D','A','A','B']
count = [grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('F')]
print(count)

#2.25
grades = ('B','B','F','C','B','A','A','D','C','D','A','A','B')
grades_lst = list(grades)
count = [grades_lst.count('A'),grades_lst.count('B'),grades_lst.count('C'),grades_lst.count('D'),grades_lst.count('F')]
print(count)

#2.26
import math
radius=10
#a
x,y=0,0
a= math.sqrt((x-0)**2)+((y-0)**2)
if a<radius:
    print('True')
else:
    print('False')

#b
x,y=10,10
a= math.sqrt((x-0)**2)+((y-0)**2)
if a<radius:
    print('True')
else:
    print('False')

#c
x,y=6,-6
a= math.sqrt((x-0)**2)+((y-0)**2)
if a<radius:
    print('True')
else:
    print('False')

#d
x,y=-7,8
a= math.sqrt((x-0)**2)+((y-0)**2)
if a<radius:
    print('True')
else:
    print('False')


#2.27
def radian(angle):
    radian = (3.14*angle)/180
    return radian
def height(length,angle):
    height = length*math.sin(angle)
    return height

#a
length = 16
angle = 75
print(height(length,radian(angle)))



#b
length = 20
angle = 0
print(height(length,radian(angle)))

#c
length = 24
angle = 45
print(height(length,radian(angle)))

#d
length = 24
angle = 80
print(height(length,radian(angle)))

#2.28
#a
list = [1,2,3,4,5,6]
idx = len(list)//2
print(idx)

#b
middle_element = list[len(list)//2]
print(middle_element)

#c
list.reverse()
print(list)

#d
list.append(list.pop(0))
print(list)
