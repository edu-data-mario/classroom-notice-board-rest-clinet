import argparse
import json
from classroom_notice_board_rest_clinet.restclient import update_poster, get_first_value_by_event


def write_poster():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--poster", action="store_true", help="updates the contents of the POSTER widget")
    group.add_argument("-t", "--team", action="store_true", help="updates the contents of the TEAM widget")
    parser.add_argument("msg", type=str, help="message")
    parser.add_argument("base_url", nargs="?", type=str, default="https://classmario.fly.dev", help="dashboard base_url, default:https://classmario.fly.dev")

    args = parser.parse_args()

    if args.poster:
        status_code = update_poster(message=args.msg, base_url=args.base_url)
        if status_code == 204:
            print("SUCCESS UPDATE POSTER")
        else:
            print("FAILED UPDATE POSTER")

    elif args.team:
        print("Features are not implemented yet.")
    else:
        print("An undefined functional call has occurred.")


def show_dashboard_data():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--specific", action="store_true", help="outputs a SPECIFIC id value.")
    group.add_argument("-a", "--all", action="store_true", help="shows all values. However, within the max value")
    parser.add_argument("id", nargs="?", type=str, help="Dashboard widget ID")
    parser.add_argument("max", nargs="?", default=10, help="Maximum number of times to search in the event stream")
    parser.add_argument("base_url", nargs="?", default="https://classmario.fly.dev", help="dashboard base_url")

    args = parser.parse_args()

    if args.specific:
        data = get_first_value_by_event(id=args.id, max_count=args.max, base_url=args.base_url)
        pretty_json = json.dumps(data, indent=2)
        print(pretty_json)
    elif args.all:
        print("Features are not implemented yet.")
    else:
        print("An undefined functional call has occurred. ex) $ class-show-data -h")



