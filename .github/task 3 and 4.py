def smallest(n:float, m:float) -> float:
    if n < m:
        return n                            # For neither. Both calls return m.
    else:
        return m

first = smallest(3, 2)              # first: 2
second = smallest(2, 2)             # second: 2. Yes because 2 < 2 is not true, so m is returned.
print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b                        # When a > b AND a > c
    elif b > c:
        return b + c                        # When a is not the largest value and b > c
    else:
        return 2 * c                        # When a is not the largest value and b < c


answer1 = function2(3, 2, 1)        # answer1: 1
answer2 = function2(2, 3, 1)        # answer2: 4
answer3 = function2(2, 1, 3)        # answer3: 6
print()









def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)                            # test (first call): False, test (second call): True
    if test:                                                    # This check prevents an IndexError
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)                    # first: None
second = checked_access([1, 0, 1], 2)                   # second: 1
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])          # For first call (length: 5, > 2)
    elif len(L) > 1:                                        # 4 + 2 + 3 (lengths of "this", "is", "the")
        result = len(L[0]) + len(L[1])                      # For third call (length: 2, > 1)
    elif len(L) > 0:                                        # 7 + 4 (lengths of "another" and "call")
        result = len(L[0])                                  # For second call (length 1, > 0)
    else:                                                   # 11 (length of "second call")
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
            # "this", "is", "confusing", "code.", "AVOID", "SUCH."
            # Both values of first and second are the same as the value of words
            # The original list is modified by the function instead of a copy.
            # All three variables are updated when the list is changed since they all point to this same list.
print()