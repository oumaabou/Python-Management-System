import sys , time
import mainlecturer
import trainer
import Student
import administrator
#import administrator main

def print_slow(word):
    for l in word:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    print_slow("|--------------♡---------------|\n")
    while True :
        ask = input("\tMenu : \n\t1.Administrator \n\t2.Trainer \n\t3.Lecturer \n\t4.Student \n\nWhat is your selected choice?")
        ask.strip()
        if ask.isdigit():
            r = int(ask)
            if 1 <= r <= 4 :
                if r == 1 :
                    administrator.main()
                elif r == 2 :
                    trainer.main()
                    break
                elif r == 3 :
                    mainlecturer.access()
                    break
                elif r == 4 :
                    Student.StudentDisplay().login()
                    break
            else :
                print("\n\033[1mError please choose from the menu given!\033[0m")
        else :
            print("\n\033[1mError please enter a valid number!\033[0m")

print(main())