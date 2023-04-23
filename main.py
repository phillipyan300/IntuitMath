
#General: fix duplicates issue
#fix too many parenthese
# allow it so that you don't always need all 6.
# crashes when there isn't a solution
# test listcopy stuff
# check negative values to make sure those don't go through
# quality control: choose answer at the end with the least parentheses

#Input: Includes list of tuples, listform
#insertionLocations as exact indices of where the parentheses need to be

#using none in python
def addParentheses(insertionLocations, originalList, value_to_find):
    #temporary = False
    #if (originalList == ["5", "+", "6", "+", "10", "*", "11", "+", "18", "+", "12"]):
      #  temporary = True

    #This is just in the case that you need to return the original list, if you get a division by 0
    #print("call")
    copyList = originalList.copy()
    for i in insertionLocations:
        originalList[i[0]] = '(' + originalList[i[0]]
        originalList[i[1]] = originalList[i[1]] + ')'

    #print(originalList)
    try:
        if int(eval("".join(originalList)) == int(value_to_find)):
            return [True, "".join(originalList)]
    except ZeroDivisionError:
        return [False, "".join(copyList)]
    else:
        return [False, "".join(originalList)]





#Will need to refactor this to make sure that it uses a stack instead (look at data structures code)
#Returns the a string. First element is a boolean, if there exists a format of the string to calculate
# which equals the value,  second element is the actual string itself
def stringCalculator(string_to_calculate, value_to_find):
    # Start by testing the case when it's already correct
    if eval(string_to_calculate) == value_to_find:
        return [True, string_to_calculate]

    #First we need to make it into list, but keep operators
    container = ""
    listForm = []
    for i in string_to_calculate:
        if i in "+-*/":
            listForm.append(container)
            listForm.append(i)
            container = ""
        else:
            container += i
    listForm.append(container)


    #Now to consider all possible parentheses; values are even indices, operators are odd.
    two_tuple_list = [(0,2), (2,4), (4,6), (6,8), (8,10)]
    three_tuple_list = [(0,2,4),(2,4,6), (4,6,8), (6,8,10)]
    four_tuple_list = [(0,2,4,6), (2,4,6,8), (4,6,8,10)]
    five_tuple_list = [(0,2,4,6,8), (2,4,6,8,10)]


    #Now all possible combinations of the above parentheses

    #Two Tuples (alternate way to implement this would require 3 nested for loops-for only 6 variables, its easier to do it like this
    for i, tuple in enumerate(two_tuple_list):
        #evaluate just that tuple parentheses
        retval = addParentheses([(two_tuple_list[i][0], two_tuple_list[i][1])], listForm.copy(), value_to_find)
        if retval[0]:
            return retval

        if (i + 2) < len(two_tuple_list):
            retval = addParentheses([(two_tuple_list[i][0], two_tuple_list[i][1]),(two_tuple_list[i+2][0], two_tuple_list[i+2][1])], listForm.copy(), value_to_find)
            if retval[0]:
                return retval
        if (i+3) < len(two_tuple_list):
            retval = addParentheses([(two_tuple_list[i][0], two_tuple_list[i][1]),(two_tuple_list[i+3][0], two_tuple_list[i+3][1])], listForm.copy(), value_to_find)
            if retval[0]:
                return retval
        if (i+4) < len(two_tuple_list):
            retval = addParentheses([(two_tuple_list[i][0], two_tuple_list[i][1]),(two_tuple_list[i+2][0], two_tuple_list[i+2][1]), (two_tuple_list[i+4][0], two_tuple_list[i+4][1])], listForm.copy(), value_to_find)
            if retval[0]:
                return retval



    #Three tuples-a similar model
    for i, tuple in enumerate(three_tuple_list):
        #evaluate just that tuple
        retval = addParentheses([(three_tuple_list[i][0], three_tuple_list[i][2])], listForm.copy(), value_to_find)
        if retval[0]:
            return retval
        if (i+3<len(three_tuple_list)):
            retval = addParentheses([(three_tuple_list[i][0], three_tuple_list[i][2]), (three_tuple_list[i+3][0], three_tuple_list[i+3][2])], listForm.copy(), value_to_find)
            if retval[0]:
                return retval

    #Two and three tuple
    for i, tuple in enumerate(two_tuple_list):
        if (two_tuple_list[i][1] + 6 < len(listForm)):
            retval = addParentheses([(two_tuple_list[i][0], two_tuple_list[i][1]), (two_tuple_list[i][1] + 2, two_tuple_list[i][1] + 6)], listForm.copy(), value_to_find)
            if retval[0]:
                return retval
        if (two_tuple_list[i][1] + 8 < len(listForm)):
            retval = addParentheses([(two_tuple_list[i][0], two_tuple_list[i][1]), (two_tuple_list[i][1] + 4, two_tuple_list[i][1] + 8)], listForm.copy(), value_to_find)
            if retval[0]:
                return retval
        if (two_tuple_list[i][0] - 6 >= 0):
            retval = addParentheses([(two_tuple_list[i][0], two_tuple_list[i][1]), (two_tuple_list[i][0] -6, two_tuple_list[i][0] - 2)], listForm.copy(), value_to_find)
            if retval[0]:
                return retval
        if (two_tuple_list[i][0] - 8 >= 0):
            retval = addParentheses([(two_tuple_list[i][0], two_tuple_list[i][1]), (two_tuple_list[i][1] - 8, two_tuple_list[i][1] - 4)], listForm.copy(), value_to_find)
            if retval[0]:
                return retval

    #Four and four-two tuples
    for i, tuple in enumerate(four_tuple_list):
        retval = addParentheses([(four_tuple_list[i][0], four_tuple_list[i][3])], listForm.copy(), value_to_find)
        if retval[0]:
            return retval
        if (four_tuple_list[i][3]+4 < len(listForm)):
            retval = addParentheses([(four_tuple_list[i][0], four_tuple_list[i][3]), (four_tuple_list[i][3]+2, four_tuple_list[i][3]+4)], listForm.copy(), value_to_find)
            if retval[0]:
                return retval
        if (four_tuple_list[i][0]-4 >= 0):
            retval = addParentheses([(four_tuple_list[i][0], four_tuple_list[i][3]), (four_tuple_list[i][0]-4, four_tuple_list[i][0]-2)], listForm.copy(), value_to_find)
            if retval[0]:
                return retval


    #Five-tuples
    for i, tuple in enumerate(five_tuple_list):
        retval = addParentheses([(five_tuple_list[i][0], five_tuple_list[i][4])], listForm.copy(), value_to_find)
        if retval[0]:
            return retval
    return [False, string_to_calculate]

