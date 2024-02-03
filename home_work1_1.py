from pathlib import Path
import re
import math

def total_salary(path):
    try:
        path = Path("file.txt")
        path.write_text("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000", encoding="utf-8")
        with open("file.txt", "r", encoding="utf-8") as fh:
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