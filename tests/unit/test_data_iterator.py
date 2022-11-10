"""Tests for iterating through a dir of image data and inserting data into a
useable variable
"""
import sys
import unittest
import numpy as np
import random as rndm
sys.path.append('./src/ippsra')
import data_iterator as di  # nopep8


class TestImageDirIter(unittest.TestCase):
    """Class to test an image iterator this function will iterate through a
    directory of images and return a list of useable data
    """
    @classmethod
    def setUpClass(cls):
        """setUpClass to include all of the needed data to test this
        function
        """
        cls.test_data_path = './data/test_data/'
        cls.wrong_path = './random/dir/DNE'  # A fake path
        

    @classmethod
    def tearDownClass(cls):
        """tearDownClass to remove all of the data that was setup in the
        setUpClass function
        """
        cls.test_data_path = None
        cls.wrong_path = None

    def test_dif_dir_data_iter(self):
        """Testing for OSError for missing directory and testing an output is
        given from a populated directory.
        """
        self.assertIsNotNone(di.data_iterator(self.test_data_path))
        with self.assertRaises(OSError):
            di.data_iterator(self.wrong_path)

    def test_correct_returns_data_iter(self):
        