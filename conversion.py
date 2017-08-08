import numpy as np
from csvReader import get_user_list
from matplotlib import pyplot as plt

newStart = 15000 #the picture number you want to start with
num = 0
imageList = get_user_list()
for image in imageList:
	if num <= newStart:
		num += 1
		continue
    target = np.asarray(np.split(np.asarray(image),48))
    plt.imshow(target, cmap='gray',interpolation="bicubic", vmin=0, vmax=255)
    plt.savefig("./images/No. " + str(num) + ".png", dpi = 113)
    num += 1
    # plt.show()





