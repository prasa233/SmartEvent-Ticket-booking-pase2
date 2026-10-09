from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..dependencies import require_admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.put("/users/{user_id}/make-organizer")
def make_organizer(
    user_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.role = "ORGANIZER"

    db.commit()
    db.refresh(user)

    return {
        "message": "User promoted to ORGANIZER",
        "user_id": user.id,
        "role": user.role
    }