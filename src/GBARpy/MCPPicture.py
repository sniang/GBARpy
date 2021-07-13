#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: samuel.niang@cern.ch
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from skimage.color import rgb2gray
import codecs
import dill


class BeamSpot:
    """
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
    """

    def __init__(self, fname, reshape=[], mcpp=None, fit="Filtered gaussian"):
        """
        Constructor of the class
        * Parameters
            * fname: string, file name of the picture, the accepted file format ["tif","jpg","jpeg","png","asc","bmp"]
            * reshape: array of 3 integers (optional), to reshape the pictures (square): x,y,length
            * fit: "Filtered gaussian", "Simple gaussian", "Two gaussians"
        * Example
            import GBARpy.MCPPicture as mcp
            bs = mcp.BeamSpot("name.tif")
        """
        # define ratio
        ratio = 1.
        if mcpp is None:
            self.mcpp = MCPParams()
        else:
            self.mcpp = mcpp
            if self.mcpp.check_ratio_is_set():
                ratio = self.mcpp.ratio

        self.fname = fname
        self.reshape = reshape
        self.img_original = self.fname
        self.img = import_image(self.fname, self.reshape)
        self.pix, self.Ix = integrate_picture_along_x(self.img)
        self.pix = self.pix * ratio
        self.piy, self.Iy = integrate_picture_along_y(self.img)
        self.piy = self.piy * ratio
        if fit == "Filtered gaussian":
            self.fit = FilteredGaussian(self.pix, self.Ix,
                                        self.piy, self.Iy)
        elif fit == "Simple gaussian":
            self.fit = SimpleGaussian(self.pix, self.Ix,
                                      self.piy, self.Iy)
        elif fit == "Two gaussian":
            self.fit = TwoGaussians(self.pix, self.Ix,
                                    self.piy, self.Iy)
        else:
            self.fit = FilteredGaussian(self.pix, self.Ix,
                                        self.piy, self.Iy)

        self.poptx, self.perrx = self.fit.params1, self.fit.errors1
        self.popty, self.perry = self.fit.params2, self.fit.errors2
        self.offsetx = self.fit.params1[-1]
        self.offsety = self.fit.params2[-1]

    def __repr__(self):
        """
        To represent the object as a string
        * Returns
            * a string variable
        * Example
            import GBARpy.MCPPicture as mcp
            bs = mcp.BeamSpot("name.tif")
            repr = bs.__repr__()
            #or to print it in the python console
            print(bs)
        """
        return self.fit.__repr__()

    def plot_y_int(self, label=""):
        """
        To plot the integral of the picture along the "y" axis
        * Parameters
            * label: (optional) a string
        * Example
            import GBARpy.MCPPicture as mcp
            bs = mcp.BeamSpot("name.tif")
            bs.plot_Y_int("Integral along the y-axis")
        """
        popt = self.popty
        popt[-1] = 0
        if np.any(np.isnan(popt)):
            plt.plot(self.piy, self.Iy, '.', ms=1, label=label)
        else:
            D = self.Iy - self.offsety
            p = plt.plot(self.piy, D, '.', ms=1, label=label)
            plt.plot(self.piy, self.fit.fitfunc(self.piy, *popt), color=p[0].get_color())
        plt.xlim([0, np.max(self.piy)])
        if len(label) != 0:
            plt.legend()

    def plot_x_int(self, label=""):
        """
        To plot the integral of the picture along the "x" axis
        * Parameters
            * label: (optional) a string
        * Example
            import GBARpy.MCPPicture as mcp
            bs = mcp.BeamSpot("name.tif")
            bs.plot_X_int("Integral along the x-axis")
        """
        popt = self.poptx
        popt[-1] = 0
        if np.any(np.isnan(popt)):
            plt.plot(self.pix, self.Ix, '.', ms=1, label=label)
        else:
            D = self.Ix - self.offsetx
            p = plt.plot(self.pix, D, '.', ms=1, label=label)
            plt.plot(self.pix, self.fit.fitfunc(self.pix, *popt), color=p[0].get_color())
        plt.xlim([0, np.max(self.pix)])
        if len(label) != 0:
            plt.legend()

    def plot_x_int_revert(self):
        """
        To plot the integral of the picture along the "x" axis and reverse the picture
        * Example
            import GBARpy.MCPPicture as mcp
            bs = mcp.BeamSpot("name.tif")
            bs.plot_X_int("Integral along the x-axis")
        """
        pix, Ix = self.pix, self.Ix
        popt = self.poptx
        popt[-1] = 0
        if np.any(np.isnan(popt)):
            plt.plot(Ix, pix, '.', ms=1)
        else:
            d = Ix - self.offsetx
            p = plt.plot(d, pix, '.', ms=1)
            g = self.fit.fitfunc(pix, *popt)
            plt.plot(g, pix, color=p[0].get_color())
        plt.ylim([np.max(pix), 0])

    def plot(self, fname="", figsize=(12, 10), fontsize=12, ftsizeticks=12):
        """
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
        """

        def conv(a):
            b = []
            for e in a:
                b.append(str(e))
            return np.array(b)

        if len(fname) == 0:
            fname = None
        fig = plt.figure(figsize=figsize)

        plt.subplot(223)
        plt.text(0, 0, self.fit.__repr__().replace('\t', ' '), fontsize=fontsize)
        plt.axis('off')

        plt.subplot(221)
        self.plot_x_int_revert()
        if self.mcpp.check_ratio_is_set():
            plt.ylabel("mm", fontsize=fontsize)
        else:
            plt.ylabel("pixels", fontsize=fontsize)
        plt.grid()
        plt.xticks(fontsize=ftsizeticks)
        plt.yticks(fontsize=ftsizeticks)
        plt.title("Integral along the x-axis", fontsize=fontsize)
        if not (np.isnan(self.poptx[0])):
            plt.xlim([0, max(self.Ix - self.offsetx) * 1.1])

        plt.subplot(222)
        plt.imshow(self.img, vmin=self.img.min(), vmax=self.img.max())
        plt.xticks(fontsize=ftsizeticks)
        plt.yticks(fontsize=ftsizeticks)
        y = len(self.img)
        x = len(np.transpose(self.img))
        if self.mcpp.check_ratio_is_set():
            l1 = np.linspace(0, x, 4)
            l2 = conv(np.floor(l1 * self.mcpp.ratio))
            plt.xticks(l1, l2)
            l1 = np.linspace(0, y, 4)
            l2 = conv(np.floor(l1 * self.mcpp.ratio))
            plt.yticks(l1, l2)
            plt.xlim(0, x)
            plt.ylim(y, 0)

        plt.subplot(224)
        self.plot_y_int()
        if self.mcpp.check_ratio_is_set():
            plt.xlabel("mm", fontsize=fontsize)
        else:
            plt.xlabel("pixels", fontsize=fontsize)
        plt.grid()
        plt.xticks(fontsize=ftsizeticks)
        plt.yticks(fontsize=ftsizeticks)
        plt.title("Integral along the y-axis", fontsize=fontsize)
        if not (np.isnan(self.popty[0])):
            plt.ylim([0, max(self.Iy - self.offsety) * 1.1])
        plt.tight_layout()
        if fname is not None:
            fig.savefig(fname)
        return fig


