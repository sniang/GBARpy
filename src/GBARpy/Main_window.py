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
import dill
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import GBARpy
from GBARpy.MCPPicture import BeamSpot, import_config, import_image
from GBARpy.MCPPicture import MCPParams as mcpp
#For edit mode
#from MCPPicture import MCPParams as mcpp
#from MCPPicture import BeamSpot, import_config, import_image

fontsize = 12

class MainWindow(tkinter.Tk):
    """
    Main window of the graphical interface
    ### Attributes
    """
    def __init__(self):
        ### Location of the static files
        static_addr = GBARpy.__file__
        static_addr = path.split(static_addr)[0]
        static_addr = path.join(static_addr,'static')
                
        ### Some variables
        self.mcp_param = mcpp()
        self.picadress = ""
        self.canBeAnalysed = False
                
        ### Main Frame
        tkinter.Tk.__init__(self)
        self.beamSpot = True
        self.title("GBARPy")
        self.geometry("1000x700")
        self.resizable(True,True)

        ### Cadre 0 Contrôle
        self.frame0 = tkinter.Frame(self,highlightbackground="black",
                                    highlightthickness=1)
        self.frame0.pack(side='top',fill='x')
        self.frame0_c = tkinter.Frame(self.frame0)
        self.frame0_c.pack(side='left')
        self.frame0_c.columnconfigure(0, pad=3)
        self.frame0_c.columnconfigure(0, pad=1)
        self.frame0_c.rowconfigure(0, pad=3)
        self.frame0_c.rowconfigure(1, pad=3)
        self.frame0_c.rowconfigure(2, pad=3)
        
        ### Buttons
        self.btn_open_img = tkinter.Button(self.frame0_c, text='Open image(s)',
                                           command=self.cmd_open_img)
        self.btn_mcpparams = tkinter.Button(self.frame0_c,text='MCP Parameters',
                                            command=self.cmd_mcp_params)
        self.btn_analysis = tkinter.Button(self.frame0_c,
                                           text='Analyse the picture',
                                           command=self.cmd_analyse)
        self.fit = tkinter.StringVar(self.frame0_c)
        self.fit.set("Filtered gaussian") # default value
        self.menu_fit = tkinter.OptionMenu(self.frame0_c, self.fit, "Filtered gaussian", 
                                           "Simple gaussian",
                                           "Two gaussians")

        self.btn_export = tkinter.Button(self.frame0_c, text='Save analysis',
                                         command=self.cmd_export_analysis)
        ### Place buttons
        self.btn_open_img.grid(row=0,column=0)
        self.btn_analysis.grid(row=1,column=0)
        self.menu_fit.grid(row=2,column=0)
        self.btn_export.grid(row=3,column=0)
        self.btn_mcpparams.grid(row=4,column=0)
        
        ### Labels
        self.str_mcp_param = tkinter.StringVar()
        self.str_mcp_param.set(self.mcp_param.__repr__())
        self.lbl_mcp_param = tkinter.Label(self.frame0_c,
                                           textvariable=self.str_mcp_param)
        self.str_info_message = tkinter.StringVar()
        self.lbl_info_message = tkinter.Label(self.frame0_c,
                                              textvariable=self.str_info_message)
        
        self.var_picadress = tkinter.StringVar()
        self.lbl_picadress = tkinter.Label(self,
                                           textvariable=self.var_picadress)
        
        ### Place labels
        self.lbl_mcp_param.grid(row=0,rowspan=4,column=1)
        self.lbl_info_message.grid(row=0,column=4)
        self.lbl_picadress.pack(side='bottom')
        
        ### Frame 1: image to analyse
        self.frame1 = tkinter.Frame(self, width=400, height=400,
                                    highlightbackground="black",
                                    highlightthickness=1)
        self.frame1.pack(side='left')
        self.img1Label = tkinter.Label(self.frame1)
        
        
        ### Frame 2: analysis result
        self.frame2 = tkinter.Frame(self, width=400, height=400,
                                    highlightbackground="black",
                                    highlightthickness=1)
        
        self.frame2.pack(side='right')
        
        ### Draw GBAR logo
        add = path.join(static_addr,"GBAR_logo.png")
        img = Image.open(add)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tkinter.Label(self.frame0, image=img)
        panel.image = img
        panel.pack(side='right')
        self.tk.call('wm', 'iconphoto', self._w, tkinter.PhotoImage(file=add))
        self.iconphoto(False, tkinter.PhotoImage(file=add))
        
        
        ### Choose picture
        self.picN = 0
        self.picI = 0
        picLeft = Image.open(path.join(static_addr,"left.png"))
        picLeft = picLeft.resize((40, 30), Image.ANTIALIAS)
        picLeft = ImageTk.PhotoImage(picLeft)
        self.btn_Left = tkinter.Button(self.frame0_c, image=picLeft,command=self.cmd_go_left)
        self.btn_Left.image = picLeft
        self.btn_Left.grid(row=5,column=2)
        
        picRight = Image.open(path.join(static_addr,"right.png"))
        picRight = picRight.resize((40, 30), Image.ANTIALIAS)
        picRight = ImageTk.PhotoImage(picRight)
        self.btn_Right = tkinter.Button(self.frame0_c, image=picRight,command=self.cmd_go_right)
        self.btn_Right.image = picRight
        self.btn_Right.grid(row=5,column=3)








        
    
    def cmd_open_img(self):
        self.str_info_message.set("")
        try:
            self.picadresses = filedialog.askopenfilenames(title='Open image(s)',
                                                        filetypes = [("tif files","*.tif"),
                                                                     ("jpg files","*.jpg"),
                                                                     ("jpeg files","*.jpeg"),
                                                                     ("png files","*.png"),
                                                                     ("asc files","*.asc"),
                                                                     ("bmp files","*.bmp")])
            self.picadress = self.picadresses[0]
            self.picN = len(self.picadresses)
            self.picI = 0
            self.var_picadress.set(self.picadresses[self.picI])
            self.str_info_message.set("Files have been opened")
            self.canBeAnalysed = True
            self.plotImage()
        except:
            self.str_info_message.set("Opening failed")
            self.canBeAnalysed = False
        self.plotImage()
        
        
    def cmd_export_analysis(self):
        self.str_info_message.set("")
        try:
            if self.canBeAnalysed == False:
                self.cmd_open_img()
            fname = filedialog.asksaveasfilename(filetypes=[("pdf files","*.pdf"),
                                                            ("jpg files","*.jpg"),
                                                            ("png files","*.png"),
                                                            ("bmp files","*.bmp")])
            if len(fname) > 0:
                self.cmd_analyse()
                fig = self.beamSpot.plot()
                fig.savefig(fname)
                self.str_info_message.set("Saved as "+path.split(fname)[-1])                
        except:
            self.str_info_message.set("Exportation failed")

        
    def cmd_mcp_params(self):
        self.str_info_message.set("")
        MCPParamsWindow(self,self.mcp_param)
    
    def cmd_go_right(self):
        if self.picI + 1 < self.picN:
            self.picI += 1
            self.picadress = self.picadresses[self.picI]
            self.plotImage()
            self.var_picadress.set(self.picadresses[self.picI])
    
    def cmd_go_left(self):
        if self.picI - 1 >= 0:
            self.picI -= 1
            self.picadress = self.picadresses[self.picI]
            self.plotImage()
            self.var_picadress.set(self.picadresses[self.picI])
    
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
            y = len(img)
            x = len(np.transpose(img))
            if self.mcp_param.checkRatioIsSet():
                pplt.set_xlabel('mm',fontsize=fontsize)
                pplt.set_ylabel('mm',fontsize=fontsize)
                l = np.linspace(0,x,4)
                pplt.set_xticks(l)
                l = conv(np.floor(l*self.mcp_param.ratio))
                pplt.set_xticklabels(l)
                l = np.linspace(0,y,4)
                pplt.set_yticks(l)
                l = conv(np.floor(l*self.mcp_param.ratio))
                pplt.set_yticklabels(l)
                pplt.set_xlim(0,x)
                pplt.set_ylim(y,0)
            if self.mcp_param.checkAllSet():
                pplt.plot(self.mcp_param.x0,self.mcp_param.y0,'+',
                         ms=15,mew=2,color='white')
                pplt.set_xlim(0,x)
                pplt.set_ylim(y,0)
                X0,Y0 = self.circleXY(self.mcp_param.x0,self.mcp_param.y0,
                                      self.mcp_param.R0)
                pplt.plot(X0,Y0,lw=3,color='white')
            canvas = FigureCanvasTkAgg(fig, master=self.frame1)
            canvas.draw()
            canvas.get_tk_widget().pack()
        
    def cmd_analyse(self):
        ### Empty and plot image
        self.str_info_message.set("")
        for widget in self.frame2.winfo_children():
            widget.destroy()
        if self.canBeAnalysed == False:
            self.cmd_open_img()
        self.plotImage()
        fit = self.fit.get()
        ### Analysis
        self.beamSpot = BeamSpot(self.picadress,mcpp=self.mcp_param,fit=fit)
        ### plot analysis
        fig = Figure(figsize=(5,2.5), dpi=100)
        pplt = fig.add_subplot(111)
        popt = self.beamSpot.poptx
        label = "along the x-axis"
        if np.any(np.isnan(popt)):
            pplt.plot(self.beamSpot.pix,self.beamSpot.Ix,'.',ms=1,label=label)
        else:
            popt = self.beamSpot.poptx
            popt[-1] = 0
            fitfunc = self.beamSpot.fit.fitfunc
            D = self.beamSpot.Ix - self.beamSpot.offsetx
            p = pplt.plot(self.beamSpot.pix,D,'.',ms=1,label=label)
            pplt.plot(self.beamSpot.pix,fitfunc(self.beamSpot.pix,*popt),
                      color=p[0].get_color())
        popt = self.beamSpot.popty
        label = "along the y-axis"
        if np.any(np.isnan(popt)):
            pplt.plot(self.beamSpot.piy,self.beamSpot.Iy,'.',ms=1,label=label)
        else:
            popt = self.beamSpot.popty
            popt[-1] = 0
            fitfunc = self.beamSpot.fit.fitfunc
            D = self.beamSpot.Iy - self.beamSpot.offsety
            p = pplt.plot(self.beamSpot.piy,D,'.',ms=1,label=label)
            pplt.plot(self.beamSpot.piy,fitfunc(self.beamSpot.piy,*popt),
                      color=p[0].get_color())
        pplt.set_xlim([0,np.max(self.beamSpot.pix)])
        pplt.grid()
        pplt.legend()
        canvas = FigureCanvasTkAgg(fig, master=self.frame2)
        canvas.draw()
        canvas.get_tk_widget().pack()
        ### Write the result
        res = self.beamSpot.__repr__()
        tkinter.Label(self.frame2, text=res).pack()
        

        
    def circleXY(self,x0,y0,R0):
        """
        To obtain cartesian coordinates of a circle
        """
        t = np.linspace(0,2*np.pi,100)
        return x0 + R0*np.cos(t), y0 + R0*np.sin(t)
    

