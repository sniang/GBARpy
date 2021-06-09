#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:07:44 2021

@author: sniang
"""
import numpy as np
from scipy.optimize import curve_fit


class FitInterface():
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
    
    
    def Fit(self,x1,y1,x2=[],y2=[],p0=None):
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
        
        ### self.fitfunc has te be defined
        popt,pcov = curve_fit(self.fitfunc,x1,y1)
        self.params1 = popt
        self.errors1 = np.diag(pcov)
        
        if len(x2) > 0:
            popt,pcov = curve_fit(self.fitfunc,x2,y2)
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
            res += self.labels[i]+':\t'+num2str(self.params1[i])
            res += " ± "+num2str(self.errors1[i])+"\n"
        if len(self.params2) > 0:
            res+=self.title2
        for i in np.arange(len(self.params2)):
            res += self.labels[i]+':\t'+num2str(self.params2[i])
            res += " ± "+num2str(self.errors2[i])+"\n"
        return res


###############################################################################


class SimpleGaussian(FitInterface):
    """
    A gaussian fit of the integral along the x and y axis
    """
    
    def __init__(self,x1,y1,x2,y2):
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
        self.labels = ["Ampli","Center","Sigma","Offset"]
        self.fitfunc = gaussian_offset
        try:
            self.Fit(x1,y1,x2,y2)
        except:
            print("The Fit has failed")
            self.params1 = np.ones(len(self.labels))+np.nan
            self.params2 = self.params1
            self.errors1 = self.params1
            self.errors2 = self.params1
    
    def Fit(self,x1,y1,x2,y2):
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
        popt,pcov = curve_fit(gaussian,x1,y1,bounds=(0,np.inf))
        p0 = np.concatenate([popt,[min(y1)]])
        popt,pcov = curve_fit(gaussian_offset,x1,y1,bounds=(0,np.inf),p0=p0)
        self.params1 = popt
        self.errors1 = np.diag(pcov)
        
        popt,pcov = curve_fit(gaussian,x2,y2,bounds=(0,np.inf))
        p0 = np.concatenate([popt,[min(y2)]])
        popt,pcov = curve_fit(gaussian_offset,x2,y2,bounds=(0,np.inf),p0=p0)
        self.params2 = popt
        self.errors2 = np.diag(pcov)


###############################################################################


class FilteredGaussian(FitInterface):
    
    def __init__(self,x1,y1,x2,y2):
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
        self.labels = ["Ampli","Center","Sigma","Offset"]
        self.fitfunc = gaussian_offset
        try:
            self.params1,self.errors1 = fit_gaussian_offset_filtered(x1,y1)
            self.params2,self.errors2 = fit_gaussian_offset_filtered(x2,y2)
        except:
            print("The Fit has failed")
            self.params1 = np.ones(len(self.labels))+np.nan
            self.params2 = self.params1
            self.errors1 = self.params1
            self.errors2 = self.params1

###############################################################################

class TwoGaussians(FitInterface):
    
    def __init__(self,x1,y1,x2,y2):
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
        self.fitfunc = twoGaussians_offset
        self.labels = ["Ampli 1","Center1","Sigma 1","Ampli 2","Center2",
                       "Sigma 2","Offset"]
        try:
            self.Fit(x1,y1,x2,y2)
        except:
            print("The Fit has failed")
            self.params1 = np.ones(len(self.labels))+np.nan
            self.params2 = self.params1
            self.errors1 = self.params1
            self.errors2 = self.params1
    
    def Fit(self,x1,y1,x2,y2):
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
        popt,pcov = curve_fit(twoGaussians,x1,y1,bounds=(0,np.inf))
        p0 = np.concatenate([popt,[min(y1)]])
        popt,pcov = curve_fit(twoGaussians_offset,x1,y1,p0 = p0,
                              bounds=(0,np.inf))
        self.params1,self.errors1 = popt,np.diag(pcov)
        
        popt,pcov = curve_fit(twoGaussians,x2,y2,bounds=(0,np.inf))
        p0 = np.concatenate([popt,[min(y2)]])
        popt,pcov = curve_fit(twoGaussians_offset,x2,y2,p0 = p0,
                              bounds=(0,np.inf))
        self.params2,self.errors2 = popt,np.diag(pcov)
        
###############################################################################            
        



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

    

def gaussian(x,a,x0,s0):
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
    return gaussian_offset(x,a,x0,s0,0)

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

def twoGaussians(x,a1,x1,s1,a2,x2,s2):
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
    return a1*normal_distribution(x,s1,x1)+a2*normal_distribution(x,s2,x2)

def twoGaussians_offset(x,a1,x1,s1,a2,x2,s2,c):
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
    return a1*normal_distribution(x,s1,x1)+a2*normal_distribution(x,s2,x2) + c
                   
                           
def num2str(a,n=3):
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
    print(a)
    y = '%.'+n+'g'
    print(y)
    return '%s' % float(y % a)

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
    return popt,perr