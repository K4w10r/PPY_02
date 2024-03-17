

"""8.
Extend the previous Python program to write the output to a file and perform operations on that file.

  a. ...

  b. ...

  c. ...

  d. ...

  e. ...

  f. ...

  g. ...

  h. Write Output to File: Write all the results (original inputs, modified data structures, type conversion results) to a file.

  i. Perform Operations on File: Open the file, read its content, and perform some operations like counting the number of lines, finding specific data, etc.

  j. Modify File Content: Modify the content of the file by, for example, changing specific lines or adding new lines.
"""

# Input
input_numbers = input("Enter a series of space-separated integers: ")

# Convert Input
numbers_list = input_numbers.split(" ")
numbers_tuple = tuple(input_numbers.split(" "))

# Manipulate List
# Append 10 to the list
numbers_list.append(10)
# Insert 20 at index 2
numbers_list.insert(2, 20)
# Remove the element 8
numbers_list.remove(8)

# Attempt to Modify Tuple (this will raise an error)
try:
    # Append 10 to the tuple
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
set1 = set(10, 11, 12)
set2 = set(8, 5)
set3 = set(1, 2, 5)
set4 = set(1, 2, 5, 9, 10, 20)
# Union
set_union = set1.union(numbers_list)
# Intersection
set_intersection = set2.intersection(numbers_tuple)
# Difference
set_difference = numbers_list.difference(set3)