###############################################################################


class FitInterface:
    """
    Super class to do the fit of the MCP pictures
    Need to be define 
    self.fitfunc : the fit function
    self.labels : the names the parameters
    
    """

    def __init__(self):
        self.params1 = []
        self.errors1 = []
        self.params2 = []
        self.errors2 = []
        self.labels = []
        self.title1 = "\nIntegral along the x-axis\n"
        self.title2 = "\nIntegral along the y-axis\n"

    def do_fit(self, x1, y1, x2=[], y2=[], p0=None):
        """
        To do the fit y = f(x)

        Parameters
        ----------
        x1 : array of float
            the first x input data 
        y1 : array of float
            the first y input data
        x2 : array of float, optional
            the second x input data 
        y2 : array of float, optional
            the second y input data
        p0 : array of floats
            the guessed parameters to help the fit

        Returns
        -------
        None.

        """

        # self.fitfunc has te be defined
        popt, pcov = curve_fit(self.fitfunc, x1, y1)
        self.params1 = popt
        self.errors1 = np.diag(pcov)

        if len(x2) > 0:
            popt, pcov = curve_fit(self.fitfunc, x2, y2)
            self.params2 = popt
            self.errors2 = np.diag(pcov)

        if len(self.labels) < len(self.params1):
            self.labels = []
            for i in np.arange(len(self.params1)):
                self.labels.append("")

    def __repr__(self):
        """
        To turn the parameters of the fit to a string 

        Returns
        -------
        res : str
            the string containing the result of the fit

        """
        res = self.title1
        for i in np.arange(len(self.params1)):
            res += self.labels[i] + ':\t' + num2str(self.params1[i])
            res += " ± " + num2str(self.errors1[i]) + "\n"
        if len(self.params2) > 0:
            res += self.title2
        for i in np.arange(len(self.params2)):
            res += self.labels[i] + ':\t' + num2str(self.params2[i])
            res += " ± " + num2str(self.errors2[i]) + "\n"
        return res


