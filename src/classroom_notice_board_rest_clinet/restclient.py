import requests


def update_poster(message: str, base_url='https://classmario.fly.dev') -> int:
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'auth_token': 'LIVING_FOR_TODAY',
        'text': message,
    }

    response = requests.post(f'{base_url}/widgets/poster', headers=headers, json=json_data)
    return response.status_code
