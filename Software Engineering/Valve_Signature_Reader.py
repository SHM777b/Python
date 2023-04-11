import tkinter as tk
from tkinter import filedialog as tkb
import re
import os
import xml.etree.ElementTree as ET
import plotly.graph_objects as go
import plotly.io as pio


class Frame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class Label(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        tk.Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class Button(tk.Button):
    def __init__(self, parent, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class Entry(tk.Entry):
    def __init__(self, parent, *args, **kwargs):
        tk.Entry.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class OptionMenu(tk.OptionMenu):
    def __init__(self, parent, *args, **kwargs):
        tk.OptionMenu.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class ValveSignature:
    def __init__(self, parent):
        self.parent = parent

        # ROOT FOLDER WHERE VLAVE SIGNATURES ARE SEARCHED FOR 'GET LATEST' AND 'GET OLDEST' BUTTON COMMANDS
        self.folder = r'Valve Signatures'

        # LABEL FRAME
        self.labelFrame = Frame(self.parent)

        # BUTTON FRAME
        self.buttonFrame = Frame(self.parent)

        # LABELS
        self.label1 = Label(self.labelFrame)
        self.label2 = Label(self.labelFrame)
        self.label3 = Label(self.labelFrame)
        self.label4 = Label(self.labelFrame)
        self.label5 = Label(self.labelFrame)

        # BUTTONS
        self.button0 = Button(self.buttonFrame)
        self.button1 = Button(self.buttonFrame)
        self.button2 = Button(self.buttonFrame)
        self.button3 = Button(self.buttonFrame)
        self.button4 = Button(self.buttonFrame)

        # ENTRY
        self.entry0 = Entry(self.buttonFrame)
        self.entry1 = Entry(self.buttonFrame)
        self.entry2 = Entry(self.buttonFrame)
        self.entry3 = Entry(self.buttonFrame)

        # DROP DOWN MENU OPTIONS
        self.options = {
            'Select Flank': ['EN 1', 'EN 2', 'ES 1', 'ES 2', 'NF 1', 'NF 2', 'WF 1', 'WF 2', 'WS 1', 'WS 2'],

            'Select Subsea Asset': ['XT 1', 'XT 2', 'XT 3', 'HIPPS', 'PMA'],

            'XT 1': ['AAV', 'AIV', 'BIV', 'DHSIV1', 'DHSIV2', 'MEGV1', 'MEGV2',
                     'MEGV3', 'MEGV4', 'MeOH', 'PMV', 'PWV', 'SIV', 'XOV'],

            'XT 2': ['AAV', 'AIV', 'BIV', 'DHSIV1', 'DHSIV2', 'MEGV1', 'MEGV2',
                     'MEGV3', 'MEGV4', 'MeOH', 'PMV', 'PWV', 'SIV', 'XOV'],

            'XT 3': ['AAV', 'AIV', 'BIV', 'DHSIV1', 'DHSIV2', 'MEGV1', 'MEGV2',
                     'MEGV3', 'MEGV4', 'MeOH', 'PMV', 'PWV', 'SIV', 'XOV'],

            'HIPPS': ['HBV1', 'HBV2', 'HBY1', 'HBY2', 'HBY3', 'MSV16'],

            'PMA': ['MSV05', 'MSV06', 'MSV07', 'MSV09', 'MSV10', 'MSV11', 'MSV12',
                    'MSV13', 'MSV15', 'MSV16', 'MSV17', 'MSV18', 'MSV19', 'MSV22'],

            'Status': ['Open', 'Close'],

            'SEM': ['A', 'B']
        }

        # A function to amend drop down menu of 'Select Valve' based on selected Subsea Structure
        def callback(*args):
            self.valveOptionMenu = tk.OptionMenu(self.labelFrame, self.valveVar, *self.options[self.subseaVar.get()])
            self.valveOptionMenu.grid(row=2, column=1, sticky='w')

        # ADDING DROPDOWN LABELS AND OPTIONS TO LABEL FRAME
        self.flankVar = tk.StringVar()  # NF 1, NF 2, ...
        self.flankVar.set('Select')  # Default Value

        self.flankOptionMenu = OptionMenu(self.labelFrame, self.flankVar, *self.options['Select Flank'])
        self.flankOptionMenu.grid(row=0, column=1, sticky='we')

        self.subseaVar = tk.StringVar()  # XT 1, XT 2, XT 3, HIPPS, PMA
        self.subseaVar.set('Select')  # Default Value
        self.subseaVar.trace('w', callback)

        self.subseaOptionMenu = OptionMenu(self.labelFrame, self.subseaVar, *self.options['Select Subsea Structure'])
        self.subseaOptionMenu.grid(row=1, column=1, sticky='w')

        self.valveVar = tk.StringVar()  # AAV, AIV, MEGV2, HBV1 ....
        self.valveVar.set('Select')  # Default Value

        self.valveOptionMenu = OptionMenu(self.labelFrame, self.valveVar, *self.options['XT 1'])
        self.valveOptionMenu.grid(row=2, column=1, sticky='w')

        self.statusVar = tk.StringVar()  # Open, Close
        self.statusVar.set('Select')  # Default Value

        self.statusOptionMenu = OptionMenu(self.labelFrame, self.statusVar, *self.options['Status'])
        self.statusOptionMenu.grid(row=3, column=1, sticky='w')

        self.semVar = tk.StringVar()  # A, B
        self.semVar.set('Select')  # Default Value

        self.semOptionMenu = OptionMenu(self.labelFrame, self.semVar, *self.options['SEM'])
        self.semOptionMenu.grid(row=4, column=1, sticky='w')

        # LABEL FRAME CONFIG
        self.labelFrame.grid(row=0, column=0, sticky='news')

        # BUTTON FRAME CONFIG
        self.buttonFrame.grid(row=0, column=1, sticky='news', padx=100)

        # LABEL CONFIG
        self.label1.grid(row=0, column=0, sticky='w')
        self.label1.config(text='Select Flank')

        self.label2.grid(row=1, column=0, sticky='w')
        self.label2.config(text='Select Subsea Structure')

        self.label3.grid(row=2, column=0, sticky='w')
        self.label3.config(text='Select Valve')

        self.label4.grid(row=3, column=0, sticky='w')
        self.label4.config(text='Status')

        self.label5.grid(row=4, column=0, sticky='w')
        self.label5.config(text='SEM')

        # OBJECTS FOR BUTTON COMMANDS
        self.valveSignatureHub = ValveSignatureHub()

        # BUTTON CONFIG
        self.button0.grid(row=0, column=0, columnspan=2, rowspan=2, sticky='ew')
        self.button0.config(text='Get Latest Valve Signature',
                            command=lambda: self.valveSignatureHub.getLatest(self.parent, self.flankVar, self.subseaVar,
                                                                             self.valveVar, self.statusVar, self.semVar,
                                                                             self.entry2, self.entry0, self.folder))

        self.button1.grid(row=2, column=0, columnspan=2, rowspan=2, sticky='ew')
        self.button1.config(text='Get Oldest Valve Signature',
                            command=lambda: self.valveSignatureHub.getOldest(self.parent, self.flankVar, self.subseaVar,
                                                                             self.valveVar, self.statusVar, self.semVar,
                                                                             self.entry3, self.entry1, self.folder))

        self.button2.grid(row=4, column=0, columnspan=2, rowspan=2, sticky='ew')
        self.button2.config(text='Select XML from directory',
                            command=lambda: self.valveSignatureHub.selectValveSignature(self.parent,
                                                                                        self.entry0, self.entry2))

        self.button3.grid(row=6, column=0, columnspan=2, rowspan=2, sticky='ew')
        self.button3.config(text='Select second XML from directory',
                            command=lambda: self.valveSignatureHub.selectValveSignature2(self.parent,
                                                                                         self.entry1, self.entry3))

        self.button4.grid(row=8, column=0, columnspan=2, rowspan=2, sticky='ew')
        self.button4.config(text='Plot Graph',
                            command=lambda: PrintValveSignature(self.valveSignatureHub.parser1,
                                                                self.valveSignatureHub.valveName1,
                                                                self.valveSignatureHub.flankName1,
                                                                self.valveSignatureHub.parser2,
                                                                self.valveSignatureHub.valveName2,
                                                                self.valveSignatureHub.flankName2
                                                                ).plot_graph())

        # ENTRY CONFIG
        self.entry0.grid(row=0, column=2, columnspan=20, ipadx=100, sticky='news')
        self.entry1.grid(row=2, column=2, columnspan=20, ipadx=100, sticky='news')
        self.entry2.grid(row=4, column=2, columnspan=20, ipadx=100, sticky='news')
        self.entry3.grid(row=6, column=2, columnspan=20, ipadx=100, sticky='news')

# --------------------------------------------------------------------------------
# The part of the code below enables the user to select the valve signature from
# a directory and extracts the necessary information from selected XML file
# --------------------------------------------------------------------------------


class ValveSignatureHub:
    def __init__(self):
        self.parser1 = None
        self.valveName1 = None
        self.flankName1 = None
        self.parser2 = None
        self.valveName2 = None
        self.flankName2 = None

    def selectValveSignature(self, parent, entry0, entry2):
        self.parser1, self.valveName1, self.flankName1 = SelectValveSignature(parent, entry0, entry2).select_path()

    def selectValveSignature2(self, parent, entry1, entry3):
        self.parser2, self.valveName2, self.flankName2 = SelectValveSignature2(parent, entry1, entry3).select_path()

    def getLatest(self, parent, flankVar, subseaVar, valveVar, statusVar, semVar, entry2, entry0, folder):
        self.parser1, self.valveName1, self.flankName1 = GetLatest(parent, flankVar, subseaVar,
                                                                   valveVar, statusVar, semVar,
                                                                   entry2, entry0, folder).get_signature()

    def getOldest(self, parent, flankVar, subseaVar, valveVar, statusVar, semVar, entry3, entry1, folder):
        self.parser2, self.valveName2, self.flankName2 = GetOldest(parent, flankVar, subseaVar,
                                                                   valveVar, statusVar, semVar,
                                                                   entry3, entry1, folder).get_signature()


class SelectValveSignature:
    def __init__(self, parent, entry0, entry2):
        self.parent = parent
        self.entry0 = entry0
        self.entry2 = entry2
        self.parser = None
        self.valveName = None
        self.flankName = None

    def select_path(self):
        filePath = tkb.askopenfilename(defaultextension='.xml',
                                       initialdir=r'Desktop',
                                       title='Please select the valve signature file from directory')
        # print(filePath)
        # print('********')

        valveName, flankName = ValveNameIdentifier(filePath).get_values()

        self.entry2.delete(0, tk.END)
        self.entry0.delete(0, tk.END)

        if len(valveName.group(3)) > 3:
            self.entry2.insert(0, flankName + '; ' + 'XT' + valveName.group(3)[-1] + ' ' +
                               valveName.group(4) + '; ' + valveName.group(5) + '; '
                               + valveName.group(1))
        else:
            self.entry2.insert(0, flankName + '; ' + valveName.group(4) + '; '
                               + valveName.group(5) + '; ' + valveName.group(1))

        parser = XmlParser(locations=(filePath,)).valueTimeCreator()

        return parser, valveName, flankName


class SelectValveSignature2:
    def __init__(self, parent, entry1, entry3):
        self.parent = parent
        self.entry1 = entry1
        self.entry3 = entry3
        self.parser = None
        self.valveName = None
        self.flankName = None

    def select_path(self):
        filePath = tkb.askopenfilename(defaultextension='.xml',
                                       initialdir=r'Desktop',
                                       title='Please select the valve signature file from directory')
        # print(filePath)

        valveName, flankName = ValveNameIdentifier(filePath).get_values()

        self.entry3.delete(0, tk.END)
        self.entry1.delete(0, tk.END)

        if len(valveName.group(3)) > 3:
            self.entry3.insert(0, flankName + '; ' + 'XT' + valveName.group(3)[-1] + ' ' +
                               valveName.group(4) + '; ' + valveName.group(5) + '; '
                               + valveName.group(1))
        else:
            self.entry3.insert(0, flankName + '; ' + valveName.group(4) + '; '
                               + valveName.group(5) + '; ' + valveName.group(1))

        parser = XmlParser(locations=(filePath,)).valueTimeCreator()

        return parser, valveName, flankName


class ValveNameIdentifier:
    def __init__(self, filePath):
        self.filePath = filePath

        pattern = re.compile(r'XXX')
        self.valveName = pattern.match(str(self.filePath))

        if self.valveName.group(2) == 'A1-1' or self.valveName.group(2) == 'B1-1':
            self.flankName = 'East North Flank 1'
        elif self.valveName.group(2) == 'A1-2' or self.valveName.group(2) == 'B1-2':
            self.flankName = 'East North Flank 2'
        elif self.valveName.group(2) == 'A2-1' or self.valveName.group(2) == 'B2-1':
            self.flankName = 'North Flank 1'
        elif self.valveName.group(2) == 'A2-2' or self.valveName.group(2) == 'B2-2':
            self.flankName = 'North Flank 2'
        elif self.valveName.group(2) == 'A3-1' or self.valveName.group(2) == 'B3-1':
            self.flankName = 'West Flank 1'
        elif self.valveName.group(2) == 'A3-2' or self.valveName.group(2) == 'B3-2':
            self.flankName = 'West Flank 2'

    def get_values(self):
        return self.valveName, self.flankName


class SortValveNames:
    """
    Extracts the valve name, type of operation and date of operation from given data. Does this for flowmeter and return
    line data
    """
    def __init__(self, valveName, flankName):
        self.valveName = valveName
        self.flankName = flankName

    def sort(self):
        if len(self.valveName.group(3)) > 3:
            dataOfMainValve = '{valve}; {operation}; {date}'. \
                format(date=self.valveName.group(1), operation=self.valveName.group(5),
                       valve='XT ' + self.valveName.group(3)[-1] + ' ' + self.valveName.group(4))
        else:
            dataOfMainValve = '{valve}; {operation}; {date}'. \
                format(date=self.valveName.group(1), operation=self.valveName.group(5),
                       valve=self.valveName.group(4))

        dataOfLp = 'LP Return; {operation}; {date}'. \
            format(date=self.valveName.group(1), operation=self.valveName.group(5))

        dataOfFlm = 'Flowmeter; {operation}; {date}'. \
            format(date=self.valveName.group(1), operation=self.valveName.group(5))

        title = '{flank}'.format(flank=self.flankName)

        return dataOfMainValve, dataOfLp, dataOfFlm, title


# --------------------------------------------------------------------------------
# The part of the code below enables the user to select the valve from the drop
# down list. It also enables the user to find the latest and oldest valve
# signatures in vale signature database
# --------------------------------------------------------------------------------


class GetLatest:
    def __init__(self, parent, flankVar, subseaVar, valveVar, statusVar, semVar, entry2, entry0, folder):
        self.parent = parent
        self.flankVar = flankVar
        self.subseaVar = subseaVar
        self.valveVar = valveVar
        self.statusVar = statusVar
        self.semVar = semVar
        self.entry2 = entry2
        self.entry0 = entry0
        self.folder = folder
        self.valveName = None
        self.flankName = None
        self.parser = None
        try:
            self.file_names = FilesPreparation(self.folder).get_file_names()
        except FileNotFoundError:
            self.file_names = None
            print('''Most probably the directory provided for foler with signatures is incorrect.
                  Please check the python script for self.folder value and change the directory accordingly''')


    def get_signature(self):
        if self.flankVar.get() == 'Select' or self.subseaVar.get() == 'Select' or self.valveVar.get() == 'Select' or \
           self.statusVar.get() == 'Select' or self.semVar.get() == 'Select':
            self.entry0.delete(0, tk.END)
            self.entry0.insert(0, 'Please provide attributes by using drop down lists on left')
        elif self.file_names is None:
            self.entry0.delete(0, tk.END)
            self.entry0.insert(0, 'No Files found in directory')
        else:
            pattern = PatternPreparation(self.flankVar, self.subseaVar, self.valveVar, self.statusVar, self.semVar).get_pattern()
            match_obj_new = None
            print(pattern)

            for i in self.file_names:
                match_obj = re.match(pattern, i)
                if match_obj:
                    if match_obj_new:
                        if match_obj.group(1) > match_obj_new.group(1):
                            match_obj_new = match_obj
                    else:
                        match_obj_new = match_obj

            if match_obj_new:
                directory = self.folder + '/' + str(match_obj_new.group(0))
                print(directory)
                valveName, flankName = ValveNameIdentifier(directory).get_values()
                self.entry0.delete(0, tk.END)
                self.entry2.delete(0, tk.END)

                if len(valveName.group(3)) > 3:
                    self.entry0.insert(0, flankName + '; ' + 'XT' + valveName.group(3)[-1] + ' ' +
                                       valveName.group(4) + '; ' + valveName.group(5) + '; '
                                       + valveName.group(1))
                else:
                    self.entry0.insert(0, flankName + '; ' + valveName.group(4) + '; '
                                       + valveName.group(5) + '; ' + valveName.group(1))
                parser = XmlParser(locations=(directory,)).valueTimeCreator()
                return parser, valveName, flankName

            else:
                self.entry0.delete(0, tk.END)
                self.entry0.insert(0, 'File Not Found')



class GetOldest:
    def __init__(self, parent, flankVar, subseaVar, valveVar, statusVar, semVar, entry3, entry1, folder):
        self.parent = parent
        self.flankVar = flankVar
        self.subseaVar = subseaVar
        self.valveVar = valveVar
        self.statusVar = statusVar
        self.semVar = semVar
        self.entry3 = entry3
        self.entry1 = entry1
        self.folder = folder
        self.valveName = None
        self.flankName = None
        self.parser = None
        try:
            self.file_names = FilesPreparation(self.folder).get_file_names()
        except FileNotFoundError:
            self.file_names = None
            print('''Most probably the directory provided for foler with signatures is incorrect.
                  Please check the python script for self.folder value and change the directory accordingly''')

    def get_signature(self):
        if self.flankVar.get() == 'Select' or self.subseaVar.get() == 'Select' or self.valveVar.get() == 'Select' or self.statusVar.get() == 'Select' or self.semVar.get() == 'Select':
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, 'Please provide attributes by using drop down lists on left')
        elif self.file_names is None:
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, 'No Files found in directory')
        else:
            pattern = PatternPreparation(self.flankVar, self.subseaVar, self.valveVar, self.statusVar, self.semVar).get_pattern()
            match_obj_new = None
            print(pattern)

            for i in self.file_names:
                match_obj = re.match(pattern, i)
                if match_obj:
                    if match_obj_new:
                        if match_obj.group(1) < match_obj_new.group(1):
                            match_obj_new = match_obj
                    else:
                        match_obj_new = match_obj

            if match_obj_new:
                print(match_obj_new)
                directory = self.folder + '/' + str(match_obj_new.group())
                valveName, flankName = ValveNameIdentifier(directory).get_values()
                self.entry1.delete(0, tk.END)
                self.entry3.delete(0, tk.END)

                if len(valveName.group(3)) > 3:
                    self.entry1.insert(0, flankName + '; ' + 'XT' + valveName.group(3)[-1] + ' ' +
                                       valveName.group(4) + '; ' + valveName.group(5) + '; '
                                       + valveName.group(1))
                else:
                    self.entry1.insert(0, flankName + '; ' + valveName.group(4) + '; '
                                       + valveName.group(5) + '; ' + valveName.group(1))
                parser = XmlParser(locations=(directory,)).valueTimeCreator()
                return parser, valveName, flankName

            else:
                self.entry1.delete(0, tk.END)
                self.entry1.insert(0, 'File Not Found')


