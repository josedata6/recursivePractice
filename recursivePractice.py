#### Counts down from a given number to 0.
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)
# Example:
countdown(5)

##### Adds the digits of a number (e.g. 123 → 1+2+3 = 6).

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
# Example:
print(sum_digits(1234))  # Output: 10

##### Reverses a given string recursively.
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello"))  # Output: "olleh"

##### Classic factorial function.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1) # If n is not 0, the function calls itself with n - 1
print(factorial(5))  # Output: 120

######### Repeats a word recursively.
def repeat_word(word, times):
    if times <= 0:
        return ""
    return word + repeat_word(word, times - 1)

# Example:
print(repeat_word("fun", 3))  # Output: "funfunfun"


##### Checks whether a string is a palindrome.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])
# Example:
print(is_palindrome("racecar"))  # Output: True

######################################################
################## non recursive #####################
######################################################
# Non-recursive countdown function
def countdown(n):
    for i in range(n, -1, -1):
        print(i)

# Example:
countdown(5)

# Non-recursive sum of digits function
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
# Example:
print(sum_digits(1234))  # Output: 10

# Non-recursive string reversal function
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result
# Example:
print(reverse_string("hello"))  # Output: "olleh"

# Non-recursive factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Example:
print(factorial(5))  # Output: 120

# Non-recursive word repetition function
def repeat_word(word, times):
    result = ""
    for _ in range(times):
        result += word
    return result
# Example:
print(repeat_word("fun", 3))  # Output: "funfunfun"

# Non-recursive palindrome check function
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example:
print(is_palindrome("racecar"))  # Output: True
