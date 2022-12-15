#!/usr/bin/python3

from library_mang_sys import User_login , shelf , software
import library_mang_sys




class color: # add colors in script
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   Orange='\033[33m'
   lightblue='\033[94m'
   lightcyan='\033[96m'
   BLUE = '\033[94m'
   Black = '\033[30m'
   GREEN = '\033[92m'
   pink='\033[95m'
   lightgreen='\033[92m'
   lightred='\033[91m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
import os 
import time 
import sys
import platform 

def logo():
    print(color.GREEN + """ 
    
   ___   ____ ______ ____  __    ____ ___   ___   ___    ___ __  __
  / _ ) /  _//_  __// __/ / /   /  _// _ ) / _ \ / _ |  / _ \\ \/ /
 / _  |_/ /   / /  _\ \  / /__ _/ / / _  |/ , _// __ | / , _/ \  / 
/____//___/  /_/  /___/ /____//___//____//_/|_|/_/ |_|/_/|_|  /_/    ~Made with Love By shirsh
                                                                                                                                                      
    """ + color.END )

current_time = color.RED + str([time.asctime()])  #gives day,date,time,year

def screen_clear():
   if os.name == 'posix': #for linux,unix,mac
      _ = os.system('clear')
   else:   #windows
      _ = os.system('cls')

def exiting():
  ask = input(color.BOLD+ color.lightblue + '\nDo You Want To Exit The Program(y:n) : ' + color.RED )
  def close():
    time.sleep(2)
    print(current_time + color.GREEN + "  Exiting the program.....")
    time.sleep(0.3)
    print(current_time + color.GREEN + "  Thanks for using SQLEET")
    time.sleep(2)
    screen_clear()
    logo()

def dependencies_check():
  screen_clear()
  print(current_time + color.BOLD + color.GREEN +  "  Checking for dependencies.....")
  import openpyxl
  time.sleep(1)
  print(current_time + color.BOLD  + color.GREEN + "  Dependencies satsfied.....")
  time.sleep(0.5)
  screen_clear()

def error_import():
  print("\n\n")
  print(color.BOLD + color.RED + color.UNDERLINE + "*"*50)
  print(color.BOLD + color.UNDERLINE + color.RED+ "INSTALLATION ERROR ===>" + color.Black + "It Seems Dependencies are not getting properly installed on your system. \nWe recommend you to Install " + color.RED + "webbrowser and mechanize" + color.Black +" module by our own according to your respective system'\n" + color.RED +"SOME KNOWN COMMANDS YOU CAN TRY : " + color.Black + "\n==> For Linux and Mac : \n* sudo pip3 install mechainze  \n* sudo pip3 install webbrowser \n==> For Termux and Windows  : \n* pip3 install mechanize \n* pip3 install webbrowser \nIf still Bug Remains Contact the develpor :)"+ color.END)
  print(color.BOLD + color.RED + "*"*50)
  print("")
  time.sleep(4)

def pip_Error():
  print("\n\n")
  print(color.RED + color.UNDERLINE + "*"*50)
  print(color.RED +  color.UNDERLINE + "PIP ERROR ===>" + color.Black + "It seems that python3-pip is not getting installed in your system. \nWe recommend you to install " + color.RED + "PIP" + color.Black + " by your own.\nSome suggestion to use ===> \nFor Termux : "+color.RED+"\n* apt install python3-pip "+color.Black+"\nFor Linux : "+color.RED+" \n* sudo apt install python3-pip  "+color.Black+"\nFor Windows : \n* install pip3 pkg from "+color.RED+"site: https://bootstrap.pypa.io/get-pip.py "+color.Black+"\n* and after Downloading run "+ color.RED + "python get-pip.py"+ color.Black+"in your cmd.exe \nFor Mac : "+color.RED+"\n* sudo easy_install pip "+color.Black+"\nIf still Bug Remains Contact the develpor :)" + color.END)   
  print(color.RED + "*"*50)
  print("")
  time.sleep(4)

try:
  dependencies_check()

