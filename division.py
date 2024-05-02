def division (num1,num2):
    if num2 == 0:
        result = None
        print ("no se puede dividir por cero")
    else:

        result=num1/num2
        print(f"{num1}/{num2} es igual a {result}")
    return result