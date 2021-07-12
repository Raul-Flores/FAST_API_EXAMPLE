__author__ = "Raul Flores"
__license__ = "GNUv3"
__version__ = "1.0"
__maintainer__ = "Raul Eduardo Flores Najera"
__email__ = "raul.flores@ciberc.com"
__status__ = "valid production"
from pydantic.networks import HttpUrl
from database import item
import uvicorn
from fastapi import FastAPI, Request
from schemas import ItemRequestModel, ItemResponseModel
from database import database as connection

app = FastAPI(tittle='CiberC demo APIs', description= 'un demo pequeno de APIs', version='1.0')
## Zona para Eventos en FAST API, crear/abrir/cerrar BD y crear tablas
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables([item])
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get('/productos/')
async def get_all_items():
    all_info = []
    query = item.select()
    for data in query:
        all_info.append({"name":data.name, "price":data.price, "quantity": data.quantity})
    return all_info
##POST Agregar nuevo producto
@app.post('/producto')
async def add_item(data: ItemRequestModel):
    data_create = item.create(
        name= data.name,
        price=data.price,
        quantity=data.quantity)    
    data_create.save()
    return "Item creado"
##Obtener solo un item
@app.get('/producto/{item_id}')
async def get_item(item_id):
    data = item.select().where(item.id == item_id).first()
    if data:
        return ItemResponseModel(id=data.id, name=data.name, price= data.price, quantity=data.quantity)
    else:
        return "item no encontrado"
##Eliminar un item
@app.delete('/producto/{item_id}')
async def delete_item(item_id):
    data = item.select().where(item.id == item_id).first()
    if data:
        item.delete_instance(data)
        return True
    else:
        return "item no encontrado"
##Actualizar un item
@app.put('/producto/{item_id}')
async def update_item(item_id, data: ItemRequestModel):
    busqueda_item = item.select().where(item.id == item_id).first()
    if busqueda_item:
        data_create = item.update(
            name= data.name,
            price=data.price,
            quantity=data.quantity).where(item.id == item_id)
        data_create.execute()
    return "Item actualizado"

if __name__ == "__main__":
    uvicorn.run("main-sql:app", host="127.0.0.1", port=8000, log_level="info", reload=True, debug=True)