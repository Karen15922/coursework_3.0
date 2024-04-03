import json 
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

def test_load_operation(data):
    pass 
            






def test_data_time(data):
    pass








def test_from_to(data):
    assert func.from_to(data) == 'Maestro 159683******5199 -> Счет **9589'



def test_hide():
    pass



def test_sum_currency():
    pass
