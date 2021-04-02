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

class BeamSpot:
    """
    Class to analyse the pictures comming from the MCP
    
    #### Attributes
    * BeamSpot.fname: string, file name of the picture
    * BeamSpot.img: 2D array, picture as an array
    * BeamSpot.pix: the pixels along the x axis
    * BeamSpot.piy: the pixels along the y axis
    * BeamSpot.Ix: array of floats, integral along the x axis
    * BeamSpot.Iy: array of floatt, integral along the y axis
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
    """
    
    
    def __init__(self,fname,reshape=[]):
        """
        Constructor of the class
        * Parameters
            * fname: string, file name of the picture, the accepted file format ["tif","jpg","jpeg","png","asc","bmp"]
            * reshape: array of 3 integers (optional), to reshape the pictures (square): x,y,length
        * Example
            import GBARpy.MCPPicture as mcp
            bs = mcp.BeamSpot("name.tif")
        """
        self.fname = fname
        self.reshape = reshape
        self.img = import_image(self.fname,self.reshape)
        self.pix,self.Ix = integrate_picture_along_X(self.img)
        self.piy,self.Iy = integrate_picture_along_Y(self.img)
        self.poptx,self.perrx = fit_gaussian_offset_filtered(self.pix,self.Ix)
        self.popty,self.perry = fit_gaussian_offset_filtered(self.piy,self.Iy)
        self.Ax,self.r0x,self.sigx,self.offsetx = self.poptx
        self.Ay,self.r0y,self.sigy,self.offsety = self.popty


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
        res = "Original picture: "+self.fname+'\n\n'
        res += "Integral along the x-axis\n"
        res += "A  = "+str(self.Ax)+"\n"
        res += "r0 = "+str(self.r0x)+"\n"
        res += "sig = "+str(self.sigx)+"\n"
        res += "offset = "+str(self.offsetx)+"\n\n"
        res += "Integral along the y-axis\n"
        res += "A  = "+str(self.Ay)+"\n"
        res += "r0 = "+str(self.r0y)+"\n"
        res += "sig = "+str(self.sigy)+"\n"
        res += "offset = "+str(self.offsety)+"\n"
        return res
    
    
    def plot_Y_int(self,label=""):
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
        if np.any(np.isnan(popt)):
            plt.plot(self.piy,self.Iy,'.',ms=1,label=label)
        else:
            D = self.Iy
            p = plt.plot(self.piy,D-popt[3],'.',ms=1,label=label)
            plt.plot(self.piy,gaussian_offset(self.piy,popt[0],popt[1],popt[2],0),color=p[0].get_color())
        plt.xlim([0,np.max(self.piy)])
        if len(label) != 0:
            plt.legend()
        
        
    def plot_X_int(self,label=""):
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
        if np.any(np.isnan(popt)):
            plt.plot(self.pix,self.Ix,'.',ms=1,label=label)
        else:
            D = self.Ix
            p = plt.plot(self.pix,D-popt[3],'.',ms=1,label=label)
            plt.plot(self.pix,gaussian_offset(self.pix,popt[0],popt[1],popt[2],0),color=p[0].get_color())
        plt.xlim([0,np.max(self.pix)])
        if len(label) != 0:
            plt.legend()
        
        
    def plot_X_int_revert(self):
        """
        To plot the integral of the picture along the "x" axis and reverse the picture
        * Example
            import GBARpy.MCPPicture as mcp
            bs = mcp.BeamSpot("name.tif")
            bs.plot_X_int("Integral along the x-axis")
        """
        pix, Ix = self.pix,self.Ix
        popt = self.poptx
        if np.any(np.isnan(popt)):
            plt.plot(Ix,pix,'.',ms=1)
        else:
            D = Ix - popt[3]
            p = plt.plot(D,pix,'.',ms=1)
            G = gaussian_offset(pix,popt[0],popt[1],popt[2],0)
            plt.plot(G,pix,color=p[0].get_color())
        plt.ylim([np.max(pix),0])
    
    
    def plot(self,fname="",figsize=(12,10),fontsize=12,ftsizeticks=12):
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
        if len(fname) == 0:
            fname = None
        fig = plt.figure(figsize=figsize)
        
        plt.subplot(221)
        self.plot_X_int_revert()
        plt.ylabel("pixels",fontsize=fontsize)
        plt.grid()
        plt.xticks(fontsize=ftsizeticks)
        plt.yticks(fontsize=ftsizeticks)
        plt.title(r"$A_x = $"+str(np.around(self.Ax,1))+" $\sigma_x = $"+str(np.around(self.sigx,1))+" $r_{0x} = $"+str(np.around(self.r0x,1)),fontsize=fontsize,loc='left')
        if not(np.isnan(self.poptx[0])):
            plt.xlim([0,self.Ax/self.sigx/np.sqrt(2*np.pi)])

        plt.subplot(222)
        plt.imshow(self.img,vmin=self.img.min(),vmax=self.img.max())
        plt.xticks(fontsize=ftsizeticks)
        plt.yticks(fontsize=ftsizeticks)
        
        plt.subplot(224)
        self.plot_Y_int()
        plt.xlabel("pixels",fontsize=fontsize)
        plt.grid()
        plt.xticks(fontsize=ftsizeticks)
        plt.yticks(fontsize=ftsizeticks)
        plt.title(r"$A_y = $"+str(np.around(self.Ay,1))+" $\sigma_y = $"+str(np.around(self.sigy,1))+" $r_{0y} = $"+str(np.around(self.r0y,1)),fontsize=fontsize,loc='left')
        if not(np.isnan(self.popty[0])):
            plt.ylim([0,self.Ay/self.sigy/np.sqrt(2*np.pi)])
        plt.tight_layout()
        if fname != None:
            fig.savefig(fname)
        return fig
    
    
