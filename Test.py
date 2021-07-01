from __future__ import  absolute_import
import os

import ipdb
import matplotlib
from tqdm import tqdm

from utils.config import opt
from data.dataset import Dataset, TestDataset, inverse_normalize
from model import FasterRCNNVGG16
from torch.utils import data as data_
from trainer import FasterRCNNTrainer
from utils import array_tool as at
from utils.vis_tool import visdom_bbox
from utils.eval_tool import eval_detection_voc
from train import train, eval
import numpy as np

matplotlib.use('agg')

def eval_(dataloader, faster_rcnn, test_num=10000):
    pred_bboxes, pred_labels, pred_scores = list(), list(), list()
    gt_bboxes, gt_labels = list(), list()
    for ii, (imgs, sizes, gt_bboxes_, gt_labels_) in tqdm(enumerate(dataloader)):
        sizes = [sizes[0][0].item(), sizes[1][0].item()]
        pred_bboxes_, pred_labels_, pred_scores_ = faster_rcnn.predict(imgs, [sizes])
        gt_bboxes += list(gt_bboxes_.numpy())
        gt_labels += list(gt_labels_.numpy())
        # gt_difficults += list(gt_difficults_.numpy())
        pred_bboxes += pred_bboxes_
        pred_labels += pred_labels_
        pred_scores += pred_scores_
        if ii == test_num: break



def test() :
    print("Begin testing")
    print('load data')
    testset = TestDataset(opt)
    test_dataloader = data_.DataLoader(testset,
                                       batch_size=1,
                                       num_workers=opt.test_num_workers,
                                       shuffle=False, \
                                       pin_memory=False
                                       ) #shuffle=False
    faster_rcnn = FasterRCNNVGG16()
    print('model construct completed')
    tester = FasterRCNNTrainer(faster_rcnn).cuda()
    tester.load(opt.load_path)
    if opt.load_path:
        tester.load(opt.load_path)
        print('load pretrained model from %s' % opt.load_path)
    eval_result = eval(test_dataloader, faster_rcnn, test_num=opt.test_num)
    print(eval_result)


if __name__ == '__main__':
    test()
    
    # import fire

    # fire.Fire(test())