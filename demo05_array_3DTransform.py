#   通过二维投影变换对此物体三维变换进行模型化，这就是专用的二维投影变换
#       [[x'],          [[a11, a12, a13],               [[x],
#        [y'],      =    [a21, a22, a23],       *        [y],
#        [z']]           [a31, a32, a33]]                [z]]
#
#       与用此方程计算仿射变换矩阵的函数 getAffineTransform 类似，OpenCV提供函数：
#           cv2.getPerspectiveTransform(src, dst)
#       不同的是这里需要输入四组对应的坐标变换，而不是三组，
#       dst和src分别是4*2的二维ndarry，每一行代表一个坐标，数据类型必须是float32，否则报错

import cv2
import numpy as np

src = np.array([[0, 0], [200, 0], [0, 200], [200, 200]], np.float32)
dst = np.array([[100, 20], [200, 20], [50, 70], [250, 70]], np.float32)
P = cv2.getPerspectiveTransform(src, dst)
print(P)
print(P.dtype)