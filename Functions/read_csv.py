import csv

def readCsv(path: str):
    list_x = [] # inputs
    list_y = [] # ouputs
    lista_str_aux = []
    list_float = []

    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for dato in row:
                lista_str_aux = dato.split(',')
                list_float.append(1)
                for i in lista_str_aux:
                    list_float.append(float(i))
                    
            
            list_x.append(list_float[0:5])
            list_y.append(list_float[5])
            list_float = []
               
    return list_x, list_y
