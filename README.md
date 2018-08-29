# IATI
TolaData to CSV (IATI)
The main script "export_to_csv.py" can export data of an organisation from TolaData to a CSV File. 
This file can then be used on the Aidstream platform to get an IATI XML File.

In this version, the database connection is made to a localhost, it needs to be changed to the production database of TolaData.
To test this script, I restored data from the Demo data in my local Database. 

To execute the file you just need to go to your terminal in the right repository and execute the main file and add a organisation name, example:
```bash
python3 export_to_csv TolaData
```


In a futur version, the IATI Identifier also needs to be entered as a parameter.
