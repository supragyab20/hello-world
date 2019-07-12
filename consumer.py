import MINIPROJECT
stock1 =MINIPROJECT.func()
basket={}
print('                   WELCOME TO CONSUMER MODULE')
print('                   __________________________')
print('                             MainMenu')
print('\n')
n=True
while(n):
        print('                  1.View all product in stock')
        print('                  2.Add to Cart')
        print('                  3.View all products of basket')
        print('                  4.Search prdoduct in stock')
        print('                  5.Remove product from Basket')
        print('                  6.Print Invoice')
        print('\n')
        n =input('KINDLY SELECT AN OPTION FROM THE TOP ')

        if n=='1':
            print("PRODUCTS IN STOCK=", stock1.keys())
            print('\n')
        elif n=='2':
            print("PRODUCTS IN STOCK=", stock1.keys())
            a = (input("ENTER THE PRODUCT YOU WANT TO ADD TO CART "))
            b = int(input('ENTER THE QUANTITY'))
            basket[a]=b
            print('Product successfully added to cart')
            print('\n')
        elif n=='3':
            print("PRODUCTS IN CART=", basket.keys())
            print('\n')
        elif n=='4':
            a = (input("ENTER THE PRODUCT YOU WANT TO SEARCH IN THE STOCK "))
            for k in stock1.keys():
                b= a in stock1
                if b==True:
                    print("ITEM IS IN STOCK")
                    break
                else:
                    print('ITEM IS NOT IN STOCK')
                    break
            print('\n')
        elif n=='5':
            print("PRODUCTS IN CART =", basket.keys())
            a = (input("ENTER THE PRODUCT YOU WANT TO REMOVE "))
            del basket[a]
            print('ITEM REMOVED')
            print('\n')
        elif n=='6':
            c=0
            import datetime
            x = datetime.datetime.now()
            print('BILLING INVOICE')
            print('_ _ _ _ _ _ _ _ _')
            print('DATE: ',x.strftime("%x"))
            print('Prodct Name          ''Unit price            ''Quantity          ''Total Price           ')
            for key, value in basket.items():
                a=stock1.get(key)
                b=value*int(a)
                print(key,'         ',a,'          ',value,'           ',b)
                c=c+b
            print('                                                              GRAND TOTAL:',c)
            print('\n')
            print('THANKYOU')
            break
