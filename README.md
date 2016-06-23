# Financial-Computation
Research Code 2015

MongoDB Database - Financial Computation. 
The purpose of this project was to build a database for specific types of economic/finacial documentation.

<b> Usage:</b>

This database was created using PyMongo. Using modules to read in the excel files, I transferred all the table data to the database.

<b> Format: </b> 

There are five main collections, each one corresponding to a different excel file. Each collection is actually an array of collections that correspond to the different sheets within that excel file. 

<b> Logic: </b>

I read in all the excel data by iterating through each row and column of each sheet, using the xlrd python module.

<b> Instructions: </b>

To create the database, the python script "FinancialComp.py" must be run on the terminal for each file, in this case 
that being five. 

To query, or search for, something in the database, the "query.py" python script must be run with the search as its 
parameter.



