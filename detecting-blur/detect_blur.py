# USAGE
# python detect_blur.py --images images

# import the necessary packages
from imutils import paths
import argparse
import cv2
import os, time 
from tqdm import tqdm

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
    help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,
    help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())
print("The Sorting hat of blurry images!")

print("""
               __  _                          
              / /_(_)___  _______  __         
             / __/ / __ \/ ___/ / / /         
            / /_/ / /_/ (__  ) /_/ /          
 ___________\__/_/ .___/____/\__, /___________
/_____/_____/   /_/         /____/_____/_____/
""")




# loop over the input images
for imagePath in paths.list_images(args["images"]):
    
    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    # method
    #print("The sorting hat is placed on the image!!")
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)

    if fm > args["threshold"]:
        cv2.imwrite("/home/mrrobot/Documents/ml_forcast/detecting-blur/notblurry/test{}.jpg".format(fm),image)
        for image in tqdm(range(1)):
            print("The Sorting hat says!!!! not blurry")
        #print("The Sorting hat says!!!! not blurry")
   
    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm < args["threshold"]:
        #print("The Sorting hat says!!!! blurry")
        cv2.imwrite("/home/mrrobot/Documents/ml_forcast/detecting-blur/bp/test{}.jpg".format(fm),image)
        for image in tqdm(range(1)):
            print("The Sorting hat says!!!! blurry")

    # for i in tqdm(range(len(imagePath))):
    #     time.sleep(.1)
print("""\n
               __  _                          
              / /_(_)___  _______  __         
             / __/ / __ \/ ___/ / / /         
            / /_/ / /_/ (__  ) /_/ /          
 ___________\__/_/ .___/____/\__, /___________
/_____/_____/   /_/         /____/_____/_____/\n
""")