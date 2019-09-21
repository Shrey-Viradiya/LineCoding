import cv2

def text2binary(string):
    output = ''.join(format(ord(x), 'b') for x in string)
    return output

def image_to_binary(data):
    ret, bw_img = cv2.threshold(data,127,255,cv2.THRESH_BINARY)
    img_str = ''
    for i in range(bw_img.shape[0]):
        for j in range(bw_img.shape[1]):
            img_str += '{0:07b}'.format(bw_img[i][j])
    return img_str