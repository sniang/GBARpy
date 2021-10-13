## Other functions

#### `fit_gaussian_offset_filtered(x, y)`

Fit with the function gaussian_offset.

- **`x`** `np.array(float[])`

   x-coordinates.

- **`y`** `np.array(float[])`

   y-coordinates.

##### Returns
   popt,perr: np.array(float[]), np.array(float[])
The parameters and the error of the fit.

#### `gaussian_offset(x, a, x0, s0, c)`

Gaussian distribution with an offset.

- **`x`** `numpy.array(float[])`

   The input.

- **`a`** `float`

   The amplitude.

- **`x0`** `float`

   The standard deviation.

- **`s0`** `float`

   The mean value, center of the distribution.

- **`c`** `float`

   The offset.

##### Returns
   - **`result`** `numpy.array(float[])`

The value of the distribution.

#### `gaussian(x, a, x0, s0)`

Gaussian distribution.

f(x) = amplitude/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2)

- **`x`** `numpy.array(float[])`

   The input.

- **`a`** `float`

   The amplitude.

- **`x0`** `float`

   The standard deviation.

- **`s0`** `float`

   The mean value, center of the distribution.

##### Returns
   - **`result`** `numpy.array(float[])`

The value of the distribution.

#### `get_index_str(n, i)`

To convert an int 'i' to a string.

- **`n`** `int`

   Order to put 0 if necessary.

- **`i`** `int`

   The number to convert.

##### Returns
   - **`res`** `str`

The number as a string.

* Examples
```python
getIndexStr(100,15)
```

Out:

```
'015'
```

#### `import_config(fname)`

To import the MCP parameters from a binary file.

- **`fname`** `str`

   The file's name.

##### Returns
   - **`mcpp`** `GBARpy.MCPPicture.MCPParams`

The MCP parameters.

#### `import_image(fname, reshape=[])`

To import the picture as an array.

- **`fname`** `string`

   Name of the file.

- **`reshape`** `int[3] or int[4]`

   [ix,iy,l] to reshape the picture as a square
or [x1,x2,y1,y2] to reshape as a rectangle.

##### Returns
   - **`img`** `np.array(float[float[])`

The picture as 2D array.

#### `integrate_picture_along_x(img)`

To integrate the picture along th X axis.

- **`img`** `numpy.array(float[float[]])`

   Image as a 2D numpy array.

##### Returns
   - **`(pix,integral)`** `(numpy.array(int[]),numpy.array(float[]))`

A tuple with pix the pixel numbers as a numpy array
and 'integral' the integral as a numpy array.

#### `integrate_picture_along_y(img)`

To integrate the picture along th Y-axis.

- **`img`** `float[float[]]`

   Image as a 2D numpy array.

##### Returns
   - **`(pix,integral)`** `(numpy.array(int[]),numpy.array(float[]))`

A tuple with pix the pixel numbers as a numpy array
and 'integral' the integral as a numpy array.

#### `normal_distribution(x, s0, x0)`

Normal distribution.

f(x) = 1/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2)

- **`x`** `numpy.array(float[])`

   The input.

- **`s0`** `float`

   The standard deviation.

- **`x0`** `float`

   The mean value, center of the distribution.

##### Returns
   - **`result`** `numpy.array(float[])`

The value of the distribution.

#### `num2str(a, n=3)`

To turn a number into a string.

- **`a`** `float`

   The number to convert.

- **`n`** `int` `default=3`

   (optional) Number of significant digits.

##### Returns
   - **`result`** `str`

The string.

#### `reshape_image_2(image, x1, y1, x2, y2)`

To reshape the image as a rectangle.

- **`image`** `float[float[]]`

   The picture as 2D array.

- **`x1`** `int`

   The first x-coordinate of the rectangle.

- **`y1`** `int`

   The first y-coordinate of the rectangle.

- **`x2`** `int`

   The second x-coordinate of the rectangle.

- **`y2`** `int`

   The second y-coordinate of the rectangle.

##### Returns
   - **`new_image`** `np.array(float[float[])`

The reshaped image.

#### `reshape_img(img, ix, iy, lm)`

To reshape an image to a squared one.

- **`img`** `float[float[]]`

   The picture as 2D array.

- **`ix`** `int`

   The index of the center of the square.

- **`iy`** `int`

   The index of the center of the square.

- **`lm`** `int`

   The half length of the square.

##### Returns
   - **`img`** `np.array(float[float[])`

The reshaped image.

#### `significant(x, sig=4)`

To turn a float as a str with a certain number of significant digits.

x: float
The input number.

sig: int, default=4
Number of significant digits.

##### Returns
   res: float
The result.

#### `two_gaussian_offset(x, a1, x1, s1, a2, x2, s2, c)`

Sum of two gaussian distribution with an offset.

- **`x`** `float or numpy.array(float[])`

   The variable(s).

- **`a1`** `float`

   Amplitude of the first distribution.

- **`x1`** `float`

   Mean value of the first distribution.

- **`s1`** `float`

   Standard deviation of the first distribution.

- **`a2`** `float`

   Amplitude of the second distribution.

- **`x2`** `float`

   Mean value of the second distribution.

- **`s2`** `float`

   Standard deviation of the second distribution.

- **`c`** `float`

   The offset.

##### Returns
   result: float or numpy.array(float[])
Value(s) of the distribution.

#### `two_gaussian(x, a1, x1, s1, a2, x2, s2)`

Sum of two gaussian distribution.

- **`x`** `float or numpy.array(float[])`

   The variable.

- **`a1`** `float`

   Amplitude of the first distribution.

- **`x1`** `float`

   Mean value of the first distribution.

- **`s1`** `float`

   Standard deviation of the first distribution.

- **`a2`** `float`

   Amplitude of the second distribution.

- **`x2`** `float`

   Mean value of the second distribution.

- **`s2`** `float`

   Standard deviation of the second distribution.

##### Returns
   result: float or numpy.array(float[])
Value(s) of the distribution.

