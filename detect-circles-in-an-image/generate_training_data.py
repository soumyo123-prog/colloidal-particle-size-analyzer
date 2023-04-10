import cv2 as cv
import numpy as np
import random


def choose_unique_color(choosen_colors):
    while True:
        r = random.randint(10, 255)
        g = random.randint(10, 255)
        b = random.randint(10, 255)
        color = (r, g, b)
        found_unique_color = True
        for choosen_color in choosen_colors:
            if (
                choosen_color[0] == r and
                choosen_color[1] == g and
                choosen_color[2] == b
            ):
                found_unique_color = False
                break
        if found_unique_color:
            return color


for i in range(291, 401):
    img = np.full((500, 500, 3), 255, dtype=np.uint8)
    num_of_circles = random.randint(5, 20)
    file = open('./train_data/labels/val/' + str(i) + '.txt', 'w')
    # choosen_colors = []
    for j in range(1, num_of_circles + 1):
        radius = random.randint(20, 100)
        center_x = random.randint(radius, 500 - radius)
        center_y = random.randint(radius, 500 - radius)
        color = (0, 0, 0)
        # color = choose_unique_color(choosen_colors)
        # choosen_colors.append(color)
        cv.circle(img, (center_x, center_y), radius, color, 3)
        if j < num_of_circles:
            file.write(
                f'0 {center_x/500} {center_y/500} {(radius * 2 + 10)/500} {(radius * 2 + 10)/500}\n')
        else:
            file.write(
                f'0 {center_x/500} {center_y/500} {(radius * 2 + 10)/500} {(radius * 2 + 10)/500}')
    file.close()
    cv.imwrite('./train_data/images/val/' + str(i) + '.png', img)