###############################################################################


class SimpleGaussian(FitInterface):
    """
    A gaussian fit of the integral along the x and y axis
    """

    def __init__(self, x1, y1, x2, y2):
        """
        The constructor of the class

        Parameters
        ----------
        x1 : array of float
            the x axis
        y1 : array of float
            integral along the x axis
        x2 : array of float
            the y axis
        y2 : array of float
            integral along the y axis

        """
        super().__init__()
        self.labels = ["Ampli", "Center", "Sigma", "Offset"]
        self.fitfunc = gaussian_offset
        try:
            self.do_fit(x1, y1, x2, y2)
        except (Exception,):
            print("The Fit has failed")
            self.params1 = np.ones(len(self.labels)) + np.nan
            self.params2 = self.params1
            self.errors1 = self.params1
            self.errors2 = self.params1

    def do_fit(self, x1, y1, x2, y2):
        """
        To do the fit y = f(x)

        Parameters
        ----------
        x1 : array of float
            the first x input data 
        y1 : array of float
            the first y input data
        x2 : array of float, optional
            the second x input data 
        y2 : array of float, optional
            the second y input data 

        Returns
        -------
        None.

        """
        popt, pcov = curve_fit(gaussian, x1, y1, bounds=(0, np.inf))
        p0 = np.concatenate([popt, [min(y1)]])
        popt, pcov = curve_fit(gaussian_offset, x1, y1, bounds=(0, np.inf), p0=p0)
        self.params1 = popt
        self.errors1 = np.diag(pcov)

        popt, pcov = curve_fit(gaussian, x2, y2, bounds=(0, np.inf))
        p0 = np.concatenate([popt, [min(y2)]])
        popt, pcov = curve_fit(gaussian_offset, x2, y2, bounds=(0, np.inf), p0=p0)
        self.params2 = popt
        self.errors2 = np.diag(pcov)


###############################################################################


class FilteredGaussian(FitInterface):

    def __init__(self, x1, y1, x2, y2):
        """
        The constructor of the class

        Parameters
        ----------
        x1 : array of float
            the x axis
        y1 : array of float
            integral along the x axis
        x2 : array of float
            the y axis
        y2 : array of float
            integral along the y axis

        """
        super().__init__()
        self.labels = ["Ampli", "Center", "Sigma", "Offset"]
        self.fitfunc = gaussian_offset
        try:
            self.params1, self.errors1 = fit_gaussian_offset_filtered(x1, y1)
            self.params2, self.errors2 = fit_gaussian_offset_filtered(x2, y2)
        except (Exception,):
            print("The Fit has failed")
            self.params1 = np.ones(len(self.labels)) + np.nan
            self.params2 = self.params1
            self.errors1 = self.params1
            self.errors2 = self.params1


###############################################################################


