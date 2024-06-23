import users
import Product
class Middleware:
    def __init__(self):
        self.users = users.Users()
        self.Product = Product.Produts()
    def authcheck(self):
        if self.users.isLogin == True:
             self.Product.addproduct()
             self.Product.displayProduct()