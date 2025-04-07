from __future__ import annotations

from advanced_alchemy.extensions.litestar.plugins import (
    SQLAlchemyInitPlugin,
)
from litestar import Litestar
from litestar_users import LitestarUsersPlugin

from config import litestar_users_config, on_startup, sqlalchemy_config
from users.controllers import UserController

app = Litestar(
    debug=True,
    on_startup=[on_startup],
    plugins=[
        SQLAlchemyInitPlugin(config=sqlalchemy_config),
        LitestarUsersPlugin(config=litestar_users_config),
    ],
    route_handlers=[UserController],
)
