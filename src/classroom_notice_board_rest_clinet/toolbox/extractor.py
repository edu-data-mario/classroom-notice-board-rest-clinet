import ast


def errmsg2ids(data: dict) -> list:
    """
    아래 형태의 data 를 입력 받아 widget_ids 추출 반환

    widget_ids = ['buzzwords', 'convergence', 'karma', 'oneTeam', 'poster', 'synergy', 'valuation']
    data = {
        "error":
        "couldn't find the event. check max_count or id. found IDs:['buzzwords', 'convergence', 'karma', 'oneTeam', 'poster', 'synergy', 'valuation']"
    }
    :return: widget_ids = ['buzzwords', 'convergence', 'karma', 'oneTeam', 'poster', 'synergy', 'valuation']
    """

    ids = data["error"].split(":")[1]

    # 리스트로 변환
    widget_ids = ast.literal_eval(ids)
    return widget_ids
