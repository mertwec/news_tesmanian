import json
import os

import settings as s


def create_dir(path_to_dir: str) -> None:
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)


def create_file(path_to_file: str) -> None:
    path_to_dir = os.path.split(path_to_file)[0]
    create_dir(path_to_dir)
    if not os.path.exists(path_to_file):
        with open(path_to_file, "w") as _:
            ...


def save_data_as_json(data: dict, path_to_jfile: str, mode: str = "w") -> None:
    with open(path_to_jfile, mode) as file_:
        json.dump(data, file_, indent=4, ensure_ascii=False)


def get_data_from_json(path_to_jfile) -> dict:
    with open(path_to_jfile, "r") as file_news:
        try:
            return json.load(file_news)
        except json.decoder.JSONDecodeError as jd:
            s.logger.error(f"json-database not exists: {s.JSON_PATH}. {jd}")
            return
