#Emir Yorgun
#Pizza Order System Project

#Importing the required libraries
import csv
import datetime
import os

#Reading the menu from the menu.txt file
def readMenu():
    with open('menu.txt', 'r') as f:
        for line in f:
            print(line, end='')

#Creating the Pizza superclass
class Pizza:
    def __init__(self):
        self.description = ''
        self.price = 0.0

    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
#Creating the subclasses of the Pizza superclass (Classic, Margherita, Turk, Plain)
class ClassicPizza(Pizza):
    def __init__(self):
        self.description = 'Classic Pizza'
        self.price = 20.0

class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = 'Margherita Pizza'
        self.price = 30.0

class TurkPizza(Pizza):
    def __init__(self):
        self.description = 'Turk Pizza'
        self.price = 40.0

class PlainPizza(Pizza):
    def __init__(self):
        self.description = 'Plain Pizza'
        self.price = 15.0

#Creating the PizzaDecorator superclass
class PizzaDecorator(Pizza):
    def __init__(self, sauces):
        self.sauces = sauces

    def getDescription(self):
        return self.sauces.getDescription() + ', ' + Pizza.getDescription(self)

    def getPrice(self):
        return self.sauces.getPrice() + Pizza.getPrice(self)

#Creating the subclasses of the PizzaDecorator superclass (Olives, Mushrooms, GoatCheese, Meat, Onion, Corn)
class Olives(PizzaDecorator):
    def __init__(self, sauces):
        self.sauces = sauces
        self.description = 'Olives'
        self.price = 7.5

class Mushrooms(PizzaDecorator):
    def __init__(self, sauces):
        self.sauces = sauces
        self.description = 'Mushrooms'
        self.price = 11.0

class GoatCheese(PizzaDecorator):
    def __init__(self, sauces):
        self.sauces = sauces
        self.description = 'Goat Cheese'
        self.price = 9.0

class Meat(PizzaDecorator):
    def __init__(self, sauces):
        self.sauces = sauces
        self.description = 'Meat'
        self.price = 17.5

class Onion(PizzaDecorator):
    def __init__(self, sauces):
        self.sauces = sauces
        self.description = 'Onion'
        self.price = 4.0

class Corn(PizzaDecorator):
    def __init__(self, sauces):
        self.sauces = sauces
        self.description = 'Corn'
        self.price = 6.0

#Creating the credit card function to get the user's credit card information
def creditCard():
    name = ''
    while name == '':
        name = input('Enter your name: ')
        if name == '':
            print('You must enter your name!')
    
    tc_Kimlik = ''
    while tc_Kimlik == '':
        tc_Kimlik = input('Enter your TC identification number: ')
        if len(tc_Kimlik) != 11:
            print('TC identification number must be 11 digits!')
            tc_Kimlik = ''

    cardNumber = ''
    while cardNumber == '':
        cardNumber = input('Enter your card number: ')
        if len(cardNumber) != 16:
            print('Card number must be 16 digits!')
            cardNumber = ''

    cardPassword = ''
    while cardPassword == '':
        cardPassword = input('Enter your card password: ')
        if len(cardPassword) != 4:
            print('Card password must be 4 digits!')
            cardPassword = ''

    return name, tc_Kimlik, cardNumber, cardPassword

#Creating the writeCreditCard function to write the user's credit card information to the Orders_Database.csv file
#if the file does not exist, it will be created and the header will be written
#else it will be appended
if not os.path.isfile('Orders_Database.csv'):
    with open('Orders_Database.csv', 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'TC Identification Number', 'Card Number', 'Card Password', 'Order Date'])
    f.close()

def writeCreditCard(name, tc_Kimlik, cardNumber, cardPassword):
    with open('Orders_Database.csv', 'a', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow([name, tc_Kimlik, cardNumber, cardPassword, datetime.datetime.now().strftime("%d-%m-%Y %H:%M")])
    f.close()

#Creating the main fuction that will do all the operations
def giveOrder():

    #Running the readMenu function to read the menu from the menu.txt file and print it on the screen
    readMenu()

    #Choosing the pizza
    pizza = ''
    while pizza == '':
        choosePizza = input('Choose your pizza: ')
        if choosePizza == '1':
            pizza = ClassicPizza()
        elif choosePizza == '2':
            pizza = MargheritaPizza()
        elif choosePizza == '3':
            pizza = TurkPizza()
        elif choosePizza == '4':
            pizza = PlainPizza()
        else:
            print('Please choose a pizza from the menu!')
    
    #Choosing the sauce
    sauce = ''
    while sauce == '':
        chooseSauce = input('Choose your sauce: ')
        if chooseSauce == '11':
            sauce = Olives(pizza)
        elif chooseSauce == '12':
            sauce = Mushrooms(pizza)
        elif chooseSauce == '13':
            sauce = GoatCheese(pizza)
        elif chooseSauce == '14':
            sauce = Meat(pizza)
        elif chooseSauce == '15':
            sauce = Onion(pizza)
        elif chooseSauce == '16':
            sauce = Corn(pizza)
        else:
            print('Please choose a sauce from the menu!')

    #Printing the order and the total price
    totalPrice = sauce.getPrice()
    pizzaDescription = sauce.getDescription()
    print('Your pizza is ready! It is a ' + pizzaDescription + ' and the total price is ' + str(totalPrice) + ' TL.')
    print('Please pay the total price to the cashier.')
    
    #Getting the credit card information and writing it to the Orders_Database.csv file
    name, tc_Kimlik, cardNumber, cardPassword = creditCard()
    writeCreditCard(name, tc_Kimlik, cardNumber, cardPassword)
    print('Payment is successful. Thank you for your order!')

#Running the main function
giveOrder()