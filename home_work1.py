from pathlib import Path
import re
import math

current_dir = Path(__file__).parent

def total_salary(path):
    try:
        with open(current_dir/"text.txt", "r", encoding="utf-8") as fh:
            full_list=fh.readlines()
            salary_list=[]
            for salary in full_list:
                salary = re.sub(r"\n", "", salary.split(",").pop(1))
                salary_list.append(int(salary))
            total = sum(salary_list)
            average = total//len(salary_list)
        return total, average 

    except FileNotFoundError:
        return "Не вдалося знайти файл."

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")