class TwoGaussians(FitInterface):

    def __init__(self, x1, y1, x2, y2):
        """
        The constructor of the class

        Parameters
        ----------
        x1 : array of float
            the x axis
        y1 : array of float
            integral along the x axis
        x2 : array of float
            the y axis
        y2 : array of float
            integral along the y axis

        """
        super().__init__()
        self.fitfunc = two_gaussian_offset
        self.labels = ["Ampli 1", "Center1", "Sigma 1", "Ampli 2", "Center2",
                       "Sigma 2", "Offset"]
        try:
            self.do_fit(x1, y1, x2, y2)
        except (Exception,):
            print("The Fit has failed")
            self.params1 = np.ones(len(self.labels)) + np.nan
            self.params2 = self.params1
            self.errors1 = self.params1
            self.errors2 = self.params1

    def do_fit(self, x1, y1, x2, y2):
        """
        To do the fit y = f(x)

        Parameters
        ----------
        x1 : array of float
            the first x input data 
        y1 : array of float
            the first y input data
        x2 : array of float, optional
            the second x input data 
        y2 : array of float, optional
            the second y input data 

        Returns
        -------
        None.

        """
        popt, pcov = curve_fit(two_gaussian, x1, y1, bounds=(0, np.inf))
        p0 = np.concatenate([popt, [min(y1)]])
        popt, pcov = curve_fit(two_gaussian_offset, x1, y1, p0=p0,
                               bounds=(0, np.inf))
        self.params1, self.errors1 = popt, np.diag(pcov)

        popt, pcov = curve_fit(two_gaussian, x2, y2, bounds=(0, np.inf))
        p0 = np.concatenate([popt, [min(y2)]])
        popt, pcov = curve_fit(two_gaussian_offset, x2, y2, p0=p0,
                               bounds=(0, np.inf))
        self.params2, self.errors2 = popt, np.diag(pcov)


###############################################################################


def gaussian_offset(x, a, x0, s0, c):
    """
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
    """
    return a * normal_distribution(x, s0, x0) + c


def gaussian(x, a, x0, s0):
    """
    Gaussian distribution
    f(x) = amplitude/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2)
    
    * Parameters
        * x:  an np array
        * a:  the amplitude
        * s0: floating number, the standard deviation
        * x0: floating number, the mean value, center of the distribution
    * Returns
        * the value of the distribution
    """
    return gaussian_offset(x, a, x0, s0, 0)


def normal_distribution(x, s0, x0):
    """
    Normal distribution 
    f(x) = 1/sqrt(2pi)/sigma * exp(-1/2 {(x-mu)/sigma}^2)
    * Parameters
        * x:  an np array
        * s0: floating number, the standard deviation
        * x0: floating number, the mean value, center of the distribution
    * Returns
        the value of the distribution
    """
    return 1 / np.sqrt(2 * np.pi) / s0 * np.exp(-(((x - x0) / s0) ** 2) / 2)


def two_gaussian(x, a1, x1, s1, a2, x2, s2):
    """
    Sum of two gaussian distribution

    Parameters
    ----------
    x : float, numpy array
        the variable.
    a1 : float
        Amplitude of the first distribution.
    x1 : float
        Mean value of the first distribution.
    s1 : float
        Standard deviation of the first distribution.
    a2 : float
        Amplitude of the second distribution.
    x2 : float
        Mean value of the second distribution.
    s2 : float
        Standard deviation of the second distribution.

    Returns
    -------
    float, numpy array
        Value of the distribution.

    """
    return a1 * normal_distribution(x, s1, x1) + a2 * normal_distribution(x, s2, x2)


def two_gaussian_offset(x, a1, x1, s1, a2, x2, s2, c):
    """
    Sum of two gaussian distribution with an offset

    Parameters
    ----------
    x : float, numpy array
        the variable.
    a1 : float
        Amplitude of the first distribution.
    x1 : float
        Mean value of the first distribution.
    s1 : float
        Standard deviation of the first distribution.
    a2 : float
        Amplitude of the second distribution.
    x2 : float
        Mean value of the second distribution.
    s2 : float
        Standard deviation of the second distribution.
    c : float
        The offset.

    Returns
    -------
    float, numpy array
        Value of the distribution.

    """
    return a1 * normal_distribution(x, s1, x1) + a2 * normal_distribution(x, s2, x2) + c


def num2str(a, n=3):
    """
    To turn a number into a string

    Parameters
    ----------
    a : float
        the number to convert.
    n : int, optional
        number of significant digits. The default is 3.

    Returns
    -------
    str
        the string.

    """
    n = str(n)
    y = '%.' + n + 'g'
    return '%s' % float(y % a)


