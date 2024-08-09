import utils
import read_csv
import charts
import pandas as pd


def run():
    '''
    
    
    data = list(filter(lambda item: item['Continent'] == continent, data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    
    '''
    continent = input('Elija Continente: Asia, Europe, Africa, North America, South America =>')
    print('Continente elegido: ', continent)

    df = pd.read_csv('data.csv')
    df = df[df['Continent']== continent]
    countries=df['Country/Territory'].values
    percentages = df['World Population Percentage'].values

    charts.generate_pie_chart(countries, percentages)
    
    #data = read_csv.read_csv('data.csv')
    country = input('Type country => ')
    print('Pais seleccionado', country)
    name_country = country
    data = read_csv.read_csv('data.csv')
    result= utils.population_by_country(data, country)
    #print(result)
    #print(result)
    if len(result)>0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(name_country, labels, values)
        

if __name__ == '__main__': 
    run()