# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []

    for each_item in number_list: 
        if each_item %2 != 0:
            new_list.append(each_item)

    return new_list      

print all_odd(number_list)


# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []

    for each_item in number_list: 
        if each_item %2 == 0:
            new_list.append(each_item)

    return new_list      

print all_even(number_list)
    

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []

    for each_item in word_list:
        if len(each_item) >= 4:
            new_list.append(each_item)

    return new_list

print long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):

    init_val = number_list[0]

    for each_number in number_list:
        if each_number < init_val:
            init_val = each_number
        else:
            continue
    return init_val


    # number_list.sort()

    # return number_list[0]

print smallest(number_list)


# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    
    sort_number = sorted(number_list)

    return sort_number[-1]

print largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):

    new_list=[]

    for each_number in number_list: 
        num_float = float(each_number)
        each_number = (num_float/2)
        new_list.append(each_number)   

    return new_list

print halvesies(number_list)  


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_word_list = []

    for each_word in word_list:
        length_of_word=len(each_word)
        new_word_list.append(length_of_word)

    return new_word_list

print word_lengths(word_list)


# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sums = 0
    for each_number in number_list:
        sums += each_number
    return sums

print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    multiplies = 1
    for each_number in number_list:
        multiplies *= each_number
    return multiplies

print mult_numbers(number_list)


# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    sent = ""
    for each_word in word_list:
        right_word = each_word + " "
        sent += right_word
    return sent

print join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    sums = 0
    count = 0

    for each_num in number_list:
        sums += float(each_num)
        count += 1
        avg = float(sums/count)
    return avg

print average(number_list)
