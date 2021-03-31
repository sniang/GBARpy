#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:52:32 2020

@author: samuel.niang@cern.ch
"""

import GBARpy.MCPPicture as mcp
import matplotlib.pyplot as plt

"""
Basic elements
For more details use help(mcp)
"""

# analyse the beam spot
#pic = mcp.BeamSpot("IMG0008.bmp",reshape=[1250,1000,600])

# or if you don't want to reshape
pic = mcp.BeamSpot("IMG0008.bmp")

# The fit will fail is the reshaping is too important, see the result with
#pic = mcp.BeamSpot("IMG0008.bmp",reshape=[1250,1000,500])


#print the information relative to the fit
print(pic)


#plot the image
plt.figure()
plt.imshow(pic.img)


#plot the fit
plt.figure()
pic.plot_X_int()
pic.plot_Y_int()


#plot all
pic.plot()

