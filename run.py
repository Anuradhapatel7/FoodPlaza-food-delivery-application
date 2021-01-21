import Template.FoodTemplate
import Template.OrderTemplate
import Template.CustomerTemplate
from Template.CartTemplate import cartRun
while(True):
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++FoodPlaza++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("1. Food")
    print("2. Customer")
    print("3. Cart")
    print("4. Order")
    print("5. Exit")
    choice=int(input("Enter the No. of operation :"))
    if choice==1:
        # food
        try:
           Template.FoodTemplate.foodRun()
        except:
           print('-------Exit From Food-------')


    elif choice==2:
        # customer
        try:
           Template.CustomerTemplate.customerRun()
        except:
           print('-------Exit From Customer-------')

    elif choice==3:
        # cart
        try:
           cartRun()
        except:
           print('-------Exit From Cart-------')


    elif choice==4:
       # order
       try:
          Template.OrderTemplate.orderRun()
       except:
           print('-------Exit From Order-------')


    elif choice==5:
       print("Thank You for visiting Food Plaza")
       break
    else:
       print("Please Enter the Valid Choice")
