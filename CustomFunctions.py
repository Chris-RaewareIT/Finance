#Operating systms

def main():

    GetOneDriveRoot()

def GetOneDriveRoot():    
    import platform


    varPlatform = platform.system()
    #print(varPlatform)

  #strRootFolder = 'C:/Users/chris/OneDrive/RITS/DCC/PaySlips/Unlocked/'

    #strRootFolder =  '/Users/chrisrae/Library/CloudStorage/OneDrive-Personal/RITS/DCC/PaySlips/Unlocked/'
    if varPlatform == 'Darwin':
            strOneDriveRoot = '/Users/chrisrae/Library/CloudStorage/OneDrive-Personal/'
    
    elif varPlatform == 'Microsoft':
            strOneDriveRoot = 'C:/Users/chris/OneDrive/'

    return strOneDriveRoot


if __name__ == "__main__":
    main()
