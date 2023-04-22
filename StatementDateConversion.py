# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:06:14 2022

@author: chris
"""
import re
import shutil
import os

def create_folder(strFolderPath):


    if not os.path.exists(strFolderPath):
       try: 
           os.makedirs(strFolderPath)
       except:
           pass

def main():

    ListObjectsInRootFolder()

def amendFileName(srcfile_name,strAccountCode):  
    strConvertedDate = ''
    newFileName = srcfile_name
    if strAccountCode == "Clarity":
        strOrigFormat = '%d-%b-%y'
    
        # for Clarity get the right 10 chars
        #then get the left 6
        # prefix 08 for the day of the statement
        newFileDate = srcfile_name[-10:]
        newFileDate = newFileDate[:6]
        newFileDate = '08-'+newFileDate
    
        strConvertedDate = convertDate(newFileDate,strOrigFormat)
        
    elif strAccountCode == "hfxrca":

        strOrigFormat = '%d%m%Y'
    
        # for hfxrca get the right 12 chars
        #then get the left 8

        newFileDate = srcfile_name[-12:]
        newFileDate = newFileDate[:8]
        
        strConvertedDate = convertDate(newFileDate,strOrigFormat)
        
    elif strAccountCode == "hfxsav":

        strOrigFormat = '%d%m%Y'
    
        # for hfxrca get the right 12 chars
        #then get the left 8

        newFileDate = srcfile_name[-12:]
        newFileDate = newFileDate[:8]
    
        strConvertedDate = convertDate(newFileDate,strOrigFormat)
        
        #Barclaycard
    elif strAccountCode == "Barclaycard":

        strOrigFormat = '%d %B %Y'
    

        newFileDate = srcfile_name.replace('.PDF','')
        strConvertedDate = convertDate(newFileDate,strOrigFormat)
        
    elif strAccountCode == "Amex":

        strOrigFormat = '%d %b %Y'
    
        # for hfxrca get the right 12 chars
        #then get the left 8

        newFileDate = srcfile_name[-10:]
        newFileDate = newFileDate[:6]
        newFileDate = newFileDate +' 2022'
        
    elif strAccountCode == "ITCurrent":
        print(srcfile_name)
        newFileDate =''
        strConvertedDate = ''
        try:
            newFileDate = re.search(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{2}",srcfile_name)[0]
            strOrigFormat = '%d-%b-%y'



    
            strConvertedDate = convertDate(newFileDate,strOrigFormat)
        except:
            strConvertedDate = 'not date'
            
    elif strAccountCode == "ITSavings":
       #print(srcfile_name)
        newFileDate =''
        strConvertedDate = ''
        try:
            newFileDate = re.search(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{2}",srcfile_name)[0]
            strOrigFormat = '%d-%b-%y'



    
            strConvertedDate = convertDate(newFileDate,strOrigFormat)
        except:
            strConvertedDate = 'not date'
            
            
            
            
    elif strAccountCode == "BarclaysCurrent":
       #print(srcfile_name)
        newFileDate =''
        strConvertedDate = ''
        try:
            newFileDate = re.search(r"[\d]{1,2}-[adfjmnos]\w*-[\d]{2}",srcfile_name)[0]
            strOrigFormat = '%d-%b-%y'



    
            strConvertedDate = convertDate(newFileDate,strOrigFormat)
        except:
            strConvertedDate = 'not date'
            
    newFileName = strConvertedDate +'_'+ srcfile_name

    #print(newFileName)
    return newFileName    
    
def getFolderobjects(parDirectory):  
    import os
    print(parDirectory)
    dirObjects = os.listdir(parDirectory)
    dirObjectsfullpaths = map(lambda name: os.path.join(parDirectory, name), dirObjects)
    
    
    
    return dirObjectsfullpaths

def ListObjectsInRootFolder():
    
    


    # Get the Folders and files in the root folder  
    # strAccountCode = 'Clarity'
    # strAccountCode = 'hfxrca'
    # strAccountCode = 'hfxsav'
    # strAccountCode = 'Barclaycard'
    # strAccountCode = 'Amex'
    strAccountCode = 'ITCurrent'
    
    # strAccountCode = 'ITSavings'
    # strAccountCode = 'BarclaysCurrent'
    
    
    
    strRootFolder = ''
    strOrigFormat = ''
    strTargetFolderPath = ''
    
    if strAccountCode == "Clarity":
        strRootFolder = 'C:/Users/chris/OneDrive/Finances/Stmt/Personal/Joint/Halifax/ClarityCC'
        #strOrigFormat = '%d-%b-%y'
        
    elif strAccountCode == "hfxsav":
            strRootFolder = 'C:/Users/chris/OneDrive/Finances/Stmt/Personal/Joint/Halifax/Savings'
        
    elif strAccountCode == "hfxrca":
        strRootFolder = 'C:/Users/chris/OneDrive/Finances/Stmt/Personal/Joint/Halifax/RCA'
        #strOrigFormat = '%d%m%Y'

 
    elif strAccountCode == "Barclaycard":
        #C:\Users\chris\OneDrive\Finances\Stmt\Personal\Beki\BarclayCard
        strRootFolder = 'C:/Users/chris/OneDrive/Finances/Stmt/Personal/Beki/BarclayCard'
        #strOrigFormat = '%d%m%Y'
        
    elif strAccountCode == "Amex":
        #C:\Users\chris\OneDrive\Finances\Stmt\Personal\Beki\BarclayCard
        strRootFolder = 'C:/Users/chris/OneDrive/Finances/Stmt/Personal/Chris/Amex'
        #strOrigFormat = '%d%m%Y'
        
    elif strAccountCode == "ITCurrent":
        #C:\Users\chris\OneDrive\Finances\Stmt\Business\ITCurrent 70728829
        #C:\Users\chris\OneDrive\Finances\Stmt\Personal\Beki\BarclayCard
        strRootFolder = 'C:/Users/chris/OneDrive/Finances/Stmt/Business/ITCurrent 70728829'
        #strOrigFormat = '%d%m%Y'
    elif strAccountCode == "ITSavings":
        #C:\Users\chris\OneDrive\Finances\Stmt\Business\ITCurrent 70728829
        #C:\Users\chris\OneDrive\Finances\Stmt\Personal\Beki\BarclayCard
        strRootFolder = 'C:/Users/chris/OneDrive/Finances/Stmt/Business/ITActive 03133923'
        
        
       #C:\Users\chris\OneDrive\Finances\Stmt\Personal\Beki\BarclaysCurrent
    elif strAccountCode == "BarclaysCurrent":
        #C:\Users\chris\OneDrive\Finances\Stmt\Personal\Beki\BarclayCard
        strRootFolder = 'C:/Users/chris/OneDrive/Finances/Stmt/Personal/Beki/BarclaysCurrent'
        
        
    strTargetFolder = '/Chronological/'
    
    
    
    strTargetFolderPath = strRootFolder + strTargetFolder
    
    # strDoneFolder = 'C:/Users/chris/OneDrive/RITS/DCC/PaySlips/Done/'
    # strProblem = 'C:/Users/chris/OneDrive/RITS/DCC/PaySlips/Problem/'
    create_folder(strTargetFolderPath)
    
    #print(strRootFolder)
    lstObjects = getFolderobjects(strRootFolder)
    # print(lstObjects)
    
    for srcFile in lstObjects:
        srcfile_name = srcFile.replace(strRootFolder,"")
        srcfile_name = srcfile_name[1:]
        print(srcfile_name)

        #file_name = file_name.replace('NASA Umbrella Ltd Payroll for Chris Rae, ','')
        
        trgfile_name = amendFileName(srcfile_name,strAccountCode)
        
        trgFile = strRootFolder + strTargetFolder + trgfile_name
        
        try:
            shutil.copy2(srcFile,trgFile)
        except:
            err_Text ='Problem with file copy' 

        #print(trgFile)

def convertDate(strOrigDate,strOrigFormat):
    from datetime import datetime
    

    #strNewDate = datetime.strftime(datetime.strptime(strOrigDate,'%d-%b-%y'),'%Y%m%d')
    try:
        strNewDate = datetime.strftime(datetime.strptime(strOrigDate,strOrigFormat),'%Y%m%d')
    except:
        strNewDate = 'not date'
    
    return strNewDate


#clarity
# =============================================================================
# strOrigFormat = '%d-%b-%y'
# strOrigDate = '08-Nov-22' 
# =============================================================================

# =============================================================================
# hfxrca
# strOrigFormat = '%d%m%Y'
# strOrigDate = '23092022' 
# =============================================================================


# =============================================================================
# BarclayCard
# strOrigFormat = '%d %B %Y'
# strOrigDate = '25 August 2022'
# =============================================================================

# =============================================================================
# Amex
# strOrigFormat = '%d %b %y'
# strOrigDate = '10 Nov' + ' 22'
# =============================================================================



# =============================================================================
# strFilename ='Statement 18-NOV-22 AC 03133923  21160102.pdf'
# 
# 
# foundDate = re.search(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{2}", strFilename)[0]
# strOrigFormat = '%d-%b-%y'
# strOrigDate = foundDate 
# 
# print(foundDate)
# 
# strConvertedDate = convertDate(strOrigDate,strOrigFormat)
# print(strConvertedDate)
# =============================================================================


if __name__ == "__main__":
    main()
