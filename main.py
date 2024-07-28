from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

is_on=True

while is_on:
  print(menu.get_items())
  choice=input("choose your favourite coffee amoung above menu: ")
  if choice=="report" :
     coffee_maker.report()
     money_machine.report()
  elif choice=="off":
     is_on=False  
  else:
     drink=menu.find_drink(choice)
     cost=drink.cost
     if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(cost):
           coffee_maker.make_coffee(drink)
     else:
        is_on=False   
  