class PatternPreparation:
    """
    Prepares the name of the required subsea location based on selected dropdown labels
    """
    def __init__(self, flankVar, subseaVar, valveVar, statusVar, semVar):
        self.flankVar = flankVar
        self.subseaVar = subseaVar
        self.valveVar = valveVar
        self.statusVar = statusVar
        self.semVar = semVar

        self.valve = self.valveVar.get()
        self.sem = self.semVar.get()
        self.position = self.statusVar.get()
        self.cm = self.subseaVar.get()
        self.xt_no = ''

        self.clusters = {'EN': 1,
                         'ES': 1,
                         'NF': 2,
                         'WF': 3,
                         'WS': 3}


    def get_pattern(self):
        cluster = self.flankVar.get()[0:2]
        for key, val in self.clusters.items():
            if cluster == key:
                cluster_no = val

        flank = self.flankVar.get()[3]
        if cluster == 'EN' or cluster == 'NF' or cluster == 'WF':
            flank_no = flank
        elif cluster == 'ES' or cluster == 'WS':
            if flank == 1:
                flank_no = 3
            elif flank == 2:
                flank_no = 4

        if self.cm == 'XT 1' or self.cm == 'XT 2' or self.cm == 'XT 3':
            xt_no = '.' + self.cm[3]
            cm = 'SCM'
        elif self.cm == 'HIPPS':
            cm = 'HCM'
        elif self.cm == 'PMA':
            cm = 'MCM'

        try:
            return re.compile(r'XXX.xml'.
                              format(cluster=cluster_no, flank=flank_no, sem=self.sem, valve=self.valve,
                                     position=self.position, control_module=cm, xt_no=xt_no))
        except NameError:
            print('cluster_no or flank_no are not defined')


