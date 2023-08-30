import requests
import json


def update_poster(message: str, base_url='https://classmario.fly.dev') -> int:
    """Update the contents of the dashboard poster.

    :param message:
    :param base_url: default -> https://classmario.fly.dev
    :return: 204 -> success

    """
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'auth_token': 'LIVING_FOR_TODAY',
        'text': message,
    }

    response = requests.post(f'{base_url}/widgets/poster', headers=headers, json=json_data)
    return response.status_code


def get_first_value_by_event(id: str, max_count=10, base_url='https://classmario.fly.dev') -> dict:
    """
    스트리밍 이벤트 중에서 특정 "id" 값의 첫번째 값을 가져옵니다.

    :param id: "id": "poster"인 이벤트의 아이디 값
    :param max_count: 이벤트 스트림에서 검색할 최대 횟수 (default: 10)
    :param url: 이벤트를 스트림으로 받아올 주소 (default: 'https://classmario.fly.dev')
    :return: "id": "oneTeam"인 이벤트의 값을 JSON 형태로 반환
    """
    response = requests.get(f'{base_url}/events', stream=True)

    count = 0
    searched_ids = []
    for line in response.iter_lines():
        if line:
            count = count + 1
            if count >= max_count:
                return {
                    "error": f"couldn't find the event. check max_count or id. found IDs:{sorted(set(searched_ids))}"
                }
            event = line.decode().replace("data: ", "")
            data = json.loads(event)
            searched_ids.append(data["id"])
            if data["id"] == id:
                return data


def update_team() -> int:
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'auth_token': 'LIVING_FOR_TODAY',
        'items': [
            {
                'label': 'item1',
                'value': 'Test1',
            },
            {
                'label': 'item2',
                'value': 'Test2',
            },
        ],
    }

    response = requests.post('https://classmario.fly.dev/widgets/oneTeam', headers=headers, json=json_data)