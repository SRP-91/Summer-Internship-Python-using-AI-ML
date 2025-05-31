# # 1. Write a function to check if a number is prime.
# def is_prime(n):
#     if(n>1):
#         for i in range(2, int(n/2)+1):
#             if(n%i==0):
#                 print(n, "is not a prime number.")
#                 break
#     else:
#           print(n, "is a prime number.")
# n=int(input("Enter a number to check if it is prime or not: "))
# is_prime(n)

# # 2. Create a function to calculate the area of a rectangle.
# def Area (length, width):
#     return length * width
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# print("The area of the rectangle is:", Area(length, width))

# # 3. Write a function to find the maximum of three numbers.
# def max_of_3(a, b, c):
#     if (a>=c) and (a>=b):
#         return a
#     elif (b>=c and (b>=a)):
#         return b
#     else:
#         return c
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print(f"Maximum of 3 between {a}, {b} & {c} is {max_of_3(a, b, c)}.")

# # 4. Write a function to reverse a string. 
# def reverse_string(s):
#     return s[::-1]
# s = input("Enter a string to reverse: ")
# print("Reversed string is:", reverse_string(s))

# # 5. Create a function to count the number of vowels in a string.
# def count_vowels(str):
#     i=0
#     count=0
#     while(i<len(str)):
#         if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
#             count+=1
#         i+=1
#     return count
# str = input("Enter a string to count the number of vowels: ")
# print("Number of vowels in the string is:", count_vowels(str))

# # 6. Write a function to check if a string is a palindrome.
# def is_palindrome(s):
#     s = s.upper()  # Convert to lowercase for case-insensitive comparison
#     return s == s[::-1]
# s = input("Enter a string to check if it is a palindrome: ")
# if is_palindrome(s):
#     print(f"{s} is a palindrome.")
# else:
#     print(f"{s} is not a palindrome.")

# # 7. Create a function to calculate the sum of a list of numbers. 
# def sum_of_list(num):
#     total= 0
#     for n in num:
#         total+= n
#     return total
# print("Enter the numbers of the list 1 by 1 to calculate their sum:")
# num = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number (or type 'done' to finish): "))
#         num.append(n)
#     except ValueError:
#         flag = False
# print("The sum of the list is:", sum_of_list(num))

# # 8. Write a function to return the Fibonacci sequence up to n terms.
# def Fibbonacci_seq(n):
#     a, b = 0, 1
#     fib_sequence = []
#     for _ in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b
#     return fib_sequence
# n = int(input("Enter the number of terms in the Fibonacci series: "))
# print(f"Fibonacci sequence up to {n} terms is: {Fibbonacci_seq(n)}")

# # 9. Write a function to convert Celsius to Fahrenheit. 
# def Celsius_to_Fahrenheit(Celsius):
#     return (Celsius * 9/5) + 32
# Celsius = float(input("Enter temperature in °C: "))
# print(f"{Celsius}°C is equal to {Celsius_to_Fahrenheit(Celsius)}°F.")

# # 10. Write a function to find the minimum value in a list.
# def find_minimum(my_list):
#     if len(my_list) == 0:
#         return None
#     minimum = my_list[0]
#     for num in my_list:
#         if num < minimum:
#             minimum=num
#     return minimum
# my_list=[]
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to find minimum in the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# print(f"The minimum in the list {my_list} is {find_minimum(my_list)}")

# # 11. Create a function to count how many times a character appears in a string.
# def count_character(str, c):
#     count=0
#     for char in str:
#         if char.upper() == c.upper():
#             count += 1
#     return count
# str = input("Enter a string to count character occurrences: ")
# c = input("Enter the character to count: ")
# print(f"The character '{c}' appears {count_character(str, c)} times in the string '{str}'.")

# # 12. Write a function to check if a number is a perfect number. 
# def is_perfect_number(n):
#     if n < 1:
#         return False
#     divisors_sum = sum(i for i in range(1, n) if n % i == 0)
#     return divisors_sum == n
# n = int(input("Enter a number to check if it is a perfect number: "))
# if is_perfect_number(n):
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")

# # 13. Create a function to find the sum of digits of a number. 
# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
# n = int(input("Enter a number to find the sum of its digits: "))
# print(f"The sum of digits of {n} is: {sum_of_digits(n)}.")

# # 14. Write a function that takes a string and returns a dictionary of character frequencies. 
# def char_frequency(s):
#     frequency = {}
#     for char in s:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     return frequency
# s = input("Enter a string to find character frequencies: ")
# print("Character frequencies:", char_frequency(s))

# # 15. Write a function that returns the average of a list of numbers. 
# def Average_of_list(my_list):
#     if len(my_list) ==0:
#         return 0
#     return sum(my_list) / len(my_list)
# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# print(f"The average of the list {my_list} is {Average_of_list(my_list)}.")

