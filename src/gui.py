import PySimpleGUI as sg
from threading import Thread
import os
import archive
import convert_DOC
import convert_png

class gui:

    def __init__(self, size_x, size_y) -> None:
        self.size_x = size_x
        self.size_y = size_y
        sg.theme("DarkPurple4")
        

    def Create_Window(self):
        Layout_Archive = [
                          [sg.Text('Каталог с архивами'), sg.Input("",key = "InputFolder", expand_x=True),sg.FolderBrowse('Выбрать',key="BrowseFolderArhiveIn")],
                          [sg.Text('Каталог выгрузки архивов'), sg.Input("",key = "OutputFolder",expand_x=True),sg.FolderBrowse('Выбрать',key="BrowseFolderArhiveOut")],
                          [sg.Button("Подтвердить", key = "ButtonArchive",font="Helvetica 15 bold", size=(self.size_x - 20,20))],
                        ]
        Layout_Convert_DOC = [
                            [sg.Text('Каталог с файлами'), sg.Input("",key = "InputFolderDoc", expand_x=True),sg.FolderBrowse('Выбрать',key="BrowseFolderDocIn")],
                            [sg.Text('Каталог выгрузки файлов'), sg.Input("",key = "OutputFolderDoc",expand_x=True),sg.FolderBrowse('Выбрать',key="BrowseFolderDocOut")],
                            [sg.Button("Подтвердить", key = "ButtonDoc",font="Helvetica 15 bold", size=(self.size_x - 20,20))]
                           ]
        Layout_Convert_PNG_JPG = [
                            [sg.Text('Каталог с файлами'), sg.Input("",key = "InputFolderPNG_JPG", expand_x=True),sg.FolderBrowse('Выбрать',key="BrowseFolderPNG_JPGIn")],
                            [sg.Text('Каталог выгрузки файлов'), sg.Input("",key = "OutputFolderPNG_JPG",expand_x=True),sg.FolderBrowse('Выбрать',key="BrowseFolderPNG_JPGOut")],
                            [sg.Button("Подтвердить", key = "ButtonPNG_JPG",font="Helvetica 15 bold", size=(self.size_x - 20,20))]
                           ]
        Layout_Convert = [[sg.TabGroup([[sg.Tab("Документ",Layout_Convert_DOC), sg.Tab("Изображение",Layout_Convert_PNG_JPG)]],expand_x=True)]]
        LayoutMain = [
            [sg.Text('Конвертер файлов. Your file -> PDF', font="Helvetica 26 bold")],
            [sg.TabGroup([[sg.Tab('Архивы',Layout_Archive, element_justification="left"),sg.Tab('Конвертер',Layout_Convert, element_justification="left")]],size=(1,140),expand_x=True)],
            [sg.Output(key="OutputWindowLogs",expand_x=True, expand_y=True)]]
        window = sg.Window("Converter", LayoutMain, size=(self.size_x, self.size_y), element_justification="center")
        return window
    
    def Unzip(self,IN,OUT):
        emp = archive.Zip(IN,OUT)
        emp.checkFiles()

    def ConvertDocFile(self,IN, OUT):
        DataFile = []
        Path = os.chdir(IN)
        FileList = os.listdir(Path)
        for TempFile in FileList:
            if (TempFile.endswith('.docx') or TempFile.endswith('.doc')):
                DataFile.append(TempFile)
        print(DataFile)
        emp1 = convert_DOC.WPDF(DataFile,IN,OUT)
        emp1.convert()

    def ConvertPNG_JPGFile(self,IN, OUT):
        DataFile = []
        Path = os.chdir(IN)
        FileList = os.listdir(Path)
        for TempFile in FileList:
            if (TempFile.endswith('.jpg') or TempFile.endswith('.jpeg') or TempFile.endswith('.jpe') or TempFile.endswith('.jfif') or TempFile.endswith('.png')):
                DataFile.append(TempFile)
        print(DataFile)
        emp2 = convert_png.PPDF(DataFile,IN,OUT)
        emp2.convert()
        
    def Event(self,window):
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'ButtonArchive':
                ThreadArchive = Thread(target=self.Unzip,args=(values["BrowseFolderArhiveIn"],values["BrowseFolderArhiveOut"],))
                ThreadArchive.start()
            if event == 'ButtonDoc':
                ThreadConvertDocFile = Thread(target=self.ConvertDocFile,args=(values["BrowseFolderDocIn"],values["BrowseFolderDocOut"],))
                ThreadConvertDocFile.start()
            if event == 'ButtonPNG_JPG':
                ThreadConvertPNG_JPGFile = Thread(target=self.ConvertPNG_JPGFile,args=(values["BrowseFolderPNG_JPGIn"],values["BrowseFolderPNG_JPGOut"],))
                ThreadConvertPNG_JPGFile.start()
        window.close()


