import json
from io import StringIO
from pathlib import Path

import requests
import pandas as pd


def test_predict_endpoint():
    """Тест для отправки POST-запроса на эндпоин"""

    url = "http://127.0.0.1:8000/api/work_with_pick_regno"
    path_file = Path('test_api', 'data_for_test', 'test_data.csv')

    test_data = formatted_dict_for_post(path_file)
    response = requests.post(url, data=json.dumps(test_data))
    assert response.status_code == 200
    result = response.json()
    assert "result" in result


def formatted_dict_for_post(path_test_data: str | Path) -> list[dict]:
    """Формирует словарь для отправки POST-запроса"""

    with open(path_test_data, 'r', encoding='utf-8') as f:
        data = f.read()
        data = data.replace('""', '"')

    df = pd.read_csv(StringIO(data), sep=',', encoding='utf-8')

    data_1 = df.to_dict(orient="records")
    return data_1
