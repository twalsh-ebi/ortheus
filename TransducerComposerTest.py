#!/usr/bin/env python3

#Copyright (C) 2008-2011 by Benedict Paten (benedictpaten@gmail.com)
#
#Released under the MIT license, see LICENSE.txt

import unittest
import os

from TransducerComposer import parseInputTransducerFile
from TransducerComposer import mainScript

class TestCase(unittest.TestCase):
    
    def setUp(self):
        test_script_file_path = os.path.realpath(__file__)
        test_script_dir_path = os.path.dirname(test_script_file_path)
        self.rootPath = os.path.join(test_script_dir_path, "models")
        unittest.TestCase.setUp(self)
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testParseInputTransducerFile(self):
        inputFile = self.rootPath + "/affineModel.sxpr"
        branchTransducerX, branchTransducerZ, rootTransducer = parseInputTransducerFile(inputFile)
        branchTransducerX.report()
        branchTransducerZ.report()
        rootTransducer.report()
        
    def testMainScript(self):
        inputFile1 = self.rootPath + "/affineModel.sxpr"
        outputFile = self.rootPath + "/temp.otra"
        outputDotFile = self.rootPath + "/temp.dot"
        mainScript(inputFile1, outputFile, outputDotFile)
        
        inputFile1 = self.rootPath + "/geometric_parent.sxpr"
        mainScript(inputFile1, outputFile, outputDotFile)
        
        inputFile1 = self.rootPath + "/doubleAffineModel.sxpr"
        mainScript(inputFile1, outputFile, outputDotFile)
        
        #Remove outputFile
        os.remove(outputFile)
        os.remove(outputDotFile)
     
if __name__ == '__main__':
    unittest.main()