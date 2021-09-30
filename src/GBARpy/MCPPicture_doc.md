##MCPPicture.**BeamSpot**

<p class="func-header">
    <i>class</i> MCPPicture.<b>BeamSpot</b>(<i>fname, reshape=[], mcpp=None, fit='Filtered gaussian'</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L16">[source]</a>
</p>

Class to analyse the pictures coming from the MCP.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>fname : <i>str</i></b>
<p class="attr">
    file name of the picture, the accepted file format ["tif","jpg","jpeg","png","asc","bmp"].
</p>
<b>reshape : <i>int[3] or int[4]</i></b>
<p class="attr">
    [ix,iy,l] to reshape the picture as a square or [x1,x2,y1,y2] to reshape as a rectangle.
</p>
<b>fit : <i>str</i></b>
<p class="attr">
    The kind of fit. Choose between "Filtered gaussian", "Simple gaussian", "Two gaussians".
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>fname : <i>str</i></b>
<p class="attr">
    file name of the picture.
</p>
<b>img : <i>float[float[]]</i></b>
<p class="attr">
    picture as an array.
</p>
<b>pix : <i>int[]</i></b>
<p class="attr">
    the pixels along the x axis.
</p>
<b>piy : <i>int[]</i></b>
<p class="attr">
    the pixels along the y axis.
</p>
<b>Ix : <i>float[]</i></b>
<p class="attr">
    integral along the x axis.
</p>
<b>Iy : <i>float[]</i></b>
<p class="attr">
    integral along the y axis.
</p>
<b>total_integral : <i>float</i></b>
<p class="attr">
    Total integral pf the image.
</p>
<b>poptx : <i>float[]</i></b>
<p class="attr">
    the parameters of the fit along the x-axis.
</p>
<b>perrx : <i>float[]</i></b>
<p class="attr">
    errors on the parameters of the fit along the x-axis.
</p>
<b>popty : <i>float[]</i></b>
<p class="attr">
    the parameters of the fit along the y-axis.
</p>
<b>perry : <i>float[]</i></b>
<p class="attr">
    errors on the parameters of the fit along the y-axis.
</p>
<b>reshape : <i>int[]</i></b>
<p class="attr">
    the parameters to reshape, see help(import_image).
</p>
<b>Fit : <i>GBARpy.MCPPicture.FitInterface</i></b>
<p class="attr">
    The fit used for the analysis.
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
```

####Methods



<p class="func-header">
    <i></i> <b>plot_y_int</b>(<i>self, label=''</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L139">[source]</a>
</p>

To plot the integral of the picture along the y-axis.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>label : <i>str, default=""</i></b>
<p class="attr">
    (optional) the label of the plot.
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

```python3
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_Y_int("Integral along the x-axis")
```



<p class="func-header">
    <i></i> <b>plot_x_int</b>(<i>self, label=''</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L172">[source]</a>
</p>

To plot the integral of the picture along the x-axis.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>label : <i>str, default=""</i></b>
<p class="attr">
    (optional) the label of the plot.
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

```python3
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_X_int("Integral along the x-axis")
```



<p class="func-header">
    <i></i> <b>plot_x_int_revert</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L205">[source]</a>
</p>

To plot the integral of the picture along the "x" axis and reverse the picture.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
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
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
bs.plot_X_int("Integral along the x-axis")
```



<p class="func-header">
    <i></i> <b>plot</b>(<i>self, fname='', figsize=(12, 10), fontsize=12, ftsizeticks=12</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L233">[source]</a>
</p>

To plot the picture and the analysis.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>fname : <i>string, default=""</i></b>
<p class="attr">
    (optional) the name of the file to save the plot.
</p>
<b>figsize : <i>(float, float), default=(12, 10)</i></b>
<p class="attr">
    (optional) (size in inch X, Y) size of the figure.
</p>
<b>fontsize : <i>int , default=12</i></b>
<p class="attr">
    (optional) size of the font.
</p>
<b>ftsizeticks : <i>int , default=12</i></b>
<p class="attr">
    (optional) size of the ticks' font.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>fig : <i>matplotlib.pyplot.Figure</i></b>
<p class="attr">
    the figure
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
import GBARpy.MCPPicture as mcp
bs = mcp.BeamSpot("name.tif")
fig = bs.plot("analysis.pdf")
# or
fig = bs.plot()
fig.savefig("analysis.pdf")
```

##MCPPicture.**FitInterface**

<p class="func-header">
    <i>class</i> MCPPicture.<b>FitInterface</b>(<i>def __init__(self</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L331">[source]</a>
</p>

Super class to do the fit of the MCP pictures
Need to be define

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>fitfunc : <i>function</i></b>
<p class="attr">
    the fit function
</p>
<b>labels : <i>str[]</i></b>
<p class="attr">
    the names the parameters
</p>
<b>params1 : <i>float[]</i></b>
<p class="attr">
    parameters of the fit along the x-axis
</p>
<b>errors1 : <i>float[]</i></b>
<p class="attr">
    errors parameters of the fit along the x-axis
</p>
<b>params2 : <i>float[]</i></b>
<p class="attr">
    parameters of the fit along the y-axis
</p>
<b>errors2 : <i>float[]</i></b>
<p class="attr">
    errors parameters of the fit along the y-axis
</p>
<b>title1 : <i>str</i></b>
<p class="attr">
    title for the fit along the x-axis
</p>
<b>title2 : <i>str</i></b>
<p class="attr">
    title for the fit along the y-axis
</p></td>
</tr>
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>do_fit</b>(<i>self, x1, y1, x2=[], y2=[], p0=None</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L372">[source]</a>
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
    <i>class</i> MCPPicture.<b>SimpleGaussian</b>(<i>x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L435">[source]</a>
</p>

A gaussian fit of the integral along the x and y axis. Inherit from FitInterface.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x1 : <i>float[]</i></b>
<p class="attr">
    the x axis.
</p>
<b>y1 : <i>float[]</i></b>
<p class="attr">
    integral along the x axis.
</p>
<b>x2 : <i>float[]</i></b>
<p class="attr">
    the y axis.
</p>
<b>y2 : <i>float[]</i></b>
<p class="attr">
    integral along the y axis.
</p></td>
</tr>
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>do_fit</b>(<i>self, x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L468">[source]</a>
</p>

To do the fit y = f(x).

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x1 : <i>float[]</i></b>
<p class="attr">
    the first x input data.
</p>
<b>y1 : <i>float[]</i></b>
<p class="attr">
    the first y input data.
</p>
<b>x2 : <i>float[]</i></b>
<p class="attr">
    the second x input data.
</p>
<b>y2 : <i>float[]</i></b>
<p class="attr">
    the second y input data.
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



##MCPPicture.**FilteredGaussian**

<p class="func-header">
    <i>class</i> MCPPicture.<b>FilteredGaussian</b>(<i>x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L506">[source]</a>
</p>

To fit with a filtered gaussian. Inherit from FitInterface.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x1 : <i>float[]</i></b>
<p class="attr">
    the x axis.
</p>
<b>y1 : <i>float[]</i></b>
<p class="attr">
    integral along the x axis.
</p>
<b>x2 : <i>float[]</i></b>
<p class="attr">
    the y axis.
</p>
<b>y2 : <i>float[]</i></b>
<p class="attr">
    integral along the y axis.
</p></td>
</tr>
    </tbody>
</table>





##MCPPicture.**TwoGaussians**

<p class="func-header">
    <i>class</i> MCPPicture.<b>TwoGaussians</b>(<i>x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L542">[source]</a>
</p>

To fit with a sum of two gaussians. Inherits from FitInterface.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x1 : <i>float[]</i></b>
<p class="attr">
    the x axis.
</p>
<b>y1 : <i>float[]</i></b>
<p class="attr">
    integral along the x axis.
</p>
<b>x2 : <i>float[]</i></b>
<p class="attr">
    the y axis.
</p>
<b>y2 : <i>float[]</i></b>
<p class="attr">
    integral along the y axis.
</p></td>
</tr>
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>do_fit</b>(<i>self, x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L574">[source]</a>
</p>

To do the fit y = f(x).

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x1 : <i>float[]</i></b>
<p class="attr">
    the first x input data.
</p>
<b>y1 : <i>float[]</i></b>
<p class="attr">
    the first y input data.
</p>
<b>x2 : <i>float[]</i></b>
<p class="attr">
    the second x input data.
</p>
<b>y2 : <i>float[]</i></b>
<p class="attr">
    the second y input data.
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



##MCPPicture.**MCPParams**

<p class="func-header">
    <i>class</i> MCPPicture.<b>MCPParams</b>(<i>name=None, r=None, x0=None, y0=None, r0=None, ratio=None</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L613">[source]</a>
</p>

Class to store the parameters of the MCP to adapt the analysis.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>name : <i>string</i></b>
<p class="attr">
    (optional) the name of the MCP.
</p>
<b>R : <i>float</i></b>
<p class="attr">
    (optional) radius of the mirror in mm.
</p>
<b>x0 : <i>int</i></b>
<p class="attr">
    (optional) x position of the center of the mirror in pixels.
</p>
<b>y0 : <i>int</i></b>
<p class="attr">
    (optional) y position of the center of the mirror in pixels.
</p>
<b>R0 : <i>int</i></b>
<p class="attr">
    (optional) radius of the mirror in pixels.
</p>
<b>ratio : <i>int</i></b>
<p class="attr">
    (optional) mm/pixels ratio. If R and R0 have been defined, then ratio is defined automatically.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>name : <i>string</i></b>
<p class="attr">
    the name of the MCP.
</p>
<b>R : <i>float</i></b>
<p class="attr">
    radius of the mirror in mm.
</p>
<b>x0 : <i>int</i></b>
<p class="attr">
    x position of the center of the mirror in pixels.
</p>
<b>y0 : <i>int</i></b>
<p class="attr">
    y position of the center of the mirror in pixels.
</p>
<b>R0 : <i>int</i></b>
<p class="attr">
    radius of the mirror in pixels.
</p>
<b>ratio : <i>float</i></b>
<p class="attr">
    mm/pixels ratio.
</p>
<b>canBePlot : <i>bool</i></b>
<p class="attr">
    boolean to know if the mirror can be plot.
</p>
<b>ratioIsSet : <i>bool</i></b>
<p class="attr">
    boolean to know if a ratio has been defined.
</p></td>
</tr>
    </tbody>
</table>



####Methods



<p class="func-header">
    <i></i> <b>define_ratio</b>(<i>self, mm, pix</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L695">[source]</a>
</p>

To define the ratio mm vs pixels.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>mm : <i>float</i></b>
<p class="attr">
    A distance in mm.
</p>
<b>pix : <i>float</i></b>
<p class="attr">
    The equivalent distance in pixels.
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
    <i></i> <b>check_ratio_is_set</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L718">[source]</a>
</p>

To check is the ratio has been set.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>boolean</i></b>
<p class="attr">
    True if the ratio has been set.
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>check_all_set</b>(<i>self</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L733">[source]</a>
</p>

To check is all has been set.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>boolean</i></b>
<p class="attr">
    True if all the parameters have been set.
</p></td>
</tr>
    </tbody>
</table>





<p class="func-header">
    <i></i> <b>save_conf</b>(<i>self, fname</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L754">[source]</a>
</p>

To save the parameters of the MCP as a binary file.
Use .mcp extension.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>fname : <i>string</i></b>
<p class="attr">
    The name of the binary file.
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
    <i>def</i> MCPPicture.<b>import_config</b>(<i>fname</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L783">[source]</a>
</p>

To import the MCP parameters from a binary file.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>fname : <i>str</i></b>
<p class="attr">
    The file's name.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>mcpp : <i>GBARpy.MCPPicture.MCPParams</i></b>
<p class="attr">
    The MCP parameters.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**gaussian_offset**

<p class="func-header">
    <i>def</i> MCPPicture.<b>gaussian_offset</b>(<i>x, a, x0, s0, c</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L806">[source]</a>
</p>

Gaussian distribution with an offset.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>numpy.array(float[])</i></b>
<p class="attr">
    The input.
</p>
<b>a : <i>float</i></b>
<p class="attr">
    The amplitude.
</p>
<b>x0 : <i>float</i></b>
<p class="attr">
    The standard deviation.
</p>
<b>s0 : <i>float</i></b>
<p class="attr">
    The mean value, center of the distribution.
</p>
<b>c : <i>float</i></b>
<p class="attr">
    The offset.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>numpy.array(float[])</i></b>
<p class="attr">
    The value of the distribution.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**gaussian**

<p class="func-header">
    <i>def</i> MCPPicture.<b>gaussian</b>(<i>x, a, x0, s0</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L835">[source]</a>
</p>

Gaussian distribution.
f(x) = amplitude/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2)

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>numpy.array(float[])</i></b>
<p class="attr">
    The input.
</p>
<b>a : <i>float</i></b>
<p class="attr">
    The amplitude.
</p>
<b>x0 : <i>float</i></b>
<p class="attr">
    The standard deviation.
</p>
<b>s0 : <i>float</i></b>
<p class="attr">
    The mean value, center of the distribution.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>numpy.array(float[])</i></b>
<p class="attr">
    The value of the distribution.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**normal_distribution**

<p class="func-header">
    <i>def</i> MCPPicture.<b>normal_distribution</b>(<i>x, s0, x0</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L862">[source]</a>
</p>

Normal distribution.
f(x) = 1/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2)

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>numpy.array(float[])</i></b>
<p class="attr">
    The input.
</p>
<b>s0 : <i>float</i></b>
<p class="attr">
    The standard deviation.
</p>
<b>x0 : <i>float</i></b>
<p class="attr">
    The mean value, center of the distribution.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>numpy.array(float[])</i></b>
<p class="attr">
    The value of the distribution.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**two_gaussian**

<p class="func-header">
    <i>def</i> MCPPicture.<b>two_gaussian</b>(<i>x, a1, x1, s1, a2, x2, s2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L886">[source]</a>
</p>

Sum of two gaussian distribution.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>float or numpy.array(float[])</i></b>
<p class="attr">
    The variable.
</p>
<b>a1 : <i>float</i></b>
<p class="attr">
    Amplitude of the first distribution.
</p>
<b>x1 : <i>float</i></b>
<p class="attr">
    Mean value of the first distribution.
</p>
<b>s1 : <i>float</i></b>
<p class="attr">
    Standard deviation of the first distribution.
</p>
<b>a2 : <i>float</i></b>
<p class="attr">
    Amplitude of the second distribution.
</p>
<b>x2 : <i>float</i></b>
<p class="attr">
    Mean value of the second distribution.
</p>
<b>s2 : <i>float</i></b>
<p class="attr">
    Standard deviation of the second distribution.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>float or numpy.array(float[])</i></b>
<p class="attr">
    Value(s) of the distribution.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**two_gaussian_offset**

<p class="func-header">
    <i>def</i> MCPPicture.<b>two_gaussian_offset</b>(<i>x, a1, x1, s1, a2, x2, s2, c</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L922">[source]</a>
</p>

Sum of two gaussian distribution with an offset.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>float or numpy.array(float[])</i></b>
<p class="attr">
    The variable(s).
</p>
<b>a1 : <i>float</i></b>
<p class="attr">
    Amplitude of the first distribution.
</p>
<b>x1 : <i>float</i></b>
<p class="attr">
    Mean value of the first distribution.
</p>
<b>s1 : <i>float</i></b>
<p class="attr">
    Standard deviation of the first distribution.
</p>
<b>a2 : <i>float</i></b>
<p class="attr">
    Amplitude of the second distribution.
</p>
<b>x2 : <i>float</i></b>
<p class="attr">
    Mean value of the second distribution.
</p>
<b>s2 : <i>float</i></b>
<p class="attr">
    Standard deviation of the second distribution.
</p>
<b>c : <i>float</i></b>
<p class="attr">
    The offset.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>float or numpy.array(float[])</i></b>
<p class="attr">
    Value(s) of the distribution.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**num2str**

<p class="func-header">
    <i>def</i> MCPPicture.<b>num2str</b>(<i>a, n=3</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L960">[source]</a>
</p>

To turn a number into a string.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>a : <i>float</i></b>
<p class="attr">
    The number to convert.
</p>
<b>n : <i>int, default=3</i></b>
<p class="attr">
    (optional) Number of significant digits.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>result : <i>str</i></b>
<p class="attr">
    The string.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**fit_gaussian_offset_filtered**

<p class="func-header">
    <i>def</i> MCPPicture.<b>fit_gaussian_offset_filtered</b>(<i>x, y</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L982">[source]</a>
</p>

Fit with the function gaussian_offset.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>np.array(float[])</i></b>
<p class="attr">
    x-coordinates.
</p>
<b>y : <i>np.array(float[])</i></b>
<p class="attr">
    y-coordinates.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>popt,perr : <i>np.array(float[]), np.array(float[])</i></b>
<p class="attr">
    The parameters and the error of the fit.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**reshape_img**

<p class="func-header">
    <i>def</i> MCPPicture.<b>reshape_img</b>(<i>img, ix, iy, lm</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L1029">[source]</a>
</p>

To reshape an image to a squared one.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>img : <i>float[float[]]</i></b>
<p class="attr">
    The picture as 2D array.
</p>
<b>ix : <i>int</i></b>
<p class="attr">
    The index of the center of the square.
</p>
<b>iy : <i>int</i></b>
<p class="attr">
    The index of the center of the square.
</p>
<b>lm : <i>int</i></b>
<p class="attr">
    The half length of the square.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>img : <i>np.array(float[float[])</i></b>
<p class="attr">
    The reshaped image.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**reshape_image_2**

<p class="func-header">
    <i>def</i> MCPPicture.<b>reshape_image_2</b>(<i>image, x1, y1, x2, y2</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L1070">[source]</a>
</p>

To reshape the image as a rectangle.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>image : <i>float[float[]]</i></b>
<p class="attr">
    The picture as 2D array.
</p>
<b>x1 : <i>int</i></b>
<p class="attr">
    The first x-coordinate of the rectangle.
</p>
<b>y1 : <i>int</i></b>
<p class="attr">
    The first y-coordinate of the rectangle.
</p>
<b>x2 : <i>int</i></b>
<p class="attr">
    The second x-coordinate of the rectangle.
</p>
<b>y2 : <i>int</i></b>
<p class="attr">
    The second y-coordinate of the rectangle.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>new_image : <i>np.array(float[float[])</i></b>
<p class="attr">
    The reshaped image.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**import_image**

<p class="func-header">
    <i>def</i> MCPPicture.<b>import_image</b>(<i>fname, reshape=[]</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L1108">[source]</a>
</p>

To import the picture as an array.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>fname : <i>string</i></b>
<p class="attr">
    Name of the file.
</p>
<b>reshape : <i>int[3] or int[4]</i></b>
<p class="attr">
    [ix,iy,l] to reshape the picture as a square or [x1,x2,y1,y2] to reshape as a rectangle.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>img : <i>np.array(float[float[])</i></b>
<p class="attr">
    The picture as 2D array.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**integrate_picture_along_y**

<p class="func-header">
    <i>def</i> MCPPicture.<b>integrate_picture_along_y</b>(<i>img</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L1149">[source]</a>
</p>

To integrate the picture along th Y-axis.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>img : <i>float[float[]]</i></b>
<p class="attr">
    Image as a 2D numpy array.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>(pix,integral) : <i>(numpy.array(int[]),numpy.array(float[]))</i></b>
<p class="attr">
    A tuple with pix the pixel numbers as a numpy array and 'integral' the integral as a numpy array.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**integrate_picture_along_x**

<p class="func-header">
    <i>def</i> MCPPicture.<b>integrate_picture_along_x</b>(<i>img</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L1171">[source]</a>
</p>

To integrate the picture along th X axis.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>img : <i>numpy.array(float[float[]])</i></b>
<p class="attr">
    Image as a 2D numpy array.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>(pix,integral) : <i>(numpy.array(int[]),numpy.array(float[]))</i></b>
<p class="attr">
    A tuple with pix the pixel numbers as a numpy array and 'integral' the integral as a numpy array.
</p></td>
</tr>
    </tbody>
</table>



##MCPPicture.**get_index_str**

<p class="func-header">
    <i>def</i> MCPPicture.<b>get_index_str</b>(<i>n, i</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L1192">[source]</a>
</p>

To convert an int 'i' to a string.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>n : <i>int</i></b>
<p class="attr">
    Order to put 0 if necessary.
</p>
<b>i : <i>int</i></b>
<p class="attr">
    The number to convert.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>res : <i>str</i></b>
<p class="attr">
    The number as a string.
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
    <i>def</i> MCPPicture.<b>significant</b>(<i>x, sig=4</i>) <a class="src-href" target="_blank" href="https://github.com/sniang/GBARpy/tree/main/src/GBARpy/MCPPicture.py#L1230">[source]</a>
</p>

To turn a float as a str with a certain number of significant digits.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>x : <i>float</i></b>
<p class="attr">
    The input number.
</p>
<b>sig : <i>int, default=4</i></b>
<p class="attr">
    Number of significant digits.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>res : <i>float</i></b>
<p class="attr">
    The result.
</p></td>
</tr>
    </tbody>
</table>

