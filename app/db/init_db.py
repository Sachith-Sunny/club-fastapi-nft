from sqlalchemy.orm import Session

import crud, schemas
# from core.config import settings
from db import base 


def init_db(db: Session) -> None:
    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    # if not user:
    #     user_in = schemas.UserCreate(
    #         email=settings.FIRST_SUPERUSER,
    #         password=settings.FIRST_SUPERUSER_PASSWORD,
    #         is_superuser=True,
    #     )
        user = crud.user.create(db, obj_in=user_in) 
