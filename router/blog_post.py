from fastapi import APIRouter, Query, Path, Body
# from pydantic import BaseModel
from typing import Optional, List, Dict
from models.blog_model import BlogModel, Image

router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
    responses={404: {"description": "Not found"}},
)

# class Image(BaseModel):
#     url: str
#     alias: str

# # blog model class
# class BlogModel(BaseModel):
#     title: str
#     content: str
#     published:Optional[bool]
#     tags: List[str]=[]
#     metadata:Dict[str,str]={}
#     image: Optional[Image]=None

@router.post(
    "/new/{id}",
    summary="Create new blog",
    description="Create new blog post",
    response_description="Create new blog post",
    )
def create_blog(blog: BlogModel, id: int,version:int=1):
    return {
        "message": f"Create new blog with id {id} version {version}",
        "data": blog
    }


@router.post(
    "/new/{id}/comment/{comment_id}",
    summary="Create new blog comment",
    description="Create new blog comment",
    response_description="Create new blog comment",
    tags=["Comment"],
    )
def create_comment(blog: BlogModel, id: int,
                   comment_title:str=Query(
                            ...,
                            title="Comment Title",
                            min_length=10,
                            max_length=100,
                            description="Title of the comment",
                            
                   ),
                    #  comment: str=Body( "Comment content ...",)
                   comment: str=Body(
                             ... , # or Ellipsis
                            min_length=10,
                            max_length=1000,
                          
                            regex="^[a-z\\s]*$"
                            ),
                    v:Optional[List[str]]=Query([1.0,2.1,3.0]),
                    # comment_id:int=Path(None,gt=5,le=10),
                    comment_id:int=Path(...,gt=5,le=10),
                     
                    ):
    return {
        "message": f"Create new blog comment with id {id}",
        "data": blog,
        "comment": comment,
        "comment_title": comment_title,
    }
   