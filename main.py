from add import add
from subtract import subttract
from multiply import multiply
from division import division
from potencia import potencia
from modulo import modulo

def game():
    score = 0
    while True:
        print('======== Menu ========'
        '\n1. Add'
        '\n2. substract'
        '\n3. multiply'
        '\n4. division'
        '\n5. potencia'
        '\n6. modulo'
        '\n0. Exit')
        option = int(input('\nChoice an option: '))
        if option == 0:
            break
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter you answer: '))
        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        
        elif option == 2:
            result=subttract(num_1,num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 3:
            result=multiply(num_1,num_2)
            if result == answer:
                score += 2
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 4:
            result=division(num_1,num_2)
            if result == answer:
                score += 2
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 5:
            result=potencia(num_1,num_2)
            if result == answer:
                score += 4
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 6:
            result=modulo(num_1,num_2)
            if result == answer:
                score += 4
                print('Correct!!')
            else:
                print('Incorrect')
        break
    
    print(f'======== Game Over ========'
    f'\nYou score is {score}'
    '\nKeep going!')


game()