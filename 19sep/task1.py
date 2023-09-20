class check():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def update(self,c):
        self.n.update(c)
    def view(self):
        return (self.n)
 
obj=check()
 
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Update Book")
    print("4. List Book")
    choice=int(input("Enter choice: "))
    if choice==1:
        n=(input("Enter the book name : "))
        obj.add(n)
        print("Book Name : ",obj.view())
 
    elif choice==2:
        n=input("Enter the Book Name to remove: ")
        obj.remove(n)
        print("The Removed Book Name is : ",obj.view())



    elif choice==3:
        n=input("Enter the Book Name to update: ")
        obj.update(n)
        print("The Updated Book Name is : ",obj.view())

    elif choice==4:
        print("List: ",obj.view())

 
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
print()