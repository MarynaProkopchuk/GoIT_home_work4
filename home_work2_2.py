from pathlib import Path
import re

def get_cats_info(path):
    try:
        with open(path, "r", encoding = "utf-8") as fh:
            info_list = fh.readlines()
            cats_info =[]
            for info in info_list:
                info = info.split(",")
                cats_info.append({"id": info[0], "name": info[1], "age": re.sub(r"\n", "", info[2])})
        return cats_info
    except FileNotFoundError:
        return "Не вдалося знайти файл."

cats_info = get_cats_info("d:\\cats_lst.txt")
print(cats_info)