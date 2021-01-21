from View.CustomerView import CustomerView
from Model.Customer import Customer

class CustomerTest:
    view=CustomerView()
    def execute(self,choice):
        if choice == 1:
            print("--------add customer----------")
            customerName=input("Enter customer name")
            customerEmail=input("Enter customer Email")
            customerPassword=input("Enter password")
            customerContact=int(input("Enter customer contact number"))
            customerAddress=input("Enter customer address")
            customer=Customer(customerName,customerEmail,customerPassword,customerContact,customerAddress)
            CustomerTest.view.addCustInfo(customer)

        elif choice == 2:
            print("--------update customer-----------")
            customerId = int(input("Enter thr existing customerId you want to update"))
            customerName = input("Enter customer name")
            customerEmail = input("Enter customer Email")
            customerPassword = input("Enter password")
            customerContact = int(input("Enter customer contact number"))
            customerAddress = input("Enter customer address")
            customer = Customer(customerName,customerEmail,customerPassword,customerContact,customerAddress)
            customer.setCustomerId(customerId)
            CustomerTest.view.updateCustInfo(customer)

        elif choice == 3:
            print("--------delete cutomer data----------")
            customerId=int(input("rnter the existing customerId to delete: "))
            test.view.deleteCustInfo(customerId)

        elif choice == 4:
            print("-------search customer info--------------")
            customerId=int(input("Enter the exsiting Id to search"))
            customer=test.view.searchCustInfo(customerId)
            print(customer)

        elif choice == 5:
            print("---------------search customer by email----------")
            customerEmail = input("enter the exixting customeremail to search: ")
            customer=test.view.searchBymail(customerEmail)
            print(customer)

        elif choice == 6:
            print("----------exit----------")
            error  # Exception to handle exit of while loop
        else:
            print("Invalid Input")








test=CustomerTest()
while(True):
    print(" 1. Add customer info \n 2. Update customer info \n 3. Delete customer info  \n 4. Search customer info \n 5. search customer info by email \n 7. Exit \n")
    choice=int(input("Enter Your Choice"))
    test.execute(choice)
