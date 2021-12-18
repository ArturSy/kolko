

planszaDoGry = {'7':' ', '8':' ', '9':' ',
                '4':' ', '5':' ', '6':' ',
                '1':' ', '2':' ', '3':' '}

klawiszeGry=[]

for key in planszaDoGry:
    klawiszeGry.append(key)


def drukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")



def gra():

    gracz = 'X'
    licznik = 0

    for i in range(10):

        drukujPlansze(planszaDoGry)

        move = input(f"To jest ruch, {gracz}. Wybierz gdzie chcesz postawić znak!")

        if planszaDoGry[move] == " ":
            planszaDoGry[move] = gracz
            licznik = +1 
        else:
            print("\n Wybrane pole jest zajęte. \nWybierz inne!")
            continue

        if licznik >= 5:
            if planszaDoGry['7'] == planszaDoGry['8'] == planszaDoGry['9']!= " ":
                drukujPlansze(planszaDoGry)
                print('\nKONIEC GRY')
                print(f'wygrał gracz: {gracz}')
                break
            elif planszaDoGry['4'] == planszaDoGry['5'] == planszaDoGry['6']!= " ":
                drukujPlansze(planszaDoGry)
                print('\nKONIEC GRY')
                print(f'wygrał gracz: {gracz}')
                break
            elif planszaDoGry['1'] == planszaDoGry['2'] == planszaDoGry['3']!= " ":
                drukujPlansze(planszaDoGry)
                print('\nKONIEC GRY')
                print(f'wygrał gracz: {gracz}')
                break
            elif planszaDoGry['7'] == planszaDoGry['4'] == planszaDoGry['1']!= " ":
                drukujPlansze(planszaDoGry)
                print('\nKONIEC GRY')
                print(f'wygrał gracz: {gracz}')
                break
            elif planszaDoGry['8'] == planszaDoGry['5'] == planszaDoGry['2']!= " ":
                drukujPlansze(planszaDoGry)
                print('\nKONIEC GRY')
                print(f'wygrał gracz: {gracz}')
                break
            elif planszaDoGry['9'] == planszaDoGry['6'] == planszaDoGry['3']!= " ":
                drukujPlansze(planszaDoGry)
                print('\nKONIEC GRY')
                print(f'wygrał gracz: {gracz}')
                break
            elif planszaDoGry['7'] == planszaDoGry['5'] == planszaDoGry['3']!= " ":
                drukujPlansze(planszaDoGry)
                print('\nKONIEC GRY')
                print(f'wygrał gracz: {gracz}')
                break
            elif planszaDoGry['9'] == planszaDoGry['5'] == planszaDoGry['1']!= " ":
                drukujPlansze(planszaDoGry)
                print('\nKONIEC GRY')
                print(f'wygrał gracz: {gracz}')
                break
# do sprawdzenia akapity
            if licznik == 9:
                print('\nKoniec gry!!!!\nJest Remis!!!')

        if gracz == 'X':
            gracz = 'O'
        else:
            gracz = 'X'

    restart = input('\nCzy chcesz zargrać jeszcze raz?? (t/n)\n')
    if  restart == 't' or restart =='T':
        for key in klawiszeGry:
            planszaDoGry[key] = ' '

        gra()


#superfunkcja

if __name__ == '__main__':
    gra()
            
