from PIL import Image
import numpy as np
from csvReader import get_user_list
from matplotlib import pyplot as plt
import cv2


num = 0
imageList = get_user_list()
for image in imageList:
    target = np.asarray(np.split(np.asarray(image),48))
    plt.imshow(target, cmap='gray',interpolation="bicubic", vmin=0, vmax=255)
    plt.savefig("./images/No. " + str(num) + ".png", dpi = 113)
    num += 1
    # plt.show()





