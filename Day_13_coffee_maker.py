class coffee:
    def __init__(self):
        choice=input("Enter your choice")
        if choice in ("espresso","latte","cappuccino"):
            print("Your order is being processed")
        water=1000
        print("Amount of water before process", water)
        water=water-200
        print("Amount of water after process",water)
        if water<200:
            print("Not enough water")
    def money(self):
        price=print("Coffee costs $2.5")
        pri=float(input("please enter the amount you have paid"))
        if pri==2.5:
            print("Transaction successful")
        elif pri<2.5:
            print("Not enough amount")
        elif pri>2.5:
            ch=pri-2.5
            print("Don't forget to take the change: ",ch)
        else:
            print("Transaction not valid")
    def report(self):
        print("Amount of ingerdients needed: ")
        finla_report=print('''Water: 100ml 
Milk: 50ml
Coffee: 76g''')


newcoffee=coffee()
newcoffee.report()
newcoffee.money()




