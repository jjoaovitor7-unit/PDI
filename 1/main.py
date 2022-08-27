# !pip install numpy pandas scikit-image matplotlib opencv-python scipy webcolors imageio

import cv2
from skimage.color import rgb2gray
from skimage.transform import resize, rotate
import matplotlib.pyplot as plt
import imageio
import numpy as np

from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)

# from google.colab.patches import cv2_imshow

for i in range(2, 5):
    print(f"\nimg0{i}.jpg")
    img = cv2.cvtColor(cv2.imread(f"imgs/img0{i}.jpg"), cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

    print(f"\nMatriz\n{img}")

    img_info = img.shape

    colors_aux = [[name, hex_to_rgb(hex)] for hex, name  in CSS3_HEX_TO_NAMES.items()]
    c_pixel = img[150, 150]
    kdt_db = KDTree([hex[1] for hex in colors_aux])
    distance, index = kdt_db.query(c_pixel)
    print(f"\nCor de um Pixel:\n{c_pixel} {colors_aux[index][0]}")

    # for j in range(img_info[0]):
    #   for k in range(img_info[1]):
    #     distance, index = kdt_db.query(img[j][k])
    #     print(img[j][k], colors_aux[index][0])

    print(f"\nAltura\n{img_info[0]}")
    print(f"\nLargura\n{img_info[1]}")
    print(f"\nCanais\n{img_info[2]}\n")

    print("Imagem (cinza)")
    gray = rgb2gray(img)
    plt.imshow(gray, cmap='gray')
    plt.show()

    print(f"\nMatriz (cinza)\n{gray}\n")

    print(f"[Máximo, Mínimo, Média] de pixels: [{img.max()}, {img.min()}, {img.mean()}]")

    print("\nImagem Redimensionada")
    resized = resize(img, (int(img_info[1]/2), int(img_info[0]/2)))
    plt.imshow(resized)
    plt.show()

    frames = []
    for l in [90, -90, 180]:
      frames.append(rotate(img, l, resize=True))

    print("\nImagem Rotacionada")
    writer = imageio.get_writer(f"imgrotate{i}.gif", mode="I")
    for idx, frame in enumerate(frames):
        plt.imshow(frame)
        plt.show()
        writer.append_data(frame.astype(np.uint8))
    writer.close()