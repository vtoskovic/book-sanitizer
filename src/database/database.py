from contextlib import contextmanager
import pandas as pd
from sqlalchemy import (Connection,
                        Engine,
                        text as sql_text)


class Database:
    def __init__(self, engine: Engine):
        self.engine = engine

    @contextmanager
    def connect(self) -> Connection:
        conn = self.engine.connect()
        try:
            yield conn
        finally:
            conn.close()

    @staticmethod
    def create_df_from_query(
            conn: Connection,
            query: str) -> pd.DataFrame:
        query = sql_text(query)
        df = pd.read_sql(query, conn)
        return df

    @staticmethod
    def create_dict_from_query(
            conn: Connection,
            query: str) -> list[dict]:
        query = sql_text(query)
        df = pd.read_sql(query, conn)
        _dict = df.to_dict(orient="records")
        return _dict
