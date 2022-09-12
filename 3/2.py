import cv2
import matplotlib.pyplot as plt

plt.grid("on")
img = cv2.cvtColor(cv2.imread("imgs/img01.jpg"), cv2.COLOR_BGR2RGB)
h = get_hist(img, 256)
print(h)
plt.plot(range(len(h)), h)
plt.show()