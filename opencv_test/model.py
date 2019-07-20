
import cv2

class LenaModel:
    def __init__(self):
        self.fname ='./data'

    def execute(self):
        """
        https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html
        """
        print('cv2 버전:'%cv2.__version__)
        original = cv2.imread(self.fname,cv2.IMREAD_COLOR)
        gray = cv2.imread(self.fname, cv2.IMREAD_GRAYSCALE)

        unchanged = cv2.imread(self.fname. cv2.IMREAD_UNCHANGED)
        """
       이미지 읽기에는 위 3가지 속성값이 있습니다.
       대신에 1,0,-1을 사용해도 됨 
       """

        cv2.imshow('Original',original)
        cv2.imshow('Gray', gray)
        cv2.imshow('Unchange', unchanged)
        cv2.waitkey(0)





