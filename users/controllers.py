from litestar import Controller, get
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import User, UserReadDTO


class UserController(Controller):
    """Controller for user-related operations."""

    path = "/users"

    @get("", return_dto=UserReadDTO)
    async def get_users(
        self,
        session: AsyncSession,  # session provided by SQLAlchemy plugin
    ):
        """
        Get all users.
        Apparently there is no included 'users' endpoint in the litestar_users plugin (or I didn't find it)
        """
        return (await session.execute(select(User))).scalars().all()
