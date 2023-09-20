

book_data=[]
users={}
class main_class:
   def add_data():
      user_name=input("Enter the User Name : ")
      book_num=int(input("Enter the Number of Books : "))
      emp_list={}
   
      for i in range(book_num):
                
                book_name=input("Enter the Book Name : ")
                book_data.append(book_name)
                print("Book Added Successfully")
                emp_list.append(book_name)
                users[user_name]=emp_list
                print(users)


# view the list of data  
   def list_data():
        print(book_data) 


# Remove a data
   def delete_data():
        rmv_book=input("Enter the book name to be Removed : ")
        book_data.remove(rmv_book)    
        print("Book removed Successfully!!!!",book_data)          

# Searching a data
   def search_data():
        search_book=input("Enter the name of the Book to be checked : ")
        if search_book in book_data:
            print("Book Found!!!!!!!")
        else:
            print("Sorry!!! No Matches Found.........")






                               
main_data=main_class
main_data.add_data()
main_data.list_data()
main_data.delete_data()
main_data.search_data()