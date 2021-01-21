class Order:

    def setOrderId(self, orderId):
        self.__orderId = orderId

    def getOrderId(self):
        return self.__orderId

    def setCustomerEmail(self, customerEmail):
        self.__customerEmail = customerEmail

    def getCustomerEmail(self):
        return self.__customerEmail

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status

    def setTotalBill(self, totalBill):
        self.__totalBill = totalBill

    def getTotalBill(self):
        return self.__totalBill

    def setDate(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    def __init__(self , orderId=None,customerEmail=None,status=None,totalBill=None,date=None):

        self.__orderId = orderId
        self.__customerEmail = customerEmail
        self.__status = status
        self.__totalBill = totalBill
        self.__date = date


    def __str__(self):
        return " Order Id : {} ,Customer Email : {} ,Status : {} ,TotalBill : {} ,Date : {}".format(self.__orderId,
                                                                                                    self.__customerEmail,
                                                                                                    self.__status,
                                                                                                    self.__totalBill,
                                                                                                    self.__date)
