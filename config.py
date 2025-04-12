from advanced_alchemy.base import UUIDBase
from advanced_alchemy.config import AsyncSessionConfig
from advanced_alchemy.extensions.litestar.plugins import SQLAlchemyAsyncConfig
from litestar.contrib.jwt import JWTAuth
from litestar_users import LitestarUsersConfig
from litestar_users.config import (
    AuthHandlerConfig,
    CurrentUserHandlerConfig,
    RegisterHandlerConfig,
    UserManagementHandlerConfig,
)

from env import env
from users.models import User, UserReadDTO, UserUpdateDTO
from users.schemas import UserRegistrationDTO
from users.services import UserService

# DATABASE_URL = "sqlite+aiosqlite:///test.db"
DATABASE_URL = "postgresql+asyncpg://user:password@db:5432/litestar_intro"
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=env.database_url,
    session_dependency_key="session",
    session_config=AsyncSessionConfig(expire_on_commit=False),
    before_send_handler="autocommit",  # otherwise it does not commit and I don't know how to deal with it, also https://mvbosch.github.io/litestar-users/usage/0-configuration/#:~:text=Warning
)
ENCODING_SECRET = "1234567890abcdef"  # noqa: S105

litestar_users_config = LitestarUsersConfig(
    secret=ENCODING_SECRET,
    user_model=User,  # pyright: ignore
    user_read_dto=UserReadDTO,
    user_update_dto=UserUpdateDTO,
    user_registration_dto=UserRegistrationDTO,
    user_service_class=UserService,  # pyright: ignore
    current_user_handler_config=CurrentUserHandlerConfig(),
    register_handler_config=RegisterHandlerConfig(),
    user_management_handler_config=UserManagementHandlerConfig(),  # deletion, update, read
    auth_backend_class=JWTAuth,
    auth_handler_config=AuthHandlerConfig(),
    require_verification_on_registration=False,  # Only for demonstration
)


async def on_startup() -> None:
    """Initialize the database."""
    UUIDBase.metadata.clear()
    async with sqlalchemy_config.get_engine().begin() as conn:  # pyright: ignore
        await conn.run_sync(UUIDBase.metadata.create_all)
