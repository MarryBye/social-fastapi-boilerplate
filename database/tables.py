from sqlalchemy import Table
from database.metadata import metadata

users = Table(
    "users",
    metadata,
    schema="private"
)

countries = Table(
    "countries",
    metadata,
    schema="private"
)

cities = Table(
    "cities",
    metadata,
    schema="private"
)

users_view = Table(
    "users_view",
    metadata,
    schema="public"
)