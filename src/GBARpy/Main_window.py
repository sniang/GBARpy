#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:00:25 2020

@author: samuel.niang@cern.ch
"""

import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog
from os import path, listdir
import dill
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import GBARpy
from GBARpy.MCPPicture import BeamSpot, import_config, import_image
from GBARpy.MCPPicture import MCPParams as Mcpp
from matplotlib import cm

# Uncomment for edit mode
# from MCPPicture import MCPParams as Mcpp
# from MCPPicture import BeamSpot, import_config, import_image

fontsize = 12


class MainWindow(tkinter.Tk):
    """
    Main window of the graphical interface
    ### Attributes

    mcp_param: GBARpy.MCPPicture.MCPParams
    picadress: str
    picadresses: [str]
    beamspots: [GBARpy.MCPPicture.BeamSpot]
    auto_reshape: [x,y,l]
    reshape_parameters: [x1,y1,x2,y2]

    frame0: tkinter.Frame
    frame0_c: tkinter.Frame
    frame1: tkinter.Frame
        Frame where is shown the picture to analyse
    frame2: tkinter.Frame
        Frame where is shown the result of the analysis

    btn_open_img: tkinter.Button
    btn_mcp_param: tkinter.Button
    btn_analysis: tkinter.Button
    btn_export: tkinter.Button
    btn_reshape_win: tkinter.Button
    fit: tkinter.StringVar
    menu_fit: tkinter.OptionMenu
    chk_3D_var: tkinter.IntVar
    chk_3D: tkinter.Checkbutton

    default_mcp: np.array([GBARpy.MCPPicture.MCPParams])
    default_mcp_names: [str]
    var_default_mcp: tkinter.StringVar
    menu_default_mcp:  tkinter.OptionMenu
    chk_reshape_mcp_var: tkinter.IntVar
    chk_reshape_mcp: tkinter.Checkbutton

    str_mcp_param: tkinter.StringVar
    lbl_mcp_param: tkinter.Label
    str_info_message: tkinter.StringVar
    lbl_info_message: tkinter.Label
    var_picadress: tkinter.StringVar
    lbl_picadress: tkinter.Label
    img1Label: tkinter.Label

    picN: int
    picI: int
    btn_Left: tkinter.Button
    btn_Right: tkinter.Button
    """

    def __init__(self):
        # Location of the static files
        static_addr = GBARpy.__file__
        static_addr = path.split(static_addr)[0]
        static_addr = path.join(static_addr, 'static')

        # Some variables
        self.mcp_param = Mcpp()
        self.picadress = ""
        self.picadresses = []
        self.beamspots = []
        self.auto_reshape = []
        self.reshape_parameters = []

        # Main Frame
        tkinter.Tk.__init__(self)
        self.beamSpot = None
        self.title("GBARPy")
        self.geometry("1000x700")
        self.resizable(True, True)

        # Cadre 0 Control
        self.frame0 = tkinter.Frame(self, highlightbackground="black", highlightthickness=1)
        self.frame0.pack(side='top', fill='x')
        self.frame0_c = tkinter.Frame(self.frame0)
        self.frame0_c.pack(side='left')
        self.frame0_c.columnconfigure(0, pad=3)
        self.frame0_c.columnconfigure(0, pad=1)
        self.frame0_c.rowconfigure(0, pad=3)
        self.frame0_c.rowconfigure(1, pad=3)
        self.frame0_c.rowconfigure(2, pad=3)

        # Buttons
        self.btn_open_img = tkinter.Button(self.frame0_c, text='Open image(s)', command=self.cmd_open_img)
        self.btn_mcp_param = tkinter.Button(self.frame0_c, text='MCP Parameters', command=self.cmd_mcp_params)
        self.btn_analysis = tkinter.Button(self.frame0_c, text='Analyse the picture(s)', command=self.cmd_analyse)
        self.fit = tkinter.StringVar(self.frame0_c)
        fit_value = ["Filtered gaussian", "Simple gaussian", "Two gaussian"]
        self.fit.set(fit_value[0])
        self.menu_fit = tkinter.OptionMenu(self.frame0_c, self.fit, *fit_value)
        self.btn_export = tkinter.Button(self.frame0_c, text='Save analysis', command=self.cmd_export_analysis)
        self.chk_3D_var = tkinter.IntVar()
        self.chk_3D_var.set(0)
        self.chk_3D = tkinter.Checkbutton(self.frame0_c, text='3D plot', variable=self.chk_3D_var, onvalue=1,
                                          offvalue=0, command=self.cmd_plot_image)
        self.btn_reshape_win = tkinter.Button(self.frame0_c, text='Reshape window', command=self.cmd_reshape_window)

        # GBAR's MCP parameters
        self.default_mcp = np.array(find_mcp_param_in_directory(static_addr))
        self.default_mcp_names = []
        for m in self.default_mcp:
            self.default_mcp_names.append(m.name)
        self.default_mcp_names = np.array(self.default_mcp_names)
        self.var_default_mcp = tkinter.StringVar(self.frame0_c)
        self.var_default_mcp.set("GBAR's MCP")
        mcp_names = np.concatenate([["GBAR's MCP"], self.default_mcp_names])
        self.menu_default_mcp = tkinter.OptionMenu(self.frame0_c, self.var_default_mcp, *mcp_names,
                                                   command=self.cmd_menu_mcp)
        self.menu_default_mcp.grid(row=0, column=1)

        # Auto reshape from MCP params
        self.chk_reshape_mcp_var = tkinter.IntVar()
        self.chk_reshape_mcp_var.set(0)
        self.chk_reshape_mcp = tkinter.Checkbutton(self.frame0_c, text='Auto reshape',
                                                   variable=self.chk_reshape_mcp_var, onvalue=1, offvalue=0,
                                                   command=self.cmd_auto_reshape_mcp)

        # Place buttons
        self.btn_open_img.grid(row=0, column=0)
        self.btn_analysis.grid(row=1, column=0)
        self.menu_fit.grid(row=2, column=0)
        self.btn_export.grid(row=3, column=0)
        self.btn_mcp_param.grid()
        self.chk_3D.grid(row=5, column=0)
        self.chk_reshape_mcp.grid(row=4, column=1)
        self.btn_reshape_win.grid(row=0, column=4)

        # Labels
        self.str_mcp_param = tkinter.StringVar()
        self.str_mcp_param.set(self.mcp_param.__repr__())
        self.lbl_mcp_param = tkinter.Label(self.frame0_c, textvariable=self.str_mcp_param)
        self.str_info_message = tkinter.StringVar()
        self.lbl_info_message = tkinter.Label(self.frame0_c, textvariable=self.str_info_message)
        self.var_picadress = tkinter.StringVar()
        self.lbl_picadress = tkinter.Label(self, textvariable=self.var_picadress)

        # Place labels
        self.lbl_mcp_param.grid(row=1, rowspan=3, column=1)
        self.lbl_info_message.grid(row=3, column=5)
        self.lbl_picadress.pack(side='bottom')

        # Frame 1: image to analyse
        self.frame1 = tkinter.Frame(self, width=400, height=400, highlightbackground="black", highlightthickness=1)
        self.frame1.pack(side='left')
        self.img1Label = tkinter.Label(self.frame1)

        # Frame 2: analysis result
        self.frame2 = tkinter.Frame(self, width=400, height=400, highlightbackground="black", highlightthickness=1)
        self.frame2.pack(side='right')

        # Draw GBAR logo
        add = path.join(static_addr, "GBAR_logo.png")
        img = Image.open(add)
        img = img.resize((100, 100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tkinter.Label(self.frame0, image=img)
        panel.image = img
        panel.pack(side='right')
        self.tk.call('wm', 'iconphoto', self._w, tkinter.PhotoImage(file=add))
        self.iconphoto(False, tkinter.PhotoImage(file=add))

        # Choose picture
        self.picN = 0
        self.picI = 0
        pic_left = Image.open(path.join(static_addr, "left.png"))
        pic_left = pic_left.resize((40, 30), Image.ANTIALIAS)
        pic_left = ImageTk.PhotoImage(pic_left)
        self.btn_Left = tkinter.Button(self.frame0_c, image=pic_left, command=self.cmd_go_left)
        self.btn_Left.image = pic_left
        self.btn_Left.grid(row=5, column=2)

        pic_right = Image.open(path.join(static_addr, "right.png"))
        pic_right = pic_right.resize((40, 30), Image.ANTIALIAS)
        pic_right = ImageTk.PhotoImage(pic_right)
        self.btn_Right = tkinter.Button(self.frame0_c, image=pic_right, command=self.cmd_go_right)
        self.btn_Right.image = pic_right
        self.btn_Right.grid(row=5, column=3)

    def cmd_open_img(self):
        """

        """
        self.str_info_message.set("")
        self.picN = 0
        self.picI = 0
        try:
            self.picadresses = filedialog.askopenfilenames(title='Open image(s)',
                                                           filetypes=[("tif files", "*.tif"),
                                                                      ("jpg files", "*.jpg"),
                                                                      ("jpeg files", "*.jpeg"),
                                                                      ("png files", "*.png"),
                                                                      ("asc files", "*.asc"),
                                                                      ("bmp files", "*.bmp")])

            self.picadresses = np.sort(self.picadresses)
            self.picadress = self.picadresses[0]
            self.picN = len(self.picadresses)
            self.picI = 0
            self.var_picadress.set(self.picadresses[self.picI])
            self.str_info_message.set("Files have been opened")
            self.cmd_plot_image()
        except (Exception,):
            self.str_info_message.set("Opening failed")

    def cmd_export_analysis(self):
        """

        """
        self.str_info_message.set("")
        try:
            if self.picN == 0:
                self.cmd_open_img()
            file_name = filedialog.asksaveasfilename(title='Export as image file',
                                                     filetypes=[("pdf files", "*.pdf"),
                                                                ("jpg files", "*.jpg"),
                                                                ("png files", "*.png")])
            if len(file_name) > 0:
                if len(self.beamspots) == 0:
                    self.cmd_analyse()
                fig = self.beamspots[self.picI].plot()
                fig.savefig(file_name)
                plt.close()
                self.str_info_message.set("Saved as " + path.split(file_name)[-1])
        except (Exception,):
            self.str_info_message.set("Exportation failed")

    def cmd_mcp_params(self):
        """

        """
        self.str_info_message.set("")
        MCPParamsWindow(self, self.mcp_param)

    def cmd_reshape_window(self):
        """

        """
        try:
            self.str_info_message.set("")
            ReshapeWindow(self)
        except (Exception,):
            self.str_info_message.set("Not possible to open the window")

    def cmd_go_right(self):
        """

        """
        if self.picI + 1 < self.picN:
            self.picI += 1
            self.picadress = self.picadresses[self.picI]
            self.cmd_plot_image()
            self.refresh_plot()
            self.var_picadress.set(self.picadresses[self.picI])

    def cmd_go_left(self):
        """

        """
        if self.picI - 1 >= 0:
            self.picI -= 1
            self.picadress = self.picadresses[self.picI]
            self.refresh_plot()
            self.var_picadress.set(self.picadresses[self.picI])

    def cmd_plot_image(self):
        """

        """
        def conv(a):
            b = []
            for e in a:
                b.append(str(e))
            return np.array(b)

        for widget in self.frame1.winfo_children():
            widget.destroy()

        if self.picN > 0:
            img = import_image(self.picadress)
            fig = Figure(figsize=(5, 5))
            if self.chk_3D_var.get() == 0:
                subplot = fig.add_subplot(111)
                subplot.imshow(img)
                subplot.set_xlabel('pixels', fontsize=fontsize)
                subplot.set_ylabel('pixels', fontsize=fontsize)
                y = len(img)
                x = len(np.transpose(img))
                if self.mcp_param.check_ratio_is_set():
                    subplot.set_xlabel('mm', fontsize=fontsize)
                    subplot.set_ylabel('mm', fontsize=fontsize)
                    line = np.linspace(0, x, 4)
                    subplot.set_xticks(line)
                    line = conv(np.floor(line * self.mcp_param.ratio))
                    subplot.set_xticklabels(line)
                    line = np.linspace(0, y, 4)
                    subplot.set_yticks(line)
                    line = conv(np.floor(line * self.mcp_param.ratio))
                    subplot.set_yticklabels(line)
                    subplot.set_xlim(0, x)
                    subplot.set_ylim(y, 0)
                if self.mcp_param.check_all_set():
                    subplot.plot(self.mcp_param.x0, self.mcp_param.y0, '+', ms=15, mew=2, color='white')
                    subplot.set_xlim(0, x)
                    subplot.set_ylim(y, 0)
                    x0, y0 = circle_xy(self.mcp_param.x0, self.mcp_param.y0,
                                       self.mcp_param.R0)
                    subplot.plot(x0, y0, lw=3, color='white')
                if len(self.auto_reshape) == 3:
                    ix, iy, lm = self.auto_reshape[0], self.auto_reshape[1], self.auto_reshape[2]
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
                    subplot.plot([min_x, max_x], [min_y, min_y], lw=3, color='green')
                    subplot.plot([min_x, max_x], [max_y, max_y], lw=3, color='green')
                    subplot.plot([min_x, min_x], [min_y, max_y], lw=3, color='green')
                    subplot.plot([max_x, max_x], [min_y, max_y], lw=3, color='green')

                if len(self.reshape_parameters) == 4:
                    x1, y1 = self.reshape_parameters[0], self.reshape_parameters[1]
                    x2, y2 = self.reshape_parameters[2], self.reshape_parameters[3]
                    subplot.plot([x1, x1], [y1, y2], lw=3, color='white')
                    subplot.plot([x1, x2], [y2, y2], lw=3, color='white')
                    subplot.plot([x2, x2], [y2, y1], lw=3, color='white')
                    subplot.plot([x2, x1], [y1, y1], lw=3, color='white')
                fig.tight_layout()
            else:
                y = np.arange(len(img))
                x = np.arange(len(img[0]))
                x, y = np.meshgrid(x, y)
                z = img
                subplot = fig.add_subplot(111, projection='3d')
                subplot.plot_surface(x, y, z, cmap=cm.plasma, linewidth=0, antialiased=False)

            canvas = FigureCanvasTkAgg(fig, master=self.frame1)
            canvas.mpl_connect('motion_notify_event', self.print_x_y_position)
            canvas.draw()
            canvas.get_tk_widget().pack()

    def print_x_y_position(self, event):
        """

        """
        x, y = event.xdata, event.ydata
        if x is not None and y is not None:
            x, y = int(x), int(y)
            res = "pix: x = " + str(x) + "\ty = " + str(y) + "\n"
            r = self.mcp_param.ratio
            if self.mcp_param.check_ratio_is_set():
                x, y = np.round(event.xdata * r, 2), np.round(event.ydata * r, 2)
                res += "mm: x = " + str(x) + "\ty = " + str(y) + "\n"
            self.str_info_message.set(res)

    def cmd_plot_analysis(self):
        """

        """
        for widget in self.frame2.winfo_children():
            widget.destroy()

        if len(self.beamspots) > 0:
            bs = self.beamspots[self.picI]

            fig = Figure(figsize=(5, 2.5), dpi=100)
            pplt = fig.add_subplot(111)
            popt = bs.poptx
            label = "along the x-axis"
            if np.any(np.isnan(popt)):
                pplt.plot(bs.pix, bs.Ix, '.', ms=1, label=label)
            else:
                popt = bs.poptx
                popt[-1] = 0
                fitfunc = bs.fit.fitfunc
                d = bs.Ix - bs.offsetx
                p = pplt.plot(bs.pix, d, '.', ms=1, label=label)
                pplt.plot(bs.pix, fitfunc(bs.pix, *popt),
                          color=p[0].get_color())
            popt = bs.popty
            label = "along the y-axis"
            if np.any(np.isnan(popt)):
                pplt.plot(bs.piy, bs.Iy, '.', ms=1, label=label)
            else:
                popt = bs.popty
                popt[-1] = 0
                fitfunc = bs.fit.fitfunc
                d = bs.Iy - bs.offsety
                p = pplt.plot(bs.piy, d, '.', ms=1, label=label)
                pplt.plot(bs.piy, fitfunc(bs.piy, *popt),
                          color=p[0].get_color())
            pplt.set_xlim([0, np.max(bs.pix)])
            pplt.grid()
            pplt.legend()
            canvas = FigureCanvasTkAgg(fig, master=self.frame2)
            canvas.draw()
            canvas.get_tk_widget().pack()
            # Write the result
            res = bs.__repr__()
            tkinter.Label(self.frame2, text=res).pack()

    def cmd_analyse(self):
        """

        """
        # Empty and plot image
        self.beamspots = []
        self.str_info_message.set("")
        reshape = []
        if len(self.auto_reshape) == 3:
            reshape = self.auto_reshape
        if len(self.reshape_parameters) == 4:
            reshape = self.reshape_parameters

        try:
            if self.picN == 0:
                self.cmd_open_img()
            self.cmd_plot_image()
            fit = self.fit.get()
            # Analysis
            if self.picN > 0:
                for file_name in self.picadresses:
                    self.beamspots.append(BeamSpot(file_name, mcpp=self.mcp_param, fit=fit, reshape=reshape))
                self.cmd_plot_analysis()

        except (Exception,):
            self.str_info_message.set("Analysis has failed")

    def cmd_menu_mcp(self, *args):
        """

        """
        name = self.var_default_mcp.get()
        if name in self.default_mcp_names:
            self.mcp_param = self.default_mcp[self.default_mcp_names == name][0]
            self.str_mcp_param.set(self.mcp_param.__repr__())
            self.var_default_mcp.set("GBAR's MCP")
            if len(self.beamspots) > 0:
                self.cmd_analyse()
            self.cmd_auto_reshape_mcp()
            self.refresh_plot()

    def cmd_auto_reshape_mcp(self):
        """

        """
        self.auto_reshape = []
        if self.mcp_param.check_all_set():
            if self.chk_reshape_mcp_var.get() == 1:
                self.auto_reshape = [self.mcp_param.x0, self.mcp_param.y0, self.mcp_param.R0]
        else:
            self.chk_reshape_mcp_var.set(0)
        self.refresh_plot()

    def refresh_plot(self):
        """

        """
        self.cmd_plot_image()
        self.cmd_plot_analysis()


###############################################################################


def circle_xy(x0, y0, r0):
    """
    To obtain cartesian coordinates of a circle
    @param x0:
    @param y0:
    @param r0:
    @return:
    """
    t = np.linspace(0, 2 * np.pi, 100)
    return x0 + r0 * np.cos(t), y0 + r0 * np.sin(t)


def find_mcp_param_in_directory(dir_mcp):
    """

    @param dir_mcp:
    @return:
    """
    res = []
    for file in listdir(dir_mcp):
        if file.endswith(".mcp"):
            res.append(import_config(path.join(dir_mcp, file)))
    return res


###############################################################################


class MCPParamsWindow(tkinter.Toplevel):
    """
    ### Arguments of the class

    master: GBARpy.Main_window.MainWindow
    mcp: GBARpy.MCPPicture.MCPParams

    e_name: tkinter.Entry(self)
    e_R: tkinter.Entry(self)
    e_x0: tkinter.Entry(self)
    e_y0: tkinter.Entry(self)
    e_R0: tkinter.Entry(self)
    e_ratio: tkinter.Entry(self)

    frame0: tkinter.Frame

    set = tkinter.Button
    save = tkinter.Button
    load = tkinter.Button
    remove = tkinter.Button
    """
    def __init__(self, master, mcp):
        """

        @param master:
        @param mcp:
        """
        tkinter.Toplevel.__init__(self, master)
        self.title("Define the MCP parameters")
        self.geometry("400x200")
        self.resizable(False, False)

        self.master = master
        self.mcp = mcp
        # The form
        tkinter.Label(self, text="MCP's name").grid(row=0)
        tkinter.Label(self, text="R (mm)").grid(row=1)
        tkinter.Label(self, text="x0 (pixels)").grid(row=2)
        tkinter.Label(self, text="y0 (pixels)").grid(row=3)
        tkinter.Label(self, text="R0 (pixels)").grid(row=4)
        tkinter.Label(self, text="ratio (mm/pixels)").grid(row=5)

        self.e_name = tkinter.Entry(self)
        self.e_R = tkinter.Entry(self)
        self.e_x0 = tkinter.Entry(self)
        self.e_y0 = tkinter.Entry(self)
        self.e_R0 = tkinter.Entry(self)
        self.e_ratio = tkinter.Entry(self)

        self.e_name.grid(row=0, column=1)
        self.e_R.grid(row=1, column=1)
        self.e_x0.grid(row=2, column=1)
        self.e_y0.grid(row=3, column=1)
        self.e_R0.grid(row=4, column=1)
        self.e_ratio.grid(row=5, column=1)

        self.fill_form(self.mcp)

        # buttons
        self.frame0 = tkinter.Frame(self)
        self.frame0.grid(row=6, column=0, columnspan=3)

        self.set = tkinter.Button(self.frame0,
                                  text='Set',
                                  command=self.cmd_set).grid(row=0,
                                                             column=0)
        self.save = tkinter.Button(self.frame0,
                                   text='Save',
                                   command=self.cdm_save).grid(row=0,
                                                               column=1)
        self.load = tkinter.Button(self.frame0,
                                   text='Load',
                                   command=self.cmd_load).grid(row=0,
                                                               column=2)
        self.remove = tkinter.Button(self.frame0,
                                     text='Remove',
                                     command=self.cmd_remove).grid(row=0,
                                                                   column=3)

    def cmd_set(self):
        """
        To set the MCP parameters
        """
        try:
            pp = self.form_to_mcp()
            self.mcp = pp
            self.master.mcp_param = pp
            self.master.str_mcp_param.set(pp.__repr__())
        except (Exception,):
            self.master.str_info_message.set("Setting failed")

    def cdm_save(self):
        """
        To save the parameters as an .mcp file
        """
        try:
            pp = self.form_to_mcp()
            f = filedialog.asksaveasfile(mode='wb', defaultextension=".mcp")
            dill.dump(pp, f)
            self.master.str_info_message.set("Parameters saved as" + f.name)
        except (Exception,):
            self.master.str_info_message.set("Saving failed")

    def cmd_load(self):
        """
        To choose an .mcp file with a dialog window
        """
        filename = filedialog.askopenfilename(title="Select file",
                                              filetypes=[("mcp files", "*.mcp")])
        try:
            pp = import_config(filename)
            self.fill_form(pp)
            if pp is not None:
                self.mcp = pp

        except (Exception,):
            self.master.str_info_message.set("Loading failed")

    def cmd_remove(self):
        """
        To empty the form
        """
        try:
            self.fill_form(None)
            self.mcp = Mcpp()
        except (Exception,):
            self.master.str_info_message.set("Removing failed")

    def fill_form(self, mcp):
        """
        To fill the form with MCP parameters
        @param mcp: GBARpy.MCPPicture.MCPParams
        @return: Nothing
        """
        self.e_name.delete(0, tkinter.END)
        self.e_R.delete(0, tkinter.END)
        self.e_x0.delete(0, tkinter.END)
        self.e_y0.delete(0, tkinter.END)
        self.e_R0.delete(0, tkinter.END)
        self.e_ratio.delete(0, tkinter.END)
        if mcp is not None:
            if mcp.name is not None:
                self.e_name.insert(0, mcp.name)
            if mcp.R is not None:
                self.e_R.insert(0, mcp.R)
            if mcp.x0 is not None:
                self.e_x0.insert(0, mcp.x0)
            if mcp.y0 is not None:
                self.e_y0.insert(0, mcp.y0)
            if mcp.R0 is not None:
                self.e_R0.insert(0, mcp.R0)
            if mcp.ratio is not None:
                self.e_ratio.insert(0, mcp.ratio)

    def form_to_mcp(self):
        """
        To convert the form to MCP parameters
        @return: GBARpy.MCPPicture.MCPParams
        """
        name = self.e_name.get()
        if len(name) == 0:
            name = None
        r = self.e_R.get()
        r = None if len(r) == 0 else float(r)
        x0 = self.e_x0.get()
        x0 = None if len(x0) == 0 else float(x0)
        y0 = self.e_y0.get()
        y0 = None if len(y0) == 0 else float(y0)
        r0 = self.e_R0.get()
        r0 = None if len(r0) == 0 else float(r0)
        ratio = self.e_ratio.get()
        ratio = None if len(ratio) == 0 else float(ratio)
        return Mcpp(name, r, x0, y0, r0, ratio)


###############################################################################


class ReshapeWindow(tkinter.Toplevel):
    """
    master: GBARpy.Main_window.MainWindow
        Main window

    frame: tkinter.Frame
        Main frame of the window
    frame_form: tkinter.Frame
        frame where is placed the form
    frame_btn: tkinter.Frame
        frame where are placed the buttons

    x1, y1, x2, y2: (int,int,int,int)
        Coordinates of the reshaping area
    img: 2D array
        picture to reshape
    click_number: int
        number of click on the picture
        0 -> select the first point of the rectangle
        1 -> first point selected, second to select
        2 -> all points selected
    fig: matplotlib.pyplot.Figure
        The figure where is plot the image
    subplot: fig.add_subplot(111)
        object used to plot
    canvas: FigureCanvasTkAgg
        Canvas attached to the figure
    last: subplot.plot
        last plotted point/rectangle

    x1_form: tkinter.Entry
        Entry for x1
    y1_form: tkinter.Entry
        Entry for y1
    x2_form: tkinter.Entry
        Entry for x2
    y2_form: tkinter.Entry
        Entry for y2

    btn_clear_button: tkinter.Button
        button to clear the form and the selection
    btn_draw_button: tkinter.Button
        button to draw the parameters from the form
    btn_reshape_button: tkinter.Button
        button to validate the reshape parameters
    """

    def __init__(self, master):
        """
        Constructor of the class
        @param master:
        """
        # constructor of the parent class
        tkinter.Toplevel.__init__(self, master)
        # Main frame
        self.frame = tkinter.Frame(self)
        self.frame.pack()
        # initialisation of the variables
        self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0
        self.click_number = 0
        # importation the picture
        self.img = import_image(master.var_picadress.get())
        # Plotting of the figure
        self.fig = Figure(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.mpl_connect('motion_notify_event', self.get_xy_position)
        self.canvas.mpl_connect('button_press_event', self.click_choose_position)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        self.subplot = self.fig.add_subplot(111)
        self.subplot.imshow(self.img)
        self.title("Reshape picture")
        self.last = self.subplot.plot(self.x1, self.y1, '+', lw=10)
        self.plot()
        # The form
        self.frame_form = tkinter.Frame(self.frame)
        self.frame_form.pack()
        tkinter.Label(self.frame_form, text="x1").grid(row=0, column=0)
        self.x1_form = tkinter.Entry(self.frame_form, width=5)
        self.x1_form.grid(row=0, column=1)
        tkinter.Label(self.frame_form, text="y1").grid(row=0, column=2)
        self.y1_form = tkinter.Entry(self.frame_form, width=5)
        self.y1_form.grid(row=0, column=3)
        tkinter.Label(self.frame_form, text="x2").grid(row=0, column=4)
        self.x2_form = tkinter.Entry(self.frame_form, width=5)
        self.x2_form.grid(row=0, column=5)
        tkinter.Label(self.frame_form, text="y2").grid(row=0, column=6)
        self.y2_form = tkinter.Entry(self.frame_form, width=5)
        self.y2_form.grid(row=0, column=7)
        # The buttons
        self.frame_btn = tkinter.Frame(self.frame)
        self.frame_btn.pack()
        self.btn_clear_button = tkinter.Button(master=self.frame_btn, text='Clear', command=self.cmd_clear)
        self.btn_clear_button.grid(row=0, column=0)
        self.btn_draw_button = tkinter.Button(master=self.frame_btn, text='Draw', command=self.cmd_draw)
        self.btn_draw_button.grid(row=0, column=1)
        self.btn_reshape_button = tkinter.Button(master=self.frame_btn, text='Reshape', command=self.cmd_reshape)
        self.btn_reshape_button.grid(row=0, column=2)

    def plot(self):
        """
        Plot the image and the rectangle corresponding to the reshaping area
        @return: Nothing
        """
        if self.x1 is not None and self.y1 is not None:
            # remove the previous rectangle/point
            for last_e in self.last:
                last_e.remove()
            # If no point have been selected, draw only a point
            if self.click_number == 0:
                self.last = self.subplot.plot(self.x1, self.y1, 'P', lw=2, color='white')
            # If at least one point have been selected, draw a rectangle
            elif self.click_number == 1:
                self.last = self.subplot.plot([self.x1, self.x1], [self.y1, self.y2], lw=3, color='white')
                self.last.append(self.subplot.plot([self.x1, self.x2], [self.y2, self.y2], lw=3, color='white')[0])
                self.last.append(self.subplot.plot([self.x2, self.x2], [self.y2, self.y1], lw=3, color='white')[0])
                self.last.append(self.subplot.plot([self.x2, self.x1], [self.y1, self.y1], lw=3, color='white')[0])
            self.canvas.draw()

    def get_xy_position(self, event):
        """
        To get the position of the mouse and save them in the form
        @param event: motion_notify_event
        @return: Nothing
        """
        # To get the position of the mouse in pixels
        x, y = event.xdata, event.ydata
        # If the mouse is on the picture
        if x is not None and y is not None:
            x, y = int(x), int(y)
            # If the first point have not been chosen
            if self.click_number == 0:
                self.x1, self.y1 = x, y
                self.plot()
            # If the first point have been chosen but not the second one
            elif self.click_number == 1:
                self.x2, self.y2 = x, y
                self.plot()
        # Empty the form
        self.empty_the_form()
        # Fill the form
        self.auto_fill_the_form()

    def click_choose_position(self, event):
        """
        To choose the coordinates of the rectangle by clicking on the picture
        @param event: button_press_event
        @return: Nothing
        """
        # To get the position of the mouse in pixels
        x, y = event.xdata, event.ydata
        x, y = int(x), int(y)
        # If the mouse is on the picture
        if x is not None and y is not None:
            # Increment the click number
            # Possible values 0, 1, 2
            self.click_number = (self.click_number + 1) % 3
            # first click to select the first point
            if self.click_number == 0:
                self.x1, self.y1 = x, y
            # second click to select the second point
            elif self.click_number == 1:
                self.x2, self.y2 = x, y

    def cmd_reshape(self):
        """
        To validate the reshape parameters
        @return: Nothing
        """
        # redraws the rectangle
        self.cmd_draw()
        # gives the parameters to the main window
        self.master.reshape_parameters = [self.x1, self.y1,
                                          self.x2, self.y2]
        # draw the rectangle in the main window's frame
        self.master.cmd_plot_image()

    def cmd_clear(self):
        """
        To clear the form and the selection
        @return: Nothing
        """
        # remove the parameters in the main window
        self.master.reshape_parameters = []
        # reset to 0 the click_number ie ready to draw a new rectangle
        self.click_number = 0
        # plot the image
        self.plot()
        # empty the form
        self.empty_the_form()

    def empty_the_form(self):
        """
        To empty the form
        @return: Nothing
        """
        self.x1_form.delete(0, tkinter.END)
        self.y1_form.delete(0, tkinter.END)
        self.x2_form.delete(0, tkinter.END)
        self.y2_form.delete(0, tkinter.END)

    def auto_fill_the_form(self):
        """
        Fill the form with the already selected values
        @return: Nothing
        """
        self.x1_form.insert(0, self.x1)
        self.y1_form.insert(0, self.y1)
        self.x2_form.insert(0, self.x2)
        self.y2_form.insert(0, self.y2)

    def cmd_draw(self):
        """
        To draw the parameters from the form
        @return: Nothing
        """
        # To insure that the selected values are positives
        self.x1 = np.abs(int(self.x1_form.get()))
        self.y1 = np.abs(int(self.y1_form.get()))
        self.x2 = np.abs(int(self.x2_form.get()))
        self.y2 = np.abs(int(self.y2_form.get()))
        # to insure that the selected values are possibles
        if self.x1 > len(self.img.T):
            self.x1 = len(self.img.T)
        if self.x2 > len(self.img.T):
            self.x2 = len(self.img.T)
        if self.y1 > len(self.img):
            self.y1 = len(self.img)
        if self.y2 > len(self.img):
            self.y2 = len(self.img)
        # Empty the form
        self.empty_the_form()
        # Fill the form
        self.auto_fill_the_form()
        # Plot the image and the rectangle
        self.plot()
        # Set the click number to 2 i.e. selection is complete
        self.click_number = 2
