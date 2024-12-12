
from models import Customer,CustomerCreate,CustomerUpdate
from db import SessionDep
from fastapi import APIRouter, HTTPException,status
from sqlmodel import select

router = APIRouter(tags = ['customers'])

@router.post("/customers",response_model=Customer,tags=["customers"])
async def create_customer(customer_data: CustomerCreate,session:SessionDep):
    customer=Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get("/customers",response_model=list[Customer],tags=["customers"])
async def list_customer(session: SessionDep):
    return session.exec(select(Customer)).all()

@router.get("/customers/{customer_id}",response_model=Customer,tags=["customers"])
async def read_costumer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer,customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,DETAIL="Customer doesn't exist")
    return customer_db

@router.patch("/customers/{customer_id}",response_model=Customer,status_code=status.HTTP_201_CREATED,tags=["customers"])
async def refresh_costumer(customer_id: int,customer_data:CustomerUpdate ,session: SessionDep):
    customer_db = session.get(Customer,customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,DETAIL="Customer doesn't exist")
    customer_data_dict = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data_dict)
    session.commit()
    session.refresh(customer_db)
    return customer_db

@router.delete("/customers/{customer_id}",tags=["customers"])
async def delete_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer,customer_id)
    if not customer_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,DETAIL="Customer doesn't exist")
    session.delete(customer_db)
    session.commit()
    return {"detail":"ok"}