# # 16. Create a function that accepts a number and prints its multiplication table. 
# def Multiplication_table(n):
#     for i in range(1, 11):
#         print(f"{n} * {i} = {n*i}")
# n = input("Enter a number to print its Multiplication table:")
# Multiplication_table(int(n))

# # 17. Write a function that accepts a list and returns the list in reverse order.
# def reverse_list(my_list):
#     return my_list[::-1]
# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# print(f"The reversed list is: {reverse_list(my_list)}")

# # 18. Write a function to find the second largest number in a list.
# def second_largest(my_list):
#     if len(my_list) < 2:
#         return None
#     first, second = float('-inf'), float('-inf')
#     for num in my_list:
#         if num > first:
#             second = first
#             first = num
#         elif num > second and num != first:
#             second = num
#     return second if second != float('-inf') else None
# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# print(f"The second largest number in the list {my_list} is: {second_largest(my_list)}")

# # 19. Create a function that accepts a list of integers and returns only the even ones. 
# def return_even(my_list):
#     even=[]
#     for num in my_list:
#         if(num%2==0):
#             even.append(num)
#     return even
# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# print(f"The even numbers in the list {my_list} are: {return_even(my_list)}.")

# # 20. Write a function to check if all characters in a string are unique.
# def are_characters_unique(str):
#     char_set = set()
#     for char in str:
#         if char in char_set:
#             return False
#         char_set.add(char)
#     return True
# str=input("Enter a string to check if all characters are unique: ")
# if are_characters_unique(str):
#     print(f"All characters in the '{str}' are unique.")
# else:
#     print(f"All characters in the '{str}' are not unique.")

# # 21. Create a function to calculate the greatest common divisor (GCD) of two numbers.
# def GCD(x, y):
#     while y:
#         x, y = y, x % y
#     return x
# a = int(input("Enter first number to find GCD: "))
# b = int(input("Enter second number to find GCD: "))
# print(f"The GCD of {a} and {b} is {GCD(a, b)}.")

# # 22. Write a function to find the least common multiple (LCM) of two numbers. 
# def LCM(a, b):
#     def gcd(x, y):
#         while y:
#             x, y = y, x % y
#         return x
#     return abs(a * b) // gcd(a, b)
# a = int(input("Enter first number to find LCM: "))
# b = int(input("Enter second number to find LCM: "))
# print(f"The LCM of {a} and {b} is {LCM(a, b)}.")

# # 23. Create a function to remove duplicates from a list.
# def remove_duplicates(my_list):
#     unique_list=[]
#     for item in my_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list
# my_list=[]
# flag=True
# while flag:
#     try:
#         element = int(input("Enter an element to add to the list (or type 'done' to finish): "))
#         my_list.append(element)
#     except ValueError:
#         flag = False
# print(f"Original List: {my_list}")
# print(f"List after removing duplicates: {remove_duplicates(my_list)}")

# # 24. Write a recursive function to compute the factorial of a number. 
# def Factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * Factorial(n-1)
# n = int(input("Enter a number to compute its factorial: "))
# print(f"The factorial of {n} is {Factorial(n)}.")

# # 25. Create a function that checks if a number is an Armstrong number.
# def is_armstrong(num):
#     sum=0
#     order = len(str(num))
#     temp = num
#     while temp>0:
#         digit= temp%10
#         sum += digit ** order
#         temp = temp//10
#     return sum == num
# num = int(input("Enter a number to check if it is an armstrong or not: "))
# if is_armstrong(num):
#     print(f"{num} is an armstrong number.")
# else:
#     print(f"{num} is not an armstrong number.")

# # 26. Write a function that returns all prime numbers up to n.
# def Prime_num_up_to_n(n):
#     prime=[]
#     for num in range(2, n + 1):
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime.append(num)
#     return prime
# n = int(input("Enter a number to find all prime numbers up to that number: "))
# print(f"All prime numbers up to {n} are: {Prime_num_up_to_n(n)}.")

# # 27. Create a function that accepts a sentence and returns the longest word. 
# def find_the_longest_word(sentence):
#     words = sentence.split()
#     return max(words, key=len)
# sentence = input("Enter a sentence to find the longest word: ")
# print(f"The longest word in the sentence is: '{find_the_longest_word(sentence)}'.")

# # 28. Write a function to compute the power of a number using recursion. 
# def power(base, exponent):
#     if (exponent==0):
#         return 1
#     elif(exponent < 0):
#         return 1 / power(base, exponent)
#     else:
#         return base * power(base, exponent - 1)
# base = float(input("Enter the base number: "))
# exponent = int(input("Enter the exponent: "))
# print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")

# # 29. Create a function that flattens a nested list. 
# def flatten_list(nested_list):
#     flat_list = []
#     for sublist in nested_list:
#         for item in sublist:
#             flat_list.append(item)
#     return flat_list
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# print("Nested List:", nested_list)
# print("Flattened List:", flatten_list(nested_list))

# # 30. Write a function to check if a list is sorted. 
# def is_already_sorted(my_list):
#     for i in range(len(my_list)-1):
#         if my_list[i] > my_list[i+1]:
#             return False
#     return True
   
# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# if is_already_sorted(my_list):
#     print(f"The list {my_list} is already sorted.")
# else:
#     print(f"The list {my_list} is not sorted.")

# # 31. Create a function to merge two sorted lists into one sorted list. 
# def merge_two_sorted_lists(list1, list2):
#     merged_list = []
#     i, j = 0, 0
    
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1
            
#     while i < len(list1):
#         merged_list.append(list1[i])
#         i += 1
        
#     while j < len(list2):
#         merged_list.append(list2[j])
#         j += 1
        
#     return merged_list

# # Convert input strings to integers
# list1 = list(map(int, input("Enter the first sorted list of numbers separated by spaces: ").split()))
# list2 = list(map(int, input("Enter the second sorted list of numbers separated by spaces: ").split()))

# print(f"The merged sorted list of {list1} and {list2} is: {merge_two_sorted_lists(list1, list2)}")

# 32. Write a function to find the most frequent element in a list. 
# def most_frequent_element(my_list):
#     frequency = {}
#     for item in my_list:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1
            
#     most_frequent = max(frequency, key=frequency.get)
#     return most_frequent, frequency[most_frequent]

# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# print(f"The most frequent element in the list {my_list} is {most_frequent_element(my_list)[0]} with a frequency of {most_frequent_element(my_list)[1]}.")

# # 33. Create a function that returns the median of a list. 
# def Find_median(my_list):
#     my_list.sort()
#     n= len(my_list)
#     if(n%2==0):
#         median = (my_list[n//2-1] + my_list[n//2])/2
#     else:
#         median= my_list[(n+1)//2]
#     return median
# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# print(f"the median of the list {my_list} is {Find_median(my_list)}.")

# # 34. Create a function that finds the intersection of two lists. 
# def Intersection_of_Two_lists(list1, list2):
#     intersection=[]
#     for item in list1:
#         if item in list2 and item not in intersection:
#             intersection.append(item)
#     return intersection
# list1 = input("Enter the first list of numbers separated by spaces: ").split()
# list2 = input("Enter the second list of numbers separated by spaces: ").split()
# print(f"The intersection of {list1} and {list2} is: {Intersection_of_Two_lists(list1, list2)}")

# # 35. Write a function that accepts variable number of arguments and returns their product
# def product_all(*args):
#     print(args)
#     product=0 
#     i=0
#     while(i<len(args)):
#         product+=args[i]
#         i+=1
#     return product
# print(product_all(1, 2, 2, 2))
# print(product_all(1, 5, 2, 10, 9, 29))


# # 36. Write a function that returns a list of tuples (element, index) from a list.
# def index_and_element(my_list, element):
#     if element in my_list:
#         return f"Element '{element}' found at index {my_list.index(element)}."
#     else:
#         return f"Element '{element}' not found in the list."
# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# n = int(input("Enter a number to find its index in the list: "))
# print(index_and_element(my_list, n))

# # 37. Create a function that accepts a string and returns a dictionary of word counts. 
# def word_count(s):
#     words = s.split()
#     count_dict = {}
#     for word in words:
#         word = word.lower()  # Convert to lowercase for case-insensitive counting
#         if word in count_dict:
#             count_dict[word] += 1
#         else:
#             count_dict[word] = 1
#     return count_dict
# s = input("Enter a string to count the words: ")
# print("Word counts:", word_count(s))

# # 38. Write a function that checks if a sentence is a pangram. 
# def check_pangram(str):
#     alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     str = str.upper()
#     return alphabet.issubset(set(str))
# str = input("Enter a string to check if it is a pangram: ")
# if check_pangram(str):
#     print(f"'{str}' is a pangram.")
# else:
#     print(f"'{str}' is not a pangram.")

# # 39. Create a function that accepts a list and a value, and returns the index of the value (or -1). 
# def find_index(my_list, value):
#     try:
#         return my_list.index(value)
#     except ValueError:
#         return -1
# my_list = []
# flag = True
# while flag:
#     try:
#         n = int(input("Enter a number to add to the list (or type 'done' to finish): "))
#         my_list.append(n)
#     except ValueError:
#         flag = False
# value = int(input("Enter a value to find its index in the list: "))
# print(f"The index of {value} in the list {my_list} is: {find_index(my_list, value)}")

# # 40. Write a function that counts the number of uppercase and lowercase characters in a string.
# def count_case(s):
#     upperCount=0
#     lowerCount=0
#     i=0
#     while(i<len(s)):
#         if(s[i].isupper()):
#             upperCount+=1
#         elif(s[i].islower()):
#             lowerCount+=1
#         i+=1
#     print("Total number of uppercase letters in '", s, "'", ":", upperCount)
#     print("Total number of lowercase letters in '", s, "'", ":", lowerCount)
# str = input("Enter a string to count uppercase and lowercase characters: ")
# count_case(str)



