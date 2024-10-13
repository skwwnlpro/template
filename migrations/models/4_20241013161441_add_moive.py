from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `movie` (
    `movie_id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `movie_name` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `movie`;"""
