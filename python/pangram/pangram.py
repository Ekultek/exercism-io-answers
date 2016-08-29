def is_pangram(sentence):
    data = split_sentence(sentence)
    item = check_for_letters(data)

    if item is True:
        return True
    else:
        return False


def split_sentence(sentence):
    return list(sentence)


def check_for_letters(new_list):
    chars = "abcdefghijklmnopqrstuvwxyz"
    count = 0

    for char in chars:
        if char.upper() in new_list or char.lower() in new_list:
            pass
        else:
            count += 1

    if count != 0:
        return False
    else:
        return True