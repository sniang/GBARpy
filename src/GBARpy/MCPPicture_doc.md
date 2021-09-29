##MCPPicture.**BeamSpot**

<p class="func-header">
    <i>class</i> MCPPicture.<b>BeamSpot</b>(<i>fname, reshape=[], mcpp=None, fit='Filtered gaussian'</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L16">[source]</a>
</p>

Class to analyse the pictures coming from the MCP
#### Attributes
* BeamSpot.fname: string, file name of the picture
* BeamSpot.img: 2D array, picture as an array
* BeamSpot.pix: the pixels along the x axis
* BeamSpot.piy: the pixels along the y axis
* BeamSpot.Ix: array of floats, integral along the x axis
* BeamSpot.Iy: array of float, integral along the y axis
* BeamSpot.Ax: float, Amplitude, fit along the x axis
* BeamSpot.Ay: float, Amplitude, fit along the y axis
* BeamSpot.sigx: float, Sigma, fit along the x axis
* BeamSpot.sigy: float, Sigma, fit along the x axis
* BeamSpot.r0x: float, Center, fit along the x axis
* BeamSpot.r0y: float, Center, fit along the x axis
* BeamSpot.offsetx: float, offset, fit along the x axis
* BeamSpot.offsety: float, offset, fit along the x axis
* BeamSpot.poptx: array of floats, the parameters of the fit along the x-axis
* BeamSpot.perrx: array of floats, errors on the parameters of the fit along the x-axis
* BeamSpot.popty: array of floats, the parameters of the fit along the y-axis
* BeamSpot.perry: array of floats, errors on the parameters of the fit along the y-axis
* BeamSpot.reshape: array of int, the parameters to reshape, see help(import_image)
* BeamSpot.Fit:

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>plot_y_int</b>(<i>self, label=''</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L104">[source]</a>
</p>

To plot the integral of the picture along the "y" axis
* Parameters
* label: (optional) a string
* Example
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_Y_int("Integral along the y-axis")

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>plot_x_int</b>(<i>self, label=''</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L126">[source]</a>
</p>

To plot the integral of the picture along the "x" axis
* Parameters
* label: (optional) a string
* Example
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_X_int("Integral along the x-axis")

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>plot_x_int_revert</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L148">[source]</a>
</p>

To plot the integral of the picture along the "x" axis and reverse the picture
* Example
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_X_int("Integral along the x-axis")

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>plot</b>(<i>self, fname='', figsize=(12, 10), fontsize=12, ftsizeticks=12</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L168">[source]</a>
</p>

To plot the picture and the analysis
* Parameters
* fname: string (optional), the name of the file to save the plot
* figsize: tuple (size in inch X, Y) (optional), size of the figure
* fontsize: int (optional), size of the font
* ftsizeticks: int (optional), size of the ticks' font
* Returns
* fig: a matplotlib.pyplot.figure
* Example
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
fig = bs.plot("analysis.pdf")
# or
fig = bs.plot()
fig.savefig("analysis.pdf")

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**FitInterface**

<p class="func-header">
    <i>class</i> MCPPicture.<b>FitInterface</b>(<i>def __init__(self</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L251">[source]</a>
</p>

Super class to do the fit of the MCP pictures
Need to be define
self.fitfunc : the fit function
self.labels : the names the parameters

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>do_fit</b>(<i>self, x1, y1, x2=[], y2=[], p0=None</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L269">[source]</a>
</p>

To do the fit y = f(x)

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x1 : <i>array of float</i></b>
<p class="attr">
    the first x input data y1 : array of float the first y input data x2 : array of float, optional the second x input data y2 : array of float, optional the second y input data p0 : array of floats the guessed parameters to help the fit
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>None. : <i></i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**SimpleGaussian**

<p class="func-header">
    <i>class</i> MCPPicture.<b>SimpleGaussian</b>(<i>x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L332">[source]</a>
</p>

A gaussian fit of the integral along the x and y axis

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>do_fit</b>(<i>self, x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L365">[source]</a>
</p>

To do the fit y = f(x)

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x1 : <i>array of float</i></b>
<p class="attr">
    the first x input data y1 : array of float the first y input data x2 : array of float, optional the second x input data y2 : array of float, optional the second y input data
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>None. : <i></i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**FilteredGaussian**

<p class="func-header">
    <i>class</i> MCPPicture.<b>FilteredGaussian</b>(<i>x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L401">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>





##MCPPicture.**TwoGaussians**

<p class="func-header">
    <i>class</i> MCPPicture.<b>TwoGaussians</b>(<i>x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L436">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>do_fit</b>(<i>self, x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L467">[source]</a>
</p>

To do the fit y = f(x)

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x1 : <i>array of float</i></b>
<p class="attr">
    the first x input data y1 : array of float the first y input data x2 : array of float, optional the second x input data y2 : array of float, optional the second y input data
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>None. : <i></i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**gaussian_offset**

<p class="func-header">
    <i>def</i> MCPPicture.<b>gaussian_offset</b>(<i>x, a, x0, s0, c</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L503">[source]</a>
</p>

Gaussian distribution with an offset
f(x) = amplitude/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2) + offset

* Parameters
* x:  an np array
* a:  the amplitude
* s0: floating number, the standard deviation
* x0: floating number, the mean value, center of the distribution
* c:  the offset
* Returns
* the value of the distribution

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**gaussian**

<p class="func-header">
    <i>def</i> MCPPicture.<b>gaussian</b>(<i>x, a, x0, s0</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L520">[source]</a>
</p>

Gaussian distribution
f(x) = amplitude/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2)

* Parameters
* x:  an np array
* a:  the amplitude
* s0: floating number, the standard deviation
* x0: floating number, the mean value, center of the distribution
* Returns
* the value of the distribution

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**normal_distribution**

<p class="func-header">
    <i>def</i> MCPPicture.<b>normal_distribution</b>(<i>x, s0, x0</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L536">[source]</a>
</p>

Normal distribution
f(x) = 1/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2)
* Parameters
* x:  an np array
* s0: floating number, the standard deviation
* x0: floating number, the mean value, center of the distribution
* Returns
the value of the distribution

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**two_gaussian**

<p class="func-header">
    <i>def</i> MCPPicture.<b>two_gaussian</b>(<i>x, a1, x1, s1, a2, x2, s2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L550">[source]</a>
</p>

Sum of two gaussian distribution

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>float, numpy array</i></b>
<p class="attr">
    the variable. a1 : float Amplitude of the first distribution. x1 : float Mean value of the first distribution. s1 : float Standard deviation of the first distribution. a2 : float Amplitude of the second distribution. x2 : float Mean value of the second distribution. s2 : float Standard deviation of the second distribution.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>float, numpy array : <i></i></b>
<p class="attr">
    Value of the distribution.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**two_gaussian_offset**

<p class="func-header">
    <i>def</i> MCPPicture.<b>two_gaussian_offset</b>(<i>x, a1, x1, s1, a2, x2, s2, c</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L580">[source]</a>
</p>

Sum of two gaussian distribution with an offset

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>float, numpy array</i></b>
<p class="attr">
    the variable. a1 : float Amplitude of the first distribution. x1 : float Mean value of the first distribution. s1 : float Standard deviation of the first distribution. a2 : float Amplitude of the second distribution. x2 : float Mean value of the second distribution. s2 : float Standard deviation of the second distribution. c : float The offset.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>float, numpy array : <i></i></b>
<p class="attr">
    Value of the distribution.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**num2str**

<p class="func-header">
    <i>def</i> MCPPicture.<b>num2str</b>(<i>a, n=3</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L612">[source]</a>
</p>

To turn a number into a string

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>a : <i>float</i></b>
<p class="attr">
    the number to convert. n : int, optional number of significant digits. The default is 3.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>str : <i></i></b>
<p class="attr">
    the string.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**fit_gaussian_offset_filtered**

<p class="func-header">
    <i>def</i> MCPPicture.<b>fit_gaussian_offset_filtered</b>(<i>x, y</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L634">[source]</a>
</p>

Fit with the function gaussian_offset.
* Parameters
* x: numpy array
* y: numpy array
* Returns
* popt,perr: numpy arrays, the parameters and the error of the fit

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**reshape_img**

<p class="func-header">
    <i>def</i> MCPPicture.<b>reshape_img</b>(<i>img, ix, iy, lm</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L673">[source]</a>
</p>

To reshape an image to a squared one
* Parameters
* img: np.array([np.array]) the image array
* ix: the index of the center of the square
* iy: the index of the center of the square
* lm: the half length of the square
*Returns
* The reshaped picture as an array

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**reshape_image_2**

<p class="func-header">
    <i>def</i> MCPPicture.<b>reshape_image_2</b>(<i>image, x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L702">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**import_image**

<p class="func-header">
    <i>def</i> MCPPicture.<b>import_image</b>(<i>fname, reshape=[]</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L715">[source]</a>
</p>

To import the picture as an array
* Parameters
* fname: string, name of the file
* reshape: array, to reshape the picture as a square [ix,iy,l]
* Returns
* the picture as 2D array

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**integrate_picture_along_y**

<p class="func-header">
    <i>def</i> MCPPicture.<b>integrate_picture_along_y</b>(<i>img</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L748">[source]</a>
</p>

To integrate the picture along th Y axis
* Parameters
* img: image as a 2D numpy array
* Returns
* (pix,integral): A tuple with pix the pixel numbers as a numpy array
and 'integral' the integral as a numpy array

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##MCPPicture.**integrate_picture_along_x**

<p class="func-header">
    <i>def</i> MCPPicture.<b>integrate_picture_along_x</b>(<i>img</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L765">[source]</a>
</p>

To integrate the picture along th X axis

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>img : <i>numpy.array(float[float[]])</i></b>
<p class="attr">
    image as a 2D numpy array
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>(pix,integral) : <i>(numpy.array(int[]),numpy.array(int[]))</i></b>
<p class="attr">
    A tuple with pix the pixel numbers as a numpy array and 'integral' the integral as a numpy array
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**get_index_str**

<p class="func-header">
    <i>def</i> MCPPicture.<b>get_index_str</b>(<i>n, i</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L785">[source]</a>
</p>

To convert an int 'i' to a string

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>n : <i>int</i></b>
<p class="attr">
    order to put 0 if necessary
</p>
<b>i : <i>int</i></b>
<p class="attr">
    the number to convert
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>res : <i>str</i></b>
<p class="attr">
    the number as a string
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
getIndexStr(100,15)
```

Out:

```
'015'
```

##MCPPicture.**significant**

<p class="func-header">
    <i>def</i> MCPPicture.<b>significant</b>(<i>x, sig=4</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L822">[source]</a>
</p>

To turn a float as a str with a certain number of significant digits

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>float</i></b>
<p class="attr">
    the input number
</p>
<b>sig : <i>int, default=4</i></b>
<p class="attr">
    number of significant digits
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>res : <i>float</i></b>
<p class="attr">
    the result
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**MCPParams**

<p class="func-header">
    <i>class</i> MCPPicture.<b>MCPParams</b>(<i>name=None, r=None, x0=None, y0=None, r0=None, ratio=None</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L848">[source]</a>
</p>

Class to store the parameters of the MCP to adapt the analysis

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>name : <i>string</i></b>
<p class="attr">
    (optional) the name of the MCP
</p>
<b>R : <i>float</i></b>
<p class="attr">
    (optional) radius of the mirror in mm
</p>
<b>x0 : <i>int</i></b>
<p class="attr">
    (optional) x position of the center of the mirror in pixels
</p>
<b>y0 : <i>int</i></b>
<p class="attr">
    (optional) y position of the center of the mirror in pixels
</p>
<b>R0 : <i>int</i></b>
<p class="attr">
    (optional) radius of the mirror in pixels
</p>
<b>ratio : <i>int</i></b>
<p class="attr">
    (optional) mm/pixels ratio if R and R0 have been defined, then ratio is defined automatically
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>name : <i>string</i></b>
<p class="attr">
    the name of the MCP
</p>
<b>R : <i>float</i></b>
<p class="attr">
    radius of the mirror in mm
</p>
<b>x0 : <i>int</i></b>
<p class="attr">
    x position of the center of the mirror in pixels
</p>
<b>y0 : <i>int</i></b>
<p class="attr">
    y position of the center of the mirror in pixels
</p>
<b>R0 : <i>int</i></b>
<p class="attr">
    radius of the mirror in pixels
</p>
<b>ratio : <i>float</i></b>
<p class="attr">
    mm/pixels ratio
</p>
<b>canBePlot : <i>bool</i></b>
<p class="attr">
    boolean to know if the mirror can be plot
</p>
<b>ratioIsSet : <i>bool</i></b>
<p class="attr">
    boolean to know if a ratio has been defined
</p></td>
</tr>
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>define_ratio</b>(<i>self, mm, pix</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L929">[source]</a>
</p>

To define the ratio mm vs pixels

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>mm : <i>float</i></b>
<p class="attr">
    a distance in mm
</p>
<b>pix : <i>float</i></b>
<p class="attr">
    the equivalent distance in pixels
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>None : <i></i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>check_ratio_is_set</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L950">[source]</a>
</p>

To check is the ratio has been set

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>boolean</i></b>
<p class="attr">
    True if the ratio has been set
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>check_all_set</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L964">[source]</a>
</p>

To check is all has been set

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>boolean</i></b>
<p class="attr">
    True if all the parameters have been set
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>save_conf</b>(<i>self, fname</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L984">[source]</a>
</p>

To save the parameters of the MCP as a binary file
Use .mcp extension

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>fname : <i>string</i></b>
<p class="attr">
    the name of the binary file
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>None : <i></i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
params = MCPParams()
params.save_config("config.mcp")
```

##MCPPicture.**import_config**

<p class="func-header">
    <i>def</i> MCPPicture.<b>import_config</b>(<i>fname</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L1010">[source]</a>
</p>

To import the MCP parameters from a binary file

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>fname : <i>str</i></b>
<p class="attr">
    the file's name
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>mcpp : <i>GBARpy.MCPPicture.MCPParams</i></b>
<p class="attr">
    the MCP parameters
</p></td>
</tr>
    </tbody>
</table>

