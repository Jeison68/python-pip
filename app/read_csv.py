import csv
# Leer Archivo CSV

# def read_csv(path):
#     with open(path, 'r') as csv_file:
#         reader = csv.reader(csv_file, delimiter=',')
#         print(header)
#         for row in reader:
#             print('++++*****++++' *5)
#             print(row)


# Convertir la lista que sale de leer el CSV a zip
def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        #print(header)
        data=[]
        for row in reader:
            iterable = zip(header, row)
            #print(list(iterable))
#Generamos un diccionario con Dictionary Comprehension
            country_dict = {key: value for key, value in iterable}
            #print(country_dict)
            data.append(country_dict)
    return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    #print(data[0]) # [0]Lee solo el primer elemento