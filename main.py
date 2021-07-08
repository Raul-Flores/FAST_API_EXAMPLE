__author__ = "Raul Flores"
__license__ = "GNUv3"
__version__ = "1.0"
__maintainer__ = "Raul Eduardo Flores Najera"
__email__ = "raul.flores@ciberc.com"
__status__ = "valid production"
import uvicorn
from fastapi import FastAPI, Request
from productos import items
app = FastAPI(tittle='CiberC demo APIs', description= 'un demo pequeno de APIs', version='1.0')
@app.get('/')
async def index():
    return 'hola a todos los ingenieros de Preventa'

@app.get('/about/')
async def about():
    return 'Estamos en el about de la aplicacion saludos'

#Listar todos los productos
@app.get('/productos/')
async def listar_productos():
    return {'mensaje': 'Lista de productos', 'Productos': items}

#Listar un solo producto 
@app.get('/producto/{product_name}')
async def producto(product_name):
    products_found = [ product for product in items if product['name'] == product_name]
    if (len(products_found) > 0):
        return {'mensaje': 'Item encontado', 'Productos': products_found[0]}
    else:
        return {'mensaje': 'Item no encontrado en la BD'} \

####POST Agregar nuevo producto
@app.post('/producto/')
async def agregar_producto(requests:Request):
    data = await requests.json()
    new_item = {
        "name": data['name'],
        "price": data['price'],
        "quantity": data['quantity']
    }
    items.append(new_item)
    return {"Message": "Producto agregado satisfactoriamente", "productos": items}

#Editar un producto
@app.put('/productos/{product_name}')
async def editar_producto(product_name, requests:Request):
    data = await requests.json()
    products_found = [ product for product in items if product['name'] == product_name]
    if (len(products_found) > 0):
        products_found[0]['name'] = data['name']
        products_found[0]['price'] = data['price']
        products_found[0]['quantity'] = data['quantity']
        return {"Message":"Producto editado", "Nuevos Datos": products_found[0]}
    else:
        return {"Mesage": "Producto no encontrado"}


#Editar un elemento de un producto
@app.patch('/productos/{product_name}')
async def editar_elemento(product_name, requests:Request):
    data = await requests.json()
    print (list(data)[0])
    products_found = [ product for product in items if product['name'] == product_name]
    if (len(products_found) > 0):
        if list(data)[0] == 'name':
            products_found[0]['name'] = data['name']
        elif list(data)[0] == 'price':
            products_found[0]['price'] = data['price']
        elif  list(data)[0] == 'quantity':
            products_found[0]['quantity'] = data['quantity']
        return {"Message":"Producto modificado", "modificado": products_found[0]}
    else:
        return {"Mesage": "Producto no encontrado"}


#Eliminar un producto
@app.delete('/productos/{product_name}')
async def eliminar_producto(product_name, requests:Request):
    products_found = [ product for product in items if product['name'] == product_name]
    if (len(products_found) > 0):
        items.remove(products_found[0])
        return {"Mesage": "Producto eliminado", "Productos": items}
    else:
        return {"Message": "Producto no encontrado"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True, debug=True)