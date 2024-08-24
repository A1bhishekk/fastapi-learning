from fastapi import APIRouter,Depends,HTTPException
from schemas import UserBase,UserDisplay
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_user
from typing import List




router = APIRouter(
    prefix="/user",
    tags=["User"],
)


# create  user 

@router.post("/",response_model=UserDisplay)
def create_user(request: UserBase,db:Session=Depends(get_db)):
    return db_user.create_user(db,request)



# # read user 
# @router.get("/",response_model=UserDisplay)
# def get_all_users(db:Session=Depends(get_db)):
#     return db_user.get_all_users(db)

@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    users = db_user.get_all_users(db)
    return users

# get user by id
@router.get("/{user_id}",response_model=UserDisplay)
def get_user_by_id(user_id:int,db:Session=Depends(get_db)):
    user = db_user.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/{user_id}/update", response_model=UserDisplay)
def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    try:
        return db_user.update_user(db, user_id, request)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# delete user
@router.delete("/{user_id}")
def delete_user(user_id:int,db:Session=Depends(get_db)):
    return db_user.delete_user(db,user_id)