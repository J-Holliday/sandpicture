import cv2
import numpy as np

class ImageRecognizer(object):
    
    def __init__(self, path, size=-1):
        self.img = self.read(path, size=size)
    
    def read(self, path, size=-1):
        
        img = cv2.imread(path)
        if not size == -1:
            img = cv2.resize(img, (size[0], size[1]))
            
        return img
    
    def countRGB(self):
        rgb = [0 for i in range(3)]
        
        for r in range(len(self.img)):
            for c in range(len(self.img[r])):
                for color in range(3):
                    rgb[color] += self.img[r][c][color]
                    
        return rgb
    
if __name__ == "__main__":
    im = ImageRecognizer("IMG_5845.jpg", size=(28, 28))
    im.countRGB()