#PABBU SAI KRISHNA
#krishna5c3@outlook.com
#GIVEN TASK: CRUD OPERATIONS ON FOOD BOOKING IN IRCTC WEBSITE


#All functions has been created to perform the user requirements as accept,display,search,delete,update.
#while loop has been used to make an infite loop as it must be appeared everytime to the user
#exit() is used to get out of the loop
#Based on the if else conditions the Requirement problems have been executed

#created a class Irctc
class Irctc:
    #init method defined
	def __init__(self, name,Id, phn, email,food,location):
		self.name = name
		self.Id=Id
		self.phn = phn
		self.email = email
		self.food = food
		self.location=location

	def accept(self, name,Id, phn, email, food, location):
		ob = Irctc(name,Id, phn, email, food, location )
		ls.append(ob)

	def display(self, ob):
			print("Name : ", ob.name)
			print("ID : ", ob.Id)
			print("Contact : ", ob.phn)
			print("Email : ", ob.email)
			print("Food : ", ob.food)
			print("Location : ", ob.location)
			print("\n")	
		
	def search(self, rn):
		for i in range(ls.__len__()):
			if(ls[i].Id == rn):
				return i	

	def delete(self, rn):
		del ls[rn-1]

	def update(self, rn, No):
		ls[rn-1].Id = No;	
ls =[]
obj = Irctc('',0,'','','','')

print("$$$$$$......WELCOME TO THE IRCTC FOOD BOOKING WEBSITE.......$$$$$$")
print("######......WE ARE HERE TO DELIVER YOUR FOOD......######")
print("////........ ORDER YOUR FOOD ENJOY THE TASTE....... ////")
while(1):
    print("\nOperations used, ")
    print("1.Accept Customer order  2.Display Customer order Details  3.Search Details of a Customer order 4.Delete Details of Customer order  5.Update Order Details 6.Exit")
    
    ch = int(input("Enter choice:"))
    if(ch == 1):
        name=input("Enter the Name : ")
        Id=input("Enter the Id: ")
        phn=input("Enter the Contact: ")
        email=input("Enter the Email: ")
        food=input("Enter the Food: ")
        location=input("Enter the Location: ")
        print("The details are entered")
        obj.accept(name, Id, phn, email,food,location)
		
    elif(ch == 2):
        print("\n")
        print("\nList of Customer order details....\n")
        for i in range(ls.__len__()):	
            obj.display(ls[i])

    elif(ch == 3):
        print("\n Customer order found....... ")
        z=int(input("ENTER CUSTOMER ID TO SEARCH: "))
        obj.display(ls[z])
		
    elif(ch == 4):
        z=int(input("ENTER CUSTOMER ID TO DELETE: "))
        obj.delete(z)
        print("customer order deleted.....")

    elif(ch == 5):
        a=int(input("Enter id to update"))
        b=int(input("Enter updated id number"))
        obj.update(a, b)
        print("customer order updated")

    else:
        print("Enter valid input...")
        print("Thank You !")
        exit()
	

	
