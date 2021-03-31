# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

#First Solution 
def solution(number):
    result = [] # create list "result"
    for i in range(1, number): #for i in range...
        if i % 3 == 0 or i % 5 == 0: #if i divisible by 3 or 5
            result.append(i)  #add i to list

    return sum(result) #return sum of items in list

#Second Solution short version of First Solution 
def solution2(number):
  return sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])

#Third Solution with lambda 
solution3 = lambda number : sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])