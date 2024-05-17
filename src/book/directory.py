import os
import pathlib
import shutil


class Directory:
    def __init__(self, base_dir: str, source_dir: str) -> None:
        self.base_dir = base_dir

    def _get_absolute_path(self, relative_path: str) -> str:
        absolute_path = os.path.join(self.base_dir, relative_path)
        return absolute_path

    def create(self, relative_path: str) -> str:
        absolute_path = self._get_absolute_path(relative_path)
        pathlib.Path(absolute_path).mkdir(exist_ok=True)
        return absolute_path

    @staticmethod
    def count_files(abs_path: str) -> int:
        no_of_files = len(os.listdir(abs_path))
        return no_of_files

    @staticmethod
    def delete_dir(abs_path: str) -> None:
        if os.path.isdir(abs_path):
            shutil.rmtree(abs_path)

    @staticmethod
    def delete_file(abs_path: str) -> None:
        if os.path.isfile(abs_path):
            os.remove(abs_path)

    @staticmethod
    def find_file(abs_path: str, file_name: str) -> str:
        for dirpath, dirnames, filenames in os.walk(abs_path):
            if file_name in filenames:
                return os.path.join(dirpath, file_name)
        return ""

    @staticmethod
    def copy_file(src_path: str, dest_path: str) -> None:
        shutil.copy(src_path, dest_path)
