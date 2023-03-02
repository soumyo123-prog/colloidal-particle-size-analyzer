import torch
import cv2
import math

model = torch.hub.load(
    'ultralytics/yolov5', 'custom',
    './models/500_images_variable_radius.pt', force_reload=True
)
im = './test_data/6.png'
results = model(im)
# results.show()

img = cv2.imread(im)
useful_results = results.xyxy[0].numpy()
for result in useful_results:
    xmin, ymin, xmax, ymax, confidence, clas = result
    x_centre = math.floor((xmin + xmax) / 2)
    y_centre = math.floor((ymin + ymax) / 2)
    radius = math.floor(min((xmax - xmin - 10)/2, (ymax - ymin - 10)/2))
    cv2.circle(img, (x_centre, y_centre), radius, (0, 255, 0), 2)

cv2.imshow('some', img)
cv2.waitKey(0)
