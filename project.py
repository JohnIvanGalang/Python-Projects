import sys
import os
import time
from rich import print
from rich.table import Table


# For Food Menu
class Food_Menu:
    menu = {}
    count = 1

    def __init__(self, fname, fprice, fstock):
        self.fname = fname
        self.fprice = fprice
        self.fstock = fstock
        self.menu[self.count] = [self.fname, self.fprice, self.fstock, 0]
        Food_Menu.count += 1

    def display_food_menu(self):
        food_table = Table()
        food_table.add_column("Food no.", style="yellow", justify="center")
        food_table.add_column("Chicken Dish", style="cyan", justify="left")
        food_table.add_column("Price", style="green", justify="center")
        food_table.add_column("Stock", style="white", justify="center")

        for food, details in self.menu.items():
            food_table.add_row(str(food), details[0], str(details[1]), str(details[2]))
        print(food_table)

    def update_stock(self, food_no, quantity):
        if food_no in self.menu:
            self.menu[food_no][2] -= quantity
            self.menu[food_no][3] += quantity
    
    def add_product(self):
        cho = input("Add new product? [Y/N]  ")
        if cho.lower() == 'y':
            new_product_name = input("Enter the name of the new product: ")
            new_product_price = int(input("Enter the price of the new product: "))
            new_product_stock = int(input("Enter the stock of the new product: "))
            new_product = [new_product_name, new_product_price, new_product_stock, 0]
            self.menu[self.count] = new_product
            self.count += 1
            print("New product added successfully!")

        elif cho.lower() == 'n':
            pass



# For Customer
class Customer:
    customer = {}

    def __init__(self, num, name):
        self.num = num
        self.name = name
        self.customer_record()

    def customer_record(self):
        self.customer[self.num] = self.name

    def add(self):
        self.num = int(input("Customer no.: "))
        self.name = input("Customer name: ")
        self.customer_record()

        cust_file = open("C:\\Users\\IZEL VARGZ\\Desktop\\Projects\\customer.txt", "a")
        cust_rec = str(self.num) + " " + str(self.name) + "\n"
        cust_file.write(cust_rec)
        cust_file.close()


# For Purchasing/Ordering food(s)
class Order(Food_Menu):
    def __init__(self):
        self.display_food_menu()
        self.order()

    def display_food_menu(self):
        food_display = Table()
        food_display.add_column("Food no.", style="yellow", justify="center")
        food_display.add_column("Chicken Dish", style="cyan", justify="left")
        food_display.add_column("Price", style="green", justify="center")
        food_display.add_column("Stock", style="white", justify="center")

        for food, details in manok.menu.items():
            food_display.add_row(str(food), details[0], str(details[1]), str(details[2]))
        print(food_display)

    def order(self):
        while True:
            try:
                self.choice = int(input("Food number: "))
                self.quantity = int(input("How many orders: "))
                self.num = int(input("Customer number: "))
                food_item = super().menu[self.choice]

                if food_item[2] >= self.quantity:
                    a_detail = manok.menu[self.choice]
                    c_detail = tao.customer[self.num]

                    amount_due = self.quantity * a_detail[1]

                    print(c_detail + ", Please pay an amount of", amount_due, "php")

                    purchase_record = (
                        str(self.num)
                        + ". "
                        + str(c_detail)
                        + " "
                        + str(self.choice)
                        + " -> "
                        + str(a_detail[0])
                        + " "
                        + str(self.quantity)
                        + " @Php "
                        + str(amount_due)
                    )

                    self.record_purchase(purchase_record)

                    super().update_stock(self.choice, self.quantity)

                else:
                    print("Insufficient stock")

            except:
                print("Invalid")
                continue

            time.sleep(3)
            menu()

    def record_purchase(self, purchase_record):
        file_record = open("C:\\Users\\IZEL VARGZ\\Desktop\\Projects\\record.txt", "a")
        file_record.write(purchase_record + "\n")
        file_record.close()

    def update_stock(self, food_no, quantity):
        super().update_stock(food_no, quantity)
        self.menu[food_no][2] -= quantity


