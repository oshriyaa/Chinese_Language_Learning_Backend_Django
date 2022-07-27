import os
import pandas as pd
import numpy as np

from django.core.management.base import BaseCommand
from api.models import Category, Vocabulary



class Command(BaseCommand):
    help = 'Populate the database with some dummy data for testing purposes'


    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        
        # get all file names in the dummy directory
        file_path = os.path.dirname(os.path.abspath(__file__))      # path of the current file
        dummy_data_path = os.path.join(file_path, 'default_data.xlsx')     # path of the excel with dummy data
        
        # read the contents of the file and store them in a dictionary
        db_main = {}
        
        xl = pd.ExcelFile(dummy_data_path)
        for sheet in xl.sheet_names:
            db_main[sheet]  = xl.parse(sheet)

        # name of all the models that need to have dummy data inserted in the order of priority
        model_list = [  Category, Vocabulary]
        
        
        for model in model_list:
            # get the model name and the dataframe
            model_name = model.__name__
            cur_db = db_main[model_name]
            
            cur_db.replace(to_replace=np.nan, value="", inplace=True)
            
            # for each row in the dataframe, create a new object of the model
            for index in cur_db.index:
                model.objects.get_or_create(**cur_db.loc[index].to_dict())