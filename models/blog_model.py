from pydantic import BaseModel
from typing import Optional, List, Dict

class Image(BaseModel):
    url: str
    alias: str

# blog model class
class BlogModel(BaseModel):
    title: str
    content: str
    published:Optional[bool]
    tags: List[str]=[]
    metadata:Dict[str,str]={}
    image: Optional[Image]=None