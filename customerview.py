from DatabaseConn import c,database
from Model.Customer import Customer

class CustomerView:
    def addCustInfo(self, customer):
        try:
            sql="insert into customer(customerName,customerEmail,customerPassword,customerContact,customerAddress) values('%s','%s','%s',%d,'%s')"
            i=c.execute(sql %(customer.getCustomerName(),customer.getCustomerEmail(),customer.getCustomerPassword(), customer.getCustomerContact(),customer.getCustomerAddress()))
            database.commit()
            print("customer Info added ", i,"rows affected")
        except Exception as ex:
            print(ex)

    def updateCustInfo(self,customer):
        try:
            sql="update customer set CustomerName='%s',CustomerEmail='%s',CustomerPassword='%s',CustomerContact=%d,CustomerAddress='%s' where CustomerId=%d"
            i = c.execute(sql % (customer.getCustomerName(),customer.getCustomerEmail(),customer.getCustomerPassword(),customer.getCustomerContact() ,customer.getCustomerAddress(),customer.getCustomerId()))
            database.commit()
            if i == 0:
                print("ID doesnt exist")
            else:
                print("value updated", i,"rows affected")
        except Exception as ex:
            print(ex)

    def deleteCustInfo(self, customerId):
        try:
            sql = "delete from customer where CustomerId=%d"
            i = c.execute(sql % (customerId))
            database.commit()
            if i is 0:
                print("id doesnt exist")
            else:
                print("data deleted", i, "rows affected")
        except Exception as ex:
            print(ex)

    def searchCustInfo(self,customerId):
        customer = None
        try:
            sql = "select * from customer where CustomerId=%d"
            i = c.execute(sql %(customerId))
            data = c.fetchone()
            customer = Customer(data[1], data[2], data[3], data[4], data[5])

            database.commit()
            if i is 0:
                print(" Id doesn't exist")
            else:
                print("data search", i, "rows added")
        except Exception as ex:
            print(ex)
        return customer

    def searchBymail(self,customerEmail):
        customer = None
        try:
            sql = 'select * from customer where CustomerEmail like "%'"{}"'%"'.format(customerEmail)
            i = c.execute(sql)
            data = c.fetchone()
            customer = Customer(data[1], data[2], data[3], data[4], data[5])
            database.commit()
            if i is 0:
                print(" Id doesn't exist")
            else:
                print("data search", i, "rows added")
        except Exception as ex:
            print(ex)
        return customer




