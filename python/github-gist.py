import argparse
import json
import platform
import random
import string
from pprint import pprint

import clipboard
import requests

''' Add Github Gists directly from Clipboard
Requirements:
clipboard==0.0.4
requests==2.11.1
'''

username = ""  # Set Username for GitHub Account
password = ""  # Set Password for GitHub Account


class Github:
    @staticmethod
    def create_gists_clipboard(description: str, file: str, public: bool):
        content = clipboard.paste()

        if not description:
            description = "Gist file created on " + platform.platform() + " from clipboard"
        if not file:
            file = "gist_clipboard_" + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))

        data = {
            "description": description,
            "public": public,
            "files": {
                file: {
                    "content": content
                }
            }
        }

        json_result = requests.post('https://api.github.com/gists',
                                    auth=(username, password),
                                    data=json.dumps(data))

        return json_result.json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-d', '--description', type=str, help='Description for gists')
    parser.add_argument('-f', '--file', type=str, help='Files that make up this gist.')
    parser.add_argument('-p', '--public', action='store_true',
                        help='Indicates whether the gist is public. Default: false')
    args = parser.parse_args()
    response = Github.create_gists_clipboard(args.description, args.file, args.public)
    pprint(response)
