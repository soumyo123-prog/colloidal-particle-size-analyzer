import cv2 as cv
import numpy as np
import random


for i in range(1, 21):
    img = np.zeros((500, 500), dtype=np.uint8)
    num_of_circles = random.randint(5, 20)
    for j in range(1, num_of_circles + 1):
        radius = random.randint(20, 100)
        center_x = random.randint(radius, 500 - radius)
        center_y = random.randint(radius, 500 - radius)
        cv.circle(img, (center_x, center_y), radius, (255, 255, 255), 2)
    cv.imwrite('./test_data/' + str(i) + '.png', img)
