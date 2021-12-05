import crud, models, schemas
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Player])
def read_players(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve players.
    """
    if crud.user.is_superuser(current_user):
        players = crud.player.get_multi(db, skip=skip, limit=limit)
    else:
        players = crud.player.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return players


@router.post("/", response_model=schemas.Player)
def create_player(
    *,
    db: Session = Depends(deps.get_db),
    player_in: schemas.PlayerCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new player.
    """
    player = crud.player.create_with_owner(db=db, obj_in=player_in, owner_id=current_user.id)
    return player


@router.put("/{id}", response_model=schemas.Player)
def update_player(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    player_in: schemas.PlayerUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an player.
    """
    player = crud.player.get(db=db, id=id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    if not crud.user.is_superuser(current_user) and (player.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    player = crud.player.update(db=db, db_obj=player, obj_in=player_in)
    return player


@router.get("/{id}", response_model=schemas.Player)
def read_player(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get player by ID.
    """
    player = crud.player.get(db=db, id=id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    if not crud.user.is_superuser(current_user) and (player.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return player


@router.delete("/{id}", response_model=schemas.Player)
def delete_player(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an player.
    """
    player = crud.player.get(db=db, id=id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    if not crud.user.is_superuser(current_user) and (player.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    player = crud.player.remove(db=db, id=id)
    return player
