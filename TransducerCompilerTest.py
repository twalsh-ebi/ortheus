#!/usr/bin/env python3

#Copyright (C) 2008-2011 by Benedict Paten (benedictpaten@gmail.com)
#
#Released under the MIT license, see LICENSE.txt

import unittest
import os

from TransducerCompiler import compileTransducerToCCode

class TestCase(unittest.TestCase):
    
    def setUp(self):
        test_script_file_path = os.path.realpath(__file__)
        test_script_dir_path = os.path.dirname(test_script_file_path)
        self.rootPath = os.path.join(test_script_dir_path, "models")
        unittest.TestCase.setUp(self)
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testCompileTransducer(self):
        inputFile = self.rootPath + "/affineModel.otra"
        outputCFile = self.rootPath + "/affineModel.c"
        outputHFile = self.rootPath + "/affineModel.h"
        compileTransducerToCCode(inputFile, outputCFile, outputHFile)
        #Remove outputFile
        os.remove(outputCFile)
        os.remove(outputHFile)
        
if __name__ == '__main__':
    unittest.main()