from utilities import *
import cv2 

img = cv2.imread('small_image.png', 2)
bw_img = image_to_binary(img)
cv2.imshow("binary image", bw_img)
print(bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
