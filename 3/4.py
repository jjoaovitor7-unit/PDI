import cv2
from skimage import io
import matplotlib.pyplot as plt

imgs = [
    "imgs/img01.jpg",
    "imgs/img06.jpg"
]

for i in imgs:
  img = cv2.cvtColor(io.imread(i), cv2.COLOR_BGR2RGB)
  h = get_hist(img, 256)
  h_oc = cv2.calcHist([img], [0], None, [256], [0, 256])
  print(h)

  fig, axs = plt.subplots(1, 2, constrained_layout=True)
  axs[0].set_title("get_histograma()")
  axs[1].set_title("calcHist()")

  axs[0].grid("on")
  axs[1].grid("on")

  axs[0].set_xlim([0, 256])
  axs[1].set_xlim([0, 256])

  axs[0].plot(range(len(h)), h)
  axs[1].plot(h_oc)
  plt.show()