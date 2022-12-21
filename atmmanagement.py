username="chandu"
password="chandu@2003"
amount=10000
print("ENTER USERNAME ")
user_name=input()
print("ENTER PASSWORD")
pass_word=input("")
if user_name==username and password==pass_word:
    print("WELCOME",user_name)
    print('''
    1.DEPOSIT
    2.WITHDRAW
    3.MINI STATEMENT
    4.EXIT
    ''')
    print("ENTER YOUR CHOICE ")
    choice=int(input())
    if choice==1:
        print("ENTER THE AMOUNT TO BE DEPOSITED ")
        deposit_amount=int(input())
        amount+=deposit_amount
        print("TOTAL BALANCE",amount)
    elif choice==2:
        print("ENTER THE AMOUNT TO BE WITHDRAW ")
        withdraw=int(input())
        amount -= withdraw
        print("TOTAL BALANCE", amount)
    elif choice==3:
        print("MINI STATEMENT")
        print("<<<<===============>>>>")
        print("USER NAME",user_name)
        print("TOTAL BALANCE",amount)
        print("<<<<===============>>>>")
        print("(: (: (:THANKS FOR VISITING (: (: (: ")
    elif choice==4:
        exit()
    else:
        print(":( :( :( PLEASE SELECT THE VALID OPTION :( :( :(")
else:
    print('''
  ---------------
    **********
    INVALID USER
    **********
 ---------------    ''')




