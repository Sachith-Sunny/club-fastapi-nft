from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.player import Player
from schemas.player import PlayerCreate, PlayerUpdate

# Create a Player for the user checking the owner

class CRUDPlayer(CRUDBase[Player, PlayerCreate, PlayerUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: PlayerCreate, owner_id: int
    ) -> Player:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Player]:
        return (
            db.query(self.model)
            .filter(Player.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


player = CRUDPlayer(Player)