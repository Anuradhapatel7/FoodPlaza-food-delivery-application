from DatabaseConn import c,database
from Model.Cart import Cart


class Cartview:

    def addToCart(self, cart):
        try:
            sql="insert into cart(foodId,foodQuantity,customerEmail) values(%d,%d,'%s')"
            i= c.execute(sql % (cart.getFoodId(),cart.getFoodQuantity(),cart.getCustomerEmail()))
            database.commit()
            print("food added to cart",i,"rows affected")
        except Exception as ex:
            print(ex)
    def updateCart(self, cart):
        try:
            sql = "update cart set foodId=%d,foodQuantity=%d,customerEmail='%s' where cartId=%d"
            i = c.execute(sql % (cart.getFoodId(),cart.getFoodQuantity(),cart.getCustomerEmail(),cart.getcartId()))
            database.commit()
            if i == 0:
                print("ID doesnt exist")
            else:
                print("value updated", i, "rows affected")
        except Exception as ex:
            print(ex)

    def showCart(self, customerEmail):
            cartlist = []
            try:
                sql = "select cartId, FoodName, FoodPrice, foodQuantity from cart inner join food on cart.foodId=food.foodId where customerEmail='%s'"
                i = c.execute(sql % (customerEmail))
                data = c.fetchall()
                for result in data:
                    cart = Cart(result[0], None, customerEmail, result[1], result[2], result[3])
                    cartlist.append(cart)
                database.commit()
                if i == 0:
                    print("cart data doesn't exist")
                else:
                    pass
            except Exception as ex:
                print(ex)
            return cartlist

    def deleteCartById(self, cartId):
        try:
            sql = "delete from cart where cartId=%d"
            i = c.execute(sql % (cartId))
            database.commit()
            if i is 0:
                print("id doesnt exist")
            else:
                print("data deleted", i, "rows affected")
        except Exception as ex:
            print(ex)

    def deleteCartByEmail(self, customerEmail):
        try:
            sql = "delete from cart where customerEmail='%s'"
            i = c.execute(sql % (customerEmail))
            database.commit()
            if i is 0:
                print("email doesnt exist")
            else:
                print("data deleted", i, "rows affected")
        except Exception as ex:
            print(ex)
