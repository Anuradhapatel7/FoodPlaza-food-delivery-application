from View.CartView import Cartview
from Model.Cart import  Cart

class CartTest:
    view=Cartview()
    def execute(self,choice):
        if choice==1:
            print("--------------Add to cart-------------")
            foodId=int(input("Enter food Id: "))
            foodQuantity=int(input("Enter Food Quantity: "))
            customerEmail=input("Enter customer Email Id:")
            cart=Cart(None, foodId,customerEmail, None, None,foodQuantity)
            test.view.addToCart(cart)
        elif choice==2:
            print("------------update cart----------------")
            cartId=int(input("Enter the existing cartId you want to update"))
            foodId = int(input("Enter food Id: "))
            foodQuantity = int(input("Enter Food Quantity: "))
            customerEmail = input("Enter customer Email Id:")
            cart = Cart(cartId, foodId, customerEmail, None,None, foodQuantity)
            test.view.updateCart(cart)

        elif choice==3:
            print("------------show cart----------------")
            customerEmail = input("Enter the existing customer email to see cart")
            cartlist = test.view.showCart(customerEmail)
            for cart in cartlist:
                print(cart)

        elif choice==4:
            print("-------------delete cart by iid_------")
            cartId=int(input("Enter the cartId you want to delete"))
            test.view.deleteCartById(cartId)

        elif choice==5:
            print("---------------delete cart by email--------------")
            customerEmail=input("Enter customer email to delete your cart")
            #cart=test.view.deleteCartByEmail(customerEmail)
            test.view.deleteCartByEmail(customerEmail)

        elif choice==6:
            print("===exit===")
            error #Exception to handle exit of while loop
        else:
            print("INvalid choice")



test=CartTest()
while(True):
    print(" 1. Add to cart  \n 2. Update cart \n 3. show cart \n 4. delete cart by id \n 5. delete cart by email \n 6. Exit \n")
    choice=int(input("Enter Your Choice"))
    test.execute(choice)
