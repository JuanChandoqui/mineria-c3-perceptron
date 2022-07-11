def operationSum(x_aux,list_w):  
    y_1 = 0
    
    for j in range(0,len(list_w)):
        y_aux = list_w[j] * x_aux[j] 
        y_1 = y_1 + y_aux
    
    return y_1


def new_weights(list_x, list_w, factor_aprendizaje,error,contador):
    lista_new_w = []

    for i in range(0,5):  
        formula_1 = factor_aprendizaje * error * list_x[contador][i]
        formula_3  = list_w[i]  + formula_1
        w_aux = formula_3
        lista_new_w.append(w_aux)
        w_aux = 0

    return lista_new_w