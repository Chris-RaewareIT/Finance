#Operating systms

def main():

    GetOperatingSystem()

def GetOperatingSystem():    
    import platform


    varPlatform = platform.system()
    print(varPlatform)


if __name__ == "__main__":
    main()
