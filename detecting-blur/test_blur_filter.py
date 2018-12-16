import unittest
import cv2
from blur_filter import blur_laplacian 
from detect_blur import imageSort, image_process

class testBlurFilter(unittest.TestCase):
    def test_blur(self):
        #self.assertAlmostEquals(blur_laplacian.laplacian(self))
        #self.assertSequenceEqual(blur_laplacian.laplacian.tolist(), blur_laplacian.laplacian.__dict__


        x = blur_laplacian.laplacian.__dict__
        print(x.)