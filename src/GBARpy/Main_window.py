#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:00:25 2020

@author: samuel.niang@cern.ch
"""

import tkinter 
from PIL import ImageTk,Image  
from tkinter import filedialog
from os import path
from GBARpy.MCPPicture import BeamSpot, gaussian_offset
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class MainWindow(tkinter.Tk):
    
    def __init__(self):
        
        ### Fenetre principale
        tkinter.Tk.__init__(self)
        self.beamSpot = True
        self.title("GBAR MCPy")
        self.geometry("900x600")
        self.resizable(False,True)
        self.canBeAnalysed = False
        self.canBeExported = False
        
        
        ### Cadre 0 Contrôle
        self.frame0 = tkinter.Frame(self,highlightbackground="black",highlightthickness=1)
        self.frame0.pack(side='top',fill='x')

        
        ### Importation de l'image
        self.picname = tkinter.StringVar()
        self.picadress = ""
        self.savedAsText = tkinter.StringVar()
        self.frame0_c = tkinter.Frame(self.frame0)
        self.frame0_c.pack(side='left')
        self.frame0_c.columnconfigure(0, pad=3)
        self.frame0_c.columnconfigure(0, pad=1)
        self.frame0_c.rowconfigure(0, pad=3)
        self.frame0_c.rowconfigure(1, pad=3)
        self.frame0_c.rowconfigure(2, pad=3)
        self.btn_choose = tkinter.Button(self.frame0_c, text='Open image', command=self.open_img)
        self.btn_choose.grid(row=0,column=0)
        self.picnamelabel = tkinter.Label(self.frame0_c, textvariable=self.picname)
        self.picnamelabel.grid(row=0,column=1)
        self.btn_analysis = tkinter.Button(self.frame0_c, text='Analyse the picture', command=self.analyse)
        self.btn_analysis.grid(row=1,column=0)
        """
        self.export = tkinter.Button(self.frame0_c, text='Export as PDF', command=self.exportAsPDF)
        self.export.grid(row=2,column=0)
        self.savedAs = tkinter.Label(self.frame0_c, textvariable=self.savedAsText)
        self.savedAs.grid(row=2,column=1)
        
        img = Image.open("img/GBAR_logo.png")
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tkinter.Label(self.frame0, image=img)
        panel.image = img
        panel.pack(side='right')
        """
        
        ### Cadre 1 Importation de l'image
        self.frame1 = tkinter.Frame(self, width=400, height=400,
                       highlightbackground="black",highlightthickness=1)
        self.frame1.pack(side='left')
        self.img1Label = tkinter.Label(self.frame1)
        

        ### Cadre 2 Analyse de l'image
        self.frame2 = tkinter.Frame(self, width=400, height=400,
                       highlightbackground="black",highlightthickness=1)
        self.frame2.pack(side='right')
        
        
       


        
    
    def open_img(self):
        self.picadress = filedialog.askopenfilename(title='Open image')
        self.picname.set(path.split(self.picadress)[-1])
        img = Image.open(self.picadress)
        img = img.resize((400, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.img1Label.configure(image=img)
        self.img1Label.image=img
        self.img1Label.pack(fill='both')
        self.canBeAnalysed = True
        self.canBeExported = False
        print(img)
        
    def analyse(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
    
        if self.canBeAnalysed == False:
            self.open_img()
            
        ### Analysis
        self.beamSpot = BeamSpot(self.picadress)
        
        
        ### plot
        fig = Figure(figsize=(5,2.5), dpi=100)
        pplt = fig.add_subplot(111)
        popt = self.beamSpot.poptx
        label = "X axis"
        if np.any(np.isnan(popt)):
            pplt.plot(self.beamSpot.pix,self.beamSpot.Ix,'.',ms=1,label=label)
        else:
            D = self.beamSpot.Ix
            p = pplt.plot(self.beamSpot.pix,D-popt[3],'.',ms=1,label=label)
            pplt.plot(self.beamSpot.pix,gaussian_offset(self.beamSpot.pix,popt[0],popt[1],popt[2],0),color=p[0].get_color())
        popt = self.beamSpot.popty
        label = "Y axis"
        if np.any(np.isnan(popt)):
            pplt.plot(self.beamSpot.piy,self.beamSpot.Iy,'.',ms=1,label=label)
        else:
            D = self.beamSpot.Iy
            p = pplt.plot(self.beamSpot.piy,D-popt[3],'.',ms=1,label=label)
            pplt.plot(self.beamSpot.piy,gaussian_offset(self.beamSpot.piy,popt[0],popt[1],popt[2],0),color=p[0].get_color())
        pplt.set_xlim([0,np.max(self.beamSpot.pix)])
        pplt.legend()
        canvas = FigureCanvasTkAgg(fig, master=self.frame2)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        ### Write the result
        res = "Integral along the x-axis: \n"
        res += "A  = "+str(np.floor(self.beamSpot.Ax))+"\t"
        res += "r0 = "+str(np.floor(self.beamSpot.r0x))+"\t"
        res += "sig = "+str(np.floor(self.beamSpot.sigx))+"\n\n"
        res += "Integral along the y-axis: \n"
        res += "A  = "+str(np.floor(self.beamSpot.Ay))+"\t"
        res += "r0 = "+str(np.floor(self.beamSpot.r0y))+"\t"
        res += "sig = "+str(np.floor(self.beamSpot.sigy))+"\n\n"
        tkinter.Label(self.frame2, text=res).pack()
        
        self.canBeExported = True
        
    def exportAsPDF(self):
        if self.canBeAnalysed == False:
            self.open_img()
            
        if self.canBeExported == False:
            self.analyse()
        fig,fname = self.beamSpot.plot()
        self.savedAsText.set("Saved as "+path.split(fname)[-1])
