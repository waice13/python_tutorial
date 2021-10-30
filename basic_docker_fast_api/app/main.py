from typing import Optional

from fastapi import FastAPI
from starlette.routing import Host

import uvicorn


app = FastAPI()


@app.get("/")

def read_root():

    car = {
        1:{
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        },
        2:{
            "brand": "Honda",
            "model": "Civic",
            "year": 2014
        },
        3:{
            "brand": "Mazda",
            "model": "3",
            "year": 2020
        },
    }
    
    return car


if __name__=="__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")