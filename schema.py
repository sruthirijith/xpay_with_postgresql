from typing import Optional
from pydantic import BaseModel



class Base(BaseModel):
    username     : str
    email        : str
    mobile_no    : str
    password     :str

class Profile(BaseModel):
    first_name   : str
    last_name    : str
    city         : str
    place_of_birth: str
    image    : str
   
