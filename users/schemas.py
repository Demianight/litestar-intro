from dataclasses import dataclass

from litestar.dto import DataclassDTO


@dataclass
class UserRegistrationSchema:
    email: str
    password: str
    name: str
    surname: str


class UserRegistrationDTO(DataclassDTO[UserRegistrationSchema]):
    """User registration DTO."""
