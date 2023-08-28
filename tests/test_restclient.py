from classroom_notice_board_rest_clinet.restclient import update_poster
import random


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
