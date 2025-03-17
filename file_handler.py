import pandas as pd

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_workbook(self, sheet_name = None):
        """ 
        Load the workbook into the pandas dataframe. 
        Optionally, you can specify the sheet name
        """
        return pd.read_excel(self.file_path, sheet_name=sheet_name, engine="openpyxl")



