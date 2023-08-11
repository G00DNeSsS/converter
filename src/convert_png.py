import convert_DOC
import os
import pathlib
from PIL import Image

class PPDF(convert_DOC.WPDF):
    
    def convert(self):
        os.chdir(self.InputFolder)
        for list_file in self.file:
            PathToFile = self.InputFolder+"\\"+list_file
            if os.path.isfile(PathToFile) == True:
                print(f"Файл {list_file} существует в {self.InputFolder}")
                if list_file.endswith('.png'):
                    fpath = pathlib.Path(PathToFile)
                    PdfNameFile = fpath.stem + ".pdf"
                    if os.path.isfile(self.OutputFolder + "\\" + PdfNameFile) == True:
                        ReplacePdfName = str(input(f"Файл {PdfNameFile} уже существует в каталоге {self.OutputFolder}, переименуйте: "))
                        image = Image.open(PathToFile)
                        im_1 = image.convert('RGB')
                        im_1.save(self.OutputFolder + "\\"+ReplacePdfName + '.pdf')
                        if os.path.isfile(self.OutputFolder + "\\" + ReplacePdfName + '.pdf') == True:
                            print(f"Файл {list_file} переименован в {ReplacePdfName} и конвертирован в PDF и сохранен в каталог {self.OutputFolder}")
                        else:      
                            print(f"Файл {list_file} переименован в {ReplacePdfName}, но не конвертирован в PDF") 
                    else:
                        image = Image.open(PathToFile)
                        im_1 = image.convert('RGB')
                        im_1.save(self.OutputFolder + "\\"+PdfNameFile)
                        if os.path.isfile(self.OutputFolder + "\\" + PdfNameFile) == True:
                            print(f"Файл {list_file} конвертирован в PDF и сохранен в каталог {self.OutputFolder}")
                        else:      
                            print(f"Файл {list_file} не конвертирован в PDF")
                elif (list_file.endswith('.jpg') or list_file.endswith('.jpeg') or list_file.endswith('.jpe') or list_file.endswith('.jfif')):
                    fpath = pathlib.Path(PathToFile)
                    PdfNameFile = fpath.stem + ".pdf"
                    if os.path.isfile(self.OutputFolder + "\\" + PdfNameFile) == True:
                        ReplacePdfName = str(input(f"Файл {PdfNameFile} уже существует в каталоге {self.OutputFolder}, переименуйте: "))
                        image = Image.open(PathToFile)
                        im_1 = image.convert('RGB')
                        im_1.save(self.OutputFolder + "\\"+ReplacePdfName + '.pdf')
                        if os.path.isfile(self.OutputFolder + "\\" + ReplacePdfName + '.pdf') == True:
                            print(f"Файл {list_file} переименован в {ReplacePdfName} и конвертирован в PDF и сохранен в каталог {self.OutputFolder}")
                        else:      
                            print(f"Файл {list_file} переименован в {ReplacePdfName}, но не конвертирован в PDF") 
                    else:
                        image = Image.open(PathToFile)
                        im_1 = image.convert('RGB')
                        im_1.save(self.OutputFolder + "\\"+PdfNameFile)
                        if os.path.isfile(self.OutputFolder + "\\" + PdfNameFile) == True:
                            print(f"Файл {list_file} конвертирован в PDF и сохранен в каталог {self.OutputFolder}")
                        else:      
                            print(f"Файл {list_file} не конвертирован в PDF")
                else: 
                    print(f"Расширение файла {list_file} не знакомо программе")
            else:
                print(f"Файл {list_file} не существует в {self.InputFolder}")

