import os
import torch as t
from utils.config import opt
from model import FasterRCNNVGG16
from trainer import FasterRCNNTrainer
from data.util import  read_image
from utils.vis_tool import vis_bbox
from utils import array_tool as at
from train import train
from Test import test

# train()

# test()

faster_rcnn = FasterRCNNVGG16()
trainer = FasterRCNNTrainer(faster_rcnn).cuda()

trainer.load(opt.load_path)
demo_path = 'demo'
img_list = os.listdir(demo_path)
imgs = list()
for filename in img_list:
    img = read_image(demo_path + '/' + filename, color=True)
    img = t.from_numpy(img)
    imgs.append(img)
_bboxes, _labels, _scores = trainer.faster_rcnn.predict(imgs, visualize=True)
# print(_bboxes, _labels, _scores)
for i in range(len(imgs)):
    vis_bbox(at.tonumpy(imgs[i]),
            at.tonumpy(_bboxes[i]),
            at.tonumpy(_labels[i]).reshape(-1),
            at.tonumpy(_scores[i]).reshape(-1))