# Dictionary Operations
numbers_dict = {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
print("Original Dictionary:", numbers_dict)
# Add a new key-value pair
numbers_dict[11] = 121
# Delete an existing key-value pair
del numbers_dict[8]

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = {elem: elem ** 2 for elem in numbers_list}
tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = {elem: elem ** 2 for elem in numbers_tuple}
set_to_list = list(set4)
set_to_tuple = tuple(set4)
set_to_dict = {elem: elem ** 2 for elem in set4}
dict_to_list = list(numbers_dict.keys())
dict_to_tuple = tuple(numbers_dict.keys())
dict_to_set = set(numbers_dict.keys())

student_number = input("Enter your student number: ")

# Write Output to File like this:
with open('students.txt', 'w') as file:
    file.write("Student Number: " + student_number + '\n' +

    "Original List: " + str(numbers_list) + '\n' +
    "Original Tuple: " + str(numbers_tuple) + '\n' +
    "Original Set: " + str(numbers_set) + '\n' +
    "Original Dictionary: " + str(numbers_dict) + '\n' + '\n' +

    "Manipulated List: " + str(numbers_list) + '\n' +
    "Manipulated Tuple: " + str(numbers_tuple) + '\n' +
    "Union of Set: " + str(set_union) + '\n' +
    "Intersection of Set: " + str(set_intersection) + '\n' +
    "Difference of Set: " + str(set_difference) + '\n' +
    "Updated Dictionary: " + str(numbers_dict) + '\n' + '\n' +

    "List to Tuple: " + str(list_to_tuple) + '\n' +
    "List to Set: " + str(list_to_set) + '\n' +
    "List to Dictionary: " + str(list_to_dict) + '\n' +
    "Tuple to List: " + str(tuple_to_list) + '\n' +
    "Tuple to Set: " + str(tuple_to_set) + '\n' +
    "Tuple to Dictionary: " + str(tuple_to_dict) + '\n' +
    "Set to List: " + str(set_to_list) + '\n' +
    "Set to Tuple: " + str(set_to_tuple) + '\n' +
    "Set to Dictionary: " + str(set_to_dict) + '\n' +
    "Dictionary to List: " + str(dict_to_list) + '\n' +
    "Dictionary to Tuple: " + str(dict_to_tuple) + '\n' +
    "Dictionary to Set: " + str(dict_to_set) + '\n')

# print "Content of the file:"

with open('students.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Perform Operations on File:
line_count = 0
integer_count = 0
integer_sum = 0
#   Count the number of lines in the file
with open('students.txt', 'r') as file:
    for line in file:
        line_count += 1
        words = line.split()
        for word in words:
            if word.isDigit():
                integer_count += 1
                integer_sum += int(word)
print(line_count)
#   Count the number of integers in the file
print(integer_count)
#   Add all integers in the file (sum).
print(integer_sum)
#   Modify the content of the file
with open('students.txt', 'a') as file:
    file.write(str('line added , file modified' + '\n'))

"""--------------------------------------------------------------------------------
**Control Statements:**
Control statements are used in programming to alter the flow of execution based on certain conditions or criteria. In Python, commonly used control statements include:

`if, elif, else:` These statements are used for conditional execution.
 They allow the program to execute different blocks of code based on specified conditions.

`for loop:` Used for iterating over a sequence (such as lists, tuples, strings, etc.) or any iterable object.
 It allows you to execute a block of code repeatedly for each item in the sequence.

`while loop:` Used for executing a block of code repeatedly as long as a specified condition is true.
 It keeps iterating until the condition becomes false.


**Loops:**
Loops are used for executing a block of code repeatedly. In Python, there are two main types of loops:

`for loop: `As mentioned earlier, the for loop iterates over a sequence or any iterable object.

`while loop:` This loop executes a block of code as long as a specified condition is true. It continues iterating until the condition becomes false.

**Other Statements:**
This category typically includes other types of statements that don't fall directly under control statements or loops. It can include various types of statements used for different purposes in Python programming, such as:

`Assignment statements:` Assigning values to variables.

`Function calls:` Invoking functions to perform specific tasks.

`Import statements:` Importing modules or packages to use their functionality in the current script or program.

`Exception handling statements: `Statements used for handling exceptions (errors) that may occur during the execution of a program, such as try, except, finally, etc.

`With statements: `Used for resource management, especially for working with files, to ensure that certain resources are properly closed or released after use.

These are fundamental constructs in Python programming that enable you to control the flow of your program, repeat tasks efficiently, and execute various types of statements to achieve desired functionality.

-------------------------------------------------------------------------------

9.  Utilizing the Largest Integer from output.txt

  Task Description:

  Transform the previous task to utilize the largest integer from the output file 'output.txt' instead of asking the user for it.

  1. Read the largest integer from the 'output.txt' file.
  2. Generate a list of all prime numbers up to the largest integer.
  3. Print the list of prime numbers.
  4. Calculate the sum of all prime numbers in the list.
  5. Determine the largest and smallest prime numbers in the list.
  6. Check if the largest integer itself is prime and print the result.
  7. Write the list of prime numbers along with the sum, largest, and smallest prime numbers to a file 'prime_numbers.txt'.
  8. Handle the scenario where the largest integer cannot be found in the file.

  Example:

  If the 'output.txt' file contains:
  Largest prime number: 20

  The program will generate the list of prime numbers up to 20, perform calculations, and write the results to 'prime_numbers.txt'.
"""

# Convert Input
numbers_list = input_numbers.split(" ")
numbers_tuple = tuple(input_numbers.split(" "))

# Manipulate List
# Append 10 to the list
numbers_list.append(10)
# Insert 20 at index 2
numbers_list.insert(2, 20)
# Remove the element 8
numbers_list.remove(8)

# Attempt to Modify Tuple (this will raise an error)
try:
    # Append 10 to the tuple
    numbers_tuple.append(10)
except AttributeError:
    print("Tuples are immutable and cannot be modified.")

# Set Operations
set1 = set(10, 11, 12)
set2 = set(8, 5)
set3 = set(1, 2, 5)
set4 = set(1, 2, 5, 9, 10, 20)
# Union
set_union = set1.union(numbers_list)
# Intersection
set_intersection = set2.intersection(numbers_tuple)
# Difference
set_difference = numbers_list.difference(set3)

# Dictionary Operations
numbers_dict = {5: 25, 2: 4, 8: 64, 1: 1, 9: 81}
print("Original Dictionary:", numbers_dict)
# Add a new key-value pair
numbers_dict[11] = 121
# Delete an existing key-value pair
del numbers_dict[8]

# Type Conversion
list_to_tuple = tuple(numbers_list)
list_to_set = set(numbers_list)
list_to_dict = {elem: elem ** 2 for elem in numbers_list}
tuple_to_list = list(numbers_tuple)
tuple_to_set = set(numbers_tuple)
tuple_to_dict = {elem: elem ** 2 for elem in numbers_tuple}
set_to_list = list(set4)
set_to_tuple = tuple(set4)
set_to_dict = {elem: elem ** 2 for elem in set4}
dict_to_list = list(numbers_dict.keys())
dict_to_tuple = tuple(numbers_dict.keys())
dict_to_set = set(numbers_dict.keys())

student_number = input("Enter your student number: ")

# Write Output to File like this:
with open('output.txt', 'w') as file:
    file.write("Student Number: " + student_number + '\n' +

    "Original List: " + str(numbers_list) + '\n' +
    "Original Tuple: " + str(numbers_tuple) + '\n' +
    "Original Set: " + str(numbers_set) + '\n' +
    "Original Dictionary: " + str(numbers_dict) + '\n' + '\n' +

    "Manipulated List: " + str(numbers_list) + '\n' +
    "Manipulated Tuple: " + str(numbers_tuple) + '\n' +
    "Union of Set: " + str(set_union) + '\n' +
    "Intersection of Set: " + str(set_intersection) + '\n' +
    "Difference of Set: " + str(set_difference) + '\n' +
    "Updated Dictionary: " + str(numbers_dict) + '\n' + '\n' +

    "List to Tuple: " + str(list_to_tuple) + '\n' +
    "List to Set: " + str(list_to_set) + '\n' +
    "List to Dictionary: " + str(list_to_dict) + '\n' +
    "Tuple to List: " + str(tuple_to_list) + '\n' +
    "Tuple to Set: " + str(tuple_to_set) + '\n' +
    "Tuple to Dictionary: " + str(tuple_to_dict) + '\n' +
    "Set to List: " + str(set_to_list) + '\n' +
    "Set to Tuple: " + str(set_to_tuple) + '\n' +
    "Set to Dictionary: " + str(set_to_dict) + '\n' +
    "Dictionary to List: " + str(dict_to_list) + '\n' +
    "Dictionary to Tuple: " + str(dict_to_tuple) + '\n' +
    "Dictionary to Set: " + str(dict_to_set) + '\n')

with open('output.txt', 'a') as file:
    file.write(str('line added , file modified' + '\n'))

prime_numbers = list()
largest_num = -float('inf')
try:
    with open('output.txt', 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.isDigit():
                    num = int(word)
                    if num > largest_num:
                        largest_num = num

    for i in range(2,largest_num+1):
        for j in range(2,num+1):
            if i%j == 0:
                break
        if i == j:
            prime_numbers.append(i)

    print(prime_numbers)

    sumOfPrimeNumbers = 0;
    for i in prime_numbers:
        sumOfPrimeNumbers += i

    print(sumOfPrimeNumbers)

    largest_prime = prime_numbers[-1]
    smallest_prime = prime_numbers[0]

    if largest_num > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (largest_num//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (largest_num % i) == 0:
                print(largest_num, "is not a prime number")
                break
        else:
            print(largest_num, "is a prime number")
    else:
        print(largest_num, "is not a prime number")

    with open('prime_numbers.txt', 'w') as file:
        file.write(prime_numbers)
        file.write('\n' + 'largest prime: ' + largest_prime + '\n')
        file.write('smallest prime: ' + smallest_prime + '\n')
except IOError:
    print('no largest prime numbers found')

"""10.
In the final main.py file, leave the results from task 8 and 9, commit and push
"""
