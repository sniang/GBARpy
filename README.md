# How to use the library

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

```python
#plot the image
fig1 = plt.figure(figsize=(5,5))
plt.imshow(pic.img)
fig1.savefig("fig_example_1.pdf")
```
![Example_1](example/fig_example_1.png)
```python
#plot the fit
fig2 = plt.figure(figsize=(5,5))
pic.plot_X_int()
pic.plot_Y_int()
fig2.savefig("fig_example_2.pdf")
```
![Example_2](example/fig_example_2.png)
```python
#plot all
pic.plot("fig_example_3.pdf","plot analysis")
```
![Example_3](example/fig_example_3.png)
