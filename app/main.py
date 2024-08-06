import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    continent = input('Elija Continente: Asia, Europe, Africa, North America, South America =>')
    print('Continente elegido: ', continent)
    data = list(filter(lambda item: item['Continent'] == continent, data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)

    country = input('Type country => ')
    print('Pais seleccionado', country)
    print("step1")
    #name_country = country
    #print(name_country*2)
    result= utils.population_by_country(data, country)
    print(result)
    #print(result)
    if len(result)>0:
        print("step3")
        country = result[0]
        print("step4")
        labels, values = utils.get_population(country)
        print("step5")
        charts.generate_bar_chart(labels, values)
        print("step6")

if __name__ == '__main__': 
    run()