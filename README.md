Sanski Language Docs 📜
Welcome to the official documentation for Sanski, a simple, scriptable programming language with keywords inspired by Hindi and Sanskrit. This guide will walk you through everything from the basics to advanced features like Object-Oriented Programming.

🚀 Getting Started
Sanski code is interpreted by a Python script. To run your Sanski programs, you 'll need Python 3 installed.

File Naming
Sanski files should use the .sns extension (e.g., my_program.sns).

Execution
To execute a Sanski file, run the interpreter from your terminal and pass the filename as an argument:

python sanski_interpreter.py your_file_name.sns


Your First Program
Create a file named pratham.sns and add the following line:

# This is a comment in Sanski
vad("Namaste, Sansar!") # Prints "Namaste, Sansar!" to the console


Run it using the command above, and you should see the greeting printed to your screen.

Core Concepts
Let's dive into the fundamental building blocks of the Sanski language.

Variables & Data Types
Variables are containers for storing data. In Sanski, you create variables using the rachay keyword. Sanski supports several standard data types.

Syntax: rachay <variable_name> = <value>

Numbers: Integers and floating-point numbers.

rachay sankhya = 10
rachay mulya = 99.5


Strings: Text enclosed in double (") or single (') quotes.

rachay naam = "Sanski"


Lists: Ordered collections of items, similar to arrays.

rachay soochi = [1, "do", True, 3.14]


Dictionaries: Key-value pairs.

rachay shabdkosh = {'key': 'value', 'naam': 'Aditya'}


Note: Sanski uses Python's underlying evaluation engine, so it supports most standard Python expressions for data types and operators (+, -, *, /, ==, and, or, etc.).

Control Flow: Loops
To repeat actions, Sanski provides a for-in loop structure using the har_ek keyword.

Syntax: har_ek <item_variable> mein <list_variable>:

The loop iterates over each item in a list or other iterable.

rachay phal = ["Seb", "Kela", "Santra"]

har_ek p mein phal:
    vad(p)

# Output:
# Seb
# Kela
# Santra


You can control the loop's execution with roko (break) and jaari_rakho (continue).

roko: Immediately exits the loop.

jaari_rakho: Skips the rest of the current iteration and proceeds to the next one.

Functions
Functions are reusable blocks of code. Define them using the karya keyword.

Syntax: karya <function_name>(<param1>, <param2>, ...):

Return Values: Use the vapasi keyword to return a value from a function.

# Function definition
karya jodo(a, b):
    vad("Sankhyaon ko jodna...")
    vapasi a + b

# Function call
rachay parinaam = jodo(5, 3)
vad(parinaam) # Prints 8


Object-Oriented Programming (OOP) 🏛️
Sanski has a powerful OOP system that includes classes, objects, and inheritance.

Classes
A class is a blueprint for creating objects. Define a class using the varg keyword.

Syntax: varg <ClassName>:

Constructor & Properties
The constructor is a special method called when an object is created. It's used to initialize object properties.

Keyword: rachna (replaces __init__ in Python).

Instance Reference: The first parameter of any method, including the constructor, must be svayam. This is Sanski's equivalent of self or this.

varg Vahan:
    # Constructor
    rachna(svayam, naam, rang):
        rachay svayam.naam = naam
        rachay svayam.rang = rang

    # Method
    karya vivaran_do(svayam):
        vad("Yeh ek " + svayam.naam + " hai jiska rang " + svayam.rang + " hai.")

# Create an instance (object) of the Vahan class
rachay meri_car = Vahan("Car", "Neela")

# Call a method on the object
meri_car.vivaran_do() # Output: Yeh ek Car hai jiska rang Neela hai.

# Access a property
vad(meri_car.rang) # Output: Neela


Inheritance
Inheritance allows a class (child) to inherit properties and methods from another class (parent).

Syntax: varg <ChildClass>(<ParentClass>):

When a child class is instantiated:

The parent class's constructor (rachna) is automatically called first.

The child class's constructor is called next.

Methods from the parent are available to the child object. If the child defines a method with the same name, it overrides the parent's method.

Example:

# Parent Class
varg Prani:
    rachna(svayam):
        rachay svayam.jeevit_hai = True
        vad("Prani rachna ki gayi.")

    karya saans_lo(svayam):
        vad("Saans le raha hai...")

# Child Class inheriting from Prani
varg Kutte(Prani):
    rachna(svayam, naam):
        rachay svayam.naam = naam
        vad("Kutte ki rachna ki gayi.")

    karya bhonko(svayam):
        vad("Bhow Bhow!")

# Create an instance of the child class
rachay mera_kutta = Kutte("Buddy")

# Parent constructor was called, then child's
# Output:
# Prani rachna ki gayi.
# Kutte ki rachna ki gayi.

# Call inherited method
mera_kutta.saans_lo() # Output: Saans le raha hai...

# Call child's own method
mera_kutta.bhonko() # Output: Bhow Bhow!


Modules & Built-ins
Importing Modules
You can split your code into multiple files and import them using the aayat keyword. This helps organize large projects.

Syntax: aayat "<filename>.sns"

Imagine you have helpers.sns:

# helpers.sns
karya alvida_kaho():
    vad("Alvida!")


You can use it in main.sns:

# main.sns
aayat "helpers.sns"

vad("Namaste!")
alvida_kaho()

# Output:
# Namaste!
# Alvida!


Important: The path in aayat is relative to the file you are running.

Built-in Functions Reference 📚
Sanski comes with a set of useful built-in functions.

Function

Description

Example

vad(expr)

Prints the evaluated expression to the console.

vad("Hello" + " " + "World")

grahan_karo(prompt)

Reads a line of input from the user.

rachay naam = grahan_karo("Aapka naam kya hai? ")

lambai(data)

Returns the length of a string, list, or dictionary.

rachay l = lambai([1,2,3])

jodo(list, item)

Appends an item to a list.

rachay s = [1]; jodo(s, 2)

string_upper(text)

Converts a string to uppercase.

string_upper("hello")

string_lower(text)

Converts a string to lowercase.

string_lower("HELLO")

string_replace(t,o,n)

Replaces a substring with another.

string_replace("hi", "i", "ello")

string_split(t,sep)

Splits a string by a separator.

string_split("a,b,c", ",")

string_strip(text)

Removes leading/trailing whitespace.

string_strip("  hi  ")

File I/O
Function

Description

file_kholo(name, mode)

Opens a file and returns a file object.

file_padho(file_obj)

Reads the entire content of the file.

file_likho(file_obj, data)

Writes data to the file.

file_band_karo(file_obj)

Closes the file.

Math Library
All functions from Python's math library are available directly.

vad(pi)      # 3.14159...
vad(sqrt(16)) # 4.0


Current Features & What's Next 🚀
Sanski is an evolving language. Our goal is to make it simple yet powerful. Here's a look at what's working today and what we're building for the future.

What Works Today
The core features of Sanski are stable and ready to use. This includes the full Object-Oriented system with classes and inheritance, functions, loops (har_ek), and the module import system (aayat). You can build complex, multi-file applications right now.

Coming Soon
We are actively working on expanding Sanski's capabilities. Here are the top features on our roadmap:

Conditional Logic: The ability to make decisions is crucial. We are planning to introduce yadi (if) and anyatha (else) to control which code runs based on conditions.

While Loops: To complement the har_ek loop, we will be adding a jab_tak (while) loop for situations where you need to repeat a block of code as long as a condition is true.

Improved Error Handling: We are working on making error messages more descriptive, including line numbers and clearer explanations, to make debugging your programs much easier.

Stay tuned for more updates as we continue to grow the Sanski language!
