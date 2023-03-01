import cv2 as cv
import numpy as np
import random


for i in range(1, 21):
    img = np.zeros((500, 500), dtype=np.uint8)
    num_of_circles = random.randint(1, 10)
    # file = open('./train_data/labels/val/' + str(i) + '.txt', 'w')
    for j in range(1, num_of_circles + 1):
        center_x = random.randint(50, 450)
        center_y = random.randint(50, 450)
        cv.circle(img, (center_x, center_y), 50, (255, 255, 255), 2)
        # if j < num_of_circles:
        #     file.write(
        #         f'0 {center_x/500} {center_y/500} {110/500} {110/500}\n')
        # else:
        #     file.write(
        #         f'0 {center_x/500} {center_y/500} {110/500} {110/500}')
    # file.close()
    cv.imwrite('./test_data/' + str(i) + '.png', img)
