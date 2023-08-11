import zipfile
import py7zr
from pyunpack import Archive
import os

class Zip:

    def __init__(self, InputFolder, OutputFolder):
        self.InputFolder = InputFolder
        self.OutputFolder = OutputFolder

    def checkFiles(self):
        os.chdir(self.InputFolder)
        Files_In_Folder = os.listdir(self.InputFolder)
        for TempFile in Files_In_Folder:
            if TempFile.endswith('.zip'):
                with zipfile.ZipFile(TempFile, 'r') as zip_file:
                    zip_file.extractall(self.OutputFolder)
                    try:
                        print(f"Архив {TempFile} распакован в каталог {self.OutputFolder}")
                    except Exception as e:
                        print(f"Ошибка - {str(e)}")
            elif TempFile.endswith('.7z'):
                with py7zr.SevenZipFile(TempFile,'r') as SevenZ_File:
                    SevenZ_File.extractall(path=self.OutputFolder)
                    try:
                        print(f"Архив {TempFile} распакован в каталог {self.OutputFolder}")
                    except Exception as e:
                        print(f"Ошибка - {str(e)}")
            elif TempFile.endswith(".rar"):
                Archive(TempFile).extractall(self.OutputFolder)
                try:
                    print(f"Архив {TempFile} распакован в каталог {self.OutputFolder}")
                except Exception as e:
                    print(f"Ошибка - {str(e)}")
            else:
                print(f"Расширение архива {TempFile} не распаковывается")