def fit_gaussian_offset_filtered(x, y):
    """
    Fit with the function gaussian_offset.
    * Parameters
        * x: numpy array
        * y: numpy array
    * Returns
        * popt,perr: numpy arrays, the parameters and the error of the fit
    """
    x = np.array(x)
    y = np.array(y)
    s = 100
    a = max(y) / np.sqrt(2 * np.pi) / s
    x0 = x[np.argmax(y)]
    c = min(y)
    p0 = [a, x0, s, c]
    try:
        popt, pcov = curve_fit(gaussian_offset, x, y, p0=p0, bounds=(0, np.inf))
        mask = np.logical_or(np.abs(y - y.max()) / y.max() < 0.2,
                             np.abs((y - popt[3]) / popt[3]) < 0.2)
        x0 = x[mask]
        y0 = y[mask]
        popt, pcov = curve_fit(gaussian_offset, x0, y0, p0=popt, bounds=(0, np.inf))
        mask = np.logical_or(np.abs(x - popt[1]) / popt[1] < 0.1,
                             np.abs((y - popt[3]) / popt[3]) < 0.05)
        x0 = x[mask]
        y0 = y[mask]
        popt, pcov = curve_fit(gaussian_offset, x0, y0, p0=popt, bounds=(0, np.inf))
        mask = np.logical_or(np.abs(x - popt[1]) / popt[1] < 0.1,
                             np.abs((y - popt[3]) / popt[3]) < 0.1)
        x0 = x[mask]
        y0 = y[mask]
        popt, pcov = curve_fit(gaussian_offset, x0, y0, p0=popt, bounds=(0, np.inf))
        perr = np.sqrt(np.diag(pcov))
    except (Exception,):
        print("The fit failed")
    return popt, perr


def reshape_img(img, ix, iy, lm):
    """
    To reshape an image to a squared one
    * Parameters
        * img: np.array([np.array]) the image array
        * ix: the index of the center of the square
        * iy: the index of the center of the square
        * lm: the half length of the square
    *Returns
        * The reshaped picture as an array
    """
    ix, iy, lm = int(ix), int(iy), int(lm)
    max_x, max_y = len(img.T), len(img)
    min_x, min_y = 0, 0
    if ix - lm > 0:
        min_x = ix - lm
    if iy - lm > 0:
        min_y = iy - lm
    if ix + lm < max_x:
        max_x = ix + lm
    if iy + lm < max_y:
        max_y = iy + lm
    ix_r = np.arange(min_x, max_x)
    iy_r = np.arange(min_y, max_y)
    img = img[iy_r]
    img = img.T[ix_r].T
    return img


def import_image(fname, reshape=[]):
    """
    To import the picture as an array
    * Parameters
        * fname: string, name of the file
        * reshape: array, to reshape the picture as a square [ix,iy,l]
    * Returns
        * the picture as 2D array
    """
    file_format = ["tif", "jpg", "jpeg", "png", "asc", "bmp"]
    ext = fname.split('.')[len(fname.split('.')) - 1]
    ext = ext.lower()
    if not (ext in file_format):
        raise TypeError(ext + ' not in ' + str(file_format))
    # if asc file
    if ext == "asc":
        with codecs.open(fname, encoding='utf-8-sig') as ff:
            img = np.array([[float(x) for x in line.split()] for line in ff])
    else:
        img = np.double(mpimg.imread(fname))
        img = rgb2gray(img)
    if len(reshape) == 3:
        img = reshape_img(img, reshape[0], reshape[1], reshape[2])

    n_index = np.concatenate(img).size
    n_index = int(0.01 * n_index)
    img -= np.mean(np.sort(np.concatenate(img))[:n_index])

    return img


def integrate_picture_along_y(img):
    """
    To integrate the picture along th Y axis
    * Parameters
        * img: image as a 2D numpy array
    * Returns
        * (pix,integral): A tuple with pix the pixel numbers as a numpy array
        and 'integral' the integral as a numpy array
    """
    integral = np.zeros_like(img[0])
    for line in img:
        integral = integral + line
    pix = np.arange(len(integral))
    integral = integral / len(img)
    return pix, integral


def integrate_picture_along_x(img):
    """
    To integrate the picture along th X axis
    *Parameters
        * img: image as a 2D numpy array
    * Returns
        * (pix,integral): A tuple with pix the pixel numbers as a numpy array and
        'integral' the integral as a numpy array
    """
    pix, ix = integrate_picture_along_y(np.transpose(img))
    integral = np.array([])
    for i in ix:
        integral = np.concatenate([integral, [i]])
    return pix, integral


