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
![Figure1](https://github.com/trandallUW/IntroToProg-Python-Mod07/blob/main/docs/pickle_pycharm.png)"Figure 1"

![Figure2](https://github.com/trandallUW/IntroToProg-Python-Mod07/blob/main/docs/pickle_cmd.png)"Figure 2"

This is the data output into a binary file.  Not the same as a list!
� � ]�(� dawg��steve�e.

## Exception Handling  - Intro to handling errors

When you are developing code, it’s likely that you will be working on a team and someone else will be collaborating with you on your code.  It’s likely that during this collaboration there will be errors in the code.  Python has built in error messages that are not usually intuitive.  Thus, using Exception Handling is a good way to build in custom error messages that are easy to understand by others.  One simple way to input exception handling is to use the “try” and “except” functions.  Try is usually followed by a statement, and if that set of code doesn’t execute properly, it will go the “except” statement.  Typically, you can use the print() function to print to the user an error that is easy to understand.   Take my previous coding example that described how to use the pickling function.  

What if the save_data_to_file () function didn’t execute properly?  Well, use the “try” and “except” function to print out a potential error message for this situation.    

Or what if the read_data_from_file() function got all messed up by your coworker?  Well, that’s a great situation to plan for and put in an error message.
Here's the same “Main Body Script” code used in my pickling example with some exception handling – notice the try and except code.  

```
# Main Body of Script ----------------------------- #
# Store the list object into a binary file
try:
    save_data_to_file(strFileName, lstCustomer)
    print("User ID and Name pickled into a file! ")
except:
    print("Error!  The data was not saved to file ")


# Read the data from the file into a new list object and display the contents
try:
    lstNewCustomerInfo = read_data_from_file(strFileName)
    print("Reading from file...This is the data that was unpickled: ")
    print(lstNewCustomerInfo)
except:
    print("Error!  The data was not read from file ")
```

Figure 3 shows my Pycharm output for these error messages.  Figure 4 shows my output in command shell.  

![Figure3](https://github.com/trandallUW/IntroToProg-Python-Mod07/blob/main/docs/errors_pycharm.png)"Figure 3"

![Figure4](https://github.com/trandallUW/IntroToProg-Python-Mod07/blob/main/docs/errors_cmd.png)"Figure 3"

### Summary

Pickling is a great way to convert your data in order to “serialize” it and make it easier to store or send over a network.  Exception Handling is a foundational way to develop custom error messages that are easy to understand by humans.  Both Python functions are foundational for any programmer or data analyst to know.  There are great resources on the internet to find out more info on these functions. 



