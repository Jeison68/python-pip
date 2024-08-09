import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4, 5]

# @app.get('/contact')
# def get_list():
#     return{'name' : 'Jeison.site'}

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <h1> Pagina en HTML </h1>
    <p> Este es el parrafo de contenido </p>

    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()