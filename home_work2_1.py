from pathlib import Path
import re


def get_cats_info(path):
    path = Path("file.txt")
    path.write_text("60b90c1c13067a15887e1ae1,Tayson,3\n"
                    "60b90c2413067a15887e1ae2,Vika,1\n"
                    "60b90c2e13067a15887e1ae3,Barsik,2\n"
                    "60b90c3b13067a15887e1ae4,Simon,12\n"
                    "60b90c4613067a15887e1ae5,Tessi,5", encoding="utf-8")
    try:
        with open("file.txt", "r", encoding = "utf-8") as fh:
            info_list = fh.readlines()
            cats_info =[]
            for info in info_list:
                info = info.split(",")
                cats_info.append({"id": info[0], "name": info[1], "age": re.sub(r"\n", "", info[2])})
        return cats_info
    except FileNotFoundError:
        return "Не вдалося знайти файл."

cats_info = get_cats_info("path/to/cats_lst.txt")
print(cats_info)