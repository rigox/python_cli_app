from .items import Book
from termcolor import cprint
from datetime import datetime
import json
import requests;

class Store:
    def __init__(self,books):
        self.books = books
        self.token =''
        self.cart = []
        self.Bearer= ''

    def listBooks(self):
        temp =  self.books
        for x in temp:
            cprint("ID: {}".format(x.get("ID")),'red')
            cprint("Title: {}".format(x.get('title')),'magenta')
            cprint("Author: {}".format(x.get('author')),'magenta')
            cprint("Description: {}".format(x.get('description')),'magenta')
            cprint("Price ${}.00".format(x.get('price')),'magenta')
            print("------------\n")
    
    def make_purchase(self):

       self.listBooks() 

       choice =  input("Enter selection: ") 
       print("\n")
       check =  input("Is the selection with the ID :{} correct y/n? ".format(choice))
       if(check=="y"):
            book =  self.find_by_id(choice)
            self.add_toCart(book)
       
    
    def find_book(self,title):
        temp  = self.books
        for x in temp:
            if(x.get('title') ==title):
                return x
    
    def make_receipt(self,b):
        transction_info  ={
             'item':b.get('title'),
             'price':b.get('price'),
             'date': datetime.today().strftime('%Y-%m-%d')
        }
        return  transction_info
    
    def add_toCart(self,book):
        self.cart.append(book)

    def  payment_login(self):
        cprint("Welcome to Banky your payment gateway","Purple")
        username  = input("Enter your username: ")
        password  = input("Enter you password: ")
        self.username=username
        res = requests.get("http://localhost:4000/Account/login",
        params={'username':username,'password':password}
        )
        x ="biggies"
        temp =  res.content
        self.token =  temp.decode('utf-8')
        self.Bearer = "Bearer {}".format(self.token)

    def checkout(self):
        items =  self.cart;
        total=0
        transaction_info=[]
        for x in items:
            total+= x.get('price')
            transaction_info.append(self.make_receipt(x))
        
        res =  requests.post("http://localhost:4000/Account/purchase",
        params={'info':json.dumps(transaction_info),'amount':total,'username':str(self.username)},
        headers={"Authorization":self.Bearer}
        )

        if res.status_code == 200:
            print("Purchase completed")
        else:
            print("Error")
    
    def find_by_id(self,ID):
        books =  self.books

        for x in books:
            if(x.get("ID")==int(ID)):
                return x
    
    def view_cart(self):
        items =  self.cart
        total = 0
        for x in items:
            cprint(x.get('title'),"yellow")
            total+=int(x.get('price'))
        
        cprint("Total: ${}".format(total),"magenta")


            




