import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import shutil
from skimage import io
from skimage.filters import threshold_otsu, threshold_local
from skimage.morphology import closing, square, label
from skimage.segmentation import clear_border
from skimage.measure import regionprops
from skimage.color import label2rgb

plt.rcParams["figure.figsize"] = (15, 10)

imgs = [
]

for idx, i in enumerate(imgs):
  fig, axs = plt.subplots(ncols=3)
  img = cv2.cvtColor(cv2.cvtColor(io.imread(i), cv2.COLOR_BGR2RGB), cv2.COLOR_RGB2GRAY)
  axs[0].imshow(img, cmap="gray")
  axs[0].set_title("Original")

  thresholded = threshold_otsu(img)
  binarized = img > thresholded
  axs[1].imshow(binarized, cmap="gray")
  axs[1].set_title("Otsu")

  thresholded_local = threshold_local(img, 35, offset=10)
  binarized_local = img > thresholded_local
  axs[2].imshow(binarized_local, cmap="gray")
  axs[2].set_title("Local")
  plt.show()

  if (idx == 0):
    dilated = closing(binarized, square(5))
    cleared = clear_border(dilated)
    labelized = label(cleared)
    overlay = label2rgb(labelized, image=img, bg_label=0)
    plt.imshow(overlay, cmap="gray")

    for region in regionprops(labelized):
      if region.area >= 100:
        minr, minc,maxr,maxc = region.bbox
        rect = mpatches.Rectangle((minc,minr),maxc - minc, maxr - minr, fill=False, edgecolor='red',linewidth=2)
        plt.gca().add_patch(rect)
    plt.show()
  print("\u2550" * shutil.get_terminal_size().columns)