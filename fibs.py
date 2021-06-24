# Assignment 2, Question 1
# Author: Catherine Li
# McGill ID: 260914784


def is_fibonacci(number):
    '''
    Parameter: number (an integer)
    Return: True if the number is one of the first 1000 Fibonacci numbers, False otherwise
    '''
    #set the first two Fibonacci numbers as variables
    first_number = 0
    second_number = 1
    
    # 998 because first two numbers will be checked separately
    for i in range(998):
        #check first two numbers
        if number == first_number or number == second_number:
            return True
        
        #Fibonacci sequence
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
        
        if next_number == number:
            return True
    #number is not a Fibonacci number if code reaches this line
    return False


def filter_fibonacci(numbers):
    '''
    Parameter: numbers (a list)
    Return: a list with all the Fibonacci numbers from numbers list up to 1000th term
    '''
    #create blank list to add numbers
    list_Fibonacci = []
    
    i = 0
    while i < len(numbers):
        number = numbers[i]
        #check if number is Fibonacci
        if is_fibonacci(number):
            list_Fibonacci.append(number)
        i += 1
    return list_Fibonacci

#created function used in get_integers_from_user()
def check_periods(string):
    '''
    Parameter: string
    Return: False if string has more than 1 period, True otherwise
    '''
    no_double_period = True
    period = "."
    counter = 0 #counter reflects the number of periods in the string
    
    #check if more than 1 period in the string
    for index in range(len(string)):
        if period in string[index]:
            counter += 1
            
    #False if more than one period
    if counter >= 2:
        no_double_period = False
        
    return no_double_period

#created function used in get_integers_from_user()
def check_num_dig(string):
    '''
    Parameter: string
    Return: True if the string only contains numbers or periods, False otherwise
    '''
    NUMBERS_AND_PERIOD = '1234567890.'
    in_or_not = True
    
    #check string for numbers and periods
    for i in string:
        if i not in NUMBERS_AND_PERIOD:
            in_or_not = False
    return in_or_not


def get_integers_from_user():
    '''
    Parameter: None
    Return: a sorted list in increasing order of all valid numbers to test for fibonacci
    Function asks user to enter a series of positive numbers, separated by a comma
    If number is decimal, convert to integer
    '''
    numbers = input("Enter number(s): ")
    
    #separate the numbers and make them elements of the list
    minus = ','
    numbers = numbers.split(minus)
    
    acceptable_numbers = []
    
    #for every element in numbers
    for i in range(len(numbers)):
        if i == len(numbers):
            break
        #for every character in an element
        for j in range(len(numbers[i])):
            string = numbers[i] #used for two created functions
        #check elements with two or more periods 
            if check_periods(string) == False:
                break
            #if the character is a number or . then add element to new list
            if check_num_dig(string):
                acceptable_numbers.append(numbers[i])
                break
    #now, the full list of acceptable numbers is made
    
    #convert numbers to int type if they are integers
    for i in range(len(acceptable_numbers)):
        acceptable_numbers[i] = float(acceptable_numbers[i])
        if acceptable_numbers[i] == int(acceptable_numbers[i]):
            acceptable_numbers[i] = int(acceptable_numbers[i])

    #set equal to number list and re-order to ascending list
    numbers = acceptable_numbers
    for i in range(len(numbers)):
        numbers.sort()
    return numbers


# Please do not alter anything below this line.
if __name__ == '__main__':
    numbers = get_integers_from_user()
    print(filter_fibonacci(numbers))
