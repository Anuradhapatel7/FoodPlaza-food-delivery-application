from Model.Food import Food
from View.FoodView import FoodView

class FoodTest:
    view=FoodView()
    def execute(self,choice):
        if choice == 1:
            print("-----------Add Food-------------")
            foodName=input("Enter the Name: ")
            foodType=input("Enter the Food Type: ")
            foodCategory=input("Enter the Food Category")
            foodDescription=input("Enter the Description")
            foodPrice=float(input("Enter the Food Price"))
            food=Food(foodName,foodType,foodCategory,foodDescription,foodPrice)
            test.view.addFood(food)

        elif choice == 2:
            print("--------update food----------------")
            foodId=int(input("ENter the existing foodID ehich you want to update "))
            foodName = input("Enter the Name: ")
            foodType = input("Enter the Food Type: ")
            foodCategory = input("Enter the Food Category")
            foodDescription = input("Enter the Description")
            foodPrice = float(input("Enter the Food Price"))
            food = Food(foodName, foodType, foodCategory, foodDescription, foodPrice)
            food.setFoodId(foodId)
            test.view.updateFood(food)






        elif choice == 3:
            print('---------------delete food---------------')
            foodId=int(input("Enter the existing foodId you want to delete"))
            test.view.deleteFood(foodId)


        elif choice == 4:
            print("----------search food------------")
            foodId=int(input("Enter the existing foodid you want to search"))
            food=test.view.searchFood(foodId)
            print(food)

        elif choice == 5:
            print("----------search food by name------------")
            foodName = input("Enter the foodname you want to search")
            foodlist = test.view.searchbyName(foodName)
            for food in foodlist:
                print(food)



        elif choice ==6:
            print("------------show menu---------------- ")
            foodlist=test.view.getAllData()
            for food in foodlist:
                print(food)


        elif choice ==7:
            print("thank you")
            error  # Exception to handle exit of while loop

        else:
            print("please enter a valid choice")



test=FoodTest()
while(True):
    print(" 1. Add Food \n 2. Update Food \n 3. Delete Food \n 4. Search Food \n 5. Search by Name \n 6. Menu \n 7. Exit \n")
    choice=int(input("Enter Your Choice"))
    test.execute(choice)
