#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:07:10 2020

@author: samuel.niang@cern.ch
"""

from GBARpy.Main_window import MainWindow
# Uncomment for edit mode
# from Main_window import MainWindow

message = """
  _|_|_|  _|_|_|      _|_|    _|_|_| 
_|        _|    _|  _|    _|  _|    _|
_|  _|_|  _|_|_|    _|_|_|_|  _|_|_| 
_|    _|  _|    _|  _|    _|  _|    _|
  _|_|_|  _|_|_|    _|    _|  _|    _|
  
--------------------------------------------------------------
Optimised for Python 3.9
Please report bugs on: https://github.com/sniang/GBARpy/issues
--------------------------------------------------------------

"""

print(message)
win = MainWindow()
win.mainloop()
win.quit()
