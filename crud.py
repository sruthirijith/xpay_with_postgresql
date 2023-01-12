import models
from database import SessionLocal
from sqlalchemy.orm import Session

db = SessionLocal()

def get_user_by_phone(db:Session, mobile_no:str):
    login_phone=db.query(models.xpay_user).filter(models.xpay_user.mobile_no==mobile_no).first()
    return login_phone
