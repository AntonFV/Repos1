import os
import pickle
if not os.path.exists('newPythonTask'):
    (os.mkdir('newPythonTask'))
class Person:
    def __init__(self, name, role):
        self.name = name
        self.role=role
    
class User(Person):
    
    def Lists(self):
        for i in library:
            print(i.title, i.author)
    
class librarian(Person):
    
    def Lists(self):
        for i in library:
            print(i.title, i.author, i.getStatus())
    def seePersons(self):
        for i in persons:
            print(i.name, i.role)
            

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

if os.path.exists("persons.pkl"):
    with open("persons.pkl","rb") as file:
        persons = pickle.load(file)
if os.path.exists("books.pkl"):
    with open("books.pkl","rb") as file:
        books = pickle.load(file)
if os.path.exists("library.pkl"):
    with open("library.pkl","rb") as file:
        library = pickle.load(file)    

print("Добро пожаловать!")
print("Введите имя и роль: ")
name = str(input())
role = str(input())

if (role =="Библиотекарь"):
    print("С возвращением", name)
    counter=0
    while(counter<1):
        print("Что будете делать?\n 1.Добавить книгу\n 2.Удалить книгу \n 3.Добавить пользователя \n 4.Посмотреть список пользователей \n 5.Посмотреть список книг \n 6.Удалить пользователя \n 0.Выход")
        variantLib = int(input())

        if (variantLib ==1):
            print("Введите название книги: ")
            Title = str(input())
            print("Введите автора книги: ")
            Author = str(input())
            newBook =Book(Title, Author, "Не выдана")
            library.append(newBook)

        if (variantLib ==2):
            print("Введите название книги")
            theName=str(input())
            for i in library:
                if (i.title==theName):
                    library.remove(i)
            
        if (variantLib ==3):
            print("Введите имя пользователя")
            name = str(input())
            theNewPerson = Person(name,"Гость") 
            persons.append(theNewPerson)

        if(variantLib ==4):
            print(librarian.seePersons(0))
        if(variantLib==5):
            print(librarian.Lists(0))
        if(variantLib ==6):
            print("Введите имя пользователя: ")
            theName=str(input())
            for i in persons:
                if (i.name==theName):
                    persons.remove(i)
        if(variantLib==0):
            counter = 1
elif(role=="Гость"):
    print("Добро пожаловать!", name)
    counter=0
    while(counter<1):
        print("Выберите действие: \n 1.Посмотреть список книг \n 2.Взять книгу \n 3.Вернуть книгу \n 4.Посмотреть список взятых книг \n 6.Выход")
        variantUser = int(input())

        if (variantUser ==1):
            print(User.Lists(0))


        if (variantUser==2):
            print("Выберите книгу: ")
            yourTurn = str(input())
            for i in library:
                
                if (i.title==yourTurn):
                    if (i.status=="Выдана"):
                        print("Книга уже выдана")
                    else:
                        print("Книга успешно выдана")
                        Book.giveForYou(i)
                        books.append(i)

        if (variantUser==3):
            print("Выберите книгу, которую хотите вернуть: ")
            yourTurnAgain = str(input())
            print("Вы вернули книгу. Вы молодец!")
            for i in library:
                
                if (i.title==yourTurn):
                        Book.returnToMe(i)
                        books.remove(i)

        if (variantUser==4):
            for i in books:
                print(i.title, i.name)

        
        if (variantUser==0):
            counter=1


with open("persons.pkl","wb") as file:
     pickle.dump(persons,file)
with open("books.pkl","wb") as file:
     pickle.dump(books,file)
with open("library.pkl","wb") as file:
     pickle.dump(library,file)

