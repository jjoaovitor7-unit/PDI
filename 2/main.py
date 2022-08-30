# !pip install numpy pandas scikit-image matplotlib opencv-python

from skimage import io
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def vizinhanca4(l, col):
    return [
        (l-1, col),
        (l, col-1),
        (l+1, col),
        (l, col+1)
    ]


def vizinhanca8(l, col):
    return vizinhanca4(l, col) + [
        (l-1, col-1),
        (l-1, col+1),
        (l+1, col-1),
        (l+1, col+1)
    ]

coords = [(5, 5), (50, 50), (100, 100), (200, 200), (250, 250)]
imgs = []

plt.rcParams["figure.figsize"] = (10, 8)

for img in imgs:
    _img = io.imread(img)
    plt.imshow(_img)
    plt.show()
    print()

    for i in coords:
        n1 = vizinhanca4(i[0], i[1])
        n2 = vizinhanca8(i[0], i[1])

        fig, axs = plt.subplots(2, 2, constrained_layout=True)
        fig.suptitle(f"Vizinhança 4 {i}")
        axs[0, 0].set_title(f"({n1[0][0]},{n1[0][1]})")
        axs[0, 1].set_title(f"({n1[1][0]},{n1[1][1]})")
        axs[1, 0].set_title(f"({n1[2][0]},{n1[2][1]})")
        axs[1, 1].set_title(f"({n1[3][0]},{n1[3][1]})")

        axs[0, 0].imshow(_img[n1[0][0]:(n1[0][0]+1), n1[0][1]:(n1[0][1]+1)])
        axs[0, 1].imshow(_img[n1[1][0]:(n1[1][0]+1), n1[1][1]:(n1[1][1]+1)])
        axs[1, 0].imshow(_img[n1[2][0]:(n1[2][0]+1), n1[2][1]:(n1[2][1]+1)])
        axs[1, 1].imshow(_img[n1[3][0]:(n1[3][0]+1), n1[3][1]:(n1[3][1]+1)])
        plt.show()
        print()

        fig, axs = plt.subplots(4, 2, constrained_layout=True)
        fig.suptitle(f"Vizinhança 8 {i}")
        axs[0, 0].set_title(f"({n2[0][0]},{n2[0][1]})")
        axs[0, 1].set_title(f"({n2[1][0]},{n2[1][1]})")
        axs[1, 0].set_title(f"({n2[2][0]},{n2[2][1]})")
        axs[1, 1].set_title(f"({n2[3][0]},{n2[3][1]})")
        axs[2, 0].set_title(f"({n2[4][0]},{n2[4][1]})")
        axs[2, 1].set_title(f"({n2[5][0]},{n2[5][1]})")
        axs[3, 0].set_title(f"({n2[6][0]},{n2[6][1]})")
        axs[3, 1].set_title(f"({n2[7][0]},{n2[7][1]})")

        axs[0, 0].imshow(_img[n2[0][0]:(n2[0][0]+1), n2[0][1]:(n2[0][1]+1)])
        axs[0, 1].imshow(_img[n2[1][0]:(n2[1][0]+1), n2[1][1]:(n2[1][1]+1)])
        axs[1, 0].imshow(_img[n2[2][0]:(n2[2][0]+1), n2[2][1]:(n2[2][1]+1)])
        axs[1, 1].imshow(_img[n2[3][0]:(n2[3][0]+1), n2[3][1]:(n2[3][1]+1)])
        axs[2, 0].imshow(_img[n2[4][0]:(n2[4][0]+1), n2[4][1]:(n2[4][1]+1)])
        axs[2, 1].imshow(_img[n2[5][0]:(n2[5][0]+1), n2[5][1]:(n2[5][1]+1)])
        axs[3, 0].imshow(_img[n2[6][0]:(n2[6][0]+1), n2[6][1]:(n2[6][1]+1)])
        axs[3, 1].imshow(_img[n2[7][0]:(n2[7][0]+1), n2[7][1]:(n2[7][1]+1)])
        plt.show()
        print()

    fig, axs = plt.subplots(1, 2, constrained_layout=True)
    # fig.suptitle("Ruído")
    axs[0].set_title("Com ruído")
    axs[1].set_title("Sem ruído")

    temp = np.asarray(_img)
    M = _img.shape[0]
    N = _img.shape[1]
    for j in range(0, M):
        values = random.sample(range(0, N), 10)
        for value in values:
            temp[j, value] = 0
    axs[0].imshow(temp)

    temp = cv2.medianBlur(temp, 5)
    axs[1].imshow(temp)

    plt.show()
    print()
