import os

from .directory import Directory

from dotenv import load_dotenv

load_dotenv()


class Sanitizer:
    def __init__(self, book: dict[str, str | int],
                 chapters: list[str]):
        self.book = book
        self.chapters = chapters

    def sanitize(self):
        base_dir = os.environ.get('BASE_DIR')
        source_dir = f"{base_dir}/source"
        directory = Directory(base_dir, source_dir)
        book_title = self.book.get('title')
        r_path = f"{directory.base_dir}/{book_title}"
        target_dir = directory.create(relative_path=r_path)

        image_src = self.book.get("image_src")
        image_file_path = directory.find_file(source_dir, image_src)
        self._copy(directory, image_file_path, target_dir)

        intro_src = self.book.get("intro_src")
        intro_file_path = directory.find_file(source_dir, intro_src)
        self._copy(directory, intro_file_path, target_dir)

        for chapter in self.chapters:
            chapter_file_path = directory.find_file(source_dir, chapter)
            self._copy(directory, chapter_file_path, target_dir)

    def _copy(self, directory: Directory, source: str, target: str):
        try:
            directory.copy_file(source, target)
        except FileNotFoundError:
            with open("log.txt", mode="a") as log:
                log.write(f"{self.book.get('title')}: File {source} not found \n")
