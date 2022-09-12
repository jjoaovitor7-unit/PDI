import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("imgs/img02.jpg"), cv2.COLOR_BGR2RGB)
_img = np.zeros(img.shape, dtype="uint8")

cv2.rectangle(_img, pt1=(180,240), pt2=(250,310), color=(0,255,0), thickness=5)
cv2.circle(_img, center=(420,275), radius=39, color=(255,255,0), thickness=5)

# plt.imshow(cv2.bitwise_or(img, _img))
plt.imshow(cv2.bitwise_xor(img, _img))
plt.show()