# !pip install imageio numpy pandas opencv-python scikit-image matplotlib webcolors scipy

import cv2
from skimage.color import rgb2gray
from skimage.transform import resize, rotate
import matplotlib.pyplot as plt
import imageio

# from scipy.spatial import KDTree
# from webcolors import (
#     CSS3_HEX_TO_NAMES,
#     hex_to_rgb,
# )

# from google.colab.patches import cv2_imshow

for i in range(2, 5):
    print(f"\nimg0{i}.jpg")
    img = cv2.cvtColor(cv2.imread(f"imgs/img0{i}.jpg"), cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

    print(f"\nMatriz\n{img}")

    img_info = img.shape

    print(f"\nCor de um Pixel:\n{img[150, 150]}")

    # for j in range(img_info[0]):
    #   for k in range(img_info[1]):
    #     colors_aux = [[name, hex_to_rgb(hex)] for hex, name  in CSS3_HEX_TO_NAMES.items()]
    #     print(colors_aux)

    #     kdt_db = KDTree([hex[1] for hex in colors_aux])
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

    print(f"Máximo de pixels: {img.max()}")
    print(f"Mínimo de pixels: {img.min()}")
    print(f"Média de pixels: {img.mean()}")

    print("\nImagem Redimensionada")
    resized = resize(img, (int(img_info[1]/2), int(img_info[0]/2)))
    plt.imshow(resized)
    plt.show()

    frames = []

    for l in [90, -90, 180]:
      frames.append(rotate(img, l, resize=True))

    print("\nImagem rotacionada")
    writer = imageio.get_writer(f"imgrotate{i}.gif", mode="I")
    for idx, frame in enumerate(frames):
        plt.imshow(frame)
        plt.show()
        writer.append_data(frame)
    writer.close()
