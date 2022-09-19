import cv2
import numpy as np
import matplotlib.pylab as plt
from skimage import io

def negative_image(img):
  img = -1 * img * 255
  return img

def linear_transformation(img, g_min, g_max):
    f_min = min(img.flatten())
    f_max = max(img.flatten())

    a = (g_max - g_min) / (f_max - f_min)
    b = g_min

    img = img - f_min

    img_new = (a*img) + b

    return np.uint8(img_new)

def get_hist(img, limit):
    arr = img.flatten()
    hist = np.zeros(limit,dtype='int')
    for i in range(0, len(arr)):
        hist[arr[i]] +=1
    return hist

imgs = [
]

for i in enumerate(imgs):
  img = cv2.cvtColor(io.imread(i[1]), cv2.COLOR_BGR2RGB)
  fig, axs = plt.subplots(1, 2, constrained_layout=True)
  axs[0].set_title("Imagem Original")
  axs[1].set_title("Imagem Negativa")

  axs[0].set_xticks([])
  axs[0].set_yticks([])

  axs[1].set_xticks([])
  axs[1].set_yticks([])

  axs[0].imshow(img)
  axs[1].imshow(negative_image(img).astype(np.uint8))
  plt.show()

  h = get_hist(img, 256)

  plt.plot(range(len(h)), h)
  plt.show()

  if (i[0] == 1):
    plt.imshow(linear_transformation(img, 0, 255))
    plt.show()

    fig, axs = plt.subplots(1, 2, constrained_layout=True)
    h_tl = get_hist(linear_transformation(img, 0, 255), 256)
    axs[0].set_title("Histograma Transformação Linear")
    axs[0].set_xlabel("Intensidade")
    axs[0].set_ylabel("Quantidade de Pixels")
    axs[0].plot(range(len(h_tl)), h_tl)
    axs[0].set_xlim([0, 256])

    h_eq = cv2.equalizeHist(h_tl.astype(np.uint8))
    axs[1].set_title("Histograma Equalizado")
    axs[1].set_xlabel("Intensidade")
    axs[1].set_ylabel("Quantidade de Pixels")
    axs[1].hist(h_eq.ravel(), 256, [0,256])
    axs[1].set_xlim([0, 256])
    plt.show()