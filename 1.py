# 1. Print numbers from 1 to 10.
# for i in range(1,11):
#     print(i, " ")

#2. Print even numbers from 1 to 20. 
# for i in range(1,21):
#     if(i%2==0):
#         print(i, " ")

# 3. Check if a number is positive, negative or zero. 
# n = int(input("Enter a number to check if it is a positive, negative or zero: "))
# if(n==0):
#     print(n, " is zero")
# elif(n>0):
#     print(n, " is positve")
# else:
#     print(n, " is negative")

# 4. Add two numbers using operators. 
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# print("{} + {} = {}".format(a, b, a + b))


# 5. Print multiplication table of a number. 
# n = int(input("Enter a number to show its multiplication table: "))
# for i in range(1, 11):
#     print("{} * {} = {}".format(n ,i , n*i))

# 6. Find the largest among two numbers. 
# print("Enter 2 numbers to check which 1 is greater")
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# if(a<b):
#     print(b, " is greater.")
# elif(a>b):
#     print(a, " is greater.")
# else:
#     print("Both ", a, " & ", b, " are equal.")

# 7. Use a while loop to print numbers 5 to 1. 
# count=5
# while(count>=1):
#     print(count)
#     count-=1

# 8. Print all characters in a string. 
# word="chbewdn "
# for i in word:
#     print(i)

# 9. Use logical operator to check if a number is between 10 and 50. 
# n=int(input("enter a number: "))
# if(n>10 and n<50):
#     print(n, " is between 10 & 50.")
# else:
#     print(n, " is not between 10 & 50.")

# 10. Sum of first 10 natural numbers. 
# sum=0
# for i in range(1, 10):
#     sum=sum+i
# print("Sum = ", sum)

# 11. Print "Odd" or "Even" for numbers 1 to 10. 
# for i in range(1, 11):
#     if(i%2==0):
#         print(i, " is even.")
#     else:
#         print(i, " is odd.")

# 12. Use “break” to stop loop when number is 5. 
# for i in range(1, 11):
#     if(i==5):
#         break
#     print(i)
    
# 13. Print 1 to 10 and use continue to skip printing 5.
# for i in range(1, 11):
#     if(i==5):
#             continue
#     print(i)

# 14. Print all elements in a list using a loop. 
# my_list = [98, 12, 45, 76, 23]
# i=0
# while(i<len(my_list)):
#     print(my_list[i])
#     i+=1

# 15. Check if a number is divisible by both 3 and 5. 
# n=int(input("Enter a number to check if it is divisible both by 3 & 5: "))
# if(n%3==0 and n%5==0):
#     print(n, "is divisble by both 3 & 5.")
# else:
#     print(n, "is not divisble by both 3 & 5.")

# 16. Square of all numbers from 1 to 5. # 
# i=1
# sq = lambda x: x*x
# while i in range(1, 6):
#     print("Square of " , i, " is ", sq(i), ".")
#     i+=1

# 17. Print ASCII values of characters in a string. 
# string=input("Enter a string to print their ASCII values: ")
# i=0
# while(i<len(string)):
#     print("ASCII value of ", string[i], " is ", ord(string[i]), ".")
#     i+=1

# 18. Count down from 10 to 1 using while. 
# i=10
# while (i>0):
#     print(i)
#     i-=1

# 19. Check if a number is divisible by 2 or 3. 
# n=int(input("Enter a number to check if it is divisible both by 2 or 3: "))
# if(n%2==0 or n%3==0):
#     print(n, "is divisble by 2 or 3.")
# else:
#     print(n, "is not divisble by 2 or 3.")

# 20. Print the first 10 even numbers.
# str=input("Enter a number to find the sum of its digits: ")
# i=0
# sum=0
# while(i<len(str)):
#     d=int(str[i])
#     sum+=d
#     i+=1
# print("Sum of digits: ", sum)

# 21. Swap two numbers using a temporary variable. 
# print("Enter 2 nunbers to swap them.")
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# print("Before Swapping: ", a, b)
# temp=b
# b=a
# a=temp
# print("After Swapping: ", a, b)

# 22. Print numbers from 1 to 100 that are divisible by 7. 
# print("Nunbers that are divisble by 7 between  1 to 100 are ")
# i=0
# while i in range(1, 101):
#     if(i%7==0):
#         print(i)
#         i+=1

# # 23. Find the factorial of a number. 
# n=int(input("Enter a number to find its factorial: "))
# factorial=1
# i=1
# while(i<=n):
#     factorial *= i
#     i+=1
# print("Factorial of", n, "is", factorial)

# 24. Count vowels in a string. 
# str=input("Enter a string to count the number of vowels: ")
# i=0
# count=0
# while(i<len(str)):
#     if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
#         count+=1
#     i+=1
# print("Total  number of vowels in '", str, "'", ":", count)

