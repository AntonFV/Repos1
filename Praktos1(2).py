import os
if not os.path.exists('newPythonTask'):
    (os.mkdir('newPythonTask'))

class Person:
    def __init__(self, name):
        self.name = name
class User(Person):
    def __init__(self,role,adress):
        self.role=role
        self.__adress=adress
    def Lists(self):
        for i in library:
            print(library)
    def iWantNewAdress(self,adress):
        self.adress=adress
class librarian(Person):
    def __init__(self,role):
        self.role=role
    def Lists(self):
        for i in library:
            print(library[i])
            print(Book.getStatus())

class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status
    def getStatus(self):
        return self.status
    def giveForYou(self):
        self.status = "Выдана"
    def returnToMe(self):
        self.status = "Не выдана"


library=[]
persons=[]
books=[]
if os.path.exists('thefirstfile.txt'):
    with open('thefirstfile.txt', 'r', encoding='utf-8') as file:
        alllib = file.read()
        splitlib = alllib.split()
        o=0
        j=1
        k=2
        for i in splitlib:
            titlee =splitlib[o]
            o=o+3
            authorr=splitlib[j]
            j=j+3
            statuss=splitlib[k]
            k=k+3
            newnewBook=Book(titlee, authorr, statuss)
            library[i]=newnewBook
if os.path.exists('thethirdfile.txt'):
    with open('thethirdfile.txt', 'r', encoding='utf-8') as file:
        allpersons = file.read()
        splitpersons = allpersons.split()
        o=0
        j=1
        k=2
        for i in splitlib:
            namee =splitpersons[o]
            o=o+3
            rolee=splitpersons[j]
            j=j+3
            adresss=splitpersons[k]
            k=k+3
            User1 = User(namee,rolee,adresss)
            persons[i]=User1
if os.path.exists('thesecondfile.txt'):
    with open('thesecondfile.txt', 'r', encoding='utf-8') as file:
        allbooks = file.read()
        splitbooks = allbooks.split()
        o=0
        j=1
        k=2
        for i in splitbooks:
            titleee =splitbooks[o]
            o=o+3
            authorrr=splitbooks[j]
            j=j+3
            statusss=splitbooks[k]
            k=k+3
            theNewBook = Book(titleee, authorrr,statusss)
            books[i]=theNewBook

print("Добро пожаловать!")
print("Введите имя и роль: ")
name = str(input())
role = str(input())

if (role =="Библиотекарь"):
    print("С возвращением", name)
    counter=0
    while(counter<1):
        print("Что будете делать?")
        variantLib = int(input())

        if (variantLib ==1):
            Title = str(input())
            Author = str(input())
            newBook =Book(Title, Author, "Не выдана")
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
            adress=str(input())
            theNewPerson = Person(name,role,adress) 
            persons.append(theNewPerson)

        if(variantLib ==4):
            print(persons)
        if(variantLib==5):
            print(librarian.Lists())
        if(variantLib==0):
            counter = 1
elif(role=="Гость"):
    print("Добро пожаловать!", name)
    counter=0
    while(counter<1):
        print("Выберите действие:")
        variantUser = int(input())

        if (variantUser ==1):
            print(User.Lists())


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
            print(books)

        if (variantUser ==5):
            print("Введите новый адрес: ")
            newAdress = str(input())
            User.iWantNewAdress(newAdress)
        if (variantUser==0):
            counter=1
filepath ='newPythonTask/thefirstfile.txt'
with open(filepath,'w', encoding='utf-8') as file:
    libraryS = ' '.join(library)
    file.write(libraryS)
filepath ='newPythonTask/thesecondfile.txt'
with open(filepath,'w', encoding='utf-8') as file:
    booksS = ' '.join(books)
    file.write(booksS)
filepath ='newPythonTask/thethirdfile.txt'
with open(filepath,'w', encoding='utf-8') as file:
    personsS = ' '.join(persons)
    file.write(personsS)