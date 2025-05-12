from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from . import schemas, models

router = APIRouter(prefix="/restaurants", tags=["restaurants"])

@router.post("/")
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = models.Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    return db_restaurant

@router.get("/nearest")
def get_nearest_restaurant(lat: float, lon: float, db: Session = Depends(get_db)):

    restaurants = db.query(models.Restaurant).all()
    return restaurants[0] if restaurants else None