class Food:
    def __init__(self ,foodName=None,foodType=None,foodCategory=None,foodDescription=None,foodPrice=None):

        self.__foodName=foodName
        self.__foodtype=foodType
        self.__foodCategory=foodCategory
        self.__foodDescription=foodDescription
        self.__foodPrice=foodPrice


    #FoodId
    def setFoodId(self,foodId):
        self.__foodId=foodId

    def getFoodId(self):
        return self.__foodId

    #foodName

    def setFoodName(self,foodName):
        self.__foodName=foodName

    def getFoodName(self):
        return self.__foodName

    #foodType

    def setFoodType(self,foodtype):
        self.__foodtype=foodtype

    def getFoodType(self):
        return self.__foodtype

    #foodCategory

    def setFoodCategory(self,foodCategory):
        self.__foodCategory=foodCategory

    def getFoodCategory(self):
        return self.__foodCategory

    # foodDescription

    def setFoodDescription(self, foodDescription):
        self.__foodDescription = foodDescription

    def getFoodDescription(self):
        return self.__foodDescription

    #foodPrice

    def setFoodPrice(self, foodPrice):
        self.__foodPrice = foodPrice

    def getFoodPrice(self):
        return self.__foodPrice

    def __str__(self):
        return "FoodName :{}       | FoodType :{}      | FoodCategory :{}      | FoodDescription :{}       | FoodPrice :{} ".format(self.__foodName,
                                                                                                            self.__foodtype,
                                                                                                            self.__foodCategory,
                                                                                                            self.__foodDescription,
                                                                                                            self.__foodPrice)

















    
