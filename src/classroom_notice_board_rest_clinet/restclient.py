import requests


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