class FilesPreparation:
    def __init__(self, folder_link):
        self.folder_link = folder_link

    def get_file_names(self):
        return os.listdir(self.folder_link)


class PrintValveSignature:
    def __init__(self, parser1, valveName1, flankName1, parser2=None, valveName2=None, flankName2=None):
        self.parser1 = parser1
        self.parser2 = parser2
        self.valveName1 = valveName1
        self.flankName1 = flankName1
        self.valveName2 = valveName2
        self.flankName2 = flankName2


    def plot_graph(self):
        if self.parser1 and self.parser2:
            dataOfMainValve1, dataOfLp1, dataOfFlm1, title1 = SortValveNames(self.valveName1, self.flankName1).sort()
            dataOfMainValve2, dataOfLp2, dataOfFlm2, title2 = SortValveNames(self.valveName2, self.flankName2).sort()

            plotter = Plot(title=title2,
                           traceNames=((dataOfMainValve1, dataOfLp1, dataOfFlm1, title1),
                                       (dataOfMainValve2, dataOfLp2, dataOfFlm2, title2)),
                           file1=self.parser1, file2=self.parser2)
            pio.show(plotter.fig)
        elif self.parser1:
            dataOfMainValve1, dataOfLp1, dataOfFlm1, title1 = SortValveNames(self.valveName1, self.flankName1).sort()
            plotter = Plot(title=title1,
                           traceNames=((dataOfMainValve1, dataOfLp1, dataOfFlm1),),
                           file1=self.parser1)
            pio.show(plotter.fig)

        elif self.parser2:
            dataOfMainValve2, dataOfLp2, dataOfFlm2, title2 = SortValveNames(self.valveName2, self.flankName2).sort()
            plotter = Plot(title=title2,
                           traceNames=((dataOfMainValve2, dataOfLp2, dataOfFlm2),),
                           file1=self.parser2)
            pio.show(plotter.fig)


