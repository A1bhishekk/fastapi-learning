from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from schemas import UserDisplay
from typing import List



def create_user(db:Session,request:UserBase):
    new_user=DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



def get_all_users(db: Session) -> List[UserDisplay]:
    users = db.query(DbUser).all()
    return users  #


# get user by id
def get_user_by_id(db: Session, user_id: int) -> UserDisplay:
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    return user


# update_user
# def update_user(db: Session, user_id: int, request: UserBase):
#     user = db.query(DbUser).filter(DbUser.id == user_id)
#     user.update({
#        DbUser.username: request.username,
#        DbUser.email: request.email,
#        DbUser.password: Hash.bcrypt(request.password)
#     })
#     db.commit()
#     return "updated"

def update_user(db: Session, user_id: int, request: UserBase) -> UserDisplay:
    # Query for the user
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    
    if user is None:
        raise ValueError("User not found")

    # Update the user's attributes
    user.username = request.username
    user.email = request.email
    user.password = Hash.bcrypt(request.password)  # Hash the password

    # Commit the changes
    db.commit()
    db.refresh(user)  # Refresh the instance to reflect the updated state

    # Return the updated user
    return UserDisplay.model_validate(user)  # Return the updated user as a UserDisplay instance


# delete user

def delete_user(db: Session, user_id: int):
    # user = db.query(DbUser).filter(DbUser.id == user_id)
    # user.delete(synchronize_session=False)
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    db.delete(user)
    db.commit()
    return "deleted"



