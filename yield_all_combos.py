def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    for i in xrange(3**len(items)):
        bag1 = []
        bag2 = []
        temp = i
        for item in items:
            check = temp % 3
            if check == 1:
                bag1.append(item)
            elif check == 2:
                bag2.append(item)
            temp = temp / 3
        yield bag1, bag2

for combo in yieldAllCombos(['a', 'b', 'c']):
    print combo[0]