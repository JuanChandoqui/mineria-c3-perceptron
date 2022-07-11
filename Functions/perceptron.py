from random import random
from Functions.operations import new_weights, operationSum
from Functions.read_csv import readCsv

def perceptron_main(list_test_x):
    error = 0
    y_calculada_aux = 0
    y_calculada = 0
    list_x, list_y = readCsv('./entrenamiento.csv')
   
    list_w = []
    contador = 0

    for i in range(5):
        valor_ran = round(random(),4)
        list_w.append(valor_ran)

    factor_aprendizaje = round(random(),4)

    while contador < len(list_x):
        y_calculada_aux = operationSum(list_x[contador], list_w)
       
        if y_calculada_aux >= 0:
             y_calculada = 1
        elif y_calculada_aux < 0:
            y_calculada = -1

        error = list_y[contador] - y_calculada

        if error == 0:
            contador = contador + 1
        else: 
            lista_w_new = new_weights(list_x, list_w, factor_aprendizaje,error,contador)
            list_w.clear()
            list_w = lista_w_new
            contador = 0
            print(f'INITIAL WEIGHTS: {list_w}')
        
    resultado = test(list_test_x, list_w, factor_aprendizaje)
    
    return resultado
          


def test(list_test_x, list_w, factor_aprendizaje):
    resultado = ''
    print( f'FINAL WEIGHTS: {list_w}')
    print(f'N: {factor_aprendizaje}')

    respuesta = operationSum(list_test_x,list_w)

    if respuesta >= 0:
        resultado = 'Iris-setosa'
        return resultado
    else:
        resultado = 'Iris-versicolor'
        return resultado
