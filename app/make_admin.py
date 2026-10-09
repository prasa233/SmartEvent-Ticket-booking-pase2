from app.database import SessionLocal
from app.models import User


db = SessionLocal()

user = db.query(User).filter(
    User.email == "prasanth23@gmail.com"
).first()

if user:
    user.role = "admin"
    db.commit()

    print("User successfully changed to ADMIN")
    print("User ID:", user.id)
    print("Email:", user.email)
    print("Role:", user.role)
else:
    print("User not found")

db.close()