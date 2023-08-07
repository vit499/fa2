from typing import Union

from pydantic import BaseModel
from .room import Room

# flat1 -> room1 -> dot1
#                -> dot2
#          room2 -> dot3
#                -> dot4
#          room3 -> dot5
# flat2 -> room4 -> dot6

class FlatBase(BaseModel):
    param1: Union[str, None] = None
    status1: Union[str, None] = None
    param2: Union[str, None] = None
    status2: Union[str, None] = None
    param3: Union[str, None] = None
    status3: Union[str, None] = None


class FlatCreate(FlatBase):
    pass


class Flat(FlatBase):
    id: int
    rooms: list[Room] = []

    class Config:
        from_attributes = True