###############################################################################

    
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
        
        self.set = tkinter.Button(self.frame0,
                                  text='Set',
                                  command=self.commandset).grid(row=0,
                                                                column=0)
        self.save = tkinter.Button(self.frame0,
                                   text='Save',
                                   command=self.commandsave).grid(row=0,
                                                                  column=1)
        self.load = tkinter.Button(self.frame0,
                                   text='Load',
                                   command=self.commandload).grid(row=0,
                                                                  column=2)
        self.remove = tkinter.Button(self.frame0,
                                     text='Remove',
                                     command=self.commandremove).grid(row=0,
                                                                      column=3)

    def commandset(self):
        """
        To set the MCP parameters
        """
        try:
            pp = self.formToMCP()
            self.mcp = pp
            self.master.mcp_param = pp
            self.master.str_mcp_param.set(pp.__repr__())
        except:
            self.master.str_info_message.set("Setting failed")
        
        
            
            
    def commandsave(self):
        """
        To save the parameters as an .mcp file
        """
        try:
            pp = self.formToMCP()
            f = filedialog.asksaveasfile(mode='wb', defaultextension=".mcp")
            dill.dump(pp, f)
            self.master.str_info_message.set("Parameters saved as",f.name)
        except:
            self.master.str_info_message.set("Saving failed")
        finally:
            f.close()

        
        
    def commandload(self):
        """
        To choose an .mcp file with a dialog window
        """
        filename = filedialog.askopenfilename(title = "Select file",
                                              filetypes = [("mcp files","*.mcp")])
        try:
            pp = import_config(filename)
            self.fillform(pp)
            if pp != None:
                self.mcp = pp 
        except:
            self.master.str_info_message.set("Loading failed")
            
            
    def commandremove(self):
        """
        To empty the forme
        """
        try:
            self.fillform(None)
            self.mcp = mcpp()
        except:
            self.master.str_info_message.set("Removing failed")
        
        
        
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
