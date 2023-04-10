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


for i in range(1, 21):
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    num_of_circles = random.randint(5, 20)
    choosen_colors = []
    for j in range(1, num_of_circles + 1):
        radius = random.randint(20, 100)
        center_x = random.randint(radius, 500 - radius)
        center_y = random.randint(radius, 500 - radius)
        color = choose_unique_color(choosen_colors)
        choosen_colors.append(color)
        cv.circle(img, (center_x, center_y), radius, color, -1)
    cv.imwrite('./test_data/' + str(i) + '.png', img)
