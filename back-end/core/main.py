import os
import datetime
import cv2
import numpy as np
from core import process, predict

def c_main(path, model, ext):
    # 读取图像
    img = cv2.imread(path)
    # 直接使用模型进行预测
    results = model(img)
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

    # 保存预测结果图像
    img_with_boxes = img.copy()
    for box in pred_boxes:
        x1, y1, x2, y2, lbl, conf = box
        cv2.rectangle(img_with_boxes, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img_with_boxes, f'{lbl} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    pid = f'pred_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.{ext}'
    draw_path = os.path.join('./tmp/draw', pid)
    cv2.imwrite(draw_path, img_with_boxes)

    return pid, image_info


if __name__ == '__main__':
    pass