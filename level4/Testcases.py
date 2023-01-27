import pytest

from Level1.FileFinder import FileFinder
from Level1.find_Drives import  SystemDiverFinder

class Test_Drive:
    def __init__(self):
        pass

    def test_DriverCase(self):
        obj=SystemDiverFinder()
        self.expected=obj.find_drivers()
        self.actual=['C']
        assert self.expected==self.actual

    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo.txt','C:\\')
        self.expected_filename=d[0]
        self.actual_res='C:\\hcl1\\demo.txt'
        assert self.expected_filename==self.actual_res

