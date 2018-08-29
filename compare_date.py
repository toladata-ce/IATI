#This function compares a date in string format to the current time
import datetime

def compare_date(str):
    format = '%Y/%m/%d'
    date = datetime.datetime.strptime(str,format)
    return date < datetime.datetime.now()