class Parser:
    def __init__(self):
        pass


class XmlParser(Parser):
    def __init__(self, locations: tuple):
        super().__init__()
        self.locations = locations
        self.valueTimeCreator()

    def valueTimeCreator(self):
        # Creating XML tree and root
        tree = ET.parse(self.locations[0])
        root = tree.getroot()

        # Creating Time list for SCM Internal Sensor Readings: Valve PI
        timeList_main = [float(sec.text) + float(nsec.text) / 10 ** 9 for sec, nsec in
                         zip(root[0][12].iter('sec'), root[0][12].iter('nsec'))]
        timeZero_main = timeList_main[0]

        for i in range(len(timeList_main)):
            timeList_main[i] -= timeZero_main

        # Creating Value list for SCM Internal Sensor Readings: Valve PI
        valueList_main = [float(value.text) for value in root[0][12].iter('value')]


        # Creating Time list for SCM Internal Sensor Readings: LP Return
        timeList_lp = [float(sec.text) + float(nsec.text) / 10 ** 9 for sec, nsec in
                       zip(root[0][13].iter('sec'), root[0][13].iter('nsec'))]
        timeZero_lp = timeList_lp[0]

        for i in range(len(timeList_lp)):
            timeList_lp[i] -= timeZero_lp

        # Creating Value list for SCM Internal Sensor Readings: LP Return
        valueList_lp = [float(value.text) for value in root[0][13].iter('value')]


        # Creating Time list for SCM Flowmeter
        timeList_flm = [float(sec.text) + float(nsec.text) / 10 ** 9 for sec, nsec in
                        zip(root[0][14].iter('sec'), root[0][14].iter('nsec'))]
        timeZero_flm = timeList_flm[0]

        for i in range(len(timeList_flm)):
            timeList_flm[i] -= timeZero_flm

        # Creating Value list for SCM Flowmeter Readings
        valueList_flm = [float(value.text) for value in root[0][14].iter('value')]

        # Inputting the Time and Value lists into a tuple for Plotly Class
        return (timeList_main, valueList_main), (timeList_lp, valueList_lp), (timeList_flm, valueList_flm)



