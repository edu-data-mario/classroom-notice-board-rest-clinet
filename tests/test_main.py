from classroom_notice_board_rest_clinet.restclient import get_first_value_by_event
from classroom_notice_board_rest_clinet.toolbox.extractor import errmsg2ids


def test_show_dashboard_data_all():
    """
    show_dashboard_data 의 오류 메세지를 통해 위젯 아이디 목록을 받아오는 테스트
    pytest tests/test_main.py::test_show_dashboard_data_all -s
    """
    data = get_first_value_by_event("nowhere else in the world")
    widget_ids = errmsg2ids(data)

    # 출력
    print(widget_ids)

    assert isinstance(widget_ids, list)
    assert 0 < len(widget_ids)
