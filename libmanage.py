# write a library class with no.of books an dbooks as a list write a program to create a library from this library class and show all the books add the book and get the number of books using different method 

# thing this system will do
# show the available books ......done
# maintain the number of books....done
# maintain teh list of those books....done
# when new book is added update the number of books...done
# when a book is issued update the number of books...done
# keep a log of the transaction....done


class Library:
    def __init__(self):
        self.books = ["harry Potter","python for beginer"]
        self.Total_books =0
        self.log=[]
    def available_books(self):
        self.books.sort()
        print("available books are :")
        for index, book in enumerate(self.books):
            print(f"\t{index+1}. {book} ")
        
    def add_book(self,name):
        self.books.append(name)
        print(f"you have succesfully added {name}")
        self.log.append(f"{user} added book {name}")


    def issue_book(self,name):
        if name in self.books:
            self.log.append(f"{user} issued book {name}")
            issued_book = self.books.pop(self.books.index(name))
            print(f"you have succesfully issued {issued_book}")
        else:
            print("the book is not available")

    def number_of_books(self):
        self.Total_books =len(self.books)
        print(f"---->the total number of books are {self.Total_books}")
    
    def _log(self):
        self.log.reverse()
        for index,l in enumerate(self.log):
            print(f"{index+1}. {l}")



ac = str(input("do you want to access the Library Management System: "))

access = True
user=""

if(ac.lower() == "yes"):
    user = str(input("Enter your name :"))
    print("things you can do : ")
    print('''    1. see the available books
    2. add a new book
    3. issue a book 
    4. see total number of available books
    5. log of transaction
    6. exit
    ''')
    access = True
else:
    access = False

lib = Library()

while(access):

    choice = int(input("enter your choice: "))

    if choice == 1:
        lib.available_books()
    elif choice ==2:
        new_book = str(input("Enter the name of the book: "))
        lib.add_book(new_book)
    elif choice == 3:
        issue_book = str(input("Enter the name of the book: "))
        lib.issue_book(issue_book)
    elif choice==4:
        lib.number_of_books()
    elif choice==5:
        lib._log()
    elif choice == 6:
        access =False
        print(f"thank you for using LMS {user}")
        break
    
