# Python Pickling and Exception Handling 
**Dev:** *trandallUW*   
**Date:** *5.31.2023*


## Pickling Introduction
As a developer or data analyst using Python, you might have a situation where you want to “serialize” your data.  “Serialize” is a technical term for converting the data into a linear form, or a series of bytes, so that it be easily stored, sent over a network, or used by other data and software functions.    To do this, you can use the pickling function.  

## How to Pickle

The pickle module consists of four methods:
1.	pickle.dump (obj, file) – use this to pickle your data into a file.
2.	pickle.dumps(obj, file) – use this to pickle your data and output a string.
3.	pickle.load() – use this unpickle your data and read a file.
4.	pickle.loads() – use this to unpickle your data and output a string.

Below is an example set of code that uses a set of classes and functions.  The purpose of this code is to collect a user ID and name from the user, store the data into a binary file, then read the data, and output the data back to the user in a a list format.  Notice how I used the import pickle, pickle.dump, and pickle.load code to convert the data.  

```
# ---------------------------------------------------------------------------- #
import pickle  # This imports code from another code file

# Data -------------------------------------------- #
strFileName = 'UserInfo.dat'
lstCustomer = []
strUserID = None
strUserName = None
lstNewCustomerInfo = None

# Input/Output------------------------------------- #
def get_user_ID ():
    user_ID = input("What is your user ID?: ")
    return (user_ID)

def get_user_name ():
    user_name = input("What is your user name?: ")
    return (user_name)

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "wb") # open file, write to binary
    pickle.dump(list_of_data, objFile) # pickle the data into file
    objFile.close() # close the file
    pass

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    userInfo = pickle.load(file)
    return(userInfo)

# Presentation ------------------------------------ #
# Get ID and NAME From user, then store it in a list object
strUserID = get_user_ID()  # get user ID
strUserName = get_user_name() # get user Name
lstCustomer = [strUserID, strUserName]

# Main Body of Script ----------------------------- #
# Store the list object into a binary file
save_data_to_file(strFileName, lstCustomer)
print("User ID and Name pickled into a file! ")

# Read the data from the file into a new list object and display the contents
lstNewCustomerInfo = read_data_from_file(strFileName)
print("Reading from file...This is the data that was unpickled: ")
print(lstNewCustomerInfo)
```
## What does the binary pickled data look like?
Here is the output of the script using Pycharm (see Figure 1).  The data is stored in a list.  Figure 2 shows my command shell ouput.


