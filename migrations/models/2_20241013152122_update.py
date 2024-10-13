from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `users`;
        DROP TABLE IF EXISTS `event`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ;"""
