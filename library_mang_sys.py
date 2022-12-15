#!/usr/bin/python3

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

from script import populate
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',)


import time

books = {'Harry Potter' : ['J.K Rowling' , '978-1-60309-502-0' , 'Fiction' , 'Available'] , 
'Animal Stories' : ['Maria Hoey' , '978-1-60309-502-1' , 'Mature' , 'Not Available'] , 
'Sherlock Holmes' : ['Sir Aurthor Canon' , '978-1-60309-502-6' , 'Fiction' , 'Available'],
'Work Wise ' : ['Rahul Kapoor' , '978-1-60309-502-2' , 'Motivation' , 'Available' ] }

login_detail = {'big_daddy@pilani.bits-pilani.ac.in' : 'cometodaddy'}



def User_login():
     email = input("Enter email: ")
     pwd = input("Enter password: ")
     stored_email  = list(login_detail.keys())
     stored_pwd = list(login_detail.values())
     if email == stored_email[0] and  pwd == stored_pwd[0]:
         print("Logged in Successfully!")
         return True
     else:
        print("Login failed! \n")
        return False


class software():
    def __init__(self):
        pass
    
    @classmethod
    def borrow_book(self,borrowing):
        self.borrowing = borrowing
        book_borrow = books[borrowing]
        if book_borrow[3]==('Available'):
            book_borrow[3] = 'Not Available'
            books.update({borrowing : book_borrow})
            print('\n'+color.GREEN + 'Book Issued Successfully !')
            return True
            time.sleep(2)
        else : 
            print('\n' + color.RED + ' Book Not Available ! ' + color.END)
            return False
            time.sleep(2)
    @classmethod
    def return_book(self,borrowed):
        self.borrowed = borrowed
        book_return = books[borrowed]
        if book_return[3] == 'Not Available':
            book_return[3] = 'Available'
            books.update({borrowed : book_return})
            logging.info('Book Returned Successfully !')
            return True
            time.sleep(2)
        else : 
            logging.warning('Wrong Query')
            return False
            time.sleep(2)

    def reserve_book(self,reserve):
       self.reserve = reserve
       book_reserve = books[reserve]
       if book_reserve[3]==('Available'):
        book_reserve[3] = 'Reserved'
        books.update({reserve : book_reserve})
        print('\n'+color.GREEN + 'Book Reserved Successfully !')
        return True
        time.sleep(2)
       else : 
        print('\n'+color.RED+'Book Not Available'+color.END)
        return False
        time.sleep(2)

class shelf():

    def __init__(self):
        pass
    @classmethod
    def show_book(self , book_tag):
        self.book_tag = book_tag 
        list_book_name = list(books.keys())
        try :
            for no in range(0,(len(list_book_name))):
                book_detail = list(books.values())
                book_detail_phir_se = list(book_detail[no])
                book_name = list_book_name[no]
                book_author = book_detail_phir_se[0]
                book_ISBN = book_detail_phir_se[1]
                book_type = book_detail_phir_se[2]
                book_status = book_detail_phir_se[3]
                if book_tag == book_type :
                    print("")
                    print(color.RED + color.UNDERLINE + "*"*50)
                    print(color.Black +  "Book Name : " + book_name)
                    print(color.BLUE+ 'Book Author : ' +  book_author)
                    print(color.CYAN+"Book ISBN : " + book_ISBN)
                    print(color.DARKCYAN+"Book Type : " + book_tag)
                    print(color.GREEN+"Book Status : " + book_status)
                    print(color.RED + color.UNDERLINE + "*"*50)
                    print("")
                else :
                    pass
        except IndexError:
            pass
    @classmethod
    def show_catalog(self):
        list_book_name = list(books.keys())
        try :
            for no in range(0,(len(list_book_name)+1)):
                book_detail = list(books.values())
                book_detail_phir_se = list(book_detail[no])
                book_tag = book_detail_phir_se[2]
                print("")
                print(color.BOLD+color.BLUE+color.UNDERLINE+ book_tag)
                print("")
        except IndexError:
            pass
    @classmethod
    def add_book(self):

        Book_name  = input("\n"+color.BLUE + 'Enter The Book Name to  add : '+color.END)
        Book_author = input('\n'+color.BLUE +"Enter The Author's Name of Book : "+color.END)
        Book_ISBN = input('\n'+color.BLUE + 'Enter The ISBN of book : '+ color.END)
        Book_type = input("\n"+color.BLUE + 'Enter The Book Type : ' + color.END)
        Book_status = input("\n"+color.BLUE + 'Enter The Book Status(Available/Non Avialable) : ' + color.END)
        print(color.GREEN+color.BOLD+"Book Added Successfully !" + color.END)

        Book_details = [Book_author , Book_ISBN , Book_type]
        entry = {Book_name  : Book_details}
        books.update(entry)

    @classmethod
    def remove_book(self,Book_name):
        self.Book_name = Book_name
        del books[Book_name]
        return True
    @classmethod
    def get_book_count(self,book_tag,ask) :
        self.book_tag = book_tag
        self.ask = ask 
        list_book_name = list(books.keys())
        if ask=='2' :
            print("\n"+color.CYAN+'total no of book in library are : ' + str(len(list_book_name)))
            return len(list_book_name)
        try :
            count = 0
            for  no in range(0,(len(list_book_name))):
                book_detail = list(books.values())
                book_detail_phir_se = list(book_detail[(no)])
                if ask =='1':
                    if book_detail_phir_se[2]==book_tag :
                        count += 1
                    else : 
                        pass
            if ask =='1':    
                print("\n"+color.DARKCYAN+ "Total no of books in this genre are : " + str(count) +color.END)
                return count     

        except IndexError:
            pass
    def populate_book(path):
        populate(color,books,path)

