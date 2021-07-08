from fastapi import FastAPI
from starlette.requests import Request
from productos import items
app = FastAPI(tittle='CiberC demo APIs', description= 'un demo pequeno de APIs', version='1.0')
@app.get('/')
async def index():
    return 'hola a todos los ingenieros de Preventa'

@app.get('/about/')
async def about():
    return 'Estamos en el about del servicio web'

#Listar todos los productos
@app.get('/productos/')
async def productos():
    return {'mensaje': 'Lista de productos', 'Productos': items}

#Listar un solo producto 
@app.get('/producto/{product_name}')
async def producto(product_name):
    products_found = [ product for product in items if product['name'] == product_name]
    if (len(products_found) > 0):
        return {'mensaje': 'Item encontado', 'Productos': products_found[0]}
    else:
        return {'mensaje': 'Item no encontrado en la BD'} \

####POST
@app.post('/producto/')
async def addproduct(requests:Request):
    print (await requests.json())