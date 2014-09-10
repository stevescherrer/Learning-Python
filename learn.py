print "Hello World!"
print "My name is TRAINWRECK"

##List Accessing
n = [1, 3, 5] #defines list n

# Add your code below
print n[1] #python indexing begins at zero. this prints second element of list n, in this case 3

##Slicing Lists and strings
animals="catdogfrog"
cat=animals[:3] #animals from begining to but not including 4
dog=animals[3:6] #animals from but not including 3 to but not including 6
frog=animals[6:] #animals from but not including 6 to end

##Maintaining Order
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"
animals=animals.insert(duck_index, "cobra") #inserts cobra

##For loops
#squaring the number
my_list = [1,9,3,8,5,7]

for number in my_list:
    print 2*number

#appending to lists, sorting lists
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number**2)
square_list.sort()
print square_list


##Key Value pairs
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106} #dictionary structure, puffin is key 104 is value. together they are a pair

print residents['Puffin'] # Prints Puffin's room number

#adding to dictionary lists
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!

menu['cream']=2
menu['cheese']=5
menu['noodle goodness']=1000


print "There are " + str(len(menu)) + " items on the menu."
print menu

#removing from dictionary lists
# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

#changing a value of a key value pair
zoo_animals['Rockhopper Penguin']='anything other than arctic exhibit'

#more complex dictionaries
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket']=['seashell','strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']=inventory['gold']+50
print zoo_animals

#dictionaries with strings
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
        "Baa" : "The sound a goat makes.",
        "Carpet": "Goes on the floor.",
        "Dab": "A small amount."
}

#looping through dictionaries
for word in webster:
    print webster[word]

#control flow and looping
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#control with intergers
for b in a:
    if b%2==0:
        print b

#control with strings
def fizz_count(x):
    count=0
    for item in x:
        if item=="fizz":
            count=count+1
    return count

#string looping
for letter in "Codecademy":
    print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter


##Grocery Store Example

prices = {
    "banana" : 4,
    "apple" : 2,
    "orange": 1.5,
    "pear" : 3
}

stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
}

#looping through two dictionaries with one index
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

total=0
for i in prices:
    a= prices[i]*stock[i]
    print a
    total=total+a
print total

#This is a list
shopping_list=["banana", "orange", "apple"]
groceries=shopping_list

"""this is a structure""" #note, 3" also same as #
stock={"banana":6,
    "apple":0,
    "orange":32,
    "pear":15
}

# Write your code below!

food="banana"

def compute_bill(food): #defines funciton compute_bill and feeds it variable food
    total = 0 #starts counter
    for item in food: #for loop assigns item to each iterative value of food
        if stock[item]>0: #looks in stock dictionary for str value matching item, checks that value > 0
            total += prices[item] #gets item price from prices dictionary by matching string
            stock[item] -= 1 #subtracts one from stock of that item
    return total #returns total after loop completes

##Student becomes the teacher excercise

lloyd = {  ##Creates dicitonary lloyd
    "name": "Lloyd", ##assigns Lloyd to name key
    "homework": [], ##leaves homework key unassigned (blank)
    "quizzes": [],
    "tests": [],
}

lloyd = {  ##adjusting lloyd dictionary
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = { #defining additional dictionarys
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students=[lloyd, alice, tyler]

for student in students: #calling list of all students and assignment totals
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]


#When you divide an integer by another integer, the result is always an integer (rounded down, if needed).
#When you divide a float by an integer, the result is always a float. float is a decimal number
#To divide two integers and end up with a float, you must first use float() to convert one of the integers to a float.

def average(numbers): #creates function average with one variable "numbers"
    total=sum(numbers) #sums numbers
    total=float(total) #converts integer to float
    total=total/len(numbers) #divides total by length of numbers (to average things)
    return total #returns total

#The \ character is a continuation character. The following line is considered a continuation of the current line.

def get_average(student):
    homework=average(student["homework"])
    quizzes=average(student["quizzes"])
    tests=average(student["tests"])
    return homework*.10+quizzes*.30+tests*.60


def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

def get_class_average(students): #function
    results=[] #empty list
    for student in students: #for loop
        results.append(get_average(student)) #appends student averages sequentially to list
    print average(results)
    print get_letter_grade(average(results))
    return average(results) #returns the results of running average function with data from results

##List Element Modification
n = [1, 3, 5]
# Do your multiplication here
n[1]=n[1]*5 #overwrites the second element of n with the result of the second element of n multiplied by five
print n

n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print n
# Remove the first item in the list here
del n[0]
print n


##Functions
number = 5

def my_function(x):
    return x * 3

print my_function(number)

#functions with multiple input parameters
m = 5
n = 13
# Add add_function here!
def add_function(m,n):
    return m+n


print add_function(m, n)

## Helloworld
n = "Hello"
# Your function here!
def string_function(n):
    m="world"
    return n+m


print string_function(n)

#passing a list to a function
def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)

