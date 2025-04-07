from __future__ import annotations

from datetime import datetime

from advanced_alchemy.base import UUIDBase
from advanced_alchemy.extensions.litestar.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class User(UUIDBase, SQLAlchemyUserMixin):
    """
    Comes with built-in fields:
    - id (UUID)
    - email
    - is_active
    - is_verified
    - password_hash

    Last two are set to True by default, for demonstration purposes.
    """

    name: Mapped[str] = mapped_column(
        nullable=False,
    )
    surname: Mapped[str] = mapped_column(
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )


class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"password_hash", "created_at", "updated_at"})


class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(
        exclude={
            "id",
            "password_hash",
            "created_at",
            "updated_at",
            "is_active",
            "is_verified",
        },
        partial=True,
    )
