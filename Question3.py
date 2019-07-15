def isValid(number):
    """Judges whether a list of integer is a valid code.

    Args:
        number: a processed number indicating whether a code is valid or not

    Returns:
         True: when the code is valid
         False:when the code isn't
    """
    if(sumOfOddPlace(number)+sumOfDoubleEvenPlace(number))%10==0:
        return True
        print ("The code is valid")
    else:
        return False
        print("The code is invalid")


def sumOfDoubleEvenPlace(number):
    """Doubles the sum of numbers in even places.

    Args:
        number: an 16-wide number has eight integers in even places

    Returns:
        sumOfOdd: double the sum of numbers in even places.
    """
    sumOfEven = 0
    str_number = str(number)

    for i in str_number[-2::-2]:
        int_i=int(i)
        if 2*int_i // 10 > 0:
            digit=1+2*(int_i-5)
        else:
            digit=2*int_i

        sumOfEven += digit

    return sumOfEven

def sumOfOddPlace ( number ) :
    """Calculates the sum of numbers in odd places.

    Args:
        number: an 16-wide number has eight integers in odd places

    Returns:
        sumOfOdd: the sum of numbers in odd places.
    """
    sumOfOdd = 0
    str_number = str(number)

    for i in str_number[-1::-2]:
        int_i=int(i)
        sumOfOdd += int_i

    return sumOfOdd

print(isValid(4388576018402626))
print(isValid(4388576018410707))

