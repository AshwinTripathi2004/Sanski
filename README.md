📜 Sanski Language Docs
Welcome to the official guide for Sanski, an elegant scripting language inspired by Sanskrit and Hindi, foundational pillars of India's linguistic heritage. By drawing from these modern languages, Sanski offers an intuitive coding experience for both new and experienced programmers.

✨ Language Philosophy
Sanski was created with a simple idea: programming should feel natural. By using words that are familiar to hundreds of millions of people, we lower the barrier to entry and make the logic of the code shine through. Our goal is to provide a language that is not only functional and powerful but also a joy to read and write.

🚀 Getting Started
Getting your first Sanski program running is easy. All you need is Python 3 installed on your system.

Step 1: Create Your File
Sanski files use the .sns extension. Create a new file named pratham.sns.

Step 2: Write Your Code
Open pratham.sns in your favorite editor and add this line:

# This is your first Sanski program!
vad("Namaste, Sansar!") # Prints "Hello, World!" to the console

Step 3: Run from Terminal
Navigate to your project folder in your terminal and execute your script:

python sanski_interpreter.py pratham.sns

You should see Namaste, Sansar! printed on your screen. You're officially a Sanski programmer!

🧠 Core Concepts
Here are the fundamental building blocks of the Sanski language.

Variables & Data Types
Variables are used to store information. In Sanski, you declare them with the rachay (create) keyword.

Syntax: rachay <variable_name> = <value>

Sanski supports all standard data types:

# Numbers (Integers and Floats)
rachay sankhya = 10
rachay mulya = 99.5

# Strings (Text)
rachay naam = "Sanski"

# Lists (Ordered, mutable collections)
rachay soochi = [1, "do", True]

# Dictionaries (Key-value pairs)
rachay shabdkosh = {'key': 'value', 'naam': 'Aditya'}

Loops
To perform repetitive tasks, Sanski uses the har_ek (for each) loop, which is perfect for iterating over lists.

Syntax: har_ek <item> mein <list>:

rachay phal = ["Seb", "Kela", "Santra"]

har_ek p mein phal:
    # This block runs for each item in the list
    vad("Current fruit: " + p)

You can control your loops with these keywords:

roko: Immediately breaks out of the loop.

jaari_rakho: Skips the current iteration and moves to the next.

Functions
Functions are reusable blocks of code. Define them with the karya (function) keyword and return values with vapasi (return).

Syntax: karya <function_name>(<parameters>):

# Defines a function that adds two numbers
karya jodo(a, b):
    vapasi a + b

# Calls the function and stores the result
rachay parinaam = jodo(5, 3)
vad(parinaam) # Output: 8

🏛️ Object-Oriented Programming (OOP)
Sanski provides a full suite of OOP features, allowing you to build robust and scalable applications.

Classes & Constructors
A class is a blueprint for creating objects. Use the varg (class) keyword to define one. The rachna (constructor) method is called when a new object is created.

Instance Reference: The first parameter of any method must be svayam (self).

varg Vahan:
    # The constructor initializes the object's properties
    rachna(svayam, naam, rang):
        rachay svayam.naam = naam
        rachay svayam.rang = rang

    # A regular method that belongs to the class
    karya vivaran_do(svayam):
        vad("This is a " + svayam.rang + " " + svayam.naam)

# Create a new object (instance) from the Vahan class
rachay meri_car = Vahan("Car", "Neela")

# Call a method on the object
meri_car.vivaran_do() # Output: This is a Neela Car

Inheritance
Inheritance allows a class to inherit all the methods and properties from another class.

Syntax: varg <ChildClass>(<ParentClass>):

# Parent Class
varg Prani:
    rachna(svayam):
        vad("A new Prani (Animal) is born.")

    karya saans_lo(svayam):
        vad("Breathing...")

# Child Class inherits from Prani
varg Kutte(Prani):
    rachna(svayam, naam):
        # The parent constructor is called automatically first!
        rachay svayam.naam = naam
        vad("It's a Kutte (Dog) named " + svayam.naam)

# Create an instance of the child class
rachay mera_kutta = Kutte("Buddy")

# The output shows both constructors were called:
# > A new Prani (Animal) is born.
# > It's a Kutte (Dog) named Buddy

# Call the inherited method from the Prani class
mera_kutta.saans_lo() # Output: Breathing...

📚 Modules & Built-ins
Importing Modules
Organize your project by splitting code into multiple files. Use aayat (import) to use code from another file.

Syntax: aayat "<filename>.sns"

For example, if you have helpers.sns with a function, you can use it in main.sns:

# In main.sns
aayat "helpers.sns"

# Now you can use any function defined in helpers.sns
alvida_kaho()

Built-in Functions
Sanski includes a rich set of built-in functions for common tasks. See the Cheat Sheet below for a quick reference.

🗺️ Roadmap: What's Next?
Sanski is an actively developed language. Here are the features we're excited to build next:

Conditional Logic (yadi/anyatha): The top priority is adding if/else statements to allow for decision-making in your code.

While Loops (jab_tak): A while loop is planned to handle situations where the number of iterations isn't known beforehand.

Enhanced Error Reporting: We're working on providing more detailed error messages, including line numbers, to make debugging a breeze.

cheat Sheet
Here is a quick reference for all Sanski keywords and built-in functions.

Keyword

Type

Purpose

rachay

Statement

Declare a new variable.

vad

Function

Print a value to the console.

karya

Statement

Define a new function.

vapasi

Statement

Return a value from a function.

varg

Statement

Define a new class.

rachna

Method

The constructor for a class.

svayam

Parameter

Refers to the current object instance (like self).

har_ek

Statement

A for-each loop to iterate over lists.

roko

Statement

Break out of a loop.

jaari_rakho

Statement

Continue to the next iteration of a loop.

aayat

Statement

Import another .sns file.

grahan_karo()

Function

Get input from the user.

lambai()

Function

Get the length of a list, string, or dictionary.

jodo()

Function

Append an item to a list.