#This will return the computation string (a bit messy), not the value
#At each iteration, only the correct string is returned.
def recurseMain(value_list,running_calculate_string, value_to_find):
    #print(value_list, running_calculate_string, value_to_find)
    # To check if you have reached the end of recursion
    if (len(value_list) == 0):
        temp =  stringCalculator(running_calculate_string, value_to_find)
        if temp[0]:
            return temp[1]
        else:
            return None

    #Now to go through each element in the value list
    for j, test_value in enumerate(value_list):
        # do i even need a copylist?
        copy_list = value_list.copy()
        del copy_list[j]
        #Addition
        potential_retstring = recurseMain(copy_list, running_calculate_string + "+" + str(test_value), value_to_find)
        if potential_retstring != None:
            return potential_retstring

        #Subtraction
        potential_retstring = recurseMain(copy_list, running_calculate_string + "-" + str(test_value), value_to_find)
        if potential_retstring != None:
            return potential_retstring

        #Multiplication
        potential_retstring = recurseMain(copy_list, running_calculate_string + "*" + str(test_value), value_to_find)
        if potential_retstring != None:
            return potential_retstring

        #Division-need to make sure that it actually works
        potential_retstring = recurseMain(copy_list, running_calculate_string + "/" + str(test_value), value_to_find)
        if potential_retstring != None:
            return potential_retstring

    #if none of the four return the right value, return this arbitrary value, which means its parent will ignore this result
    return None



#Turns the input into a list. Fix when there are multiple spaces.
def inputParser(values):
    listForm = list(values.split(" "))
    for i in range(0,len(listForm)):
        listForm[i] = int (listForm[i])
    return listForm


if __name__ == '__main__':
    initial_value = input("Enter the 6 values, space separated: ")
    final_value = input("Enter the final value: ")
    return_expression = ""

    inputList = inputParser(initial_value)
    for i, value in enumerate(inputList):
        copyList = inputList.copy()
        if (value == final_value):
            return_expression = value
        del copyList[i]
        tempVar = recurseMain(copyList, str(value), final_value)
        if tempVar != None:
            print(tempVar)
        # if int(eval(recurseMain(copyList, str(value), final_value))) == int(final_value):
        #     print(recurseMain( copyList, str(value), final_value))

