class Cart:
    def setcartId(self, cartId):
        self.__cartId = cartId

    def getcartId(self):
        return self.__cartId

    def setFoodId(self, foodId):
        self.__foodId = foodId

    def getFoodId(self):
        return self.__foodId

    def setFoodQuantity(self, foodQuantity):
        self.__foodQuantity = foodQuantity

    def getFoodQuantity(self):
        return self.__foodQuantity

    def setCustomerEmail(self, customerEmail):
        self.__customerEmail = customerEmail

    def getCustomerEmail(self):
        return self.__customerEmail

    def __init__(self, cartId=None, foodId=None, customerEmail=None, FoodName=None, FoodPrice=None, foodQuantity=None):
        self.__cartId = cartId
        self.__foodId = foodId
        self.__customerEmail = customerEmail
        self.__FoodName = FoodName
        self.__FoodPrice = FoodPrice
        self.__foodQuantity = foodQuantity



    def __str__(self):
        return "Cart ID : {}, customer email : {}, FoodName : {}, FoodPrice : {}, foodQuantity : {}".format(self.__cartId,self.__customerEmail,self.__FoodName,self.__FoodPrice,self.__foodQuantity)
