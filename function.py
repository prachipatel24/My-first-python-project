# def even_odd(num):
#     if num % 2 == 0:
#         return "Even Number"
    
#     else:
#         return "Odd Number"
    
# print(even_odd(9))

# def check_age(age):
#     if age < 13:
#         return "child"
#     elif age < 18:
#         return "Teenager"
#     elif age < 60:
#         return "Adult"
#     else:
#         return "Senior Citizen"

# print(check_age(35))

def is_palindrome(word):
    return word == word[::-1]

def palindrome_project():
    word = input("Enter word: ")

    if is_palindrome(word) :
        print("Yes, palindrome")

    else:
        print("No, palindrome")

palindrome_project()        