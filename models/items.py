

class Book:
    def __init__(self,title,price,description,author,isbn):
        self.title=title
        self.price=price
        self.description=description
        self.author = author
        self.isbn  = isbn

    def setTitle(self,title):
        self.title =  title

    def setPrice(self,price):
        self.price=  price        

    def getBookInfo(self):
         info={"title":self.title,'price':self.price,
         'description':self.description,
         'author':self.author,
         'isbn':self.isbn}    
         return  info


    

    