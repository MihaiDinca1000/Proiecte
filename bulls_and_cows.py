from random import randint
from time import time
import re

'''
    JOCUL BULLS AND COWS !
        reguli:
             -Calculatorul va genera un numar de 4 cifre
             -Tu trebuie sa gasesti numarul si vei fi ajutat de urmatoarele 2 indicii
                *daca ai inimerit un numar dar nu si pozitia este bulls
                *daca ai inimerit un numar dar si pozitia este vaca
    
    posibila greseala!!!            
                
    As far as I could see, none of the solutions are 100% correct.
Reason: if the correct guess is 1211 and the user inputs 2222, he will get 1 cow 3 bulls, but that is obviously not right.
Did someone make a code with that in mind? I couldn't figure a way to make it right


linia 50 pentru verificare !!!!
'''




def guess(guess_number):

    cows = 0
    bulls = 0

    for i in range(0,4):
        if guess_number[i] == input_number[i]:
            cows +=1

        if guess_number[i] in input_number:
            bulls +=1

    print('in your number you have {} cows and  {} bulls\n'.format(cows, bulls))

    return cows,bulls

if __name__=="__main__":
    print("JOCUL BULLS AND COWS ! \n reguli:\n"
          "   -Calculatorul va genera un numar de 4 cifre\n"
          "   -Tu trebuie sa gasesti numarul si vei fi ajutat de urmatoarele 2 indicii:\n"
          "      *daca ai inimerit un numar dar nu si pozitia este bulls\n"
          "      *daca ai inimerit un numar dar si pozitia este vaca")

    guess_number = str(randint(1000, 10000))
    # print(guess_number)
    tries = 0
    status = True
    t0 = time()

    while(status):
        
        input_number = input('ghiceste numarul: ')

        if re.search('[a-zA-Z]', input_number):
            print('your are stupid, this is not a number !!! Malparido ...')
            continue #aici poti sa-l faci tu sa continue
        elif len(input_number) != 4:
            print("The number has not the required length, please read the rules!")
            break
        
        if input_number == '0000':
            print("You stop the game here")
            break

        cows, bulls = guess(guess_number)
        tries +=1

        
        
        t1 = time()
        t10 = t1-t0
        if  cows == 4:
            print('bravo ai castigat')
            print('ai avut {} incercari'.format(tries))
            status = False
            print('Ai rezolvat problema in: {} secunde, numarul era: {}'.format(t10,guess_number))            









