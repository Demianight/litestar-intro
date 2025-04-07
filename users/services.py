from typing import Any

from litestar import Request
from litestar_users.service import BaseUserService

from users.models import User


class UserService(BaseUserService[User, Any, Any]):  # type: ignore[type-var]
    async def post_registration_hook(
        self, user: User, request: Request | None = None
    ) -> None:
        # Could use Kafka to notify another services
        return await super().post_registration_hook(user, request)

    async def send_verification_token(self, user: User, token: str) -> None:
        """
        Could be an email notification, also with Kafka
        Anyway, it's disabled in the config.py
        """
