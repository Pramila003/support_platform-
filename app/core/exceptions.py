from fastapi import Request
from fastapi.responses import JSONResponse

class UserAlreadyExistsError(Exception):
    pass

async def user_already_exist_handler(request:Request, exc:UserAlreadyExistsError):
    return JSONResponse(
        status_code=409,
        content={
            "detail":"An Account with this Email already exist"
            
        },
    )
    
class InvalidCredentialsError(Exception):
    pass

async def Invalid_creadentials_handler(request:Request, exc:InvalidCredentialsError):
    return JSONResponse(
        status_code=401,
        content={
            "datail":"Incorrect Username or Passwpord"
        },
        headers={"www-authenticate":"bearer"},
    )