def hey(phrase):
    phrase = phrase.strip()
    if phrase == '':
        return 'Fine. Be that way!'
    elif phrase[-1] == '?' and not phrase.isupper():
        return 'Sure.'
    elif phrase[-1] == '?' and phrase.isupper():
        return 'Calm down, I know what I\'m doing!'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
