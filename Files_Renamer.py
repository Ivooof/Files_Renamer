#CREATED BY IVOOF_

import os
import time
import sys

print("Welcome to the renamer file system!")
print("Remember that when you go to put the path of the files, put a slash (\) at the end of the path.")
route = input("Enter the path of the files (EXAMPLE: D:\Taaaa\):")
name = input("Enter the NEW NAME for the files to be replaced with this NEW NAME:")
termination = input("Enter file ending to be replaced:")

def main():
        i = 0
        path = route
        for filename in os.listdir(path):
            my_dest = name + str(i) + termination
            my_source = path + filename
            my_dest = path + my_dest
            os.rename(my_source, my_dest)
            i += 1
try:
    if __name__ == '__main__':
        main()
        print("Renaming your files, be patient...")
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width + 1))
        for i in range(toolbar_width):
            time.sleep(0.1)
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n")
except:
    print("An error occurred, please try again.")
finally:
    print("It finished replacing the name of all the files correctly!")

#CREATED BY IVOOF_