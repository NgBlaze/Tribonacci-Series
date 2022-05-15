import sys


def tribonacci(signature, n):
    if n == 0:
        b = []
        return b
        sys.exit()

    if (signature[0] == signature[1] == signature[2] == 1) and (n == 1):
        c = [1]
        return c
        sys.exit()
    if (len(signature) >= 3) and n == 1:
        firstElement = signature[0]
        firstList = []
        add__ = firstList.append(firstElement)

        return firstList
        sys.exit()

    if (len(signature) >= 3) and n == 2:
        element1= signature[0]
        element2 = signature[1]
        secondList = []
        add1 = secondList.append(element1)
        add2 = secondList.append(element2)
        return secondList
        sys.exit()


    if (len(signature) >= 3) and n == 3:
        elementt1= signature[0]
        elementt2 = signature[1]
        element3 = signature[2]
        thirdList = []
        add_1 = thirdList.append(elementt1)
        add_2 = thirdList.append(elementt2)
        add_3 = thirdList.append(element3)
        return thirdList
        sys.exit()



    count = len(signature) + 1
    newList = []

    first = signature[-3:]

    newList.append(first)

    add_ = sum(first)
    newList.append(add_)
    signature.append(add_)

    for i in signature:
      if count < n:
        first = signature[-3:]
        newList.append(first)

        add_ = sum(first)
        signature.append(add_)
        count += 1

    return signature

