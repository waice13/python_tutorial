from typing import Optional

from fastapi import FastAPI
from starlette.routing import Host

import psycopg2
from sqlalchemy import create_engine
import pandas as pd

import uvicorn


app = FastAPI()


@app.get("/")

def read_root():

    engine = create_engine('postgresql+psycopg2://root:root@postgresql_db/ws_db')
    con = engine.connect()

    df = pd.read_sql('SELECT kind, etag, id, title FROM public.uscategory;', con)  

    return df.to_dict(orient='records')


if __name__=="__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")