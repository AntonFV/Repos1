import os
filepath ='newPythonTask/thefirstfile.txt'
if not os.path.exists(filepath):
    (os.mkdir(filepath))
class Person:
    def __init__(self, name, role):
        self.name = name
        self.role= role
class User(Person):
    
    def Lists(self):
        for i in library:
            print(library)


class librarian(Person):
    
    def Lists(self):
        for i in library:
            print(Book.title, Book.author, Book.getStatus())


class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.__status = status
    def getStatus(self):
        return self.__status
    # def giveForYou(self):
    #     self.__status = "Выдана"
    # def returnToMe(self):
    #     self.__status = "Не выдана"
    def setStatus(self,status):
        self.__status = status


library=[]
persons=[]
books=[]

if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        alllib = file.read()
        splitlib = alllib.split()
        print(splitlib)
        o=0
        j=1
        k=2
        p=2
        while(p<len(splitlib)):
            titlee =splitlib[o]
            o=o+3
            authorr=splitlib[j]
            j=j+3
            statuss=splitlib[k]
            k=k+3
            p=p+3
            newnewBook=Book(titlee, authorr, Book.setStatus(Book,statuss))
            library.append(newnewBook)
    filepath ='newPythonTask/thethirdfile.txt'
if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        allpersons = file.read()
        splitpersons = allpersons.split()
        print(splitpersons)
        o=0
        j=1
        p=1
        while(p<len(splitpersons)):
            namee =splitpersons[o]
            o=o+2
            rolee=splitpersons[j]
            j=j+2            
            p=p+2
            User1 = User(namee, rolee)
            persons.append(User1)
filepath ='newPythonTask/thesecondfile.txt'
if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        allbooks = file.read()
        splitbooks = allbooks.split()
        print(splitbooks)
        o=0
        j=1
        k=2
        p=2
        while(p<len(splitbooks)):
            titleee =splitbooks[o]
            o=o+3
            authorrr=splitbooks[j]
            j=j+3
            statusss=splitbooks[k]
            k=k+3
            p=p+3
            theNewBook = Book(titleee, authorrr,Book.setStatus(Book,statusss))
            books.append(theNewBook)

print("Добро пожаловать!")
print("Введите имя и роль: ")
name = str(input())
role = str(input())

if (role =="Библиотекарь"):
    print("С возвращением", name)
    counter=0
    while(counter<1):
        print("Что будете делать?\n 1.Добавить книгу\n 2.Удалить книгу \n 3.Добавить пользователя \n 4.Посмотреть список пользователей \n 5.Посмотреть список книг \n 0.Выход")
        variantLib = int(input())

        if (variantLib ==1):
            Title = str(input())
            Author = str(input())
            newBook =Book(Title, Author, "Не_выдана")
            library.append(newBook)

        if (variantLib ==2):
            print("Введите название книги")
            theName=str(input())
            for i in library:
                if (i[Title]==theName):
                    library.pop(i)

        if (variantLib ==3):
            print("Введите имя пользователя, его роль и адрес: ")
            name = str(input())
            role = str(input())
            theNewPerson = User(name,role)
            persons.append(theNewPerson)

        if(variantLib ==4):
            for i in persons:
                print(i.name)
                print(i.role)
            
        if(variantLib==5):
            for book in library:
                print(book.title)
                print(book.author)
                print(Book.getStatus(book))
        if(variantLib==0):
            counter = 1
elif(role=="Гость"):
    print("Добро пожаловать!", name)
    counter=0
    while(counter<1):
        print("Выберите действие: \n 1.Посмотреть список книг \n 2.Взять книгу \n 3.Вернуть книгу \n 4.Посмотреть список взятых книг \n 0.Выход")
        variantUser = int(input())

        if (variantUser ==1):
            for book in library:
                print(book.title)
                print(book.author)


        if (variantUser==2):
            print("Выберите книгу: ")
            yourTurn = str(input())
            for i in library:

                if (Book.Title==yourTurn):
                    if (library(Book.status)=="Выдана"):
                        print("Книга уже выдана")
                    else:
                        print("Книга успешно выдана")
                        Book.giveForYou(library[i])
                        books.append(library[i])

        if (variantUser==3):
            print("Выберите книгу, которую хотите вернуть: ")
            yourTurnAgain = str(input())
            print("Вы вернули книгу. Вы молодец!")
            for i in library:

                if (Book.Title==yourTurn):
                    Book.returnToMe(library[i])
                    books.remove(library[i])

        if (variantUser==4):
            for book in books:
                print(book.title)
                print(book.author)
                

    
        if (variantUser==0):
            counter=1
filepath ='newPythonTask/thefirstfile.txt'
with open(filepath, 'w', encoding='utf-8') as file:
    book_strings = []
    for book in library:
        jei = Book.getStatus(book)
        book_strings.append(f"{book.title} {book.author} {jei}")
    file.write(', '.join(book_strings))
filepath ='newPythonTask/thesecondfile.txt'
with open(filepath, 'w', encoding='utf-8') as file:
    Tbook_strings = []
    for book in books:
        jei = Book.getStatus(book)
        Tbook_strings.append(f"{book.title} {book.author} {jei}")
    file.write(', '.join(Tbook_strings))
filepath ='newPythonTask/thethirdfile.txt'
with open(filepath, 'w', encoding='utf-8') as file:
    persons_strings = []
    for user in persons:
        persons_strings.append(f"{user.name} {user.role}")
    file.write(', '.join(persons_strings))