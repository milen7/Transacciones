from fastapi import APIRouter
from models import Plan,CustomerPlan
from db import SessionDep


router = APIRouter(tags = ['plans'])

@router.post("/plan",response_model=Plan,tags=["plans"])
async def create_plan(plan_data: Plan,session:SessionDep):
    plan_db=Plan.model_validate(plan_data.model_dump())
    session.add(plan_db) 
    session.commit()
    session.refresh(plan_db)
    return plan_db

