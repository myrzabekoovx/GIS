from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from . import schemas, models

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    return db_order

@router.get("/{order_id}/status")
def get_order_status(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    return {"status": order.status} if order else None