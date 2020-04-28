import cv2
import sys

#   灰度图转化为ndarray（利用OpenCV的imread函数）（灰度0~255,0黑\255白）
#   imread(const string\&filename, int flags=1)
#   _________________________________________________________________________
#   |   参数   | OpenCV2.X解释                           | OpenCV3.X解释    |
#   |----------|-----------------------------------------|------------------|
#   | filename | 图像文件名                              | 同2.X            |
#   |----------|-----------------------------------------|------------------|
#   | flags    | CV_LOAD_IMAGE_COLOR       ：彩色图像    | IMREAD_COLOR     |
#   |          | CV_LOAD_IMAGE_GREAYSCALE  ：灰度图像    | IMREAD_GRAYSCALE |
#   |          | CV_LOAD_IMAGE_ANYCOLOR    ：任意图像    | IMREAD_ANYCOLOR  |
#   -------------------------------------------------------------------------

if __name__ == "__main__":
    # 输入图像矩阵
    if len(sys.argv) > 1:
        img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
        # img2 = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
    else:
        print("Usge:python imgToArray.py imageFile")
    # 显示图像
    cv2.imshow("img", img)
    # cv2.imshow("img", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

