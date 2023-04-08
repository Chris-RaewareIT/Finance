#Operating systms

def main():

    TestOperatingSystem()

def TestOperatingSystem():    
    from CustomFunctions import GetOperatingSystem  


    varPlatform = GetOperatingSystem()
    print(varPlatform)
    


if __name__ == "__main__":
    main()
