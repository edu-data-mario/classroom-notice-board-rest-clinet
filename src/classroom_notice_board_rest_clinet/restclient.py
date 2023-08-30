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


def append_team(widgets_id: str, label: str, value: str, is_reset=False, max_count=10, base_url='https://classmario.fly.dev') -> int:
    """
    이 함수는 팀 정보를 추가합니다. 기존 값을 모두 지우고 해당 값만 넣으려면 is_reset=True 로 설정합니다.

    widgets_id에 해당하는 팀 정보를 가져온 후, `label`에 해당하는 값을 `value`로 업데이트합니다.
    is_reset가 True 이면 값을 초기화합니다.

    **Args:**

    * widgets_id: 팀 위젯의 ID입니다.
    * label`: 업데이트할 값의 레이블입니다.
    * value: 업데이트할 값입니다.
    * is_reset: 값을 초기화할지 여부입니다. 기본 값은 False 입니다. 새로운 값을 추가합니다.
    * max_count
    * base_url: 팀 데이터베이스의 URL입니다. 기본값은 https://classmario.fly.dev 입니다.

    **Returns:**

    * 정상 수행되는 경우 204 값을 리턴합니다.

    **Raises:**

    * TODO : `ValueError`: `widgets_id`에 해당하는 팀 정보가 없으면 발생합니다.
    * TODO : `KeyError`: `label`에 해당하는 값이 데이터베이스에 존재하지 않으면 발생합니다.
    """
    if is_reset:
        items = []
    else:
        data = get_first_value_by_event(id=widgets_id, max_count=max_count, base_url=base_url)
        items = data.get('items', [])

    add_msg = {'label': label, 'value': value}
    items.append(add_msg)

    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'auth_token': 'LIVING_FOR_TODAY',
        'items': items,
    }

    response = requests.post(f"{base_url}/widgets/{widgets_id}", headers=headers, json=json_data)

    return response.status_code
