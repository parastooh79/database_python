# in this code we connect to mongodb database , create the new user and connecting to database using username and password 
# get an input and check the input is exist in database or not

import urllib.parse
import pymongo
from pymongo import MongoClient
from getpass import getpass

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycollection= mydb["Numbers"]
add_new_user = mydb.add_user('username', password='password', read_only=None, session=None)

# new user in mongodb server was added 
# username = "username"
# password = "password" or you can using "None" 

username = input('Username?')    
password = getpass('Password?')

authenticate = mydb.authenticate(username,password)

if authenticate == True:
    myclient = pymongo.MongoClient(f"mongodb://{username}:{urllib.parse.quote_plus(password)}@localhost:27017/")
    print('Connected to Database')

    num = int(input('Give me a number: '))

    find_output = mycollection.find_one({'number':num})

    if find_output == None:
        insert_new = mycollection.insert_one({'number':num})
        print('Your number was added in database')

    else:

        print('Your number is exist in database')
        print(find_output)
        
else :
    print('username or password not valid')
