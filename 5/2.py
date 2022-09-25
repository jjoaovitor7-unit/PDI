import cv2
import numpy as np
import matplotlib.pylab as plt
from PIL import Image, ImageFilter

plt.rcParams["figure.figsize"] = (10, 10)
img = cv2.imread("imgs/img01.jpg")

fig, axs = plt.subplots(1, 3, constrained_layout=True)
titles = ["Original", "Média", "Moda"]

imgs = [img, cv2.GaussianBlur(img, (9, 9), 0), Image.fromarray(img).filter(ImageFilter.ModeFilter)]
for i in range(0, len(imgs)):
  axs[i].set_xticks([])
  axs[i].set_yticks([])
  axs[i].set_title(titles[i])
  axs[i].imshow(imgs[i])
plt.show()

fig, axs = plt.subplots(1, 4, constrained_layout=True)
img_f = img.flatten()

prewitt_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewitt_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt = cv2.filter2D(img, -1, prewitt_x) + cv2.filter2D(img, -1, prewitt_y)

roberts_x = np.array([[0, 1], [-1, 0]]).flatten()
roberts_y = np.array([[1, 0], [0, -1]]).flatten()
roberts = np.sqrt(np.square(np.convolve(img_f, roberts_x, mode="same")) + np.square(np.convolve(img_f, roberts_y, mode="same")))
roberts = roberts.reshape(img.shape[0], img.shape[1], -1)

sobel = {
    "x": cv2.Sobel(img, cv2.CV_64F, 1, 0),
    "y": cv2.Sobel(img, cv2.CV_64F, 0, 1),
    "xy": cv2.Sobel(img, cv2.CV_64F, 1, 1)
}

titles = ["Original", "Ordem (Derivada de 1º Ordem)", "Prewitt", "Roberts"]
imgs = [img, sobel["xy"], prewitt, roberts]
for i in range(0, len(imgs)):
  axs[i].set_xticks([])
  axs[i].set_yticks([])
  axs[i].set_title(titles[i])
  axs[i].imshow(imgs[i])
plt.show()
