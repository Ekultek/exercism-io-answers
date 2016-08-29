def distance(strand1, strand2):
    difference = 0

    for char1, char2 in zip(strand1, strand2):
        if char1 != char2:
            difference += 1

    return difference



#distance('GGACGGATTCTG', 'AGGACGGATTCT')