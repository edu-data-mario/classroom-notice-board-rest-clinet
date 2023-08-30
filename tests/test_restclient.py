from classroom_notice_board_rest_clinet.restclient import update_poster, get_first_value_by_event, append_team
import random
from faker import Faker


def test_update_poster():
    mantra = [
        "Stay hungry, stay foolish.",
        "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle.",
        "Your time is limited, so don't waste it living someone else's life.",
        "Don't be afraid to fail. It's not the end of the world. In fact, it can be the best thing that happens to you.",
        "Innovation is the only way to stay ahead of the competition.",
        "Design is not just what it looks like and feels like. Design is how it works.",
        "Think different.",
        "The best way to predict the future is to create it.",
    ]

    response_status_code = update_poster(message=random.choice(mantra))
    assert 204 == response_status_code


def test_get_first_value_by_event():
    r = get_first_value_by_event('poster')
    print(r)
    assert isinstance(r, dict)


def test_update_team():
    """
    pytest tests/test_restclient.py::test_update_team
    :return:
    """
    # https://faker.readthedocs.io/en/master/locales/ko_KR.html?highlight=korea  #
    fake = Faker(['ko_KR'])
    status_code = append_team(widgets_id="oneTeam", label=fake.name(), value=fake.job())
    assert 204 == status_code


def test_update_team_empty_widget_data():
    """
    pytest tests/test_restclient.py::test_update_team
    :return:
    """
    # https://faker.readthedocs.io/en/master/locales/ko_KR.html?highlight=korea  #
    fake = Faker(['ko_KR'])
    status_code = append_team(widgets_id="twoTeam", label=fake.name(), value=fake.job())
    assert 204 == status_code
