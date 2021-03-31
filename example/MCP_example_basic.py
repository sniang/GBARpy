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

# reshape analyse the beam spot
pic = mcp.BeamSpot("IMG0008.bmp",reshape=[1250,1000,600])
# the reshape array is a made of 3 elements: positionX, positionY, length (in pixel)
# if you don't want to reshape
pic = mcp.BeamSpot("IMG0008.bmp")

# The fit will fail is the reshaping is too important, see the result with
#pic = mcp.BeamSpot("IMG0008.bmp",reshape=[1250,1000,500])


#print the information relative to the fit
print(pic)


#plot the image
fig1 = plt.figure(figsize=(5,5))
plt.imshow(pic.img)
fig1.savefig("fig_example_1.pdf")
fig1.savefig("fig_example_1.png")


#plot the fit
fig2 = plt.figure(figsize=(5,5))
pic.plot_X_int()
pic.plot_Y_int()
fig2.savefig("fig_example_2.pdf")
fig2.savefig("fig_example_2.png")


#plot all
pic.plot("fig_example_3.pdf")
pic.plot("fig_example_3.png")

