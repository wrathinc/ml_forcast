# USAGE
# python detect_blur.py --images images

# import the necessary packages
from imutils import paths
import argparse
import cv2
import os, time 
import threading

start = time.time()

def create_folders():
    blurry_pics = "blury_photo"
    not_blurry_photo = "not_blurry"
    image_folder = "images"

    if not os.path.exists(blurry_pics):
        os.mkdir(blurry_pics)

    if not os.path.exists(not_blurry_photo):
        os.mkdir(not_blurry_photo)

    if not os.path.exists(image_folder):
        os.mkdir(image_folder)

create_folders()

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    print(time.time()-start)
    return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
    help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=10.0,
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
def imageloop():
    for imagePath in paths.list_images(args["images"]):
        start = time.time()
        # load the image, convert it to grayscale, and compute the
        # focus measure of the image using the Variance of Laplacian
        # method
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        dirpath = os.getcwd()

        if fm > args["threshold"]:
            cv2.imwrite(dirpath+"/not_blurry/test{}.jpg".format(fm),image)
            print(time.time()-start)
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
        if fm < args["threshold"]:
        #print("The Sorting hat says!!!! blurry")
            cv2.imwrite(dirpath+"/blury_photo/test{}.jpg".format(fm),image)
            print(time.time()-start)


imageloop()

print(time.time()-start)



