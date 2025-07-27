#defining display menu
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove_Item")
    print("3. View List") 
    print("4. Exit") 

def main():
     shopping_list =[]

while True :
        display_menu()
        choice = input("enter your choice: ")
        shopping_list = []
        

        if choice == "1":
                updated_list = shopping_list.append(input("enter the item to add: "))
                pass
                
        
        elif choice == "2":
            updated_list = shopping_list.remove(input("enter the item to remove: "))
            pass

        elif choice == "3":
                for items in shopping_list:
                        print(items)
                        pass

        elif choice == 4:
                print("Goodbye!")
                break

        else:
                print("Invalid choice. Please try again. ")

if __name__ == "__main__":
    main()


        
