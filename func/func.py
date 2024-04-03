import json  
import datetime 
def load_operation(file):
    """
    Читает файл и распечатывает его
    """
    with open(file) as f:
        data = json.loads(f.read())
        executed_data = []
        for i in data:
            if 'state' in i.keys():
                if i['state'] == 'EXECUTED':
                    executed_data.append(i)     
    return executed_data

def date_time(data):
    """
    Сортирует по значению ключа и переводит в нужный формат 
    """
    sorted_data = sorted(data, key=lambda x: x["date"])
    for i in range(len(sorted_data)):
        data_time = datetime.datetime.strptime(sorted_data[i]["date"], "%Y-%m-%dT%H:%M:%S.%f")
        sorted_data[i]["data_time"] = data_time
        sorted_data[i]["correct_date"] = data_time.strftime("%d.%m.%Y")
    return sorted_data[-5:]

def from_to(data):
    """
    Проверяет на наличие ключа если его нет то выводит пустой список 
    """
    if "from" in data.keys():
        from_ = hide(data["from"])
    else:
        from_ = ""

    if "to" in data.keys():
        to_ = hide(data["to"])
    else:
        to_ = ""
    return f"{from_} -> {to_}"

def hide(data):
    """
    Шифрует симвволы  номера счата и номера карты 
    """
    account = data.split()
    prefix = account[:-1]
    check = account[-1]
    if len(check) == 16:
        return f"{' '.join(prefix)} {check[:4]} {check[4:6]}** **** {check[-4:]}"
    else:
        return f"{' '.join(prefix)} **{check[-4:]}"
   """
   Выводит сумму и валюту 
   """ 
def sum_currency(data):
    return f"{data['oper}ationAmount']['amount']} {data['operationAmount']['currency']['name']}"
