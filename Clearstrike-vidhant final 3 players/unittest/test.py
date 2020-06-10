import os,sys
parentPath = os.path.abspath("..")
# Setting path for accessing player.py
if parentPath not in sys.path:
    sys.path.insert(0,parentPath)
from test_carrom_board import TestCarromBoard
# calling the TestCarromBoard and test_creation
ob=TestCarromBoard()
ob.setUp()
ob.test_creation()