except ImportError :
  print(current_time + color.GREEN + color.BOLD + "  Dependency Not Satisfied.....")
  time.sleep(0.5)
  print(current_time + color.GREEN + color.BOLD + "  Installing Required Dependency.....")
  time.sleep(0.5)
  print(current_time + color.BOLD + color.GREEN + "  Identifying your system")

  if platform.system() == 'Linux': ##system is linux/Termux
    time.sleep(0.5)
    print(current_time + color.BOLD + color.GREEN + "  system identified !!" + color.END)
    print(current_time + color.BOLD + color.GREEN + "  your system is : %s" %platform.system() + color.END)
    time.sleep(0.5)
    try:
      print(current_time + color.BOLD + color.GREEN + "  Checking for pip in your system....")
      os.system('sudo apt install python3-pip')
      print(current_time + color.BOLD + color.GREEN + "  Upgrading PIP....")
      time.sleep(0.5)
      os.system('pip3 install --upgrade pip')
      try:
        print(current_time + color.BOLD + color.GREEN + "  installing Mechanize module...\n" + color.END)
        time.sleep(0.5)
        os.system('pip3 install openpyxl')
        print("\n\n")
        print(current_time + color.GREEN + color.BOLD + "  All dependency uploaded\n")
        time.sleep(2)
        try:
          dependencies_check()
        except:
          error_import()
      except:
        error_import()
    except:
      pip_Error()

  elif platform.system() == 'Darwin': #mac
    time.sleep(0.5)
    print(current_time + color.BOLD + color.GREEN + "  system identified !!" + color.END)
    print(current_time + color.BOLD + color.GREEN + "  your system is : %s" %platform.system() + color.END)
    time.sleep(0.5)
    try:
      print(current_time + color.BOLD + color.GREEN + "  Print Checking for pip in your system....")
      os.system('sudo easy_install pip')
      print(current_time + color.BOLD + color.GREEN + "  Upgrading PIP....")
      time.sleep(0.5)
      os.system('pip3 install --upgrade pip')
      time.sleep(0.5)
      try:
        print(current_time + color.BOLD + color.GREEN + "  installing Mechanize module..." + color.END)
        time.sleep(0.5)
        os.system('sudo pip3 install openpyxl')
        print("\n\n")
        print(current_time + color.GREEN + color.BOLD + "  All dependency uploaded")
        time.sleep(2)
        try:
          dependencies_check()
        except:
          error_import()
      except:
        error_import()
    except:
      pip_Error()

  else:  #window
    time.sleep(0.5)
    print(current_time + color.BOLD + color.GREEN + "  system identified !!" + color.END)
    print(current_time + color.BOLD + color.GREEN + "  your system is : %s" %platform.system() + color.END)
    time.sleep(0.5)
    try:
      print(current_time + color.BOLD + color.GREEN + "  Print Checking for PIP in your system....")
      os.system('python -m pip --upgrade pip')
      print(current_time + color.BOLD + color.GREEN + "  PIP succesfully upgraded!!!!!")
      try:
        print(current_time + color.BOLD + color.GREEN + "  installing Mechanize module..." + color.END)
        time.sleep(0.5)
        os.system('pip3 install openpyxl')
        print("\n\n")
        print(current_time + color.GREEN + color.BOLD + "  All dependency uploaded")
        time.sleep(2)
        try:
          dependencies_check()
        except:
          error_import()
      except:
        error_import()
    except:
      pip_Error()



def menu():
  print("")
  print(color.PURPLE+color.BOLD+" [1] => Borrow Book"+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.YELLOW+color.BOLD+" [2] =>  Return Book "+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.CYAN+color.BOLD+" [3] => Reserve Book "+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.GREEN+color.BOLD+" [4] => You want to see all books  "+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.YELLOW+color.BOLD+" [5] => you want to see catalog "+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.YELLOW+color.BOLD+" [6] => Libriaian Login :  "+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")
  print(color.Orange+color.BOLD+" [7] CLOSE !"+color.END)
  print("")
  print(color.lightblue+color.BOLD+"="*80+color.END)
  print("")

def librarian_menu():
    print("")
    print(color.PURPLE+color.BOLD+" [1] => Add Book : "+color.END)
    print("")
    print(color.lightblue+color.BOLD+"="*80+color.END)
    print("")
    print(color.YELLOW+color.BOLD+" [2] =>  Remove Book :"+color.END)
    print("")
    print(color.lightblue+color.BOLD+"="*80+color.END)
    print("")
    print(color.CYAN+color.BOLD+" [3] => Get Book Count : "+color.END)
    print("")
    print(color.lightblue+color.BOLD+"="*80+color.END)
    print("")
    print(color.CYAN+color.BOLD+" [4] => Fetch book Data from Excel sheet "+color.END)
    print("")
    print(color.lightblue+color.BOLD+"="*80+color.END)




screen_clear()
logo()
print("")
menu()
print("")
option = input(color.lightred+color.BOLD+" [+] What you want to select = "+color.END)

if '1' in option:
  borrowing  = input("\n"+color.BOLD + color.GREEN +'Enter the Name of book to Borrow : ' + color.END)
  software.borrow_book(borrowing)

elif '2' in option: 
  borrowed  = input('\n'+color.BOLD + color.GREEN + 'Enter the Name of book to return : '+color.END)
  software.return_book(borrowed)

elif '3' in option:
  reserve  = input('\n'+color.GREEN+ color.BOLD + 'Enter the Name of book to reserve : '+color.END)
  software.reserve_book(reserve)

elif '4' in option:
  book_tag = input(color.PURPLE + color.BOLD + 'Please Enter The genre you want (Fiction/Mature/Motivation) : ' + color.END )
  shelf.show_book(book_tag)

elif '5' in option:
  shelf.show_catalog()

elif '6' in option:
  screen_clear()
  if User_login()==True:
        screen_clear()
        logo()
        print("")
        librarian_menu()
        print("")
        option = input(color.lightred+color.BOLD+" [+] What you want to select = "+color.END)
        if '1' in option:
            shelf.add_book()

        elif '2' in option:
            Book_name = input("\n"+color.BLUE + 'Enter The Book Name to remove : ' +color.END)
            shelf.remove_book(Book_name)

        elif '3' in option:
            ask = input("\n"+color.BLUE + 'Do you want to get count of shelf(1) or whole library(2) : ' + color.END)
            book_tag = input(color.PURPLE + color.BOLD +'\n'+'Please Enter The genre you want (Fiction/Mature/Motivation) : ' + color.END )
            shelf.get_book_count(book_tag , ask)

        elif '4' in option:
            path = input("\n"+color.lightgreen+"Excel File ka path de na Love day : "+color.END)
            shelf.populate_book()
        else : 
            exiting()
  elif User_login() == False:
    "Login Failed !"
    exiting()

  else : 
    exiting()
