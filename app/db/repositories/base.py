from typing import Any, List, Sequence, Tuple

#import asyncio
#import aiomysql
#from aiomysql.connection import Connection
from aiomysql.cursors import Cursor
#from asyncpg import Record
#from asyncpg.connection import Connection
from loguru import logger


def _log_query(query: str, query_params: Tuple[Any, ...]) -> None:
    logger.debug("query: {0}, values: {1}", query, query_params)


class BaseRepository:
    def __init__(self, cur: Cursor) -> None:
        #self._conn = conn
        self._cur = cur
        #with conn.cursor(aiomysql.DictCursor) as cur:
            #self._cur = cur

    @property
    def connection(self) -> Cursor:
        return self._cur

    async def _log_and_fetch_one(self, query: str, *query_params: Any) -> Any:
        _log_query(query, query_params)
        await self._cur.execute(query, *query_params)
        return await self._cur.fetchone()

    async def _log_and_fetch_all(self, query: str, *query_params: Any) -> Any:
        _log_query(query, query_params)
        await self._cur.execute(query, *query_params)
        return await self._cur.fetchall()
    
    '''
    async def _log_and_fetch_value(self, query: str, *query_params: Any) -> Any:
        _log_query(query, query_params)
        await self._cur.execute(query, *query_params)
        return await self._cur.fetchmany()'''

    async def _log_and_execute(self, query: str, *query_params: Any) -> None:
        _log_query(query, query_params)
        await self._cur.execute(query, *query_params)

    async def _log_and_execute_many(
        self, query: str, *query_params: Sequence[Tuple[Any, ...]]
    ) -> None:
        _log_query(query, query_params)
        await self._cur.executemany(query, *query_params)