class Plot:
    """
    This class plots the parsed xml data. It can receive either one or two data sets and will plot accordingly.
    """
    pio.renderers.default = "browser"

    def __init__(self, title: str, traceNames: tuple, file1, file2=None):
        self.file1 = file1
        self.file2 = file2
        self.traceNames = traceNames
        self.title = title
        self.fig = go.Figure()
        self.data = self.trace_number()



        self.layout = {
            "title": self.title + " Valve Signature",
            "xaxis": {
                "type": "linear",
                "color": "blue",
                "title": "Time [s]",
                "autorange": True
            },
            "yaxis": {
                "type": "linear",
                "color": "blue",
                "title": "Pressure [bar]",
                "autorange": True
            },
            "yaxis2": {
                "type": "linear",
                "color": "rgb(83, 81, 84)",
                "title": "Flow [L]",
                "anchor": "free",
                "overlaying": "y",
                "side": "right",
                "position": 1,
                "autorange": True
            },
            "legend": {
                "x": 1.0204520990312163,
                "y": 0.009685230024213076
            },
            "autosize": True,
            "showlegend": True
        }

        self.fig = {'data': self.data, 'layout': self.layout}



    def prepare_trace(self):
        trace1 = {
            "uid": "e59e0e",
            "name": self.traceNames[0][0],
            "type": "scatter",
            "mode": "lines",
            "line": {
                "color": "rgb(57, 106, 177)"
            },
            "x": self.file1[0][0],
            "y": self.file1[0][1],
            "opacity": 1
        }

        trace2 = {
            "uid": "e59e0e",
            "name": self.traceNames[0][1],
            "type": "scatter",
            "mode": "lines",
            "line": {
                "color": "rgb(204, 37, 41)"
            },
            "x": self.file1[1][0],
            "y": self.file1[1][1],
            "opacity": 1
        }
        trace3 = {
            "uid": "e59e0e",
            "name": self.traceNames[0][2] + "<br>Total: {} lt<br>".format(self.file1[2][1][-1]),
            "type": "scatter",
            "mode": "lines",
            "line": {
                "color": "rgb(83, 81, 84)"
            },
            "x": self.file1[2][0],
            "y": self.file1[2][1],
            "opacity": 1,
            "yaxis": "y2"
        }

        return trace1, trace2, trace3

    def prepare_trace2(self):
        trace4 = {
            "uid": "e59e0e",
            "name": self.traceNames[1][0],
            "type": "scatter",
            "mode": "lines",
            "line": {
                "color": "rgb(62, 150, 81)"
            },
            "x": self.file2[0][0],
            "y": self.file2[0][1],
            "opacity": 1
        }

        trace5 = {
            "uid": "e59e0e",
            "name": self.traceNames[1][1],
            "type": "scatter",
            "mode": "lines",
            "line": {
                "color": "rgb(218, 124, 48)"
            },
            "x": self.file2[1][0],
            "y": self.file2[1][1],
            "opacity": 1
        }
        trace6 = {
            "uid": "e59e0e",
            "name": self.traceNames[1][2] + "<br>Total: {} lt<br>".format(self.file2[2][1][-1]),
            "type": "scatter",
            "mode": "lines",
            "line": {
                "color": "rgb(107, 76, 154)"
            },
            "x": self.file2[2][0],
            "y": self.file2[2][1],
            "opacity": 1,
            "yaxis": "y2"
        }

        return trace4, trace5, trace6

    def trace_number(self):
        if self.file1 and self.file2:
            trace1, trace2, trace3 = self.prepare_trace()
            trace4, trace5, trace6 = self.prepare_trace2()
            return [trace1, trace2, trace3, trace4, trace5, trace6]
        elif self.file1 or self.file2:
            trace1, trace2, trace3 = self.prepare_trace()
            return [trace1, trace2, trace3]
        else:
            print('No XML file is selected')


if __name__ == '__main__':
    mainWindow = tk.Tk()
    mainWindow.title = 'Valve Signature Reader'
    mainWindow.geometry('950x170+10+10')
    ValveSignature(mainWindow)
    mainWindow.mainloop()
