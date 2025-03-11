import cv2
import numpy as np

def predict(image_data, model, file_ext):
    # 直接调用模型进行预测
    results = model(image_data)
    det = results[0].boxes.cpu().numpy()

    pred_boxes = []
    count = 0
    image_info = {}
    for box in det:
        x1, y1, x2, y2 = box.xyxy[0].astype(int)
        conf = box.conf[0]
        cls_id = int(box.cls[0])
        lbl = model.names[cls_id]
        pred_boxes.append((x1, y1, x2, y2, lbl, conf))
        count += 1
        key = '{}-{:02}'.format(lbl, count)
        image_info[key] = ['{}×{}'.format(x2 - x1, y2 - y1), np.round(float(conf), 3)]

    return image_info