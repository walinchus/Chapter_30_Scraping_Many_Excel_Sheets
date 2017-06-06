import scraperwiki
import xlrd

#set a variable for the spreadsheet location
XLS = 'http://webarchive.nationalarchives.gov.uk/20130402145952/http://transparency.dh.gov.uk/files/2012/10/DailySR-Pub-file-WE-11-11-123.xls'
#use the scrape function on that spreadsheet to create a new variable
xlbin = scraperwiki.scrape(XLS)
#use the open_workbook function on that new variable to create another
book = xlrd.open_workbook(file_contents=xlbin)
sheetstotal = book.nsheets

id = 0
sheetsrange = range(0,sheetstotal)
for sheetnum in sheetsrange:
 print "scraping sheet ", sheetnum
  #use the sheet_by_index method to open the first (0) sheet in variable 'book' - and put it into new variable 'sheet'
 sheet = book.sheet_by_index(sheetnum)
  #use the row_values method and index (1) to grab the second row of 'sheet', and put all cells into the list variable 'title'
 title = sheet.row_values(1)
    #print the string "Title:", followed by the third item (column) in the variable 'title' 
 print "Title:", title[2]
 sheettitle = str(title[2])
 print "sheet.name", sheet.name
 sheetname = sheet.name
    #put cells from the 15th row into 'keys' variable 
 keys = sheet.row_values(14)
 record = {}
    #loop through a range - from the 16th item (15) to a number generated by using the .nrows method on 'sheet' (to find number of rows in that sheet)
    #put each row number in 'rownumber' as you loop
 for rownumber in range(15, sheet.nrows):
   print rownumber
   record['SHA'] = sheet.row_values(rownumber)[1]
   record['Code'] = sheet.row_values(rownumber)[2]
   record['Name'] = sheet.row_values(rownumber)[3]
   record['date1'] = sheet.row_values(rownumber)[4]
   record['date2'] = sheet.row_values(rownumber)[5]
   record['date3'] = sheet.row_values(rownumber)[6]
   record['title'] = title[2]
   id+=1
   record['id'] = id
   print "---", record
   scraperwiki.sqlite.save(['id'], record)
        
