print('welcome to bank of india')
restart=('y')
chances=3
balance=100.00
while chances>= 0:
    print('u only have 3 chance')
    pin= int(input('please enter you 4digit pin:'))
    
    if pin == (5050):
        print("you entered your pin correctly\n")
        while restart not in('n','NO','no','N'):
            print('please press1 for your bal\n')
            print('please press2 to make a withdrawl...\n')
            print('please press3 tp pay in...\n')
            print('please press4 to return card...\n')
            option=int(input('what would you like to choose?'))
            if option==1:
                print("your balance is A $100; balance,\n")
                restart = input("would you like to go back?")
                if restart in ('n','NO','no','N'):
                    print('Thankyou')
                    break
            elif option == 2:
                 option2=('y')
                 withdrawl=float(input('How much would you like to withdraw?\n A $10, A $20, A $40, A $60, A $80, A $100'))
                 if withdrawl in [10,20,40,60,80,100]:
                        balance=balance-withdrawl
                        print('\n your balance is now A', balance)
                        restart = input ('would you like to go back?')
                        if restart in ('n','no','NO','N'):
                            print('Thankyou')
                            break
                 elif withdrawl!=[10,20,40,60,80,100]:
                            print('Invaid amount,please re=try \n')
                            restart=('y')
                 elif withdrawl == 1:
                            withdrawl = float(input('please Enter desired amount:'))
            elif option == 3:
                    pay_in = float (input('How much would you like to pay in?'))
                    balance = balance + pay_in
                    print('\n your balnce is  now A $',balance)
                    restart = input('would you like to go back?')
                    if restart in ('n', 'NO','no','N'):
                        print('Thankyou')
                        break
            elif option == 4:
                    print ('please wait whil your card is returned...\n')
                    print('Thankyou for your services')
                    break
            
            else:
                    print('please Enter a correct number....\n')
                    
                    restart =('y')
    elif pin != ('5050'):
        print('incorrect password')
        chances = chances-1
        if chances == 0:
            print('\n no more tries')
            break
