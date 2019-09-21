def text2binary(string):
    output = ''.join(format(ord(x), 'b') for x in string)
    return output