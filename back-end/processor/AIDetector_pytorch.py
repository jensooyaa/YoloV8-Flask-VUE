import cv2
import numpy as np
import logging
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords, letterbox
from utils.torch_utils import select_device
from random import randint

logging.basicConfig(level=logging.INFO)


class Detector(object):

   # 初始化模型
    def __init__(self):
        self.img_size = 640
        self.threshold = 0.4
        self.max_frame = 160
        try:
            self.init_model()
        except Exception as e:
            logging.error(f"Model initialization failed: {e}")
   # 加载预训练模型
    def init_model(self):
        self.weights = 'weights/best.pt'
        self.device = '0' if torch.cuda.is_available() else 'cpu'
        self.device = select_device(self.device)
        model = attempt_load(self.weights, map_location=self.device)
        model.to(self.device).eval()
        model.half()
        self.m = model
        self.names = model.module.names if hasattr(
            model, 'module') else model.names
        self.colors = [
            (randint(0, 255), randint(0, 255), randint(0, 255)) for _ in self.names
        ]
        logging.info("Model initialized successfully.")
# 预处理 调整大小 通道转化 归一化
    def preprocess(self, img):
        try:
            img0 = img.copy()
            img = letterbox(img, new_shape=self.img_size)[0]
            img = img[:, :, ::-1].transpose(2, 0, 1)
            img = np.ascontiguousarray(img)
            img = torch.from_numpy(img).to(self.device)
            img = img.half()  # 半精度
            img /= 255.0  # 图像归一化
            if img.ndimension() == 3:
                img = img.unsqueeze(0)
            return img0, img
        except Exception as e:
            logging.error(f"Image preprocessing failed: {e}")
            return None, None
# 绘制目标边界框 添加类别和置信度
    def plot_bboxes(self, image, bboxes, line_thickness=None):
        tl = line_thickness or round(
            0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
        for (x1, y1, x2, y2, cls_id, conf) in bboxes:
            color = self.colors[self.names.index(cls_id)]
            c1, c2 = (x1, y1), (x2, y2)
            cv2.rectangle(image, c1, c2, color,
                          thickness=tl, lineType=cv2.LINE_AA)
            tf = max(tl - 1, 1)  # font thickness
            t_size = cv2.getTextSize(
                cls_id, 0, fontScale=tl / 3, thickness=tf)[0]
            c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
            cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
            cv2.putText(image, '{} ID-{:.2f}'.format(cls_id, conf), (c1[0], c1[1] - 2), 0, tl / 3,
                        [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        return image
# 执行目标检测任务
    def detect(self, im):
        try:
            im0, img = self.preprocess(im)
            if im0 is None or img is None:
                return im, {}
            pred = self.m(img, augment=False)[0]
            pred = pred.float()
            pred = non_max_suppression(pred, self.threshold, 0.3)

            pred_boxes = []
            image_info = {}
            count = 0
            for det in pred:
                if det is not None and len(det):
                    det[:, :4] = scale_coords(
                        img.shape[2:], det[:, :4], im0.shape).round()

                    for *x, conf, cls_id in det:
                        lbl = self.names[int(cls_id)]
                        x1, y1 = int(x[0]), int(x[1])
                        x2, y2 = int(x[2]), int(x[3])
                        pred_boxes.append(
                            (x1, y1, x2, y2, lbl, conf))
                        count += 1
                        key = '{}-{:02}'.format(lbl, count)
                        image_info[key] = ['{}×{}'.format(
                            x2 - x1, y2 - y1), np.round(float(conf), 3)]

            im = self.plot_bboxes(im, pred_boxes)
            return im, image_info
        except Exception as e:
            logging.error(f"Object detection failed: {e}")
            return im, {}
