## GBARpy.MCPPicture.FitInterface

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

