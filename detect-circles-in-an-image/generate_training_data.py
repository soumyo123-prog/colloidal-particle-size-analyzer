import cv2 as cv
import numpy as np
import random

# x_center = 60
# y_center = 60
# x_centers = []
# y_centers = []

# for i in range(0, 30):
#     x_centers.append(x_center)
#     y_centers.append(y_center)
#     x_center += 10
#     y_center += 10

for i in range(131, 191):
    img = np.zeros((500, 500), dtype=np.uint8)
    num_of_circles = random.randint(5, 20)
    file = open('./train_data/labels/val/' + str(i) + '.txt', 'w')
    for j in range(1, num_of_circles + 1):
        radius = random.randint(20, 100)
        center_x = random.randint(radius, 500 - radius)
        center_y = random.randint(radius, 500 - radius)
        cv.circle(img, (center_x, center_y), radius, (255, 255, 255), 2)
        if j < num_of_circles:
            file.write(
                f'0 {center_x/500} {center_y/500} {(radius * 2 + 10)/500} {(radius * 2 + 10)/500}\n')
        else:
            file.write(
                f'0 {center_x/500} {center_y/500} {(radius * 2 + 10)/500} {(radius * 2 + 10)/500}')
    file.close()
    cv.imwrite('./train_data/images/val/' + str(i) + '.png', img)
