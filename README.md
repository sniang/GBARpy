# How to use the library

## Installation
## MCPpicture library
### Basic examples
The examples corresponds to the python scripts [MCP_example_basic.py](https://github.com/sniang/GBARpy/blob/3be859b67a0037ad0769b641c9f237496ce881ea/example/MCP_example_basic.py) and [MCP_example_small_functions.py](https://github.com/sniang/GBARpy/blob/3be859b67a0037ad0769b641c9f237496ce881ea/example/MCP_example_small_functions.py).

```python
# Import the library
import GBARpy.MCPPicture as mcp
import matplotlib.pyplot as plt
```
Let's see how to import a beam spot picture (you can try with the file []()):
```python
# reshape analyse the beam spot
pic = mcp.BeamSpot("IMG0008.bmp",reshape=[1250,1000,600])
# the reshape array is a made of 3 elements: positionX, positionY, length (in pixel)
# if you don't want to reshape
pic = mcp.BeamSpot("IMG0008.bmp")
```
With this minimal code, the picture is analysed and the parameters of the fit can be obtained usign ```print(img)```.
