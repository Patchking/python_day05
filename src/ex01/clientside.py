import requests, argparse

def post_file(filename: str):
    lnk = "http://127.0.0.1:8000/push/"
    with open(filename, "rb") as f:
        files = {"file": (filename, f.read())}

    response = requests.post(lnk, files=files)
    return response

def get_list():
    lnk = "http://127.0.0.1:8000/list/"
    response = requests.get(lnk)
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser_command = parser.add_subparsers(dest="command", required=True)
    parser_command.add_parser("upload").add_argument("filename")
    parser_command.add_parser("list")
    args = parser.parse_args()

    if args.command == "upload":
        response = post_file(args.filename)
        print(response.status_code)
    elif args.command == "list":
        response = get_list()
        print(response.text)
