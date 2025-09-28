from typing import Dict, Any, List

class TeacherUser:
    def __init__(self, user_id: str, name: str, email: str = "",
                 instruments: List[str] = None, course_ids: List[str] = None) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        self.instruments = list(instruments or [])
        self.course_ids = list(course_ids or [])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "TeacherUser",
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "instruments": self.instruments,
            "course_ids": self.course_ids,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TeacherUser":
        return cls(
            user_id=data.get("user_id",""),
            name=data.get("name",""),
            email=data.get("email",""),
            instruments=data.get("instruments", []) or [],
            course_ids=data.get("course_ids", []) or [],
        )

    def __repr__(self) -> str:
        return f"TeacherUser(user_id={self.user_id!r}, name={self.name!r}, instruments={self.instruments})"


class Course:
    def __init__(self, course_id: str, name: str, day: str, time: str,
                 room: str, teacher_id: str, student_ids: List[str] = None) -> None:
        self.course_id = course_id
        self.name = name
        self.day = day
        self.time = time
        self.room = room
        self.teacher_id = teacher_id
        self.student_ids = list(student_ids or [])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "course_id": self.course_id,
            "name": self.name,
            "day": self.day,
            "time": self.time,
            "room": self.room,
            "teacher_id": self.teacher_id,
            "student_ids": self.student_ids,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Course":
        return cls(
            course_id=data.get("course_id",""),
            name=data.get("name",""),
            day=data.get("day",""),
            time=data.get("time",""),
            room=data.get("room",""),
            teacher_id=data.get("teacher_id",""),
            student_ids=data.get("student_ids", []) or [],
        )

    def __repr__(self) -> str:
        return f"Course({self.course_id!r}, {self.name!r}, {self.day} {self.time}, room={self.room})"
