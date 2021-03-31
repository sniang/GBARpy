#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:52:32 2020

@author: sniang
"""

### Need to be adapted, depends on where you placed the file
### and the definition of the PATH
import GBARpy.MCPPicture as mcp
import matplotlib.pyplot as plt

"""

More details

"""

### Import the Picture
img = mcp.import_image("IMG0008.bmp")
fig4 = plt.figure(figsize=(5,5))
plt.imshow(img)
fig4.savefig("fig_example_4.pdf")
fig4.savefig("fig_example_4.png")


### Import the Picture and reshape
img = mcp.import_image("IMG0008.bmp",reshape=[1250,1000,600])
fig5 = plt.figure(figsize=(5,5))
plt.imshow(img)
fig5.savefig("fig_example_5.pdf")
fig5.savefig("fig_example_5.png")


### Integrals along the X and Y axis
Px,Ix = mcp.integrate_picture_along_X(img)
Py,Iy = mcp.integrate_picture_along_Y(img)
fig6 = plt.figure(figsize=(10,5))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.plot(Px,Ix)
plt.plot(Py,Iy)
fig6.savefig("fig_example_6.pdf")
fig6.savefig("fig_example_6.png")


### Fit of the integrals
poptX,perrX=mcp.fit_gaussian_offset_filtered(Px,Ix)
poptY,perrY=mcp.fit_gaussian_offset_filtered(Py,Iy)
fig7 = plt.figure(figsize=(5,5))
plt.plot(Px,Ix,'.',color='tab:red',ms=1)
plt.plot(Px,mcp.gaussian_offset(Px,*poptX),color='tab:red')
plt.plot(Py,Iy,'.',color='tab:blue',ms=1)
plt.plot(Py,mcp.gaussian_offset(Py,*poptY),color='tab:blue')
fig7.savefig("fig_example_7.pdf")
fig7.savefig("fig_example_7.png")
