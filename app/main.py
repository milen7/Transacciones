import pytz
from datetime import datetime

from models import Transaction,Invoice
from db import create_all_tables
from fastapi import FastAPI
from .routers import customers,transactions

app = FastAPI(lifespan=create_all_tables)
app.include_router(customers.router)
app.include_router(transactions.router)

@app.get("/")
async def root():
    return {"message": "Hola, Luis!"}

country_timezones = {
    "CO":"America/Bogota",
    "MX":"America/Mexico_City",
    "AR":"America/Argentina/Buenos_Aires",
    "BR":"America/Sao_Paulo",
    "PE":"America/Lima"
}

@app.get("/time/{iso_code}")
async def time(iso_code:str):
    iso=iso_code.upper()
    timezone_str=country_timezones.get(iso)
    tz=pytz.timezone(timezone_str)
    return {"time": datetime.now(tz)}



@app.post("/Invoices",response_model=Invoice)
async def create_invoice(invoice_data: Invoice):
    breakpoint()
    return invoice_data




