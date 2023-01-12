from typing import Dict
import time
import jwt

SECRET_KEY    = "daf9125d55281af81215b9b5224b46c6"

AL= "HS256"


JWT_SECRET = SECRET_KEY
JWT_ALGORITHM = AL


def token_response(token: str):
    return  token


#  we can wde the below function it is access token every route can set the header 


def signJWT_access(mobile_number: str)-> Dict[str, str]:
    payload = {
        "mobile_number": mobile_number,
        "expires": time.time()+900
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)



'''
Refresh  token for genarate new access token  
the new access token expired in smaller time and the refresh one is more validity
compare to access token because we can use the refresh token for regenarate new access token '''

def signJWT_refresh(mobile_number: str)-> Dict[str, str]: 
    payload = {
        "mobile_number": mobile_number,
        "expires": time.time()+2.592e+6
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)




# def signJWT_mobile_otp(otp: str)-> Dict[str, str]:
#     payload = {
#         "otp":otp,
#         "expires": time.time()+180
#     }

#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

#     return token_response(token)



# decode function it is decoder , we can get encoded token the token can decoded by the decode function
def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decode_token if decode_token["expires"] >= time.time() else None
    except:
        return {}