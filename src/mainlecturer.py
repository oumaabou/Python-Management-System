import sys,time
import lecturer


def print_slow(word):
    for l in word:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1)

def access():
    print_slow("|--------------♡---------------|\n")
    while True :
        ask = input("\tWould you like to? \n\tMenu: \n\t1.Login \n\t2.Register \n\nWhat is your selected choice?")
        ask.strip()
        if ask.isdigit():
            r = int(ask)
            if  1 <= r <= 2 :
                if r == 1 :
                     lecturer.login('test1.txt')
                     break
                    #access to the lecturer pages of login
                elif r == 2 :
                    lecturer.register_lecturer('test1.txt')
                    break
                    #acces to the register lecturer from the lecturer py pages
            else :
                print("\n\033[1mError please choose from the menu given!\033[0m")
        else :
            print("\n\033[1mError please enter a valid number!\033[0m")


