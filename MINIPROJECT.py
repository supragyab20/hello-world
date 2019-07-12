print("        MINI PROJECT:ONLINE RETAIL SHOP       ")
print("______________________________________________")

print("          WELCOME TO ADMIN MODULE")
print('\n')
stock ={'mouse':'15',
    'keyboard':'25',
    'monitor':'250',
    'cpu':'550',
    'ups':'300',
    'laptop':'600',
    'mobile hone':'450',
    't.v':'350',
    'pendrive':'30'}
print(type(stock))


def func():
    return stock

print('               MainMenu')
print('\n')
n=True
while n:
    print('1.Add product in Stock')
    print('2.Update product in stock')
    print('3.Remove product in stock')
    print('4.View all product in stock')
    print('5.Logout')
    print('\n')
    n =input('KINDLY SELECT AN OPTION FROM THE TOP ')

    if n=='1':
        print("PRODUCTS IN STOCK=", stock.keys())
        a=(input("ENTER THE PRODUCT YOU WANT TO ADD"))
        b=int(input("ENTER THE PRICE OF THE PRODUCT"))
        stock[a]=b
    elif n=='2':
        print("PRODUCTS IN STOCK=", stock.keys())
        a = (input("ENTER THE PRODUCT YOU WANT TO UPDATE "))
        b=int(input('ENTER THE NEW PRICE'))
        stock[a] = b
    elif n=='3':
        print("PRODUCTS IN STOCK=", stock.keys())
        a = (input("ENTER THE PRODUCT YOU WANT TO REMOVE "))
        del stock[a]
    elif n=='4':
        print("PRODUCTS IN STOCK=", stock.keys())
    elif n=='5':
        print('LOGGING OUT')
        break



