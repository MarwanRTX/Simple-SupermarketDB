from fastapi import FastAPI,HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4


APP = FastAPI()

class SuperMarket_DB(BaseModel):
    product_id: UUID = uuid4() 
    product_name: str
    description: str


product_db = []


@APP.post("/Supermarket/", response_model=SuperMarket_DB)
def add_product(product: SuperMarket_DB):
    product_db.append(product)
    return product


@APP.get("/Supermarket/", response_model=List[SuperMarket_DB])
def reveal_products():  
    return product_db


@APP.delete("/Supermarket/{product_id}", response_model=SuperMarket_DB)
def delete_product(product_id: UUID):
    for idx, product in enumerate(product_db):
        if product.product_id == product_id:
            return product_db.pop(idx)

    raise HTTPException(status_code=404, detail="Product not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(APP, port=8000)
