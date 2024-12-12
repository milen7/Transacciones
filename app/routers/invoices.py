
from models import Invoice
from fastapi import APIRouter

router = APIRouter(tags = ['invoice'])

@router.post("/Invoices",response_model=Invoice,tags = ['invoice'])
async def create_invoice(invoice_data: Invoice):
    breakpoint()
    return invoice_data