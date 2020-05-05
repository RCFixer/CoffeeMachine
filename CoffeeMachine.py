class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def __repr__(self):
        return "Water: {}, Milk: {}, Coffee Beans: {}," \
               " Cups: {}, Money: {}".format(self.water,
                                             self.milk,
                                             self.coffee_beans,
                                             self.cups,
                                             self.money)

    def __str__(self):
        return '\nThe coffee machine has:\n' \
               '{water} of water\n' \
               '{milk} of milk\n' \
               '{coffee} of coffee beans\n' \
               '{cups} of disposable cups\n' \
               '${money} of money\n'.format(water=self.water,
                                            milk=self.milk,
                                            coffee=self.coffee_beans,
                                            money=self.money,
                                            cups=self.cups)

    def fill(self, water, milk, coffee_beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.cups += cups

    def check_res(self, use_water, use_milk, use_coffee_beans):
        if self.water < use_water:
            return False, 'water'
        elif self.milk < use_milk:
            return False, 'milk'
        elif self.coffee_beans < use_coffee_beans:
            return False, 'coffee beans'
        elif self.cups == 0:
            return False, 'cups'
        return True, 'I have enough resources, making you a coffee!'

    def make_coffee(self, water, milk, coffee_beans, money):
        self.water -= water
        self.milk -= milk
        self.coffee_beans -= coffee_beans
        self.money += money
        self.cups -= 1

    def buy(self, order):
        if order == '1':
            is_enough, message = self.check_res(250, 0, 16)
            if is_enough:
                self.make_coffee(250, 0, 16, 4)
                print(message)
                return
            print('Sorry, not enough {}!'.format(message))
            return
        elif order == '2':
            is_enough, message = self.check_res(350, 75, 20)
            if is_enough:
                self.make_coffee(350, 75, 20, 7)
                print(message)
                return
            print('Sorry, not enough {}!'.format(message))
            return
        elif order == '3':
            is_enough, message = self.check_res(200, 100, 12)
            if is_enough:
                self.make_coffee(200, 100, 12, 6)
                print(message)
                return
            print('Sorry, not enough {}!'.format(message))
            return
        elif order == 'back':
            return


def main():
    coffee_machine = CoffeeMachine()
    while True:
        action = input('Write action (buy, fill, take, remaining, exit):').strip()
        if action == 'buy':
            order = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            coffee_machine.buy(order)
        elif action == 'fill':
            water = int(input('Write how many ml of water do you want to add:'))
            milk = int(input('Write how many ml of milk do you want to add:'))
            coffee_beans = int(input('Write how many grams of coffee beans do you want to add:'))
            cups = int(input('Write how many disposable cups of coffee do you want to add:'))
            coffee_machine.fill(water, milk, coffee_beans, cups)
        elif action == 'take':
            print('I gave you ${}\n'.format(coffee_machine.money))
            coffee_machine.money = 0
        elif action == 'remaining':
            print(coffee_machine)
        elif action == 'exit':
            break


main()
