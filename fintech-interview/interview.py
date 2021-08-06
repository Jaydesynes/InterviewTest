#1# A function that takes in three variables as input and checks if any two are equal and return True if any two are equal or return false False

def checkEqual(a, b, c):
    if(a == b or a == c  or b == c):
        return True
    else: 
        return False

print(checkEqual(3,5,3))

#2# A function that takes a number n as input and returns True if the number is a prime number anf falsse if it is not

def checkIfPrime(n):
    if (n > 1):
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
           return True
    else: 
        return False

print(checkIfPrime(4))

#3# A function that takes in an array as input and removes any duplicates found in the array and returns the resulting array without duplicates

def removeArrayDuplicate(arr):
    arr = list(arr)
    new_array = list(dict.fromkeys(arr))
    return new_array


caseArray = ["a", "b", "a", "c", "c"]
caseString = "hello"
print(removeArrayDuplicate(caseArray))

#4# A function that takes an array and an integer as input. return any two numbers in the array that when summed up would be equal to the value of the integer

def getPairs(arr, n, sum):
 
    pairs = []
 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                pairs.append(arr[i])
                pairs.append(arr[j])
                break
 
    return pairs[2:]

def checkTwoNumbersinArray(arr, sum):
    n = len(arr)
    return getPairs(arr, n, sum)


testArray = [1, 5, 7, -1, 5]
testNumber = 6

print(checkTwoNumbersinArray(testArray, testNumber))


#5# A function that returns true if a word is a palindrome and false if not
def isPalindrome(n):
    if(n == n[::-1]):
        return True
    else:
        return False

print(isPalindrome("mom"))

#Bonus# A functions that takes in an array and return true if it containes duplicate values and false if not
def containsDuplicateValues(arr):
    arr = list(arr)
    if(len(arr) != len(set(arr))):
        return True
    else:
        return False

caseArray = ["a", "b","c",]

print(containsDuplicateValues(caseArray))