#returning only first index
def list_function(x):
    return x[1]

n = [3, 5, 7]

print list_function(n)

#modifying a list wiht a function
def list_function(x):
    x[1]=x[1]+3
    return x

n = [3, 5, 7]

print list_function(n)

#appending lists
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst

print list_extender(n)

#printing a list item by item
n = [3, 5, 7]

for i in range(0, len(n)):
    print n[i]

n = [3, 5, 7]

#nesting for loops in a function
def print_list(x):
    for i in range(0, len(x)):
        x[i]=x[i]*2
        print x[i]
    return x

print print_list(n)

##Range Command
#The range function has three different versions:

#range(stop)
#range(start, stop)
#range(start, stop, step)
#In all cases, the range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.

#If omitted, start defaults to zero and step defaults to one

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0,3))

#Iterating over a list function
n = [3, 5, 7]

def total(numbers):
    result=0
    for i in range(len(numbers)):
        result+=numbers[i]
    return result

##using strings in lists in functions
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result=""
    for i in range(len(words)):
        result+=words[i]
    return result


print join_strings(n)

#Joining lists by concatenating
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
    return x+y

print join_lists(m, n)


#Using a list of lists as a function

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(lists):
    results=[]
    for numbers in lists:
        for lst in numbers:
            print lst
            results+=lists[numbers[lst]]
    return results


##Battle Ship##
board=[]
for loop in range(0,5):
    a=["O"]*5
    board.append(a)
board=[]


for loop in range(0,5):
    a=["O"]*5
    board.append(a)

#join command
def print_board(board):
    for row in board:
        print " ".join(row) #removes commas from list
    return board

print_board(board)

#importing command functions from a module
from random import randint #imports randint function from random module

#defining random variables (columns and rows)
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

##For Debugging
#print ship_row
#print ship_col

for turn in range(4):
    print "Turn" , turn+1

##Waiting for user input and forcing input as an interger
#raw_input prompts user for raw input. user input is a string by default. use int() function to force interger
    guess_row = int(raw_input("Guess Row:")) #creates a new variable called guess row and assigns input to be an interger

    guess_col = int(raw_input("Guess Col:"))

    if guess_row==ship_row and guess_col==ship_col:
        print "Congratulations! You sank my battleship!"
        break
    else:
        if guess_col not in range(5) or guess_row not in range(5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col]=="X": #else if
            print "You guessed that one already."

        else:
            print "You missed my battleship!"
            board[guess_row][guess_col]="X" ##To specify a single element in a 2-dimensional list, you need to give two indices. The syntax is: list_name[i][j], where i is an element in the outer list and j is an element in the inner list.
    if turn==3:
        print "Game Over"
    else:
        print print_board(board)


####While Statements
#The while loop is similar to an if statement: it executes the code inside of it if some condition is true. The difference is that the while loop will continue to execute as long as the condition is true. In other words, instead of executing if something is true, it executes while that thing is true.
count = 0

if count < 10:
    print "Hello, I am an if statement and count is", count

while count < 10:
    print "Hello, I am a while and count is", count
    count += 1

num = 1

while num<101:  # Fill in the condition
    # Print num squared
    # Increment num (make sure to do this!)
    print num**2
    num+=1

#use while to validate input data
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