# For Recording
class Record:
    def __init__(self):
        self.record_file()

    def record_file(self):
        file_record = open("C:\\Users\\IZEL VARGZ\\Desktop\\Projects\\record.txt", "r")
        content = file_record.read()

        if content == "":
            print("No record found")
            time.sleep(0.8)
        else:
            print(content)
            file_record.close()
            while True:
                rpt = input("Press [ B ] to go back  ")
                if rpt.lower() == "b":
                    menu()
                else:
                    print("Invalid Input")
                    continue


def menu():
    os.system("cls")
    print(">-----John Ivan and Nathan's Titilaok-----<")
    print("\t    Kaon-kaona tam manok")
    print("\n   System Menu")
    print("\t[ 1 ] Order ->")
    print("\t[ 2 ] Food Menu ->")
    print("\t[ 3 ] Customer ->")
    print("\t[ 4 ] Customer Record ->")
    print("\t[ 5 ] Add Customer ->")
    print("\t[ 6 ] Sales Report ->")
    print("\t[ 7 ] Exit ->")

    user_input = input("\nInput here>> ")
    try:
        user_input = int(user_input)
        if user_input == 1:
            choice = Order()
        elif user_input == 2:
            manok.display_food_menu()
            print("")
            manok.add_product()
            while True:
                go_back = input("Press [ B ] to go back  ")
                if go_back.lower() == "b":
                    menu()
                else:
                    print("Invalid Input")
                    continue
        elif user_input == 3:
            table = Table()
            table.add_column("Number", style="cyan", justify="center")
            table.add_column("Customer Name", style="green", justify="left")

            for num, name in Customer.customer.items():
                table.add_row(str(num), name)
            print(table)

            while True:
                go_back = input("Press [ B ] to go back  ")
                if go_back.lower() == "b":
                    menu()
                else:
                    print("Invalid Input")
                    continue
        elif user_input == 4:
            basta_record = Record()
        elif user_input == 5:
            new_cust = tao.add()
        elif user_input == 6:
            sales_report()
        elif user_input == 7:
            print("Thank you, Come Again!")
            sys.exit()
        else:
            print("Invalid Number")
            time.sleep(1)
            menu()

    except ValueError:
        print("Invalid, Please enter a number between [1-5]")
        time.sleep(1)
        menu()


def sales_report():
    total_orders = sum([food[3] for food in manok.menu.values()])
    total_stock = sum([food[2] for food in manok.menu.values()])
    total_income = sum([food[1] * food[3] for food in manok.menu.values()])

    sales_table = Table()
    sales_table.add_column("Food", style="yellow", justify="center")
    sales_table.add_column("Orders", style="white", justify="center")
    sales_table.add_column("Stock", style="magenta", justify="center")

    for food, details in manok.menu.items():
        sales_table.add_row(details[0], str(details[3]), str(details[2]))

    print("Sales Report")
    print(sales_table)
    print(f"Total Orders: {total_orders}")
    print(f"Total Stock: {total_stock}")
    print(f"Total Income: Php {total_income}")
    

    while True:
        rpt = input("Press [ B ] to go back: ")
        if rpt.lower() == "b":
            menu()
        else:
            print("Invalid Input")
            continue


# List of items
manok = Food_Menu("Chicken Curry", 150, 10)
manok = Food_Menu("Barbecue Chicken", 100, 10)
manok = Food_Menu("Garlic Chicken", 185, 10)
manok = Food_Menu("Lemon Chicken", 180, 10)
manok = Food_Menu("Buttered Chicken", 150, 10)
manok = Food_Menu("Fried Chicken", 120, 10)
manok = Food_Menu("Garlic Chicken", 150, 10)
manok = Food_Menu("Chicken Parmesan", 200, 10)
manok = Food_Menu("Chicken Enchiladas", 130, 10)
manok = Food_Menu("Chicken Pesto", 150, 10)
manok = Food_Menu("Chicken Masala", 200, 10)
manok = Food_Menu("Chicken Salad", 180, 10)
manok = Food_Menu("Chicken Biryani", 150, 10)

# List of customers
tao = Customer(1, "John Ivan")
tao = Customer(2, "Nathan Paul")
tao = Customer(3, "Ivanacci Depaz")
tao = Customer(4, "Dio Brando")

# Main function of the program
menu()


