class Customer:
    def __init__(self , customerName=None, customerEmail=None, customerPassword=None, customerContact=None, customerAddress=None):

        self.__customerName = customerName
        self.__customerEmail = customerEmail
        self.__customerPassword = customerPassword
        self.__customerContact = customerContact
        self.__customerAddress = customerAddress


    #customerId
    def setCustomerId(self, customerId):
        self.__customerId = customerId

    def getCustomerId(self):
        return self.__customerId

    #customerName

    def setCustomerName(self,customerName):
        self.__customerName=customerName

    def getCustomerName(self):
        return self.__customerName

    #customerEmail

    def setCustomerEmail(self,customerEmail):
        self.__customerEmail=customerEmail

    def getCustomerEmail(self):
        return self.__customerEmail

    #customerPassword

    def setCustomerPassword(self,customerPassword):
        self.__customerPassword=customerPassword

    def getCustomerPassword(self):
        return self.__customerPassword

    # customerContact

    def setCustomerContact(self, customerContact):
        self.__customerContact = customerContact

    def getCustomerContact(self):
        return self.__customerContact

    #customerAddress

    def setCustomerAddress(self,customerAddress):
        self.__customerAddress = customerAddress

    def getCustomerAddress(self):
        return self.__customerAddress

    def __str__(self):
        return "customerName :{}       | CustomerEmail :{}      | CustomerPassword :{}      | CustomerContact :{}       | CustomerAddress :{} ".format(self.__customerName,
                                                                                                            self.__customerEmail,
                                                                                                            self.__customerPassword,
                                                                                                            self.__customerContact,
                                                                                                            self.__customerAddress)

