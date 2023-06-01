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