def normal_distribution(x,s0,x0):
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
    return 1/np.sqrt(2*np.pi)/s0*np.exp(-(((x-x0)/s0)**2)/2)


def gaussian_offset(x,a,x0,s0,c):
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
    return a*normal_distribution(x,s0,x0) + c


def fit_gaussian_offset_filtered(x,y):
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
    a = max(y)/np.sqrt(2*np.pi)/s
    x0 = x[np.argmax(y)]
    c = min(y)
    p0 = [a,x0,s,c]
    try:
        popt,pcov = curve_fit(gaussian_offset,x,y,p0=p0,bounds=(0,np.inf))
        mask = np.logical_or(np.abs(y-y.max())/y.max() < 0.2,
                             np.abs((y-popt[3])/popt[3]) < 0.2)
        x0 = x[mask]
        y0 = y[mask]
        popt,pcov = curve_fit(gaussian_offset,x0,y0,p0=popt,bounds=(0,np.inf))
        mask = np.logical_or(np.abs(x-popt[1])/popt[1] < 0.1,
                             np.abs((y-popt[3])/popt[3]) < 0.05)
        x0 = x[mask]
        y0 = y[mask]
        popt,pcov = curve_fit(gaussian_offset,x0,y0,p0=popt,bounds=(0,np.inf))
        mask = np.abs(y-gaussian_offset(x,*popt))/y < 0.1
        mask = np.logical_or(np.abs(x-popt[1])/popt[1] < 0.1,
                             np.abs((y-popt[3])/popt[3]) < 0.1)
        x0 = x[mask]
        y0 = y[mask]
        popt,pcov = curve_fit(gaussian_offset,x0,y0,p0=popt,bounds=(0,np.inf))
        perr = np.sqrt(np.diag(pcov))
    except:
        print("The fit failed")
        popt = [np.nan,np.nan,np.nan,np.nan]
        perr = [np.nan,np.nan,np.nan,np.nan]
    return popt,perr

###################################################################################

def reshapeIMG(img,ix,iy,l):
    """
    To reshape an image to a squared one
    * Parameters
        * img: np.array([np.array]) the image array
        * ix: the index of the center of the square
        * iy: the index of the center of the square
        * l: the half length of the square
    *Returns
        * The reshaped picture as an array
    """
    ix = int(ix)
    iy = int(iy)
    IX = np.arange(ix-l,ix+l)
    IY = np.arange(iy-l,iy+l)
    img = img[IY]
    img = ((img.T)[IX]).T
    return img


def import_image(fname,reshape=[]):
    """
    To import the picture as an array
    * Parameters
        * fname: string, name of the file
        * reshape: array, to reshape the picture as a square [ix,iy,l]
    * Returns
        * the picture as 2D array
    """
    fileformat = ["tif","jpg","jpeg","png","asc","bmp"]
    ext = fname.split('.')[len(fname.split('.'))-1]
    ext = ext.lower()
    if not(ext in fileformat):
        raise TypeError(ext+' not in '+str(fileformat))
    # if asc file
    if   ext == "asc":
            with codecs.open(fname, encoding='utf-8-sig') as ff:
                img = np.array([[float(x) for x in line.split()] for line in ff])
    else:
        img = np.double(mpimg.imread(fname))
        img = rgb2gray(img)
    if len(reshape) == 3:
        img = reshapeIMG(img,reshape[0],reshape[1],reshape[2])
        
    N = np.concatenate(img).size
    N = int(0.01*N)
    img -= np.mean(np.sort(np.concatenate(img))[:N])
    
    return img


def integrate_picture_along_Y(img):
    """
    To integrate the picture along th Y axis
    * Parameters
        * img: image as a 2D numpy array
    * Returns
        * (pix,Iy): A tupple with pix the pixel numbers as a numpy array and Iy the integral as a numpy array
    """
    I = np.zeros_like(img[0])
    for l in img:
        I = I + l
    pix = np.arange(len(I))
    Iy = I/len(img)
    return pix,Iy


def integrate_picture_along_X(img):
    """
    To integrate the picture along th X axis
    *Parameters
        * img: image as a 2D numpy array
    * Returns
        * (pix,Ix): A tupple with pix the pixel numbers as a numpy array and Ix the integral as a numpy array
    """
    pix,ix = integrate_picture_along_Y(np.transpose(img))
    Ix = np.array([])
    for i in ix:
        Ix = np.concatenate([Ix,[i]])
    return pix,Ix


def getIndexStr(N,i):
    """
    To convert an int 'i' to a string
    * Example
        getIndexStr(100,15) #returns '015'
    """
    if i < 0 or i > N:
        raise ValueError("N >= i or i > 0 is required")
    l = len(str(N))
    res = str(i)
    while l > len(res):
        res = "0" + res
    return res



            
