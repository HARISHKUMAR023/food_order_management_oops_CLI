import users

class MainClass:
    def __init__(self):
        self.users = users.Users()
        
    def main(self):
        while True:
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.users.Login()
            elif choice == '2':
                self.users.Register()
            elif choice == '3':
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    main_class = MainClass()
    main_class.main()
