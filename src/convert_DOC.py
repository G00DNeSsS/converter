import os
from docx2pdf import convert
import pathlib

class WPDF:

    def __init__(self, file, InputFolder, OutputFolder) -> None:
        self.file = file
        self.InputFolder = InputFolder
        self.OutputFolder = OutputFolder

    def convert(self):
        os.chdir(self.InputFolder)
        for list_file in self.file:
            PathToFile = self.InputFolder+"\\"+list_file
            if os.path.isfile(PathToFile) == True:
                print(f"Файл {list_file} существует в {self.InputFolder}")
                fpath = pathlib.Path(PathToFile)
                PdfNameFile = fpath.stem + ".pdf"
                if os.path.isfile(self.OutputFolder + "\\" + PdfNameFile) == True:
                    ReplacePdfName = str(input(f"Файл {PdfNameFile} уже существует в каталоге {self.OutputFolder}, переименуйте: "))
                    convert(PathToFile, self.OutputFolder + "\\" + ReplacePdfName + '.pdf') 
                    if os.path.isfile(self.OutputFolder + "\\" + ReplacePdfName + '.pdf') == True:
                        print(f"Файл {ReplacePdfName}.docx конвертирован в PDF и сохранен в каталог {self.OutputFolder}")
                    else:      
                        print(f"Файл {ReplacePdfName}.docx не конвертирован в PDF")    
                else:
                    convert(PathToFile, self.OutputFolder + "\\" + PdfNameFile)
                    if os.path.isfile(self.OutputFolder + "\\" + PdfNameFile) == True:
                        print(f"Файл {list_file} конвертирован в PDF и сохранен в каталог {self.OutputFolder}")
                    else:      
                        print(f"Файл {list_file} не конвертирован в PDF")   
            else:
                print(f"Файл {list_file} не существует в {self.InputFolder}")
                        

        
    
# emp = WPDF(["sad.docx", "s.docx", "sad copy.docx"], "C:\code\VSCODE\convert\In", "C:\code\VSCODE\convert\Out")

# emp.convert()