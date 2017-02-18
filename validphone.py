import re

def telephone_check(num):
    pattern = '^1?\s?[(]?[0-9]{3}[-,)]?\s?[0-9]{3}[-,\s]?[0-9]{4}$'
    if re.match(pattern,num):
        return True

    return False


if __name__ == "__main__":
    print 'Enter a telephone number to check: '
    num = raw_input()
    valid = telephone_check(num)
    pass
