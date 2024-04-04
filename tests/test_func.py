import pytest
from func import func

data = {
            "id": 41428829,
                "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                        "operationAmount": {
                                  "amount": "8221.37",
                                        "currency": {
                                                    "name": "USD",
                                                            "code": "USD"
                                                                  }
                                         },
                            "description": "Перевод организации",
                                "from": "Maestro 1596837868705199",
                                    "to": "Счет 64686473678894779589"
                                      }

def test_load_operation():
    assert func.load_operation('load.json') == [data]
            






def test_date_time():
    pass



def test_from_to():
    assert func.from_to(data) == 'Maestro 1596 83** **** 5199 -> Счет **9589'



def test_hide():
    assert func.hide('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert func.hide('Счет 64686473678894779589') == 'Счет **9589'



def test_sum_currency():
    assert func.sum_currency(data) == '8221.37 USD'
