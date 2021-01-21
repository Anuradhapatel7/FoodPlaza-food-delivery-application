
from View.OrderView import OrderView

class OrderTest:
    view=OrderView()
    def execute(self,choice):
        if choice == 1:
            print("---------------place order---------------")
            customerEmail = input("Enter customer Email :")
            test.view.placeOrder(customerEmail)

        elif choice == 2:
            print("----------show order------------")
            customerEmail = input("Enter customer Email")
            orderlist=test.view.showOrder(customerEmail)
            for order in orderlist:
                print(order)

        elif choice == 3:
            print("----------deliver order------------")
            customerEmail = input("enter customer email")
            test.view.deliverOrder(customerEmail)

        elif choice ==4:
            print("------------cancel order---------------- ")
            customerEmail = input("enter customer email")
            test.view.cancelOrder(customerEmail)


        elif choice ==5:
            print("thank you")
            error  # Exception to handle exit of while loop

        else:
            print("please enter a valid choice")



test=OrderTest()
while(True):
    print(" 1. Place Order\n 2. show order \n 3. Deliver order \n 4. cancel order \n 5. Exit \n")
    choice=int(input("Enter Your Choice"))
    test.execute(choice)
