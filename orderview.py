from DatabaseConn import database,c
from Model.Order import Order
import datetime

class OrderView:
    def placeOrder(self, customerEmail):
        status = "processing"
        try:
            date = datetime.date.today()
            sql = "select sum(FoodPrice*foodQuantity) from cart inner join food on cart.FoodId=food.FoodId where CustomerEmail='%s'"
            i = c.execute(sql % (customerEmail))
            data = c.fetchone()
            totalBill = data[0]
            print("Total bill :", totalBill)

            sql1 = "insert into orders (CustomerEmail,Status,TotalBill,Date) values("'"{}"'","'"{}"'","'"{}"'","'"{}"'")".format(customerEmail,status,totalBill,date)
            i = c.execute(sql1)
            database.commit()
            print("your order placed")

        except Exception as ex:
            print(ex)

    def showOrder(self, customerEmail):
        orderlist = []
        try:
            sql="select * from Orders where CustomerEmail='%s'"
            i=c.execute(sql % (customerEmail))
            data=c.fetchall()
            for row in data:
                order = Order(row[0],row[1],row[2],row[3])
                orderlist.append(order)
            database.commit()
            if i ==0:
                print("order doesnt exist")
            else:
                print("show order", i, "rows affected")

        except Exception as ex:
            print(ex)

        return orderlist

    def deliverOrder(self, customerEmail):
        try:
            sql = "update orders set status= 'Delivered' where customerEmail='%s'"
            i = c.execute(sql % (customerEmail))
            database.commit()
            if i == 0:
                print("customer doesnt exist")
            else:
                print("values updated", i, "rows affected")
        except Exception as ex:
            print(ex)

    def cancelOrder(self, customerEmail):
        try:
            sql = "update orders set status= 'cancel' where customerEmail='%s'"
            i = c.execute(sql % (customerEmail))
            database.commit()
            if i == 0:
                print("customer doesnt exist")
            else:
                print("values updated", i, "rows affected")

        except Exception as ex:
            print(ex)
