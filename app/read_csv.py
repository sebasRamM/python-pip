import csv

def read_csv(path):
    #abrir archivo csv
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        #el nombre de las columnas esta en la primera fila
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row) # une los valores de las listas en tuplas
            country_dict = {key: value for key, value in iterable} #los guarda como un iterable de dictionary
            data.append(country_dict)
        return data

if __name__ == '__main__':
   data = read_csv('./app/data.csv')
   print(data[0])