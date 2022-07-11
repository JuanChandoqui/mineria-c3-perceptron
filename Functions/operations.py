def operationSum(x_aux,list_w):  
    y_1 = 0
    
    for j in range(0,len(list_w)):
        y_aux = list_w[j] * x_aux[j] 
        y_1 = y_1 + y_aux
    
    return y_1


def new_weights(list_x, list_w, n,error,count):
    lista_new_w = []

    for i in range(0,5):  
        multiplication = n * error * list_x[count][i]
        sum_multiplication  = list_w[i]  + multiplication
        w_aux = sum_multiplication
        lista_new_w.append(w_aux)
        w_aux = 0

    return lista_new_w