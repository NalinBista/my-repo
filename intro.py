# Button calling --> Dial
from argparse import RawDescriptionHelpFormatter


def dial(phone_num):
   print("f{phone_num} \ncalling ...")

   def openDialer(user_provided_number):
    if user_provided_num > 10:
        print("NUmber Invalid")
    elif user_provided_number < 10:
        print("Call ended")
    elif user_provided_number == 10:
         dial(user_provided_number)      
    else:
        return

    recipent_num = (input("please provide nunmber"))    
    openDialer (int(len (recipent_num)))      