class Produts:
    def __init__(self) :
        self.Produts=[]
        
    def addproduct(self):
        totalproduct = int(input("Enter how many product you are going to add:"))
       
        for i in range(totalproduct):
            productitem={"name":None,"price":None}
            nameproduct=input("enter Product name:")
            price = input("ENter price : ")
            productitem["name"]=nameproduct
            productitem["price"]=price
            self.Produts.append(productitem)
            print(f"The Product item {nameproduct} and it price {price} is add")
        print(self.Produts)
    def displayProduct(self):
        for i in self.Produts:
            for itemname , itemvalue in i.items():
                print(f'The Product  {itemname} is {itemvalue}' , end=" ")
                
my=Produts()
my.addproduct()
my.displayProduct()