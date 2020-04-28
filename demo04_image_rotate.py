#   旋转函数rotate(OpenCV3.X 新特性)：
#       cv2.rotate(ImputArray src, OutputArray dst, int rotateCode)
#       __________________________________________________________________________
#       |   参数     | 解释                                                      |
#       |------------|-----------------------------------------------------------|
#       | src        | 输入图像矩阵(单、多通道矩阵都可以)                        |
#       | dst        | 输入矩阵                                                  |
#       | rotateCode | ROTATE_90_CLOCKWISE: 顺时针旋转90°                       |
#       |            | ROTATE_180:          顺时针旋转180°                      |
#       |            | ROTATE_90_COUNTERCLOCKWISE: 顺时针旋转270°               |
#       --------------------------------------------------------------------------
#   虽然是图像矩阵旋转，但是不需要利用放射变换，只是行列互换的矩阵转置操作。
import cv2
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1], cv2.IMREAD_ANYCOLOR)
    else:
        print("Usage: python roate.py image")

    # 显示原图
    cv2.imshow("image", image)

    # 图像旋转：cv2.ROATE_180     cv2.ROTATE_90_COUNTERCLOCKWISE
    rImg1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    rImg2 = cv2.rotate(image, cv2.ROTATE_180)
    rImg3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # 显示旋转结果
    cv2.imshow("rImg1", rImg1)
    cv2.imshow("rImg2", rImg2)
    cv2.imshow("rImg3", rImg3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
