import unittest
import django.test
import os

class CommandTest(unittest.TestCase):
    
    def test_min_row_count(self):
        fin, fout = os.popen4('python manage.py statistic')
        
        n = len(fout.readlines())
        self.failUnless(n,5)