#While/Else
#Something completely different about Python is the while/else construction. while/else is similar to if/else, but there is a difference: the else block will execute anytime the loop condition is evaluated to False. This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be executed.
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

#for looping
print "Counting..."

for i in range(20):
    print i


##More than one way to skin a cat... The following works both ways.
hobbies = []
# Add your code below!

for counter in range(3):
    hobbies.append(raw_input("What are some of your hobbies?"))
#or

hobbies=[]
counter=0
while counter<3:
    counter+=1
    hobbies.append(raw_input("What are some of your hobbies?"))

#for loops with strings
thing = "spam!"

for c in thing:
    print c

#The , character after our print statement means that our next print statement keeps printing on the same line.
word = "eggs!"

# Your code here!
for w in word:
    print w,

phrase = "A bird in the hand..."

# Add your for loop

for char in phrase:
    if char=='A' or char=='a':
        print 'X',
    else:
        print char,

#Don't delete this print statement!
print

##Looping over a dictionary you get the key which you can use to get the value.
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key + " " + d[key]

##Enumerate: enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item #We don't want the user to see things listed from index 0, since this looks unnatural. Instead, the items should appear to start at index 1


##Zip: zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list. Zip can handle three or more lists as well!

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a>b:
        print a
    elif b>a:
        print b
    else:
        print a+"and"+b + "are the same number!"


#another way to do things again
def digit_sum(n):
    a=str(n)
    count=0
    for x in a:
        x=int(x)
        count+=x
    return count

#or to get the rightmost digit of a number, you can modulo (%) the number by 10. To remove the rightmost digit you can floor divide (//) the number by 10

def is_prime(x):
    if x<=1:
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i==0:
                return False
                break
        else:
            return True


#returning a string in reverse
def reverse(text): #inputs string
    word="" #creates new empty string
    for i in range(len(text)): #i iterates from 0 to length of text -1
        word+=text[(len(text)-i-1)] #word adds the letter from the length of the word minus what iteration it is on minus 1 to account for offset indicies
    return word

#removing specific bits of a string
def anti_vowel(text):
    new_word=""
    for letter in range(0,len(text)):
        if text[letter] not in "a,e,i,o,u,A,E,I,O,U":
            new_word+=text[letter]
    return new_word

#scrabble score=summing dictionary elements pulled by key in a for loop
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10}

def scrabble_score(word):
    tally=0
    word=word.lower() ##makes lower case
    for letter in word:
        tally+=score[letter]
    return tally

##Changing specific words from a string
def censor(text, word): #where text is the string and word is the word you are changing
    split_words=text.split()
    for index in range(len(split_words)):
        if split_words[index]==word:
            split_words[index]=len(split_words[index])*'*'
        print split_words
    return " ".join(split_words)

#matching a str in a sequence
def count(sequence, item):
    count=0
    str_item=str(item)
    for i in sequence:
        str_i=str(i)
        if str_i==str_item:
            count+=1
    return count

#filtering a list of intergers
def purify(x):
    new_list=[]
    for index in range(0,len(x)):
        if x[index]%2==0:
            new_list.append(x[index])
    return new_list

def product(interger_list):
    prod_out=intergers[0]
    for i in range(1, len(interger_list)):
        prod_out*=interger_list[i]
    return prod_out

def remove_duplicates(x):
    new_list=[]
    for i in range(0,len(x)):
        if x[i] not in new_list:
            new_list.append(x[i])
    return new_list


def median(x):
    y=sorted(x)
    if len(y)%2==0:
        return (y[(len(y)/2)-1] + y[len(y)/2])/2.0 #note that (2 + 3) / 2 is not the same as (2 + 3) / 2.0! The former is integer division, meaning Python will try to give you an integer back. You'll want a float, so something like (2 + 3) / 2.0 is the way to go.
    else:
        return y[len(y)/2]

##Basic statistics
print "Let's compute some stats!"
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average=grades_average(scores)
    variance=0
    for score in scores:
        variance+=(average-score)**2
    return variance/float(len(scores))

print grades_variance(grades)

def grades_std_deviation(variance):
    return variance**0.5

