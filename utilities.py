# import cv2

def text2binary(string):
    """
    Converts text to binary string.
    >>> text = 'Hello'
    >>> binary_text = text2binary(text)
    >>> print(binary_text)
    '10010001100101110110011011001101111'
    """

    # creates a list of binary representation of each character
    # and joins the list to create full binary string
    output = ''.join('{0:08b}'.format(ord(x), 'b') for x in string)
    return output

def image_to_binary(data):
    """
    Converts an grayscale image to binary string.
    >>> import cv2
    >>> from utilities import *
    >>> data = cv2.imread("small_image.png", 2)
    >>> data.shape
    (11, 12)
    >>> binary_string = image_to_binary(data)
    >>> print(binary_string)
    000000011...0000000
    """

    # threshold to remove outliers
    ret, bw_img = cv2.threshold(data,127,255,cv2.THRESH_BINARY)

    # result string to store binary representation of each pixel as string
    img_str = ''

    # convert every pixel to binary string and adds them to result string
    for i in range(bw_img.shape[0]):
        for j in range(bw_img.shape[1]):
            # create and append a constant length binary string of the pixel
            img_str += '{0:07b}'.format(bw_img[i][j])
    return img_str