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
import GBARpy
from GBARpy.MCPPicture import BeamSpot, gaussian_offset, import_config, import_image
from GBARpy.MCPPicture import MCPParams as mcpp
import pickle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

fontsize = 12

class MainWindow(tkinter.Tk):
    
    def __init__(self):
        ### Location of the static files
        static_addr = GBARpy.__file__
        static_addr = path.split(static_addr)[0]
        static_addr = path.join(static_addr,'static')
        self.mcp_param = mcpp()
        self.picadress = None
        
        
        ### Fenetre principale
        tkinter.Tk.__init__(self)
        self.beamSpot = True
        self.title("GBAR MCPy")
        self.geometry("1000x600")
        self.resizable(True,True)
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
        
        self.btn_mcpparams = tkinter.Button(self.frame0_c, text='MCP Parameters', command=self.defineMCPParams)
        self.btn_mcpparams.grid(row=2,column=0)
        
        """
        self.export = tkinter.Button(self.frame0_c, text='Export as PDF', command=self.exportAsPDF)
        self.export.grid(row=2,column=0)
        self.savedAs = tkinter.Label(self.frame0_c, textvariable=self.savedAsText)
        self.savedAs.grid(row=2,column=1)
        """
        
        add = path.join(static_addr,"GBAR_logo.png")
        img = Image.open(add)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tkinter.Label(self.frame0, image=img)
        panel.image = img
        panel.pack(side='right')
        self.tk.call('wm', 'iconphoto', self._w, tkinter.PhotoImage(file=add))
        self.iconphoto(False, tkinter.PhotoImage(file=add))
        
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
        try:
            self.picadress = filedialog.askopenfilename(title='Open image')
            self.picname.set(path.split(self.picadress)[-1])
            self.canBeAnalysed = True
            self.plotImage()
        except:
            print("Opening failed")
            self.canBeAnalysed = False
        
    
    def plotImage(self):
        def conv(a):
            b = []
            for e in a:
                b.append(str(e))
            return np.array(b)
        
        for widget in self.frame1.winfo_children():
            widget.destroy()
        if self.canBeAnalysed:   
            img = import_image(self.picadress)
            fig = Figure(figsize=(5,4))
            pplt = fig.add_subplot(111)
            pplt.imshow(img)
            pplt.set_xlabel('pixels',fontsize=fontsize)
            pplt.set_ylabel('pixels',fontsize=fontsize)
            if self.mcp_param.checkRatioIsSet():
                pplt.set_xlabel('mm',fontsize=fontsize)
                pplt.set_ylabel('mm',fontsize=fontsize)
                
                y = len(img)
                x = len(np.transpose(img))
                l = np.linspace(0,x,int(x/300))
                pplt.set_xticks(l)
                l = conv(np.floor(l*self.mcp_param.ratio))
                pplt.set_xticklabels(l)
                
                l = np.linspace(0,y,int(y/300))
                pplt.set_yticks(l)
                l = conv(np.floor(l*self.mcp_param.ratio))
                pplt.set_yticklabels(l)
            canvas = FigureCanvasTkAgg(fig, master=self.frame1)
            canvas.draw()
            canvas.get_tk_widget().pack()
        
    def analyse(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
    
        if self.canBeAnalysed == False:
            self.open_img()
        self.plotImage()
        ### Analysis
        self.beamSpot = BeamSpot(self.picadress,mcpp=self.mcp_param)
        
        
        ### plot
        fig = Figure(figsize=(5,2.5), dpi=100)
        pplt = fig.add_subplot(111)
        popt = self.beamSpot.poptx
        label = "along the x-axis"
        if np.any(np.isnan(popt)):
            pplt.plot(self.beamSpot.pix,self.beamSpot.Ix,'.',ms=1,label=label)
        else:
            D = self.beamSpot.Ix
            p = pplt.plot(self.beamSpot.pix,D-popt[3],'.',ms=1,label=label)
            pplt.plot(self.beamSpot.pix,gaussian_offset(self.beamSpot.pix,popt[0],popt[1],popt[2],0),color=p[0].get_color())
        popt = self.beamSpot.popty
        label = "along the y-axis"
        if np.any(np.isnan(popt)):
            pplt.plot(self.beamSpot.piy,self.beamSpot.Iy,'.',ms=1,label=label)
        else:
            D = self.beamSpot.Iy
            p = pplt.plot(self.beamSpot.piy,D-popt[3],'.',ms=1,label=label)
            pplt.plot(self.beamSpot.piy,gaussian_offset(self.beamSpot.piy,popt[0],popt[1],popt[2],0),color=p[0].get_color())
        pplt.set_xlim([0,np.max(self.beamSpot.pix)])
        pplt.grid()
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
        
    def defineMCPParams(self):
        MCPParamsWindow(self,self.mcp_param)

class MCPParamsWindow(tkinter.Toplevel):
    
    def __init__(self,master,mcp):
        tkinter.Toplevel.__init__(self,master)
        self.title("Define the MCP parameters")
        self.geometry("400x200")
        self.resizable(False,False)
        
        self.master = master
        self.mcp = mcp
        # The form
        tkinter.Label(self, text="MCP's name").grid(row=0)
        tkinter.Label(self, text="R (mm)").grid(row=1)
        tkinter.Label(self, text="x0 (pixels)").grid(row=2)
        tkinter.Label(self, text="y0 (pixels)").grid(row=3)
        tkinter.Label(self, text="R0 (pixels)").grid(row=4)
        tkinter.Label(self, text="ratio (mm/pixels)").grid(row=5)
        
        self.e_name  = tkinter.Entry(self)
        self.e_R     = tkinter.Entry(self)
        self.e_x0    = tkinter.Entry(self)
        self.e_y0    = tkinter.Entry(self)
        self.e_R0    = tkinter.Entry(self)
        self.e_ratio = tkinter.Entry(self)
                
        self.e_name.grid(row=0, column=1)
        self.e_R.grid(row=1, column=1)
        self.e_x0.grid(row=2, column=1)
        self.e_y0.grid(row=3, column=1)
        self.e_R0.grid(row=4, column=1)
        self.e_ratio.grid(row=5, column=1)
        
        self.fillform(self.mcp)
        
        # buttons
        self.frame0 = tkinter.Frame(self)
        self.frame0.grid(row=6, column = 0, columnspan = 3)
        
        self.set = tkinter.Button(self.frame0, text='Set',command=self.commandset).grid(row=0, column=0)
        self.save = tkinter.Button(self.frame0, text='Save',command=self.commandsave).grid(row=0, column=1)
        self.load = tkinter.Button(self.frame0, text='Load',command=self.commandload).grid(row=0, column=2)
        self.remove = tkinter.Button(self.frame0, text='Remove',command=self.commandremove).grid(row=0, column=3)

    def commandset(self):
        """
        To set the MCP parameters
        """
        try:
            pp = self.formToMCP()
            print(pp)
            self.mcp = pp
            self.master.mcp_param = pp
        except:
            print("Setting failed")
        
        
            
            
    def commandsave(self):
        """
        To save the parameters as an .mcp file
        """
        try:
            pp = self.formToMCP()
            f = filedialog.asksaveasfile(mode='wb', defaultextension=".mcp")
            pickle.dump(pp, f)
            print("Parameters saved as",f.name)
        except:
            print("Saving failed")
        finally:
            f.close()

        
        
    def commandload(self):
        """
        To choose an .mcp file with a dialog window
        """
        filename = filedialog.askopenfilename(title = "Select file",filetypes = [("mcp files","*.mcp")])
        try:
            pp = import_config(filename)
            self.fillform(pp)
            if pp != None:
                self.mcp = pp 
            print(self.mcp)
        except:
            print("Loading failed")
            
            
    def commandremove(self):
        """
        To empty the forme
        """
        try:
            self.fillform(None)
            self.mcp = mcpp()
        except:
            print("Removing failed")
        
        
        
    def fillform(self,mcp):
        """
        To fill the form with MCP parameters
        * Parameters
            * mcp: GBARpy.MCPPicture.MCPParams
        """
        self.e_name.delete(0,tkinter.END)
        self.e_R.delete(0,tkinter.END)
        self.e_x0.delete(0,tkinter.END)
        self.e_y0.delete(0,tkinter.END)
        self.e_R0.delete(0,tkinter.END)
        self.e_ratio.delete(0,tkinter.END)
        if mcp != None:
            if mcp.name != None:
                self.e_name.insert(0,mcp.name)
            if mcp.R != None:
                self.e_R.insert(0,mcp.R)
            if mcp.x0 != None:
                self.e_x0.insert(0,mcp.x0)
            if mcp.y0 != None:
                self.e_y0.insert(0,mcp.y0)
            if mcp.R0 != None:
                self.e_R0.insert(0,mcp.R0)
            if mcp.ratio != None:
                self.e_ratio.insert(0,mcp.ratio)
    
    
    def formToMCP(self):
        """
        To convert the form to MCP parameters
        * Returns
            * GBARpy.MCPPicture.MCPParams
        """
        name  = self.e_name.get()
        if len(name) == 0:
            name = None 
        R     = self.e_R.get()
        R     = None if len(R) == 0 else float(R)
        x0    = self.e_x0.get()
        x0    = None if len(x0) == 0 else float(x0)
        y0    = self.e_y0.get()
        y0    = None if len(y0) == 0 else float(y0)
        R0    = self.e_R0.get()
        R0    = None if len(R0) == 0 else float(R0)
        ratio = self.e_ratio.get()
        ratio = None if len(ratio) == 0 else float(ratio)
        return mcpp(name,R,x0,y0,R0,ratio)