variance=grades_variance(grades)

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)


my_dict={
    "key one":"value pair 1",
    "key two":"value pair 2",
}

print my_dict.keys()
print my_dict.values()
#Note that the items() function doesn't return key/value pairs in any specific order.You can think of dictionaries as unordered key/value pairs.

#Whereas items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary:

#The keys() function returns an array of the dictionary's keys, and
#The values() function returns an array of the dictionary's values.
#Again, these functions will not return the keys or values from the dictionary in any specific order.

#You can think of a tuple as an immutable (that is, unchangeable) list (though this is an oversimplification); tuples are surrounded by ()s and can contain any data type.

#For iterating over lists, tuples, dictionaries, and strings, Python also includes a special keyword: in

for number in my_dict:
    print number,
    print my_dict[number]


#List comprehensions are a powerful way to generate lists using the for/in and if keywords.
#list comprehension syntax
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [i**2 for i in range(1,12) if i%2==0]

print even_squares

cubes_by_four = [x**3 for x in range(1,11) if x**3%4==0] #numbers 1-10 if their cube is evenly divisible by 4

print cubes_by_four

#list slicing syntax
#List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:
    #[start:end:stride]
#Where start describes where the slice starts (inclusive), end is where it ends (exclusive), and stride describes the space between items in the sliced list. For example, a stride of 2 would select every other item from the original list to place in the sliced list.

#Omitting Indices
#If you don't pass a particular index to the list slice, Python will pick a default.

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E']

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']

my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2]

#A negative stride progresses through the list from right to left. AKA reverse stride count backwards stride
my_list = range(1, 11)

backwards=my_list[::-1]
print backwards

#A positive stride length traverses the list from left to right, and a negative one traverses the list from right to left. Further, a stride length of 1 traverses the list "by ones," a stride length of 2 traverses the list "by twos," and so on.

to_one_hundred = range(101)

backwards_by_tens=to_one_hundred[::-10]
print backwards_by_tens

to_21=range(1,22)
odds=to_21[::2]
middle_third=to_21[7:14]

#One of the more powerful aspects of Python is that it allows for a style of programming called functional programming, which means that you're allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

#See the lambda bit? Typing
lambda x: x % 3 == 0
#Is the same as
def by_three(x):
    return x % 3 == 0

#Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an anonymous function.

#When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.

#Lambda functions are defined using the following syntax:

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)
#Lambdas are useful when you need a quick function to do some work for you.

#If you plan on creating a function you'll use over and over, you're better off using def and giving that function a name.
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x=="Python", languages)


squares=[x**2 for x in range(1,11)]#creates a list of the square of a list of numbers between 1 and 10

print filter(lambda i: i>=30 and i<70, squares)#prints only squares between 30 and 70

#Iterating Over Dictionaries

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print movies.items()

#Comprehending Comprehensions
threes_and_fives = [i for i in range(1, 16) if i%3==0 or i%5==0]

#List Slicing
#You can think of a Python string as a list of characters.
str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
str[start:end:stride]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message=garbled[::-2]

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message=filter(lambda x: x != 'X', garbled)
print message

#Bitwise operations are operations that directly manipulate bits. In all computers, numbers are represented with bits, a series of zeros and ones. In fact, pretty much everything in a computer is represented by bits. This course will introduce you to the basic bitwise operations and then show you what you can do with them.

print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

#In binary we count in base two, where each place can hold one of two values: 0 or 1. The counting pattern is the same as in base 10 except when you carry over to a new column, you have to carry over every time a place goes higher than one (as opposed to higher than 9 in base 10).

#For example, the numbers one and zero are the same in base 10 and base 2. But in base 2, once you get to the number 2 you have to carry over the one, resulting in the representation "10". Adding one again results in "11" (3) and adding one again results in "100" (4).

#Contrary to counting in base 10, where each decimal place represents a power of 10, each place in a binary number represents a power of two (or a bit). The rightmost bit is the 1's bit (two to the zero power), the next bit is the 2's bit (two to the first), then 4, 8, 16, 32, and so on.

#The binary number '1010' is 10 in base 2 because the 8's bit and the 2's bit are "on":

