## GBARpy.MCPPicture.MCPParams

#### `define_ratio(mm, pix)`

To define the ratio mm vs pixels.

- **`mm`** `float`

   A distance in mm.

- **`pix`** `float`

   The equivalent distance in pixels.

* Returns
   None

#### `check_ratio_is_set()`

To check is the ratio has been set.

* Returns
   result: boolean
True if the ratio has been set.

#### `check_all_set()`

To check is all has been set.

* Returns
   result: boolean
True if all the parameters have been set.

#### `save_conf(fname)`

To save the parameters of the MCP as a binary file (.mcp).

- **`fname`** `string`

   The name of the binary file.

* Returns
   None

*Examples
   ```python
params = MCPParams()
params.save_config("config.mcp")
```