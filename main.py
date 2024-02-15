import eel
import json
import os
import pandas as pd
import openpyxl

def save_excel_file(data, num_files):
    columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
               "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", 'ընդհանուր']
    excelData = []

    for obj in data['list']:
        userDays = []
        for col in columns:
            if col in obj['days']:
                userDays.append(' x ')
            elif col == 'ընդհանուր':
                userDays.append(f"{len(obj['days'])}")
            else:
                userDays.append(' ')

        excelData.append(userDays)

    df = pd.DataFrame(data=excelData,
                      index=[obj['full_name'] for obj in data['list']],
                      columns=columns)
    # Export DataFrame to Excel
    df.to_excel(f"excel/{num_files} {data['title']}.xlsx", sheet_name='new_sheet_name')


@eel.expose
def delete_data(number):
    file_path = os.path.join("data", f"{number}.json")
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    else:
        return False


@eel.expose
def get_one_data(number):
    file_path = os.path.join("data", f"{number}.json")
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data


@eel.expose
def get_data():
    data_folder = "data"
    all_data = []

    if not os.path.exists(data_folder):
        return []

    for filename in os.listdir(data_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(data_folder, filename)
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
                all_data.append(data)

    return all_data[::-1]


@eel.expose
def save_data(data, number, exportExcel):
    try:
        if not os.path.exists("data"):
            os.makedirs("data")

        files_in_data_directory = os.listdir("data")
        num_files = number if number else len(files_in_data_directory)+1
        data['number'] = num_files
        file_path = os.path.join("data", f"{num_files}.json")
        with open(file_path, "w") as json_file:
            json.dump(data, json_file)

        if exportExcel:
            if not os.path.exists("excel"):
                os.makedirs("excel")
            save_excel_file(data, num_files)

        return True
    except Exception as exc:
        return exc


if __name__ == '__main__':
    eel.init("web")
    eel.start('main.html')