8's bit  4's bit  2's bit  1's bit
    1       0       1      0
    8   +   0    +  2   +  0  = 10
#In Python, you can write numbers in binary format by starting the number with 0b. When doing so, the numbers can be operated on like any other number!
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11 #4
print 0b11 * 0b11 #9

#Here are a few numbers that will be good to know going forward -

2**0 = 1
2**1 = 2
2**2 = 4
2**3 = 8
2**4 = 16
2**5 = 32
2**6 = 64
2**7 = 128
2**8 = 256
2**9 = 512
2**10 = 1024

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

#The bin() Function
#There are Python functions that can aid you with bitwise operations. In order to print a number in its binary representation, you can use the bin() function. bin() takes an integer as input and returns the binary representation of that integer in a string. (Keep in mind that after using the bin function, you can no longer operate on the value like a number.)

#You can also represent numbers in base 8 and base 16 using the oct() and hex() functions. (We won't be dealing with those here, however.)

i=range(0,6)
for s in i:
    print bin(i[s]) #prints bit numbers for all numbers range 0-5

#the int() function can turn non-integer input into an integer.What you might not know is that the int function actually has an optional second parameter.

int("110", 2) # ==> 6

#When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)

#the left and right shift bitwise operators. These operators work by shifting the bits of a number over by a designated number of slots.

#The block below shows how these operators work on the bit level. Note that in the diagram, the shift is always a positive integer:

# Left Bit Shift (<<)
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right=shift_right>>2
shift_left=shift_left<<2
print bin(shift_right) #prints 0b11
print bin(shift_left) #prints 0B100

#The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1. For example:
    
    a=       00101010   #42
    b=       00001111   #15
    #===================
    a & b=   00001010  # 10

#for every given bit in a and b:

#0 & 0 = 0
#0 & 1 = 0
#1 & 0 = 0
#1 & 1 = 1

#Therefore, 0b111 (7) & 0b1010 (10) = 0b10 which equals two.

#The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1

#Note that the bitwise | operator can only create results that are greater than or equal to the larger of the two integer inputs.

#So remember, for every given bit in a and b:

0 | 0 == 0
0 | 1 == 1
1 | 0 == 1
1 | 1 == 1

#Meaning
    
#110 (6) | 1010 (10) = 1110 (14)

print bin(0b1110 | 0b101)

#The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.

a=  00101010   #42
b=  00001111   #15
#================
a ^ b:  00100101   #37

print bin(0b1110^0b101) #returns 0b1011

#The bitwise NOT operator (~) just flips all of the bits in a single number. What this actually means to the computer is actually very complicated, so we're not going to get into it. Just know that mathematically, this is equivalent to adding one to the number and then making it negative.
print ~1 #-2
print ~2 #-3
print ~3 #-4
print ~42 #-43
print ~123 #-124

#A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "Bit was on"
#In the example above, we want to see if the third bit from the right is on.

#First, we first create a variable num containing the number 12, or 0b1100.
#Next, we create a mask with the third bit on.
#Then, we use a bitwise-and operation to see if the third bit from the right of num is on.
#If desired is greater than zero, then the third bit of num must have been one.

def check_bit4(b):
    check=0b1000
    if check & b>0:
        return "on"
    else:
        return "off"

#You can also use masks to turn a bit in a number on using |. For example, let's say I want to make sure the rightmost bit of number a is turned on. I could do this:

a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

#Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.
a = 0b10111011
mask=0b100
print bin(a | mask) #prints 0b10111111

#Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.

#For example, let's say I want to flip all of the bits in a. I might do this:
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

a = 0b11101110 #=2+4+8+32+64+128
mask=0b11111111 #1+2+4+8+16+32+64+128
desired=bin(a ^ mask)
print desired #prints 0b10001 #1+16

#Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.
a = 0b101
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten
desired = a ^ mask

#Let's say that I want to turn on the 10th bit from the right of the integer a.

#Instead of writing out the entire number, we slide a bit over using the << operator.

#We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.

def flip_bit(number,n):
    mask=0b1<<(n-1)
    result=number^mask
    return bin(result)


