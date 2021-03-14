
#Complete the square sum function so that it squares each number passed into it and then sums the results together.

#For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    #your code here





   (THIS IS THE EASIEST WAY >> 
    def square_sum(numbers):
        return sum(x ** 2 for x in numbers))
   
   
   
    #answers

    def square_sum(numbers):
        return sum(x ** 2 for x in numbers)


    def square_sum(numbers):
    return sum(x * x for x in numbers) 

    def square_sum(numbers):
    res = 0
    for num in numbers:
        res = res + num*num
    return res

    def square_sum(numbers):
    return sum([x**2 for x in numbers])
   

