from typing import Optional
from pydantic import BaseModel


# Shared properties
class PlayerBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on Player creation
class PlayerCreate(PlayerBase):
    title: str


# Properties to receive on Player update
class PlayerUpdate(PlayerBase):
    pass


# Properties shared by models stored in DB
class PlayerInDBBase(PlayerBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Player(PlayerInDBBase):
    pass


# Properties properties stored in DB
class PlayerInDB(PlayerInDBBase):
    pass
