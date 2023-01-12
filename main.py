import shutil
from fastapi import FastAPI, Depends, UploadFile
from sqlalchemy.orm import Session
from security.jwt_handler import signJWT_access, signJWT_refresh, decodeJWT
from security.jwt_bearer import JWTBearer
from database import engine, Base, get_db
import models
import schema
import crud

Base.metadata.create_all(bind=engine)
app= FastAPI(title="User_Registration")


@app.post('/xpay_user_creation')
async def user_register(data:schema.Base, user_db:Session=Depends(get_db)):
    """user registration"""
    receive_data = user_db.query(models.xpay_user).filter(models.xpay_user.mobile_no==data.mobile_no).first()
    if receive_data:
        return 'phone number already in db'
    receive_data1 = user_db.query(models.xpay_user).filter(models.xpay_user.email==data.email).first()
    if receive_data1:
        return ' email already in db'
    user_details = models.xpay_user(**data.dict())
    user_db.add( user_details)
    user_db.commit()
    receive_data2 = user_db.query(models.xpay_user.id).filter(models.xpay_user.mobile_no==data.mobile_no).first()
    return data,receive_data2
@app.post('/employee login')
def employee_login(email:str,password:str,user_db:Session=Depends(get_db)):
    """login a user by email and password"""
    login_data=user_db.query(models.xpay_user).filter(models.xpay_user.email==email, models.xpay_user.password==password).first()
    if login_data:
        access_token=signJWT_access(login_data.mobile_no)
        refresh_token=signJWT_refresh(login_data.mobile_no)
        return {"message":"login succesfull","access_token":access_token,"refresh_token":refresh_token}
    return "invalid username/password"  
@app.post("/profile creation", tags=["profile"])   
async def profile_creation(first_name:str, last_name:str,city:str,
                           place_of_birth:str,image:UploadFile,
                           user_db:Session = Depends(get_db),
                           token:str=Depends(JWTBearer())):
    """profile creation by adding image"""                       
    decodedata= decodeJWT(token)
    users = crud.get_user_by_phone(user_db,mobile_no=decodedata['mobile_number'])
    if users:
        profile_id = user_db.query(models.xpay_profile).filter(models.xpay_profile.user_id==users.id).first()
        if profile_id:
            return "profile already exist"
        file_path = f"profile_img/{image.filename}"
        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(image.file,buffer)
            profile_details=models.xpay_profile(first_name= first_name,
                                        last_name = last_name,
                                        city = city,
                                        place_of_birth= place_of_birth,
                                        image = file_path,
                                        user_id=users.id)
        user_db.add(profile_details)
        user_db.commit()                            
        return "profile added succesfully"                                 