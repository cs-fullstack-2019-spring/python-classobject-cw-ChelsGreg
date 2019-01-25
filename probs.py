def main():
    #prob1()
    # prob2()
    # prob3()
    prob4()


# class People:
#     def __init__(self, name = "", weight = 0, height = 0):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     def printBMI(self):
#         return (self.weight/(self.height*self.height) * 703)
#





# Create a class Dog. Make sure it has the attributes name, breed, color, gender.
# Create a function that will print all attributes of the class.
# Create an object of Dog in your problem1 function and print all of it's attributes.

# def prob1():
#
#     class Dog:
#         def __init__(self, name = "", breed = "", color = "", gender = ""):
#             self.name = name
#             self.breed = breed
#             self.color = color
#             self.gender = gender
#
#         def printClass(self):
#             return (self.name, self.breed, self.color, self.gender)
#
#
#
#     newPet = Dog("Spot", "Terrier", "Brown", "Male")
#     newPet.printClass()
#

#
#
# #Create a function that has a loop that quits with the equal sign.
# # If the user doesn't enter the equal sign, ask them to input another string.
#
#
#
# # def prob2():
# #
# #
# #     askThis = ""
# #
# #
# #     while(askThis != ("=")):
# #         askThis = input("What do you like to eat?")
# #         print("I like " + askThis + " too!")
# #         if (askThis == "="):
# #             break
# #
#
#
#
# # In your main file create three Person objects.
# # Change the weight and height of each one.
# # Afterwards, print the BMI (body mass index) of each Person.

# def prob3():
#
#     client1 = People("Chelsea", 120, 54)
#     client2 = People("Bob", 230, 60)
#     client3 = People("Amanda", 180, 52)
#     client1.weight = 150
#     client2.weight = 200
#     client3.weight = 145
#     client1.height = 57
#     client2.height = 62
#     client3.height = 56
#     print(client1.name, "has a BMI of:", client1.printBMI())
#     print(client2.name, "has a BMI of:", client2.printBMI())
#     print(client3.name, "has a BMI of:", client3.printBMI())
#
#



#Create a class Product that represents a product sold online. A product has a name, price, and quantity.
#  The class should have changeProduct:
#  a) If changeProduct has one parameter, it can change the name of the product.
#  b) If changeProduct has two parameters it can change the name and price of the product.
#  c) If changeProduct has three parameters it can change the name, price, and quantity of the product.
#  Create an object of Product in your problem4 function and print all of it's attributes.


def prob4():


    class Product:

        def __init__(self, name = "", price = 0, quantity = 0):
            self.name = name
            self.price = price
            self.quantity = quantity



        def changeProduct(self, name = "", price = 0, quantity = 0):

            self.name = name
            self.price = price
            self.quantity = quantity

            return (name, price, quantity)

        def printThis(self):
            print(self.name, self.price, self.quantity)

    newProd = Product("Fruity Pebbles", 3, 19)
    newProd.printThis()
    newProd.changeProduct("Frosted Flakes", 2, 45)
    newProd.printThis()



if __name__ == '__main__':
    main()