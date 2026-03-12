import os

def create_file(filename):
    try:
        with open (filename,'x')as f:
            print(f"file name{filename}:successfully created")
            
    except FileExistsError:
        print("file already exists")
    except Exception as e:
        print("An error occured")
        
def find_all_files():
    files= os.listdir()
    if not files:
        print("file not in directory")
    else:
        print("files in directory:")
        for file in files:
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted")
    except FileNotFoundError:
        print("file not found")
        
    except Exception as e:
        print("An error occured")
        
def read_file(filename):
    try:
        with open (filename,'r') as f:
            content = f.read()
            print(f"content of '{filename}':\n{content}")
            
    except FileNotFoundError:
        print("file doesn't exists")
        
    except Exception as e:
        print("An error occured")
    
def edit_file(filename):
    try:
        with open(filename,'a')as f:
            content = input("enter dada to add:")
            f.write(content + "\n")
            print(f"content added to {filename}")
            
    except FileNotFoundError:
        print("file doesn't exists")
        
    except Exception as e:
        print("An error occured")
        
def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1 : CREATE FILE")
        print("2 : VIEW ALL FILES")
        print("3 : DELETE FILE")
        print("4 : READ FILE")
        print("5 : EDIT FILE")
        print("6 : EXIT")
        
        choice= input("enter your choice (1-6)=")
        
        if choice=='1':
            filename=input("enter file name=")
            create_file(filename)
            
        elif choice == '2':
            find_all_files()
            
        elif choice=='3':
            filename=input("enter file name that want to delete=")
            delete_file(filename)
            
        elif choice =='4':
            filename=input("enter file name that you want to read=")
            read_file(filename)
            
        elif choice =='5':
            filename=input("enter file name to edit")
            edit_file(filename)
            
        elif choice =='6':
            print("closing the app...")
            break
        
        else:
            print("invalid choice")
            
if __name__ == "__main__":
    main()