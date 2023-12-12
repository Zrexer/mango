#!/usr/bin/env python3

"""

Dev: HOST1LET

"""

print("DEV:Host1let\n\n")

import platform
import subprocess
import os 

try:
    from PIL import Image 
    import pytesseract
except ImportError:
    subprocess.getoutput('pip install Pillow')
    subprocess.getoutput('pip install pytesseract')
    subprocess.getoutput('cls || clear')

osx = platform.system()
os.system('')


class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'

def info(msg):
    return "[INFO] {}".format(msg)

def err(msg):
    return "[ERROR] {}".format(msg)

def main(pathOfPyst):
    
    pytesseract.pytesseract.tesseract_cmd = pathOfPyst
    
    while 1:
        
        user = str(input(f'\n{colors.white}{colors.underline}Mango{colors.white} > '))
        
        if user == "panel" or user == "help":
            print('\nFor Set Path of Image: add path=PATH')
        
        if user.startswith('add'):
            path = user.replace('add ', '').split()[0].split('=')[-1]
            
            data = pytesseract.image_to_string(Image.open(path))
            print(f"\n {data} \n")


pathOfTesseract = None

if osx == "Windows":
    #print(info('Try to Download Tesseract ExE file'))
    #webbrowser.open('https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe')
    print("Please Download this and run exe file, after that go to your download path and there is a filename called ' tesseract.exe ' : copy paths of that and Enter path to this: ")

    pathOfTesseract = str(input('\nEnter Path of tesseract (Like Up ↑) > '))
    
    if pathOfTesseract == '' or pathOfTesseract == " " or pathOfTesseract == None:
        pathOfTesseract = './core/tesseract.exe'
    else:
        
        if os.path.exists(pathOfTesseract):
            print(info('File Does Exists, keep process ...'))
            main(pathOfTesseract)
            
        else:
            exit(err('File Does Not Exists, Try Again !'))
        
else:
    pathOfTesseract = str(input('Enter Path of tesseract > '))
    
    if pathOfTesseract == '' or pathOfTesseract == " " or pathOfTesseract == None:
        pathOfTesseract = './core/tesseract.exe'
    else:
        if os.path.exists(pathOfTesseract):
            print(info('File Does Exists, keep process ...'))
            main(pathOfTesseract)
            
        else:
            exit(err('File Does Not Exists, Try Again !'))
            
