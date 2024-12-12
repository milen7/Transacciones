from models import Transaction
from fastapi import APIRouter

router = APIRouter(tags = ['transactions'])

@router.post("/Transactions",tags = ['transactions'])
async def create_transation(transaction_data: Transaction):
    return transaction_data