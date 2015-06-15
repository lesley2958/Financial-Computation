# Financial-Computation
MongoDB Database - Financial Computation. 

<b> Usage:</b>

This database was created using PyMongo. Using modules to read in the excel files, I transferred all the table data to the database.

<b> Format: </b> 

There are five main collections, each one corresponding to a different excel file. Each collection is actually an array of collections that correspond to the different sheets within that excel file. 

<b> Logic: </b>

I read in all the excel data by iterating through each row and column of each sheet, using the xlrd python module.



