from typing import Dict, Any, List
from .user import User

class StudentUser(User):
    """Student user model (inherits from User)."""
    def __init__(self, user_id: str, name: str, email: str = "",
                 enrolled_course_ids: List[str] = None, grade_level: str = "") -> None:
        super().__init__(user_id, name, email)
        # TODO: Call the parent class's __init__ method using super().
        self.enrolled_course_ids = list(enrolled_course_ids or [])
        # TODO: Initialize an empty list called 'enrolled_course_ids' to store the IDs of courses.
        self.grade_level = grade_level

    # helpers
    def enroll(self, course_id: str) -> bool:
        cid = str(course_id)
        if cid not in self.enrolled_course_ids:
            self.enrolled_course_ids.append(cid)
            return True
        return False

    def drop(self, course_id: str) -> bool:
        cid = str(course_id)
        if cid in self.enrolled_course_ids:
            self.enrolled_course_ids.remove(cid)
            return True
        return False

    def is_enrolled(self, course_id: str) -> bool:
        return str(course_id) in self.enrolled_course_ids

    # persistence
    def to_dict(self) -> Dict[str, Any]:
        base = super().to_dict()
        base.update({
            "type": "StudentUser",
            "enrolled_course_ids": self.enrolled_course_ids,
            "grade_level": self.grade_level,
        })
        return base

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StudentUser":
        return cls(
            user_id=data.get("user_id",""),
            name=data.get("name",""),
            email=data.get("email",""),
            enrolled_course_ids=data.get("enrolled_course_ids", []) or [],
            grade_level=data.get("grade_level",""),
        )

    def __repr__(self) -> str:
        return f"StudentUser(user_id={self.user_id!r}, name={self.name!r}, courses={self.enrolled_course_ids})"
