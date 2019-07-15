def isPrime(n):
    """Judges whether an integer is a prime or not.

    Args:
        n: an integer needed to be judged whether it is a prime.

    Returns:
        True: when the integer is a prime
        False: when the integer isn't
    """
    for i in range(2,n) :
        if n % i == 0 :
            return False
            break


    return True


def isEmirp(n):
    """ Judges whether an integer is emirp or not.

    Args:
        n: an integer needed to be judged whether it is a emirp.

    Returns:
        True: when the integer is a emirp
        False: when the integer isn't

    """
    str_n = str(n)
    n_reverse = int(str_n[::-1])

    if isPrime(n) and isPrime(n_reverse):
        return True
    else:
        return False



n=0
num=0

while (True):
        n+=1
        if isEmirp(n):
            print(n,end=' ')
            num+=1
        if (num%10==0) and (isEmirp(n)):
            print("\n")
        if num==100:
            break



