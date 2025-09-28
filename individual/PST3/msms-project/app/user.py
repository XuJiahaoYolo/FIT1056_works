from typing import Dict, Any

class User:
    """Base user model."""
    def __init__(self, user_id: str, name: str, email: str = "") -> None:
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "User", "user_id": self.user_id, "name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        return cls(user_id=data.get("user_id",""), name=data.get("name",""), email=data.get("email",""))

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, name={self.name!r})"
