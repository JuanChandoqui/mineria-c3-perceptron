from random import random
from Functions.operations import new_weights, operationSum
from Functions.read_csv import readCsv

def perceptron_main(list_test_x):
    error = 0
    y_calculada_aux = 0
    y_calculada = 0
    list_x, list_y = readCsv('./entrenamiento.csv')
   
    list_w = []
    count = 0

    #pesos iniciales
    for i in range(5):
        valor_ran = round(random(),4)
        list_w.append(valor_ran)
    
    #tasa de aprendizaje
    n = round(random(),4)

    while count < len(list_x):
        y_calculada_aux = operationSum(list_x[count], list_w)
       
        if y_calculada_aux >= 0:
             y_calculada = 1
        elif y_calculada_aux < 0:
            y_calculada = -1

        error = list_y[count] - y_calculada

        if error == 0:
            count = count + 1
        else: 
            lista_w_new = new_weights(list_x, list_w, n,error,count)
            list_w.clear()
            list_w = lista_w_new
            count = 0
            print(f'INITIAL WEIGHTS: {list_w}')
        
    resultado = test(list_test_x, list_w, n)
    
    return resultado
          


def test(list_test_x, list_w, n):
    resultado = ''
    print( f'FINAL WEIGHTS: {list_w}')
    print(f'N: {n}')

    respuesta = operationSum(list_test_x,list_w)

    if respuesta >= 0:
        resultado = 'Iris-setosa'
        return resultado
    else:
        resultado = 'Iris-versicolor'
        return resultado
