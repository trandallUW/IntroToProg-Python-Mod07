# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demo code for Assignment 07
# ChangeLog (Who,When,What):
# trandallUW, 5.30.2023, added code to start Assignment 07
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