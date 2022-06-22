# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:


# 2. Print the difference between the largest and smallest value:


# 3. Print True if the list contains a 2 next to a 2 somewhere.


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 


#Question 1
evenNumbers = []

for number in numbers:
    if number % 2 == 0:
        evenNumbers.append(number)
print(evenNumbers)

#Question 2
#sortedList = numbers
#sortedList.sort()
#print(sortedList[-1] - sortedList[1])

#Question 3
previous = numbers[0]
current = numbers[4]
counter = 2

while previous != current:
    previous = current
    current = numbers[counter]
    counter += 1
    if previous == 2 and current == 2:
        print(True)

#Question 4
total = 0
sixFound = False
sevenFound = False

for number in numbers:
    if ((sixFound == False) or (sevenFound == True)) and (number != 6):
        total += number
    if number == 6:
        sixFound = True
    if number == 7:
        sixFound = False
print(total)

#Question 5
i= 0
while number[i] != 13:
    