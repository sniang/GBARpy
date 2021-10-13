## GBARpy.MCPPicture.BeamSpot

#### `plot_y_int(label="")`

To plot the integral of the picture along the y-axis.

- **`label`** `str` `default=""`

   (optional) the label of the plot.

##### Returns
   None

* Examples
```python3
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_Y_int("Integral along the x-axis")
```

#### `plot_x_int(label="")`

To plot the integral of the picture along the x-axis.

- **`label`** `str` `default=""`

   (optional) the label of the plot.

##### Returns
   None

* Examples
```python3
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_X_int("Integral along the x-axis")
```

#### `plot_x_int_revert()`

Reverse & plot the integral along the x-axis.

##### Returns
   None

* Examples
```python
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_X_int("Integral along the x-axis")
```

#### `plot(fname="", figsize=(12, 10), fontsize=12, ftsizeticks=12)`

To plot the picture and the analysis.

- **`fname`** `string` `default=""`

   (optional) the name of the file to save the plot.

- **`figsize`** `(float` `float)` `default=(12` `10)`

   (optional) (size in inch X, Y) size of the figure.

- **`fontsize`** `int ` `default=12`

   (optional) size of the font.

- **`ftsizeticks`** `int ` `default=12`

   (optional) size of the ticks' font.

##### Returns
   fig: matplotlib.pyplot.Figure
the figure

* Examples
```python
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
fig = bs.plot("analysis.pdf")

fig = bs.plot()
fig.savefig("analysis.pdf")
```

#### `do_fit(x1, y1, x2=[], y2=[], p0=None)`

To do the fit y = f(x).

- **`x1`** `array of float`

   the first x input data
- **`y1`** `array of float`

   the first y input data
- **`x2`** `array of float` `optional`

   the second x input data
- **`y2`** `array of float` `optional`

   the second y input data
- **`p0`** `array of floats`

   the guessed parameters to help the fit

##### Returns
   None.

#### `do_fit(x1, y1, x2, y2)`

To do the fit y = f(x).

- **`x1`** `float[]`

   the first x input data.

- **`y1`** `float[]`

   the first y input data.

- **`x2`** `float[]`

   the second x input data.

- **`y2`** `float[]`

   the second y input data.

##### Returns
   None

#### `do_fit(x1, y1, x2, y2)`

To do the fit y = f(x).

- **`x1`** `float[]`

   the first x input data.

- **`y1`** `float[]`

   the first y input data.

- **`x2`** `float[]`

   the second x input data.

- **`y2`** `float[]`

   the second y input data.

##### Returns
   None


#### `define_ratio(mm, pix)`

To define the ratio mm vs pixels.

- **`mm`** `float`

   A distance in mm.

- **`pix`** `float`

   The equivalent distance in pixels.

##### Returns
   None

#### `check_ratio_is_set()`

To check is the ratio has been set.

##### Returns
   result: boolean
True if the ratio has been set.

#### `check_all_set()`

To check is all has been set.

##### Returns
   result: boolean
True if all the parameters have been set.

#### `save_conf(fname)`

To save the parameters of the MCP as a binary file (.mcp).

- **`fname`** `string`

   The name of the binary file.

##### Returns
   None

* Examples
```python
params = MCPParams()
params.save_config("config.mcp")
```

