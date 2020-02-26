#import asyncpg
#import asyncio
import aiomysql
from fastapi import FastAPI
from loguru import logger

from app.core.config import HOST, PORT, USER, PWD, DB, DATABASE_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT


#loop = asyncio.get_event_loop()
async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {0}", repr(DATABASE_URL))

    app.state.pool = await aiomysql.create_pool(host=str(HOST), port=int(PORT),
                                           user=str(USER), password=str(PWD),
                                           db=str(DB), loop=None, autocommit=False)

    '''
    app.state.pool = await asyncpg.create_pool(
        str(DATABASE_URL),
        min_size=MIN_CONNECTIONS_COUNT,
        max_size=MAX_CONNECTIONS_COUNT,
    )
    '''
    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await app.state.pool.close()

    logger.info("Connection closed")
