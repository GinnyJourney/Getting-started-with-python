def isAnagram(s1,s2):
    """Judges whether a pair of strings is anagram.

    Args:
        s1: one of a pair of strings needed to be judged
        s2: the other of a pair of strings needed to be judged

    Returns:
         True: when the pair of strings is anagram
         False: when the pair isn't
    """
    l1=list(s1)
    l2=list(s2)

    l1.sort(key=None, reverse=False)
    l2.sort(key=None, reverse=False)

    if len(l1)==len(l2):
        for i in range(0,len(l1)):
            if l1[i]!=l2[i]:
               return False
        return True
    else:
        return False

print("the string is anagram",isAnagram("happy","stream"))
print("the string is anagram",isAnagram("listen","silent"))
