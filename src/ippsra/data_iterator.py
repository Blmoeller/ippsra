"""Script to iterate through a directory of data and input the images into
a useable array
"""
import os
import cv2
import glob


imageDir = './data/test_data/'  # Dir for the test dataset
ext = ['png', 'jpg']  # Different image formats

def data_iterator(imageDir, ext = ['png', 'jpg']):
    """Function to iterate through a directory of image data

    Args:
        imageDir (str): Directory for the dataset.
        ext (list, optional): Different image formats to check for. Defaults
        to ['png', 'jpg'].
    """
    # Checking if the directory exists
    if os.path.exists(imageDir) == False:
        raise OSError("This directory is empty")
    # Checking if the dir is empty or not
    if len(imageDir) == 0:
        raise OSError("This directory is empty")

    images = []  # Setting up a list to add image data to
    [images.extend(glob.glob(imageDir + '*.' + e)) for e in ext]

    images = [cv2.imread(file) for file in images]

    return images
