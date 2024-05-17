import os
from typing import Union

from sqlalchemy import create_engine
from src.database import Database
from src.book import Sanitizer

from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    mysql_engine = create_engine(f"{os.environ.get('DB_URL')}")
    db = Database(mysql_engine)

    with db.connect() as mysql_conn:
        all_books_query = "SELECT id, image_src, intro_src, title FROM slusrsf6rs_db.books;"
        books: list[dict[str, Union[str, int]]] = db.create_dict_from_query(mysql_conn, all_books_query)
        for book in books:
            book_id = book.get("id")
            chapters_query = f"SELECT source_link FROM slusrsf6rs_db.chapters WHERE book_id = {book_id};"
            df_chapters = db.create_df_from_query(mysql_conn, chapters_query)
            chapters: list[str] = df_chapters["source_link"].to_list()
            sanitizer = Sanitizer(book, chapters)
            sanitizer.sanitize()
            break
