import unittest
import numpy as np
import pandas as pd
import numpy.testing as np_testing
import pandas.testing as pd_testing
import os
import import_ipynb


class Test(unittest.TestCase):

    def _dirname_if_file(self, filename):
        if os.path.isdir(filename):
            return filename
        else:
            return os.path.dirname(os.path.abspath(filename))

    def setUp(self):    
        import Exercise1_02_codeExtension.ipynb
        self.activity = Exercise1_02_codeExtension
       
        self.tips = pd.read_csv('tips.csv')

        
    def test_input_frames(self):
        pd_testing.assert_frame_equal(self.activity.tips, self.tips)


if __name__ == '__main__':
    unittest.main()