#3.17
#a
a = eval('2*3+1')
print(a)

#b
b = eval("'hello'")
print(b)

#c
c = eval("'hello'+' ' + 'world!'")
print(c)

#d
d = eval("'ASCII'.count('I')")
print(d)

#e
e = eval("'x = 5'")
print(e)

#3.18
a,b,c = 3,4,5

#a
if a < b:
    print('OK')
#b
if c < b:
    print('OK')
#c
if a+b==c:
    print('OK')

#d
if (a**2) + (b**2) == c**2:
    print('OK')

#3.19
#a
if a < b:
    print('OK')
else:
    print('NOT OK')
#b
if c < b:
    print('OK')
else:
    print('NOT OK')
#c
if a+b==c:
    print('OK')
else:
    print('NOT OK')

#d
if (a**2) + (b**2) == c**2:
    print('OK')
else:
    print('NOT OK')

#3.20
lst = ['January', 'February', 'March']
for i in lst:
    print(i[:3])

#3.21
lst = [2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    if i%2==0:
        print(i, end=' ')

#3.22
lst =  [2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    if i**2%8==0:
        print(i)

#3.23
#a
for i in range(2):
    print(i, end=' ')

#b
for i in range(1):
    print(i, end=' ')
        
#c
for i in range(3,7):
    print(i, end=' ')

#d
for i in range(1,2):
    print(i)

#e
for i in range(0,4):
    if i%3==0:
        print(i, end=' ')

# #f
# for i in range(4,22):
#     i = i+4
#     print(i)

#3.24
# words = eval(input())
# for i in words:
#     if i!='secret':
#         print(i)

# #3.25
# student_names = eval(input())
# for i in student_names:
#     if i[0]<'M':
#         print(i)

#3.26
# nonempty_list =  eval(input())
# print('The first list element is', nonempty_list[0])
# print('The last list element is', nonempty_list[-1])

#3.27
n = 5
for i in range(n):
    i = i*n
    print(i)

#3.28
n =3
for i in range(n):
    i = i**2 
    print(i)

#3.29
n = 49
for i in range(1,n+1):
    if n%i==0:
        print(i)

#3.30
first_number = 4.5
second_number = 3
third_number = 3
fourth_number = 3.5
average = (first_number+second_number+third_number)/3
if average==fourth_number:
    print('Equal')
else:
    print('Not Equal')

#3.31
#3.32
n = int(input("Enter a positive four-digit integer: "))
print('{}\n{}\n{}\n{}'.format(n//n,n//n+1,n//n+2,n//n+3))
#3.33
def reverse_string(string):
    print(string[::-1])
reverse_string(str(input("Enter a three-letter string: ")))        

#3.34
def pay(wage,hours):
    employee_pay = wage*hours
    if hours>40:
        employee_pay = (wage*hours)+25
    return employee_pay

print(pay(int(input("Enter hourly wage: ")),int(input("Enter no. of hours: "))))

#3.35
def prob(n):
    probability = 2**-n
    return probability

print(prob(int(input("Enter a nonegative integer: "))))

#3.36

def reverse_int(n):
    revs_number = 0
    while (n>0):
        remainder = n%10
        print(remainder)
        revs_number = (revs_number*10)+remainder
        print(revs_number)
        n = n//10
        print(n)
    return revs_number

print(reverse_int(int(input("Enter a 3 digit integer: "))))

#3.37
import math
def points(x1,y1,x2,y2):
    slope = (y2-y1)/(x2-x1)
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return slope, distance
x1 = int(input("Enter x1 coordinate: "))
y1 = int(input("Enter y1 coordinate: "))
x2 = int(input("Enter x2 coordinate: "))
y2 = int(input("Enter y2 coordinate: "))
print(points(x1,y1,x2,y2))

#3.38
def abbreviation(day):
    return day[:2]

print(abbreviation(str(input('Enter the day of the week: '))))

#3.39
def collision(x1,y1,r1,x2,y2,r2):
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    if distance**2 < (r1+r2)**2:
        return True
    else:
        return False
x1 = int(input("Enter the coordinates x1: "))
x2 = int(input("Enter the coordinates x2: "))
y1 = int(input("Enter the coordinates y1: "))
y2 = int(input("Enter the coordinates y2: "))
r1 = int(input("Enter the radius r1: "))
r2 = int(input("Enter the radius r2: "))
print(collision(x1,y1,r1,x2,y2,r2))

#3.40
def partition(soccer_players):
    for i in soccer_players:
        if i[0] >= 'A' and i[0] <= 'M':
            print(i)

print(partition(list(input("Enter a list of first names(as strings) of soccer players: "))))

#3.41
def lastF(FirstName, Lastname):
    print("'{}, {}.'".format(Lastname,FirstName[0]))

FirstName = str(input('Enter the first name: '))
LastName = str(input('Enter the last name: '))
print(lastF(FirstName, LastName))    


#3.42
def avg(grades):
    avg1 = sum(grades[0])/len(grades[0])
    avg2 = sum(grades[1])/len(grades[1])
    avg3 = sum(grades[2])/len(grades[2])
    avg4 = sum(grades[3])/len(grades[3])
    print('{}\n{}\n{}\n{}'.format(avg1,avg2,avg3,avg4))

grades = list(input(list('Enter first student marks comma separated:'),list('Enter second student marks comma separated:'),list('Enter third student marks comma separated:'),list('Enter fourth student marks comma separated:')))
avg(grades)


#3.43
def hit(x1,y1,x2,y2,r):
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    if distance <= (r):
        return True
    else:
        return False
print(hit(0, 0, 3, 4, 0))

#3.44




