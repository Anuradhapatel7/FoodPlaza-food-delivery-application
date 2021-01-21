from DatabaseConn import c,database
#from Template.FoodTemplate import FoodTest
from Model.Food import Food

class FoodView:
    def addFood(self,food):
        try:
            sql = "insert into food (FoodName,FoodType,FoodCategory,FoodDescription,FoodPrice) values('%s','%s','%s','%s',%d)"
            i = c.execute(sql % (food.getFoodName(),food.getFoodType(),food.getFoodCategory(),food.getFoodDescription(),food.getFoodPrice()))
            database.commit()
            print("food Info added ", i, "rows affected")
        except Exception as ex:
            print(ex)

    def updateFood(self,food):
        try:
            sql="update food set FoodName='%s',FoodType='%s',FoodCategory='%s',FoodDescription='%s',FoodPrice=%d where foodId=%d"
            i=c.execute(sql % (food.getFoodName(),food.getFoodType(),food.getFoodCategory(),food.getFoodDescription(),food.getFoodPrice(),food.getFoodId()))
            database.commit()
            if i==0:
                print("ID doesnt exist")
            else:
                print("value updated", i,"rows affected")
        except Exception as ex:
            print(ex)



    def deleteFood(self,foodId):
        try:
            sql="delete from food where foodId=%d"
            i=c.execute(sql %(foodId))
            database.commit()
            if i==0:
                print("id doesnt exist")
            else:
                print("data deleted",i,"rows affected")
        except Exception as ex:
            print(ex)




    def searchFood(self,foodId):
        try:
            sql = "select * from food where foodId=%d"
            i = c.execute(sql %(foodId))
            data=c.fetchone()
            food=Food(data[1],data[2],data[3],data[4],data[5])

            database.commit()
            if i==0:
                print("food Id doesn't exist")
            else:
                print("data search", i,"rows added")
        except Exception as ex:
            print(ex)
        return food

    def searchbyName(self, foodName):
        foodlist=[]
        try:
            sql = 'select * from food where foodName like "%'"{}"'%"'.format(foodName)
            i = c.execute(sql)
            data = c.fetchall()
            for result in data:
                food = Food(result[1], result[2], result[3], result[4], result[5])
                foodlist.append(food)
            database.commit()
            if i == 0:
                print("Food doesn't exist")
            else:
                print("data search", i, "rows added")
        except Exception as ex:
            print(ex)
        return foodlist

    def getAllData(self):
        foodlist=[]
        try:
            sql = "select * from food"
            i = c.execute(sql)
            data = c.fetchall()
            for result in data:
                food = Food(result[1], result[2], result[3], result[4], result[5])
                foodlist.append(food)
            database.commit()
            if i == 0:
                print("menu data doesn't exist")
            else:
                pass
        except Exception as ex:
            print(ex)
        return foodlist






