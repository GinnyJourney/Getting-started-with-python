def reverseLock(lockSequence,startLocker):
    """Reverses state of each locker from an start locker.

    Args:
        lockSequence: a bool list indicating current state of all the lockers
        startLocker: a locker number where a reversing operation starts from

    Returns:
         a bool list indicating states of all the lockers after changed
    """
    for i in range(startLocker,100):
        lockSequence[i-1]=not lockSequence[i-1]

def main():
    lockSequence=[False]*100

    print(lockSequence)

    for i in range(1,100):
        reverseLock(lockSequence,i)
        print (lockSequence)

if __name__ == '__main__':
    main()


