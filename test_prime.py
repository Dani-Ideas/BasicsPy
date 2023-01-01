def testPrime(numberByUser):
    #la variable count no sirve como indicador o vadera para detectar si es un numero primo
    count=0
    for i in range(1, numberByUser+1):#de debe de poner el +1 en numbrerByUser porque el siclo for no cuenta el ulimo numero
        if i ==1 or i==numberByUser:#este condisional es para saltar los numeror que no pueden dar posibles faslos positivos
            continue
        elif numberByUser % i == 0:#count solo incrementara cuando detecte que un numero no primo, recodemos que los numero primos solo se pueden dividir ente ellos mimos y el uno
            count+=1
    if count ==0:
        return True
    else:
        return False

def run():
    number = int(input('Escribe un numero para saber si es primo '))
    if testPrime(number):
        number= str(number)
        print('el numero ' + number + ' es un numero primo')
    else:
        number= str(number)
        print('el numero ' + number + ' no es un numero primo')

if __name__ == '__main__': 
    run()