import torch

model = torch.hub.load(
    'ultralytics/yolov5', 'custom',
    './models/100_images_black_bg_white_border_circle.pt', force_reload=True
)
im = './test_data/6.png'
results = model(im)
results.show()
