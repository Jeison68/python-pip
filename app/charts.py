import matplotlib.pyplot as plt

#Funcion para generar Graficos fijos
# def generate_bar_chart():
#     labels = ['a', 'b', 'c']
#     values = [100, 200, 300]

#     fig, ax = plt.subplots()
#     ax.bar(labels, values)
#     plt.show()

# Ahora vamos a recibir valores dinamicos 
def generate_bar_chart(labels, values): #add labels y valus like parametros 
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('bar.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c'] #movemos labels y values dentro del if
    values = [100, 200, 50]
    generate_bar_chart(labels, values) #add labels and values like parametros
    generate_pie_chart(labels, values)