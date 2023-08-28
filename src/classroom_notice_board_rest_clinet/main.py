import argparse
from classroom_notice_board_rest_clinet.restclient import update_poster


def main():
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