def get_index_str(n, i):
    """
    To convert an int 'i' to a string
    * Example
        getIndexStr(100,15) #returns '015'
    """
    if i < 0 or i > n:
        raise ValueError("N >= i or i > 0 is required")
    lm = len(str(n))
    res = str(i)
    while lm > len(res):
        res = "0" + res
    return res


def significant(x, sig=4):
    """
    To turn a float as a str with a certain number of significant digits
    """
    res = np.round(x, sig - int(np.floor(np.log10(np.abs(x)))) - 1)
    return str(res)


###################################################################################


class MCPParams:
    """
    Class to store the parameters of the MCP to adapt the analysis
    
    #### Attributes
    * MCPParams.R: radius of the mirror in mm
    * MCPParams.x0: x position of the center of the mirror in pixels
    * MCPParams.y0: y position of the center of the mirror in pixels
    * MCPParams.R0: radius of the mirror in pixels
    * MCPParams.ratio: mm/pixels ratio
    * MCPParams.canBePlot: boolean to know if the mirror can be plot
    * MCPParams.ratioIsSet: boolean to know if a ratio has been defined
    """

    def __init__(self, name=None, r=None, x0=None, y0=None,
                 r0=None, ratio=None):
        """
            Constructor of the class
            * Parameters
                * name: (optional) string, the name of the MCP
                * R: (optional), float, radius of the mirror in mm
                * x0: (optional), int, x position of the center of the mirror in pixels
                * y0: (optional), int, y position of the center of the mirror in pixels
                * R0: (optional), int, radius of the mirror in pixels
                * ratio: (optional), mm/pixels ratio
                    if R and R0 have been defined, then ratio is defined automatically
            """
        self.name = name
        self.R = r
        self.x0 = x0
        self.y0 = y0
        self.R0 = r0
        self.ratio = ratio
        if r is not None and r0 is not None:
            self.ratio = r / r0
        self.ratioIsSet = False
        self.check_ratio_is_set()

    def __repr__(self):
        """
        To translate the object as a string
        * Returns
            * the string
        * Example
            params = MCPParams()
            print(params)
            #or
            r = params.__repr__()
        """
        res = "MCP Parameters\n"
        res += "name: " + str(self.name) + "\n"
        res += "R: " + str(self.R) + "\n"
        res += "x0: " + str(self.x0) + "\n"
        res += "y0: " + str(self.y0) + "\n"
        res += "R0: " + str(self.R0) + "\n"
        res += "ratio: " + str(self.ratio) + "\n"
        return res

    def define_ratio(self, mm, pix):
        """
        To define the ratio mm vs pixels
        * Parameters
            mm: float, a distance in mm
            pix: float, the equivalent distance in pixels
        """
        try:
            r = mm / pix
            self.ratio = r
            self.check_ratio_is_set()
        except (Exception,):
            print("The setting of the ratio has failed")

    def check_ratio_is_set(self):
        """
        To check is the ratio has been set
        * Return
            boolean
        """
        if self.ratio is None:
            self.ratioIsSet = False
        else:
            self.ratioIsSet = True
        return self.ratioIsSet

    def check_all_set(self):
        """
        To check is all has been set
        * Return
            boolean
        """
        if self.R is None:
            return False
        if self.x0 is None:
            return False
        if self.y0 is None:
            return False
        if self.R0 is None:
            return False
        if self.ratio is None:
            return False
        return True

    def save_conf(self, fname):
        """
        To save the parameters of the MCP as a binary file
        Use .mcp extension
        * Parameters
            fname: string, the name of the binary file
        * Example
            params = MCPParams()
            params.save_config("config.mcp")
        """
        with open(fname, 'wb') as f1:
            dill.dump(self, f1)
        print("Parameters saved as", fname)


###############################################################################


def import_config(fname):
    """
    To import the MCP parameters from a binary file
    * Parameters
        fname: string, the file's name
    """
    pp = None
    try:
        with open(fname, 'rb') as f1:
            pp = dill.load(f1)
    except (Exception,):
        print("Importation of", fname, "has failed")
    return pp
