from fastapi import FastAPI, HTTPException, Depends, status
from models.db import db
from models.models import Sheep
from typing import List

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this ID does not exist.")
    return db.get_sheep(id)

@app.post("/sheep/", response_model=Sheep, status_code= status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists.")
    
    db.data[sheep.id] = sheep
    return sheep

@app.delete("/sheep/{sheep_id}", response_model=Sheep, status_code = status.HTTP_200_OK)
def delete_sheep(sheep_id: int):
    if sheep_id not in db.data:
        raise HTTPException(status_code= 404, detail="Sheep with this ID does not exist.")

    deleted_sheep_data =  db.data[sheep_id]
    del db.data[sheep_id]

    return deleted_sheep_data

@app.put("/sheep/", response_model=Sheep, status_code=status.HTTP_200_OK)
def update_sheep(sheep: Sheep):
    if sheep.id not in db.data:
        raise HTTPException(status_code= 404, detail="Sheep with this ID does not exist.")
    
    db.data[sheep.id] = sheep
    return sheep

@app.get("/sheep/", response_model=List[Sheep], status_code=status.HTTP_200_OK)
def read_sheep():
    return list(db.data.values())

