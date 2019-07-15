def cal_sqrt(n,lastGuess):
    """ Calculates square root of n.

    Args:
        n: a radicand
        lastGuess: an initial integer necessary to start the calculate

    Returns:
         nextGuess: the square root of the radicand, n
    """
    nextGuess = (lastGuess + (n / lastGuess)) / 2

    while (nextGuess-lastGuess>0.0001) or (nextGuess-lastGuess<-0.0001):

        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2

    return nextGuess


print("result=",cal_sqrt(8.0,1.0 ))



