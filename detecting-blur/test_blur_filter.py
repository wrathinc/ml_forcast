import unittest
import cv2
from blur_filter import blur_laplacian 
from detect_blur import imageSort, image_process

class testBlurFilter(unittest.TestCase):
    def test_blur(self):
        self.assertAlmostEquals(blur_laplacian.laplacian(self))
