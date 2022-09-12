import cv2
from skimage.color import rgb2gray
from skimage.transform import resize
import matplotlib.pyplot as plt
from PIL import Image

from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)

# import numpy as np
# from google.colab.patches import cv2_imshow

for i in range(2, 5):
    img_name = f"imgs/img0{i}.jpg"
    print(f"\n{img_name}")
    img = cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2RGB)
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

    print(f"\n(Altura, Largura, Canais) da imagem:\n{img_info}")

    print("\nImagem (cinza)")
    gray = rgb2gray(img)
    plt.imshow(gray, cmap='gray')
    plt.show()
    print(f"\nMatriz (cinza)\n{gray}\n")

    print(f"[Máximo, Mínimo, Média] de pixels: \n[{img.max()}, {img.min()}, {img.mean()}]")

    print("\nImagem Redimensionada")
    resized = resize(img, (int(img_info[1]/2), int(img_info[0]/2)))
    plt.imshow(resized)
    plt.show()

    print("\nImagem Rotacionada")
    frames = []
    for l in [90, -90, 180]:
      img_rotate = Image.fromarray(img).rotate(l, expand=True)
      plt.imshow(img_rotate)
      plt.show()
      frames.append(img_rotate)
    frames[0].save(f"img0{i}_rotate.gif", save_all=True, append_images=frames[1:], loop=0)
