import cv2
from skimage import io
import matplotlib.pyplot as plt

imgs = [
    "imgs/img04.jpg",
    "imgs/img05.jpg"
]

for i in imgs:
  plt.grid("on")
  img = cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2RGB)
  h = get_hist(img, 256)
  print(h)
  plt.plot(range(len(h)), h)
  plt.show()