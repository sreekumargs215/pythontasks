

book_data=[]
users={}




class main_class:
 def add_data():
      user_name=input("Enter the User Name : ")

    
      emp_list=[]
      book_num=int(input("Enter the Number of Books : "))
      for i in range(book_num):
                
                book_name=input("Enter the Book Name : ")
                book_data.append(book_name)
                emp_list.append(book_name)               
                print("Book Added Successfully")
                users[user_name]=emp_list
                print(users)


# view the list of data  
 def list_data():
        print(book_data) 


# Remove a data
 def delete_data():
        rmv_book=input("Enter the book name to be Removed : ")
        book_data.remove(rmv_book)    
        print("Book removed Successfully!!!!",)
        book_data[users]=rmv_book
        print(book_data)

# Searching a data
 def search_data():
        search_book=input("Enter the name of the Book to be checked : ")
        if search_book in book_data:
            print("Book Found!!!!!!!")
        else:
            print("Sorry!!! No Matches Found.........")

#enroll the data
 def enroll():
       user_det={"Name : ","ID : ","Age :", "Books : "," "}
       user_det["Name"]=input("Name : ")
       user_det["ID"]=int(input("ID : "))
       user_det["Age"]=int(input("Age : "))
       #user_det[]=input("Name : ")
       num=int(input("Enter the Number of books to be entered : "))
       numli=[]
       for i in range(num):
           cname=input("Enter the name of the book to be added : ")
           user_det["Books"]=numli.append(cname)
       print(user_det)
 
 def addBook():
       print(users)

choice=1
while choice!=0:
      add=main_class
      print("1. Add Book")
      print("2. Delete Book")
      print("3. search Book")
      print("4. List Book")
      print("5. Search Data")
      print("6.Exit")
      choice=int(input("Enter choice: "))

      if choice==1:
        add.add_data()
      
      elif choice==2:
        add.delete_data()
       
      elif choice==3:
        add.search_data()
    
      elif choice==4:
        add.list_data()

      elif choice==5:
        add.search_data()

      elif choice==6:
        print("Exiting!")
        exit()

      else:
        print("Invalid choice!!") 
print()
                               
# main_data=main_class
# main_data.add_data()
# main_data.list_data()
# main_data.enroll()
# main_data.delete_data()
# main_data.search_data()