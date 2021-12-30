# import os
import sys
# import subprocess
from rndstr import rndstr

def main():
    # デフォルトの出力数
    defaultNumber = 8

    if len(sys.argv) == 2:
        try:
            print(rndstr.rndstr(int(sys.argv[1])))
        except ValueError:
            print ("Error! Please do not enter characters other than numbers!")
            sys.exit()
    elif len(sys.argv) >= 3:
        print('Please enter only one args!')
        sys.exit()
    else:
        print(rndstr.rndstr(defaultNumber))

if __name__ == "__main__":
    main()