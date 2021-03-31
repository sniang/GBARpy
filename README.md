# How to use the library

This library is made to work with python 3.
## Table of Contents
* [Installation](#installation)
* [MCPpicture library](#mcppicture-library)
    * [Basic code for an analysis](#basic-code-for-an-analysis)
    * [More examples](#more-examples)
    
## Installation


## MCPpicture library
### Basic code for an analysis
The examples corresponds to the python scripts [MCP_example_basic.py](https://github.com/sniang/GBARpy/blob/3be859b67a0037ad0769b641c9f237496ce881ea/example/MCP_example_basic.py) and [MCP_example_small_functions.py](https://github.com/sniang/GBARpy/blob/3be859b67a0037ad0769b641c9f237496ce881ea/example/MCP_example_small_functions.py).

```python
# Import the library
import GBARpy.MCPPicture as mcp
import matplotlib.pyplot as plt
```
Let's see how to import a beam spot picture (you can try with the file [IMG0008.bmp](https://github.com/sniang/GBARpy/blob/c71caf96d084198b507d1d23e0e8ee9dba43295b/example/IMG0008.bmp)):
```python
# reshape analyse the beam spot
pic = mcp.BeamSpot("IMG0008.bmp",reshape=[1250,1000,600])
# the reshape array is a made of 3 elements: positionX, positionY, length (in pixel)
# if you don't want to reshape
pic = mcp.BeamSpot("IMG0008.bmp")
```
With this minimal code, the picture is analysed and the parameters of the fit can be obtained usign ```print(img)```.
If it then possible to see and save the pictures as in the following example:
```python
#plot the image
fig1 = plt.figure(figsize=(5,5))
plt.imshow(pic.img)
fig1.savefig("fig_example_1.pdf")
```
Even if it can be written manually, there are line codes to plot the intgrals along the x-axis and the y-axis:
![Example_1](example/fig_example_1.png)
```python
#plot the fit
fig2 = plt.figure(figsize=(5,5))
pic.plot_X_int()
pic.plot_Y_int()
fig2.savefig("fig_example_2.pdf")
```
![Example_2](example/fig_example_2.png)

or to plot a summary of the fit:
```python
#plot all
pic.plot("fig_example_3.pdf")
```
![Example_3](example/fig_example_3.png)
### More examples
To import the required librairies for the following examples:
```python
# Import the library
import GBARpy.MCPPicture as mcp
import matplotlib.pyplot as plt
```

For some reasons, you might desire to import the picture without analysing it:
```python
### Import the Picture
img = mcp.import_image("IMG0008.bmp")
fig4 = plt.figure(figsize=(5,5))
plt.imshow(img)
fig4.savefig("fig_example_4.png")
```
![Example_4](example/fig_example_4.png)
```python
### Import the Picture and reshape
img = mcp.import_image("IMG0008.bmp",reshape=[1250,1000,600])
fig5 = plt.figure(figsize=(5,5))
plt.imshow(img)
fig5.savefig("fig_example_5.png")
```
![Example_5](example/fig_example_5.png)

Once the pictures imported as a 2D array, it it possible to get the integrals along the x or y axis
```python
### Integrals along the X and Y axis
Px,Ix = mcp.integrate_picture_along_X(img)
Py,Iy = mcp.integrate_picture_along_Y(img)
fig6 = plt.figure(figsize=(10,5))
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.plot(Px,Ix)
plt.plot(Py,Iy)
fig6.savefig("fig_example_6.png")
```
![Example_6](example/fig_example_6.png)

and then, using the fit function defined in the library
```python
### Fit of the integrals
poptX,perrX=mcp.fit_gaussian_offset_filtered(Px,Ix)
poptY,perrY=mcp.fit_gaussian_offset_filtered(Py,Iy)
fig7 = plt.figure(figsize=(5,5))
plt.plot(Px,Ix,'.',color='tab:red',ms=1)
plt.plot(Px,mcp.gaussian_offset(Px,*poptX),color='tab:red')
plt.plot(Py,Iy,'.',color='tab:blue',ms=1)
plt.plot(Py,mcp.gaussian_offset(Py,*poptY),color='tab:blue')
fig7.savefig("fig_example_7.png")
```
![Example_7](example/fig_example_7.png)
