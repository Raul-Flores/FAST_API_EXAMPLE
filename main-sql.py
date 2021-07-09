__author__ = "Raul Flores"
__license__ = "GNUv3"
__version__ = "1.0"
__maintainer__ = "Raul Eduardo Flores Najera"
__email__ = "raul.flores@ciberc.com"
__status__ = "valid production"
from database import item
import uvicorn
from fastapi import FastAPI, Request
from schemas import ItemRequestModel
from database import database as connection

app = FastAPI(tittle='CiberC demo APIs', description= 'un demo pequeno de APIs', version='1.0')
#Eventos en FAST API
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables([item])
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
####POST Agregar nuevo producto
@app.post('/producto')
async def add_product(data: ItemRequestModel):
    data_create = item.create(
        name= data.name,
        price=data.price,
        quantity=data.quantity)    
    data_create.save()
    return "Item creado"

if __name__ == "__main__":
    uvicorn.run("main-sql:app", host="127.0.0.1", port=8000, log_level="info", reload=True, debug=True)