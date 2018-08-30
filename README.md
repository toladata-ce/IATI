# IATI
TolaData to CSV (for IATI)
The main script "export_to_csv.py" can export data of an organisation from TolaData to a CSV File that can report against required IATI fields. This file can then be used to publish on IATI using a platform like [Aidstream](www.aidstream.org) to generate an IATI XML File needed for publishing.

In this version, the database connection is made to a localhost. For production use, it needs to be pointed to a production database.

To execute the file you just need to go to your terminal in the right repository and execute the main file and add a organisation name, example:
```bash
python3 export_to_csv TolaData
```


In a future version, the IATI Identifier also needs to be entered as a parameter.
