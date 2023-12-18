import random
import time
import sys
import os

def generating_load():
    os.system("cls")
    n = 101
    for i in range(n):
        time.sleep(0.03)
        sys.stdout.write('\r' + 'Generating Random Password ' + str(i))
        sys.stdout.flush()

    os.system("cls")
    sys.stdout.write('\r' + "Finished.")


while True:

    try:
        lower_case = "qwertyuiopasdfghjklzxcvbnm"
        upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
        numbers = "1234567890"
        symbols = "!@#%*:;/."

        all = lower_case + upper_case + numbers + symbols
        print("")
        limit = int(input("Enter Password Limit[8-71]: "))

        if limit <= 71 and limit >= 8:
            password = "".join(random.sample(all,limit))
            print("")
            generating_load()
            print(f"\nRandom Password is: {password}")
            print("")

            try: 
                choice = input("Generate Again?[Y/N]: ")
                if choice == 'Y' or choice == 'y':
                    os.system("cls")
                    continue
                    
                elif choice == 'N' or choice == 'n':
                    break

            except:
                print("Invalid Input!")
                continue

        else:
            print("Must be [8-71]\n")
            continue
    except:
        print("Invalid Input!")
        continue