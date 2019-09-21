import cv2

def text2binary(string):
    output = ' '.join(format(ord(x), 'b') for x in string)
    return output

def image_to_binary(data):
    ret, bw_img = cv2.threshold(data,127,255,cv2.THRESH_BINARY)
    return bw_img
