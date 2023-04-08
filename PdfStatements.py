# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 07:28:05 2022

@author: chris
"""



#"C:\Users\chris\OneDrive\Finances\Stmt\Stmt\Personal\Joint\Halifax\ClarityCC\pdfread\2209_Statement_4852_Sep-22.pdf"




    
    
    
strInputFile = r"C:\Users\chris\OneDrive\Finances\Stmt\Stmt\Personal\Joint\Halifax\ClarityCC\pdfread\2209_Statement_4852_Sep-22.pdf"
strFileNameNoext = ""


import PyPDF3

#strInputFileyFile = r"C:\Users\chris\OneDrive\RITS\DCC\PaySlips\Unlocked_NASA Umbrella Ltd Payroll for Chris Rae Week33 2022.pdf"

#strInputFileyFile = r"C:\Users\chris\OneDrive\RITS\DCC\PaySlips\NASA Umbrella Ltd Payroll for Chris Rae Week33 2022.pdf"

strInputFileyFile = strInputFile
  
# creating a pdf file object
pdfFileObj = open(strInputFileyFile, 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
  
# printing number of pages in pdf file
print(pdfReader.numPages)
  
# creating a page object
pageObj = pdfReader.getPage(0)
print(pageObj)    
# extracting text from page
#print(pageObj.extractText())
strPDF = pageObj.extractText()
print(strPDF)  
# closing the pdf file object
pdfFileObj.close()