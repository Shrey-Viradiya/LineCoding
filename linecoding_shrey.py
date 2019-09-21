from utilities import text2binary

def polarRZ(message):
    output = []
    for x in text2binary(message):
        if (x == '0'):
            output.append('-10')
        else:
            output.append('10')
    return output