class Users:
    def __init__(self):
        self.email = None
        self.password = None
        self.phone = None
        self.address = None
        self.city = None
        self.state = None
        self.zip = None
        self.name = None
        self.role = None
        self.users = {}
        self.isLogin = False
    def Login(self):
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")
        # Check if email and password are valid
        if self.email in self.users and self.users[self.email] == self.password:
            self.isLogin=True
            print(f"Login successful {self.email}")
            
        else:
            print("Login failed")
            print("Please try again")

    def Register(self):
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")
        self.phone = input("Enter your phone number: ")
        self.address = input("Enter your address: ")
        self.city = input("Enter your city: ")
        self.state = input("Enter your state: ")
        self.zip = input("Enter your zip code: ")
        self.name = input("Enter your name: ")
        self.role = input("Enter your role: ")
        self.users[self.email] = self.password
        print(f"Registration successful {self.name}")
        print("Please login to continue")
