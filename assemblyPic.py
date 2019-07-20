import os

import numpy as np
import cv2

"""A tool for HackMIT 2019, problem 5."""


DATA_DIR = "data/"
id_list = list(range(0,760))
ans_id = []
for id in id_list:
    image = cv2.imread("data/shard-{}.png".format(id))
    flag = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r, g, b = image[i][j]
            if (r==0 and g==0 and b==0) or (r==255 and g==255 and b==255):
                flag=1
                break
    if flag==1:
        ans_id.append(id)

print(ans_id)
print(len(ans_id))
for id in ans_id:
    os.system("cp data/shard-{}.png useful/shard-{}.png".format(id, id))


