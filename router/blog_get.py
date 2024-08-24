from fastapi import status,Response,APIRouter
from enum import Enum
from typing import Optional


router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
    responses={404: {"description": "Not found"}},
)


# endpoint with query parameters
@router.get(
        "/all",
        summary="Get all blogs",
        description="Get all blogs with pagination",
        response_description="List of blogs",
        )
def get_all_blogs(page=1,page_size:Optional[int]=None):
    return {"message": f"All Blogs page {page} page_size {page_size}"}

# endpoint with path parameters and query parameters
@router.get("/{id}/comments/{comment_id}",tags=["Comment"])
def get_blog_comment(id: int, comment_id: int,valid:bool=True, name: Optional[str] = None):
    """
    Get a specific blog comment
    - **id**: Blog id
    - **comment_id**: Comment id
    - **valid**: Comment is valid or not (default True) optional query parameter
    - **name**: Commenter name optional query parameter

    """
    return {"message": f"Blog {id} Comment {comment_id} valid {valid} name {name}"}

# Note: Predefined path parameters predefined with Enum class
class BlogType(str, Enum):
    tech = "tech"
    health = "health"
    business = "business"

@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog Type {type}"}

@router.get("/{id}",status_code=status.HTTP_200_OK,)
def get_blog(id: int,response:Response):
    if id>5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Blog not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog {id}"}
        







