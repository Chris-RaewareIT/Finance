#Operating systms

def main():

    TestOperatingSystem()

def TestOperatingSystem():    
    from CustomFunctions import GetOneDriveRoot  


    varRoot = GetOneDriveRoot()
    print(varRoot)
    


if __name__ == "__main__":
    main()