# 25. Reverse a number using loop. 
# n=int(input("Enter a number to reverse it: "))
# reversedNum=0
# while(n>0):
#     digit=n%10
#     reversedNum = (reversedNum*10)+digit
#     n=n//10
# print("Result:", reversedNum)

# 26. Find the maximum in a list using loop.
# my_list=[]
# n=int(input("Enter number of elements in the list:"))
# for i in range(n):
#     element=int(input("Enter element:"))
#     my_list.append(element)
# print("List:", my_list)
# for i in range(len(my_list)):
#     for j in range(i+1, len(my_list)):
#         if my_list[i] > my_list[j]:
#             my_list[i], my_list[j] = my_list[j], my_list[i]
# print("Maximum element in the list is:", my_list[-1])

# 27. Prime number check using loop. 
# n=int(input("Enter a number to check if it is prime or not: "))
# if(n>1):
#     for i in range(2, int(n/2)+1):
#         if(n%i==0):
#             print(n, "is not a prime number.")
#             break
#     else:
#         print(n, "is a prime number.")

# 28. Sum of even numbers in a list. 
# my_list=[]
# n=int(input("Enter number of elements in the list:"))
# sum=0
# for i in range(n):
#     element=int(input("Enter element:"))
#     my_list.append(element)
#     if(element%2==0):
#         sum+=element
# print("Hence the sum of the evn elements present in the list:", sum)

# # 29. Print number pattern using nested loops.
# n= int(input("Enter the number of rows for the pattern: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# # 30. Count frequency of digits in a number.
# n = input("Enter a number to count the frequency of its digits: ")
# frequency = {}
# for digit in n:
#     if digit in frequency:
#         frequency[digit] += 1
#     else:
#         frequency[digit] = 1
# print("Frequency of digits in", n, "is:")
# for digit, count in frequency.items():
#     print(f"{digit}: {count}")

# 31. GCD of two numbers using loop. 
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# print("Enter two numbers to find their GCD:")
# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))
# result = gcd(num1, num2)

# 32. Check if a number is a palindrome. 
# n=int(input("Enter a number to check if its a pallindrome: "))
# num=n
# reverseDigit=0
# while(n>0):
#     digit=n%10
#     reverseDigit=reverseDigit*10+digit
#     n=n//10
# if(num==reverseDigit):
#     print(num, "is a pallindrome number.")
# else:
#     print(num, "is not a pallindrome number.")

# 33. Count words in a sentence. 
# n=input("Enter a sentence to count the number of words in it: ")
# count=0
# i=0
# while(i<len(n)):
#     if(n[i]==' '):
#         count+=1
#     i+=1
# print("Total number of words in '", n, "'", ":", count+1)

# 34. Find common elements in two lists.
# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8]
# common_elements = []
# for element in l1:
#     if element in l2:
#         common_elements.append(element)
# print("Common elements in the two lists:", common_elements)

# 35. Use elif to grade students based on score. 
# n=int(input("Enter student marks to check their grade:"))
# if n>=90:
#     print("Grade: O")
# elif n>=80:
#     print("Grade: A+")
# elif n>=70:
#     print("Grade: A")
# elif n>=60:
#     print("Grade: B")
# elif n>=50:
#     print("Grade: C")
# elif n>=40:
#     print("Grade: F")

# 36. Print a right-angled triangle using *. 
# #printing a right triangle with asterisks
# n=int(input("Enter the number of rows for the right triangle: "))
# for i in range(1, n + 1):
#     print('*' * i)

# 37. Check if a year is a leap year. 
# n=int(input("Enter a year to check if it is a leap year or not: "))
# if(n%4==0):
#     if(n%100==0):
#         if(n%400==0):
#             print(n, "is a leap year.")
#         else:
#             print(n, "is not a leap year.")

# 38. Print Fibonacci series using loop. 
# n = int(input("Enter the number of terms in the Fibonacci series: "))
# a, b = 0, 1
# print("Fibonacci series:")
# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# 39. Count uppercase and lowercase letters in a string. 
# n=input("Enter a string to count its uppercase & lowercase letters:")
# upperCount=0
# lowerCount=0
# i=0
# while(i<len(n)):
#     if(n[i].isupper()):
#         upperCount+=1
#     elif(n[i].islower()):
#         lowerCount+=1
#     i+=1
# print("Total number of uppercase letters in '", n, "'", ":", upperCount)
# print("Total number of lowercase letters in '", n, "'", ":", lowerCount)

# 40. Print numbers from 100 to 1 using loop. 
# i=100
# while(i>=1):
#     print(i)
#     i-=1



