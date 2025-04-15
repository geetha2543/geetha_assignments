import datetime
#MaxFile class 
from pkg.file import File 
fs = File(r"C:\Users\Geetha\handson")
fs.getMaxSizeFile(2) # gives two max file names 
fs.getLatestFiles(datetime.date(2018,2,1))
#Returns list of files after 1st Feb 2018 
