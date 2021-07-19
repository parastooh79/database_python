# in this case we will add people data from Excel file to mongodb database
from pymongo import MongoClient
import pandas as pd
import pymongo

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["people"]
mycol= mydb["info"]
print('Connected to Database')

df = pd.read_excel('file_example_XLSX_100.xlsx')
print('I get your file!!!')

for i in range(100):
  
   # my age value's type is <class 'numpy.int64'> and we should get item of that.
    # so we used .item() method 
    
    info = {'Name':df['First Name'][i]+' '+df['Last Name'][i],'Gender':df['Gender'][i],'Age':(df['Age'][i]).item(),'Country':df['Country'][i]} 
     exist = mycol.find_one(info)
    
    if exist == None:
        insinfo = mycol.insert_one(info)
        print('New member was added')
    else:
        print('this member is exist')
    
